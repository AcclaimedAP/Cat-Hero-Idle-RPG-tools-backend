from django.views.generic import View
from django.http import JsonResponse
from django.utils.dateparse import parse_datetime

from apikey.models import ApiKey
from .models import ExchangeTrade
import uuid
import json
import io
from django.http import HttpResponse
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.dates as mdates
from django.utils import timezone
from django.db import models
import seaborn as sns
from django.db.models import Avg, Case, Value, CharField
from django.db.models.functions import ExtractHour
from matplotlib.ticker import MaxNLocator
from django.db.models import F


class ExchangeCreateView(View):
    def post(self, request, *args, **kwargs):
        try:
            exchange_data = json.loads(request.body)
            for exchange_uuid, data in exchange_data.items():
                if 'expired' in data:
                    exchange_uuid_obj = uuid.UUID(exchange_uuid)
                    ExchangeTrade.objects.filter(exchange_uuid=exchange_uuid_obj).delete()
                else:
                    listing_time_parsed = parse_datetime(data.get('listing_time'))
                    exchange_uuid = uuid.UUID(exchange_uuid)

                    ExchangeTrade.objects.update_or_create(
                        exchange_uuid=exchange_uuid,
                        defaults={
                            'price': data.get('price'),
                            'listing_time': listing_time_parsed,
                            'gear_type': data.get('gear_type'),
                            'rarity': data.get('rarity'),
                            'level': data.get('level', 0),
                            'exchange_left': data.get('exchange_left', 0),
                            'durability': data.get('durability', 0),
                        }
                    )

            return JsonResponse({'status': 'success', 'message': 'Exchange trades created/updated successfully.'}, status=200)

        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)


class GetExchangesView(View):
    def post(self, request, *args, **kwargs):
        api_key = request.headers.get('X-API-KEY')
        exist = ApiKey.objects.filter(id=api_key, usable=True).update(usage_count=F('usage_count') + 1)

        if not exist:
            return JsonResponse({'error': 'Invalid API Key'}, status=403)

        try:
            data = json.loads(request.body)
            days = int(data.get('day', 7))
            gear_type = data.get('type', None)
            rarity = data.get('rarity', None)
            level = data.get('level', None)
            durability = data.get('durability', None)
            exchange_left = data.get('exchange_left', None)
            order_by = data.get('order_by', None)
            start_date = timezone.now() - timezone.timedelta(days=days)
            exchanges = self.filter_trades(gear_type, rarity, level, durability, exchange_left, order_by, start_date)

            custom_data = self.format_data(exchanges)

            return JsonResponse(custom_data, safe=False)

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)

    def format_data(self, exchanges):
        custom_data = {}
        for item in exchanges:
            item_id = str(item.pk)
            fields = {
                'price': item.price,
                'listing_time': item.listing_time,
                'gear_type': item.gear_type,
                'rarity': item.rarity,
                'level': item.level,
                'exchange_left': item.exchange_left,
                'durability': item.durability
            }
            custom_data[item_id] = fields
        return custom_data

    def filter_trades(self, gear_type, rarity, level, durability, exchange_left, order_by, start_date):
        trades = ExchangeTrade.objects.filter(listing_time__gte=start_date)

        if gear_type is not None:
            trades = trades.filter(gear_type=gear_type)
        if rarity is not None:
            trades = trades.filter(rarity=rarity)
        if level is not None:
            trades = trades.filter(level=level)
        if durability is not None:
            trades = trades.filter(durability=durability)
        if exchange_left is not None:
            trades = trades.filter(exchange_left=exchange_left)
        if order_by is not None:
            trades = trades.order_by(order_by)
        return trades


class CreateGraphView(View):
    def post(self, request, *args, **kwargs):
        api_key = request.headers.get('X-API-KEY')
        exist = ApiKey.objects.filter(id=api_key, usable=True).update(usage_count=F('usage_count') + 1)

        if not exist:
            return JsonResponse({'error': 'Invalid API Key'}, status=403)

        try:
            data = json.loads(request.body)
            days = int(data.get('day', 7))
            gear_type = data.get('type', None)
            rarity = data.get('rarity', None)
            level = data.get('level', None)
            durability = data.get('durability', None)
            exchange_left = data.get('exchange_left', None)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)

        start_date = timezone.now() - timezone.timedelta(days=days)

        trades_grouped = self.filter_and_group_trades(gear_type, rarity, level, durability, exchange_left, start_date)

        if len(trades_grouped) > 4:
            dates = [trade['listing_day'] for trade in trades_grouped]
            prices = [trade['average_price'] for trade in trades_grouped]

            buf = self.create_graph(days, gear_type, rarity, level, durability, dates, prices)

            response = HttpResponse(buf.getvalue(), content_type='image/png')
            response['Content-Length'] = str(len(response.content))
            return response
        else:
            return JsonResponse({'error': 'Not enough data to create a graph, try searching with less specific parameters or for a longer period of time.'}, status=400)

    def calculate_limit(self, numbers):
        from decimal import Decimal
        if not numbers:
            return Decimal('0'), Decimal('1')
        min_num = min(numbers)
        max_num = max(numbers)
        range_num = max_num - min_num

        if range_num == Decimal('0'):
            return min_num - Decimal('1'), max_num + Decimal('1')

        padding = range_num * Decimal('0.2')
        return min_num - padding, max_num + padding

    def create_graph(self, days, gear_type, rarity, level, durability, dates, prices):
        rarity_colors = {
            "common": "#8598a7",
            "uncommon": "#6db834",
            "rare": "#4cafd1",
            "epic": "#c16ee3",
            "legendary": "#ee5b69",
        }
        color = rarity_colors.get(rarity.lower(), "black")

        sns.set_theme(style="whitegrid")
        fig = Figure(figsize=(10, 6), dpi=100)
        ax = fig.add_subplot(111)

        ax.plot(dates, prices, marker='o', linestyle='-', color=color, markersize=8, linewidth=2, label='Price Trend')
        ax.fill_between(dates, 0, prices, color=color, alpha=0.3)

        ax.xaxis.set_major_formatter(mdates.DateFormatter('%m-%d %H:%M'))
        ax.xaxis.set_major_locator(mdates.HourLocator(interval=12))
        fig.autofmt_xdate(rotation=45)
        ax.yaxis.set_major_locator(mdates.AutoDateLocator())
        ax.set_ylim(self.calculate_limit(prices))
        ax.yaxis.set_major_locator(MaxNLocator(integer=True, steps=[1, 2, 5, 10]))

        title = self.generate_title(days, gear_type, rarity, level, durability)
        ax.set_title(title, fontsize=14, fontweight='bold', color=color)

        ax.set_xlabel('Date', fontsize=12)
        ax.text(0.5, -0.3, "The prices for the last two days may not accurately represent the real market prices as not all trades have been confirmed as completed yet.",
                fontsize=9, ha='center', va='bottom', transform=ax.transAxes, style='italic')
        ax.set_ylabel('Price (Black Gems)', fontsize=12)
        ax.grid(True, linestyle='--', alpha=0.5)
        ax.legend(loc='best')

        ax.set_xlim([dates[0], dates[-1]])
        fig.tight_layout()

        buf = io.BytesIO()
        canvas = FigureCanvas(fig)
        canvas.print_png(buf)
        return buf

    def convert_to_datetime(self, queryset):
        from datetime import datetime, time
        new_data = []
        for entry in queryset:
            day = entry['listing_day']
            if entry['half_day_interval'] == 'AM':
                new_time = time.min
            else:
                new_time = time(12, 0)
            new_datetime = datetime.combine(day, new_time)
            new_data.append({
                'listing_day': new_datetime,
                'average_price': entry['average_price']
            })
        return new_data

    def filter_and_group_trades(self, gear_type, rarity, level, durability, exchange_left, start_date):
        trades = ExchangeTrade.objects.filter(listing_time__gte=start_date)

        if gear_type is not None:
            trades = trades.filter(gear_type=gear_type)
        if rarity is not None:
            trades = trades.filter(rarity=rarity)
        if level is not None:
            trades = trades.filter(level=level)
        if durability is not None:
            trades = trades.filter(durability=durability)
        if exchange_left is not None:
            trades = trades.filter(exchange_left=exchange_left)

        trades_grouped = trades.annotate(
            hour=ExtractHour('listing_time'),
            listing_day=models.functions.Trunc('listing_time', 'day', output_field=models.DateField())
        ).annotate(
            half_day_interval=Case(
                models.When(hour__lt=12, then=Value('AM')),
                default=Value('PM'),
                output_field=CharField(),
            )
        ).values('listing_day', 'half_day_interval').annotate(
            average_price=Avg('price')
        ).order_by('listing_day', 'half_day_interval')
        return list(self.convert_to_datetime(trades_grouped))

    def generate_title(self, days, gear_type, rarity, level, durability):
        title = 'Price Evolution'
        if rarity != 'all':
            title += f" for {rarity.capitalize()}"
        if gear_type != 'all':
            title += f" {gear_type.capitalize()}"
        else:
            title += " gear"
        if level is not None:
            title += f", Level {level}"
        if durability is not None:
            title += f", Durability {durability}"

        if days > 0:
            title += f" - Last {days} Days"
        return title

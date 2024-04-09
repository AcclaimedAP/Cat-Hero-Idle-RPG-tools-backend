from django.views.generic import View
from django.http import JsonResponse
from django.utils.dateparse import parse_datetime
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


class CreateGraphView(View):
    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)
            days = int(data.get('day', 0))
            gear_type = data.get('type', 'all')
            rarity = data.get('rarity', 'all')
            level = data.get('level', None)
            durability = data.get('durability', None)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)

        start_date = timezone.now() - timezone.timedelta(days=days)

        trades_grouped = self.filter_and_group_trades(gear_type, rarity, level, durability, start_date)

        if len(trades_grouped) > 4:
            dates = [trade['listing_day'] for trade in trades_grouped]
            prices = [trade['average_price'] for trade in trades_grouped]

            buf = self.create_graph(days, gear_type, rarity, level, durability, dates, prices)

            response = HttpResponse(buf.getvalue(), content_type='image/png')
            response['Content-Length'] = str(len(response.content))
            return response
        else:
            return JsonResponse({'error': 'Not enough data to create a graph, try searching with less specific parameters.'}, status=400)

    def create_graph(self, days, gear_type, rarity, level, durability, dates, prices):
        sns.set_theme(style="whitegrid")
        fig = Figure(figsize=(10, 6), dpi=100)
        ax = fig.add_subplot(111)

        ax.plot(dates, prices, marker='o', linestyle='-', color='darkcyan', markersize=8, linewidth=2, label='Price Trend')
        from matplotlib.ticker import MaxNLocator

        ax.xaxis.set_major_formatter(mdates.DateFormatter('%m-%d'))
        ax.xaxis.set_major_locator(mdates.DayLocator(interval=1))
        fig.autofmt_xdate(rotation=45)
        ax.yaxis.set_major_locator(MaxNLocator(integer=True))

        title = self.generate_title(days, gear_type, rarity, level, durability)
        ax.set_title(title, fontsize=14, fontweight='bold')
        ax.set_xlabel('Date', fontsize=12)
        ax.set_ylabel('Price (Black Gems)', fontsize=12)
        ax.grid(True, which='both', linestyle='--', alpha=0.5)

        ax.legend(loc='best')

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

    def filter_and_group_trades(self, gear_type, rarity, level, durability, start_date):
        trades = ExchangeTrade.objects.filter(listing_time__gte=start_date)

        if gear_type.lower() != 'all':
            trades = trades.filter(gear_type=gear_type)
        if rarity.lower() != 'all':
            trades = trades.filter(rarity=rarity)
        if level is not None:
            trades = trades.filter(level=level)
        if durability is not None:
            trades = trades.filter(durability=durability)

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
        if rarity.lower() != 'all':
            title += f" for {rarity.capitalize()}"
        if gear_type.lower() != 'all':
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

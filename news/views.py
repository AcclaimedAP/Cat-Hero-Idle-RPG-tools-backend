from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .models import News
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


@method_decorator(csrf_exempt, name='dispatch')
class NewsIndexView(View):
    """
    Provides a paginated list of news articles, optionally filtered by type.
    - `type` (str): Filter news by type (e.g., 'website', 'guides').
    - `page` (int): The page of results to retrieve.
    - `per_page` (int): The number of news articles to return per page.
    """

    def get(self, request):
        news_type = request.GET.get('type', None)
        page = request.GET.get('page', 1)

        per_page = request.GET.get('per_page', 10)
        per_page = int(per_page) if per_page.isdigit() else 10
        per_page = 1 if per_page == 0 else per_page

        if news_type:
            news_queryset = News.objects.filter(type=news_type)
        else:
            news_queryset = News.objects.all()

        # Paginate the queryset
        paginator = Paginator(news_queryset.order_by('-created_at'), per_page)
        try:
            news_page = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            news_page = paginator.page(1)
            page = 1
        except EmptyPage:
            # If page is out of range (e.g., 9999), deliver last page of results.
            news_page = paginator.page(paginator.num_pages)
            page = paginator.num_pages

        # Format news articles for the response
        news_list = [
            {
                'slug': news.slug,
                'title': news.title,
                'body': news.body[:100] + '...',  # Preview of the body
                'created_at': news.created_at,
                'updated_at': news.updated_at,
                'type': news.type,
                'author': news.author
            } for news in news_page
        ]

        # Pagination data for the response
        pagination_data = {
            'current_page': int(page),
            'per_page': int(per_page),
            'total_pages': paginator.num_pages,
        }

        # Return JSON response with news data and pagination info
        return JsonResponse({'data': news_list, 'pagination_data': pagination_data, 'type': news_type if news_type else 'all'}, status=200)


@method_decorator(csrf_exempt, name='dispatch')
class NewsDetailView(View):
    """
    Retrieves the details of a news article using its slug.

    This view returns a JSON response containing detailed information about
    a news article, identified by a slug. The response includes the title,
    body, creation and update timestamps, type, and author of the news article.

    If a news article with the given slug does not exist, it returns a JSON
    response with an error message and a 404 status code.

    Parameters:
    - slug (str): The slug of the news article to retrieve.

    Returns:
    - JsonResponse: A JSON response containing the news article details or an error message.
    """

    def get(self, request, slug):
        try:
            news = News.objects.get(slug=slug)
            news_data = {
                'title': news.title,
                'body': news.body,
                'created_at': news.created_at,
                'updated_at': news.updated_at,
                'type': news.type,
                'author': news.author,
            }
            return JsonResponse({'news': news_data})
        except News.DoesNotExist:
            return JsonResponse({'error': 'No news found with the provided slug'}, status=404)

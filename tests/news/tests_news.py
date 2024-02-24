import pytest
from django.test import Client
from django.urls import reverse


@pytest.mark.django_db
@pytest.mark.parametrize("news_type,page,per_page,expected_status_code", [
    (None, 1, 10, 200),
    ('website', 1, 10, 200),
    ('nonexistent', 1, 10, 200),
    (None, 'invalid', 10, 200),
    (None, 1, 'invalid', 200),
    (None, 9999, 10, 200),
])
def test_news_index_view(news_type, page, per_page, expected_status_code):
    client = Client()
    params = {}
    if news_type is not None:
        params['type'] = news_type
    if page is not None:
        params['page'] = page
    if per_page is not None:
        params['per_page'] = per_page

    url = reverse('news_index')
    response = client.get(url, params)
    assert response.status_code == expected_status_code

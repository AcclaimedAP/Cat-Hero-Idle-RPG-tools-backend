import json
import pytest
from django.urls import reverse
from django.test import Client


@pytest.mark.django_db
def test_build_create_view():
    client = Client()
    build_string = "Your build string here"
    response = client.post(reverse('create'), data=json.dumps({'build_string': build_string}), content_type='application/json')
    assert response.status_code == 201
    assert 'build_id' in response.json()


@pytest.mark.django_db
def test_build_detail_view_not_found():
    client = Client()
    response = client.get(reverse('detail', kwargs={'build_id': "does not exist"}))
    assert response.status_code == 404
    assert 'error' in response.json()

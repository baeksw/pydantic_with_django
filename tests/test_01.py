import pytest

from rest_framework.test import APIRequestFactory
from rest_framework.test import APIClient, RequestsClient, CoreAPIClient

from django.urls import reverse
from django.contrib.auth.models import User, Group
from app.models import Person

# Using the standard RequestFactory API to create a form POST request

from requests.auth import HTTPBasicAuth


'''
@pytest.mark.django_db
def test_patch():
    factory = APIRequestFactory()
    user = User.objects.get(username='admin')
    client = APIClient()
    client.login(username='admin', password='admin#1123')
    response = client.get('http://localhost:8000/users/')
    assert response.status_code == 200
'''


#@pytest.mark.django_db(transaction=True)
@pytest.mark.django_db
def test_django_db_create(logger):
    obj = Person.objects.create(first_name='f2', last_name='l1')
    assert obj 


@pytest.mark.django_db
def test_django_db_create_after_get(client, logger):
    obj = Person.objects.create(first_name='f2', last_name='l1')
    res = client.get('/api/persons/')
    assert res.status_code == 200

@pytest.mark.django_db
def test_make_person_by_api_and_get_person(client, logger):
    r = client.post('/api/persons/',{'first_name' : 'f33' , 'last_name' : 'l22' })
    assert r.status_code == 201
    res = client.get('/api/persons/', {}, ACCEPT='application/json')
    assert res.status_code == 200

@pytest.mark.django_db
def test_view(logger, client):
    pass



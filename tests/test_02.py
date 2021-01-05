from django.contrib.auth.models import User, Group
from django.urls import reverse
import pytest
from requests.auth import HTTPBasicAuth

from app.models import Person


@pytest.mark.django_db
def test_django_db_create(logger):
    user = User.objects.create(
        first_name="Jordan", 
        last_name="Eremieff", 
        email="jordan@eremieff.com"
    )


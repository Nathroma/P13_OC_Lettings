import pytest
from .models import Letting, Address
from django.test import Client
from django.urls import reverse


class TestLettings:

    def setup_method(self):
        self.address = Address.objects.create(
            number='76', 
            street='Saint-Quentin', 
            city='Metz', 
            state='France', 
            zip_code=57000, 
            country_iso_code='FR'
        )
        self.letting = Letting.objects.create(title='Art', address=self.address)

    def test_index(self,client):
        response = client.get(reverse('lettings:index'))
        assert response.status_code == 200
        assert "<title>Lettings</title>" in response.content.decode('utf-8')

    def test_profile(self,client):
        response = client.get(reverse('lettings:letting', args=[1]))
        assert response.status_code == 200
        assert "<title>Art</title>" in response.content.decode('utf-8')
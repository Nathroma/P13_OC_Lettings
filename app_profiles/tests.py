import pytest
from django.urls import reverse
from django.contrib.auth.models import User
from .models import  Profile

class TestProfiles:

    def setup_method(self):
        self.user = User.objects.create(username='test', password='123')
        self.profile = Profile.objects.create(user=self.user , favorite_city='Metz')

    @pytest.mark.django_db
    def test_index(self,client):
        response = client.get(reverse('profiles:index'))
        assert response.status_code == 200
        assert "<title>Profiles</title>" in response.content.decode('utf-8')

    @pytest.mark.django_db
    def test_profile(self,client):
        response = client.get(reverse('profiles:profile', args=['abc']))
        assert response.status_code == 200
        assert "<title>Titre</title>" in response.content.decode('utf-8')
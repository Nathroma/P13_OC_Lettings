from django.test import TestCase
from django.urls import reverse

from .models import Address, Letting


class TestViews(TestCase):

    def setUp(self):
        self.address_obj = Address.objects.create(
            number='100',
            street='Morris Ave',
            city='New York',
            state='NY',
            zip_code='10455',
            country_iso_code='USA',
        )
        self.letting_obj = Letting.objects.create(title='TestTitle', address=self.address_obj)

        self.lettings_index_url = reverse('lettings_index')
        self.letting_url = reverse('letting', args=[self.letting_obj.id])

    def test_index_GET(self):
        response = self.client.get(self.lettings_index_url)
        self.assertEquals(response.status_code, 200)

    def test_index_template(self):
        response = self.client.get(self.lettings_index_url)
        self.assertTemplateUsed(response, 'lettings/index.html')

    def test_letting_GET(self):
        response = self.client.get(self.letting_url)
        self.assertEquals(response.status_code, 200)

    def test_letting_title(self):
        response = self.client.get(self.letting_url)
        self.assertIn(b'TestTitle', response.content)

    def test_letting_template(self):
        response = self.client.get(self.letting_url)
        self.assertTemplateUsed(response, 'lettings/letting.html')

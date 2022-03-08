from django.urls import reverse

class TestHomePage:

    def test_index(self,client):
        response = client.get(reverse('index'))
        assert response.status_code == 200
        assert "<title>Holiday Homes</title>" in response.content.decode('utf-8')
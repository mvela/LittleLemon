from django.test import TestCase
from restaurant.models import Menu
from django.urls import reverse
from restaurant.serializers import MenuSerializer
from django.http import JsonResponse
import json
from decimal import Decimal

class DecimalJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return str(obj)
        return super().default(obj)
    
class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(name="Gelato", price=4.99, inventory=64)
        Menu.objects.create(name="Pizza Slice", price=5.99, inventory=44)
        Menu.objects.create(name="Soda", price=1.59, inventory=33)

    def test_menu_list_view(self):
        url = reverse('menu')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        
        queryset = Menu.objects.all()
        expected_data = [{'id':item.id,'name':item.name,'price':item.price,'inventory':item.inventory} for item in queryset]
        expected_json_response = json.dumps(expected_data, cls=DecimalJSONEncoder)

        response_data = json.loads(response.content)
        normalized_response_content = json.dumps(response_data, cls=DecimalJSONEncoder)

        self.assertEqual(normalized_response_content, expected_json_response)

# from django.test import TestCase
# from appherokureg.models import Workshop

# class WorkshopTestCase(TestCase):
#     def setUp(self):
#         Workshop.objects.create(title="Sydney Workshop", slug="sydney_workshop")
#         Workshop.objects.create(title="Melbourne Workshop", slug="melbourne_workshop")

#     def test_animals_can_speak(self):
#         """Animals that can speak are correctly identified"""
        
#         sydney = Animal.objects.get(slug="sydney_workshop")
#         melbourne = Animal.objects.get(name="melbourne_workshop")
        
#         self.assertEqual(sydney.slug, 'sydney_workshop')
#         self.assertEqual(melbourne.title, 'Melbourne Workshop')
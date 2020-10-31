from django.test import TestCase
from .models import NeighbourHood
from django.contrib.auth.models import User
# Create your tests here.
class NeighbourHoodTestClass(TestCase):

    # Set up method
    def setUp(self):
        # Creating a new location and saving it
        self.new_user=User(username='denno',email='a@gmail.com',password='qwerty1234')
        self.new_user.save()
        
        self.new_hood= NeighbourHood(hood_admin=self.new_user,hood_name='Wazazi',hood_location='Chuom')
        self.new_hood.save()



    # Tear Down method
    def tearDown(self):
        NeighbourHood.objects.all().delete()
        User.objects.all().delete()

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.new_hood,NeighbourHood))    

    # Testing Save Method
    def test_create_neighbourhood_method(self):
        self.new_hood1= NeighbourHood(hood_admin=self.new_user,hood_name='Wazazi',hood_location='Chuom')
        self.new_hood1.create_neighbourhood()
        hoods = NeighbourHood.objects.all()
        self.assertTrue(len(hoods) == 2)  



    # Testing delete method
    def test_delete_neighbourhood(self):
        NeighbourHood.delete_neighbourhood(self.new_hood.id)
        hoods = NeighbourHood.get_all_neighbourhoods()
        self.assertTrue(len(hoods) == 0)     

    # Testing get all NeighbourHoods Method
    def test_get_all_neighbourhoods_method(self):
        hoods = NeighbourHood.get_all_neighbourhoods()
        self.assertTrue(len(hoods) == 1) 


    # Testing find NeighbourHood Method
    def test_find_neighbourhood_method(self):
        hood = NeighbourHood.find_neighbourhood(self.new_hood.id)
        self.assertEqual(hood.id,self.new_hood.id)   





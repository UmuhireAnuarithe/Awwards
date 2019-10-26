from django.test import TestCase
from .models import Profile
# Create your tests here.
class ProfileTestClass(TestCase):
     # Set up method
    def setUp(self):
        self.anitha= Profile(Profile_picture = 'passion.jpeg', user_bio ='Passion',location='Musanze',username='anne',email='a@gmail.com')
        
        # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.anitha,Profile))


    def test_save_profile(self):
        self.james = Profile(Profile_picture = 'passion.jpeg', user_bio ='Passion',location='Musanze',username='anne',email='a@gmail.com')
        self.james.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles)>0)
    
    def test_update_profile(self):
        self.ange = Profile(Profile_picture = 'passion.jpeg', user_bio ='Passion',location='Musanze',username='anne',email='a@gmail.com')
        self.ange.save_profile()
        cars =Profile.objects.filter(location='Musanze').first()
        update= Profile.objects.filter(id=cars.id).update(location='Burera')
        updated = Profile.objects.filter(location='Burera').first()
        self.assertNotEqual(cars.location , updated.location)


from django.test import TestCase
from .models import Profile ,Projects
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

    def test_delete_profile(self):
        self.fina = Profile(Profile_picture = 'passion.jpeg', user_bio ='Passion',location='Musanze',username='anne',email='a@gmail.com')
        self.fina.save_profile()
        nature = Profile.objects.filter(username='anne').first()
        tree = Profile.objects.filter(id =nature.id).delete()
        trees =Profile.objects.all()
        
class ProjectsTestClass(TestCase):
       # Set up method
    def setUp(self):
        self.quotes= Projects(Project_image= 'passion.jpeg',name ='Quotes',description='QUOTES APP',link='https//quote')
        
        # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.quotes,Projects))

    def test_save_project(self):
        self.quotes= Projects(Project_image= 'passion.jpeg',name ='Quotes',description='QUOTES APP',link='https//quote')
        self.quotes.save_project()
        projects = Projects.objects.all()
        self.assertTrue(len(projects)>0)
    

    def test_update_project(self):
        self.quotes= Projects(Project_image= 'passion.jpeg',name ='Quotes',description='QUOTES APP',link='https//quote')
        self.quotes.save_project()
        quote =Projects.objects.filter(name ='Quotes',).first()
        update= Projects.objects.filter(id=quote.id).update(name ='Goals')
        updated = Projects.objects.filter(name ='Goals').first()
        self.assertNotEqual(quote.name , updated.name)

    def test_delete_project(self):
        self.quotes= Projects(Project_image= 'passion.jpeg',name ='Quotes',description='QUOTES APP',link='https//quote')
        self.quotes.save_project()
        QUOTES = Projects.objects.filter(name ='Quotes').first()
        quotes = Projects.objects.filter(id =QUOTES.id).delete()
        quotes = Projects.objects.all()
        
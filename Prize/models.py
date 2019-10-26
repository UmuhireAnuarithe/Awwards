from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
   username = models.CharField(max_length =30)
   Profile_picture= models.ImageField(upload_to = 'pictures/')
   email = models.EmailField()
   user_bio = models.CharField(max_length =30)
   location = models.CharField(max_length =30)



   @classmethod
   def search_projects(cls,search_term):
      projects = cls.objects.filter(project__project__icontains=search_term)
      return projects

class Projects(models.Model):
   name = models.CharField(max_length =30 )
   description = models.TextField(max_length= 300)
   link = models.CharField(max_length =100)
   username = models.ForeignKey(User,on_delete=models.CASCADE, null=True)

   @classmethod
   def count_projects(cls,current_user):
     
      username = User.objects.filter(username = current_user).first()
      projects = Projects.objects.filter(username_id = username.id).all()

      project_count = 0
      for project in projects:
         project_count += 1

      return project_count

   def __repr__(self):
      return f'Projects {self.name}'

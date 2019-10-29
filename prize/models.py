from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
   username = models.CharField(max_length =30)
   Profile_picture= models.ImageField(upload_to = 'pictures/')
   email = models.EmailField()
   user_bio = models.CharField(max_length =30)
   location = models.CharField(max_length =30)
   def __str__(self):
      return self.location
   def save_profile(self):
      self.save()

   def update_profile(self):
      self.update()

   def delete(self):
      self.delete()

class Projects(models.Model):
   name = models.CharField(max_length =30 )
   description = models.TextField(max_length= 300)
   link = models.URLField(max_length =100,db_index = True,unique =True,null=True)
   username = models.ForeignKey(User,on_delete=models.CASCADE, null=True)
   Project_image= models.ImageField(upload_to = 'pictures/',null=True)
   @classmethod
   def search_projects(cls,search_term):
      projects = cls.objects.filter(name__icontains=search_term)
      return projects


   @classmethod
   def count_projects(cls,current_user):
     
      username = User.objects.filter(username = current_user).first()
      IP = Projects.objects.filter(username_id = username.id).all()

      project_count = 0
      for project in IP:
         project_count += 1

      return project_count

   def __str__(self):
      return self.name

   def save_project(self):
      self.save()

   def update_project(self):
      self.update()

   def delete(self):
      self.delete()

class Rates(models.Model):
   content = models.IntegerField(default=0)
   usability = models.IntegerField(default=0)
   design = models.IntegerField(default=0)
   score = models.IntegerField(default=0)
   username = models.ForeignKey(User,on_delete=models.CASCADE, null=True)
   project = models.ForeignKey(Projects, null=True)



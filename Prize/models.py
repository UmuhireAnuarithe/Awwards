from django.db import models

class Profile(models.Model):
   username = models.CharField(max_length =30)
   Profile_picture= models.CharField(max_length =30)
   email = models.EmailField()
   user_bio = models.CharField(max_length =30)
   location = models.CharField(max_length =30)



   @classmethod
   def search_projects(cls,search_term):
      projects = cls.objects.filter(project__project__icontains=search_term)
      return projects
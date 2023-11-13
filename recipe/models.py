from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

#Add recipe 
class Recipe(models.Model):
    recipe_name = models.CharField(max_length=250)
    recipe_description = models.TextField()
    recipe_image = models.ImageField(upload_to='recipic_image')
   # date_posted = models.DateTimeField(default=timezone.now)
   # user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.recipe_name


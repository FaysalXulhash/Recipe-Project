from django.db import models


#Add recipe 
class Recipe(models.Model):
    recipe_name = models.CharField(max_length=250)
    recipe_description = models.TextField()
    recipe_image = models.ImageField(upload_to='recipic_image')

    def __str__(self):
        return self.recipe_name


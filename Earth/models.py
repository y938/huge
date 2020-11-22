from django.db import models


class AllCategories(models.Model):
    Title = models.CharField(max_length=255)
    img = models.ImageField(upload_to='home_images')

    def __str__(self):
        return self.Title


class Image(models.Model):
    relate = models.ForeignKey(AllCategories, on_delete=models.CASCADE)
    caption = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="img/%y/%m/%d")
    profile_pic = models.ImageField(upload_to="profile", default="default.jpg")
    
    def __str__(self):
        return self.caption


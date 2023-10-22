from django.db import models
from django.urls import reverse

# Create your models here.
class Type(models.Model):
    house_type = models.CharField(max_length=264,blank=False)
    dealer_name = models.CharField(max_length=264)
    dealer_number = models.CharField(max_length=15,blank=False)

    def __str__(self):
        return self.house_type
    
    def get_absolute_url(self):
        return reverse("realapp:detail",kwargs={'pk':self.pk})
    

class Houses(models.Model):
    property_name = models.CharField(max_length=264)
    property_location = models.CharField(max_length=264)
    special_feature = models.CharField(max_length=264)
    property_price = models.CharField(max_length=264)
    type = models.ForeignKey(Type,related_name="houses", on_delete=models.CASCADE)
    


    def __str__(self):
        return self.property_name


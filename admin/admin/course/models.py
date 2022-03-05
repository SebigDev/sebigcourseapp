from datetime import timezone
from django.db import models

class Category(models.Model):
    category_name = models.CharField(max_length=100)
    
    class Meta:
        db_table = 'category'
    
    def __str__(self):
        return self.category_name
    
class Channel(models.Model):
    channel_name = models.CharField(max_length=50)
    categories = models.ForeignKey(Category, blank=True, on_delete=models.CASCADE,related_name='categories')
    
    class Meta:
        db_table = 'channel'
    
    def __str__(self):
        return self.channel_name
    
       
class Course(models.Model):
    course_name = models.CharField(max_length=200, blank=False)
    course_description = models.TextField(blank=False)
    course_details = models.TextField(blank=False)
    course_channel = models.OneToOneField(Channel, on_delete=models.SET_NULL, null=True, related_name='course_channel')
    course_creator = models.CharField(max_length=500, blank=False)
    uploaded_on = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=False)
    course_price = models.DecimalField(decimal_places=2, max_digits=15, default=0.00)
    course_image_url = models.URLField(null=True, blank=True)
    
    class Meta:
        db_table = 'course'
    
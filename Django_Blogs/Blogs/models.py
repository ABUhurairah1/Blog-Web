from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Blog(models.Model):
    host = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=300,default='',blank=True,null=True)
    description = models.TextField(default='',blank=True,null=True)
    image = models.ImageField(upload_to= 'static/media/blog_images/',default='',blank=True,null=True)
    created = models.DateTimeField()

    class Meta : 
        ordering = ['-created']

    def __str__(self):
        return self.title
    
class Comments(models.Model):

    host = models.ForeignKey(User,on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE)
    text = models.TextField(default='',blank=True,null=True)
    created = models.DateTimeField()

    class Meta : 
        ordering = ['-created']

    def __str__(self):
        return self.text



from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

# Create your models here.

class Post(models.Model):
    user = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    body = models.TextField(max_length=5000, blank=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.title} by {self.user.username}"
    

class Comment(models.Model):
    user = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    commented_post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    body = models.TextField(max_length=3000)
    pub_date = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.user.username



class Contact(models.Model):
    user_from = models.ForeignKey(User, on_delete=models.CASCADE, related_name='contact_from')
    user_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='contact_to')
    contact_date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        indexes = [
            models.Index(fields=['-contact_date'])
        ]
        ordering = ['-contact_date']
        
    def __str__(self):
        return f'{self.user_from} follows {self.user_to}'
    

user_model = get_user_model()
user_model.add_to_class('following', models.ManyToManyField('self', through=Contact, related_name='followers', symmetrical=False))


class Action(models.Model):
    user = models.ForeignKey(User, related_name='actions', on_delete=models.CASCADE)
    action = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    target_ct = models.ForeignKey(ContentType, blank=True, null=True, related_name='target_object', on_delete=models.CASCADE)
    target_id = models.PositiveIntegerField(blank=True, null=True)
    target = GenericForeignKey('target_ct', 'target_id')
    
    class Meta:
        indexes = [ models.Index(fields=['-created'])]
        ordering = ['-created']
        
    def __str__(self):
        return f'{self.user} {self.action} {self.target}'
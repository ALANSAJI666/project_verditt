from django.db import models
from django.contrib.auth import get_user_model
# from django.utils.encoding import python_2_unicode_compatible
from six import python_2_unicode_compatible
import uuid
from datetime import  datetime
# Create your models here.

User  = get_user_model()
class Profile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    id_user = models.IntegerField()
    bio = models.TextField(blank=True)
    current_status = models.TextField(blank=True)
    educational_qualifications = models.TextField(blank=True)
    contact_info= models.TextField(blank=True)
    open_to_work = models.TextField(blank=True)
    profileimg = models.ImageField(upload_to = 'profile_images', default = 'blank_profile_pic.png')
    location = models.CharField(max_length=100,blank=True)

    def __str__(self):
        return self.user.username



class Post(models.Model):
    id = models.UUIDField(primary_key=True, default= uuid.uuid4)
    user = models.CharField(max_length=100)
    image = models.ImageField(upload_to= 'post_images')
    caption = models.TextField()
    # rating = models.DecimalField(max_digits=2, decimal_places=1)
    created_at = models.DateTimeField(default=datetime.now)
    no_of_likes =  models.IntegerField(default=0)

    def __str__(self):
        return self.user


class LikePost(models.Model):
    post_id = models.CharField(max_length= 500)
    username = models.CharField(max_length=100)

    def __str__(self):
        return self.username


class FollowersCount(models.Model):
    follower = models.CharField(max_length=100)
    user = models.CharField(max_length = 100)

    def __str__(self):
        return self.user
class Rating(models.Model):
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    user = models.CharField(max_length=100)

# class Conversation(models.Model):
#     user1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='conversations_as_user1')
#     user2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='conversations_as_user2')
#     started_at = models.DateTimeField(auto_now_add=True)
#
#     class Meta:
#         unique_together = ['user1', 'user2']
#
#     def __str__(self):
#         return f"{self.user1.username} - {self.user2.username}"


# class Message(models.Model):
#     conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE)
#     sender = models.ForeignKey(User, on_delete=models.CASCADE)
#     content = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return f"{self.sender.username} - {self.conversation.user1.username} - {self.conversation.user2.username}"







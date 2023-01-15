from django.db import models
class Event(models.Model):
    title=models.CharField(max_length=200) #shorter
    description=models.TextField() #longer
    location=models.CharField(max_length=200)
    created_at=models.DateTimeField(auto_now_add=True) #set to current time
    online=models.BooleanField()
    is_open=models.BooleanField(default=True)
    image=models.URLField()
    min_attendees=models.IntegerField()
    max_attendees=models.IntegerField()
    owner_id=models.CharField(max_length=200) #change to a foreign key that will store user ID


# class Pledge(models.Model):
#     amount = models.IntegerField()
#     comment = models.CharField(max_length=200)
#     anonymous = models.BooleanField()
#     #linking to above project model
#     project = models.ForeignKey(
#         'Project',
#         on_delete=models.CASCADE, #delete everything linked when deleted
#         related_name='pledges' #attribute we can access eg.my_project.pledges
#     )
#     supporter = models.CharField(max_length=200) #update when user model is made

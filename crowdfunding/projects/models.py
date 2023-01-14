from django.db import models
class Project(models.Model):
    title=models.CharField(max_length=200) #shorter
    description=models.TextField() #longer
    goal=models.IntegerField()
    image=models.URLField()
    is_open=models.BooleanField()
    date_created=models.DateTimeField(auto_now_add=True) #set to current time
    owner=models.CharField(max_length=200) #change to a foreign key that will store user ID


class Pledge(models.Model):
    amount = models.IntegerField()
    comment = models.CharField(max_length=200)
    anonymous = models.BooleanField()
    #linking to above project model
    project = models.ForeignKey(
        'Project',
        on_delete=models.CASCADE, #delete everything linked when deleted
        related_name='pledges' #attribute we can access eg.my_project.pledges
    )
    supporter = models.CharField(max_length=200) #update when user model is made

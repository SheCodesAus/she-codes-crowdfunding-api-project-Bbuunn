from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

# class Attendance(models.Model):
#     #linking to above event model
#     event = models.ForeignKey(
#         'Event',
#         on_delete=models.CASCADE, #delete everything linked when deleted
#         related_name='attendees' #attribute we can access eg.my_event.attendees
#     )

#     attendee = models.ForeignKey( #supporter in class example #previously user
#         User,
#         on_delete=models.CASCADE,
#         related_name='attendances'
#     )
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
    owner=models.ForeignKey( #previously owner_id
        User, #previously User,
        on_delete=models.CASCADE,
        related_name='events' #user.events = all the events owned by user
    )
    attendees=models.ManyToManyField(User, related_name="attended_events")
    # attendee=models.ForeignKey(
    #     Attendance,
    #     on_delete=models.DO_NOTHING,
    #     # null=True,
    #     related_name='attendees'
    # )

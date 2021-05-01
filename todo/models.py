from django.db import models

# Create your models here.
from accounts.models import Customer
from django.contrib.auth.models import User

status=['Created',"Completed", "Submitted" ]
STATUS_CHOICES = (
    ("1", "CREATED"),
    ("2", "FINISHED"),
    ("3", "SUBMITTED"),
    
)
class Task(models.Model):
    title = models.CharField(max_length=100)
    details = models.TextField()
    time =models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='created_by')
    finished_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='finished_by',null=True)
    status=models.CharField(max_length=20,choices=STATUS_CHOICES,default='1')
    def __str__(self):
        return self.title


class Notification(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='sender_notification')
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipient_notification')
    message = models.TextField()
    read = models.BooleanField(default=False)
    recieved_date = models.DateTimeField(auto_now_add=True)
    related_task=models.ForeignKey(Task,on_delete=models.CASCADE,null=True,related_name="related_task")
    is_created=models.BooleanField(default=True)
    def __str__(self):
        return self.message


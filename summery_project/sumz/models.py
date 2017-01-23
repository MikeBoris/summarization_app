from __future__ import unicode_literals
from django.db import models
from django.utils import timezone

class User_input(models.Model):
	user_id = models.IntegerField(primary_key=True)
	user_input_text = models.TextField()
	user_entered_text = models.TextField()
	user_upload_text = models.TextField()
	user_date = models.DateTimeField(default=timezone.now)	

class Output_summary(models.Model):
	summary_output_text = models.TextField()
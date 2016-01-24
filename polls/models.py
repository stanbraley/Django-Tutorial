import datetime

from django.db import models
from django.utils import timezone
from django,utils import python_2_unicode_compatible

# Create your models here.

def was_published_recently(self):
	return self.pub_date >= timezone.timedelta(days=1)

class Question(models.Model):
	question_text=models.CharField(
		max_length=200)
	pub_date=models.DateTimeField('date published')
class Choice(models.Model):
	question=models.ForeignKey(Question, on_delete=models.CASCADE)
	choice_text=models.IntegerField(default=0) 
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Exam(models.Model):

    def __str__(self):
        return self.title

    admin=models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    title=models.CharField(max_length=50)
    duration=models.DurationField()
    create_date=models.DateTimeField()
    time=models.DateTimeField()
    type=models.CharField(max_length=50)

class Category(models.Model):

    def __str__(self):
        return self.title

    admin=models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    title=models.CharField(max_length=50)
    desc=models.CharField(max_length=2000)

class Question(models.Model):

    def __str__(self):
        return self.content

    cate_id=models.ForeignKey(Category, on_delete=models.CASCADE)
    content=models.CharField(max_length=500)
    type=models.CharField(max_length=50)
    correct_ans=models.CharField(max_length=50)
    a_ans=models.CharField(max_length=500)
    b_ans = models.CharField(max_length=500)
    c_ans = models.CharField(max_length=500, default='-')
    d_ans = models.CharField(max_length=500, default='-')
    mark=models.FloatField()

    def get_absolute_url(self):
        return reverse('exam:ques_detail', kwargs={'pk':self.pk})

class Ques_Exam(models.Model):

    exam_id=models.ForeignKey(Exam, on_delete=models.CASCADE)
    ques_id=models.ForeignKey(Question, on_delete=models.CASCADE)
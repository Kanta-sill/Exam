from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Exam, Ques_Exam, Question
from django.db import connection
import random

# def ques_random():
#
#     return ques_id


def ques_exam_create(self):

    multi_list=[]
    TF_list=[]


    quess = Question.objects.all()
    ques_multi = quess.filter(type='Multiple choice')
    for ques in ques_multi:
        multi_list.append(ques.id)
    ran_ques_multi = random.sample(multi_list, 2)

    ques_TF = quess.filter(type='True/False')
    for ques in ques_TF:
        TF_list.append(ques.id)
    ran_ques_TF = random.sample(TF_list, 3)

    ques_id=[]
    for i in ran_ques_multi:
        ques_id.append(i)

    for i in ran_ques_TF:
        ques_id.append(i)

    c = connection.cursor()
    for id in ques_id:
        c.execute("insert into exams_ques_exam(exam_id_id, ques_id_id) values (%s, %s);", [self.id, id])

@receiver(post_save, sender=Exam)
def random_ques(sender, instance, created ,**kwargs):
    if created:
        ques_exam_create(instance)


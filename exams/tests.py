from django.test import TestCase
from .models import Ques_Exam
import random

# Create your tests here.

class Ques_exam_test(TestCase):

    def ques_test(self):
        ques=Ques_Exam.objects.all()
        ques_id=ques.id
        return ques_id

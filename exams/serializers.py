from rest_framework import serializers
from .models import Ques_Exam

class Qu_Ex_serializer(serializers.ModelSerializer):
    class Meta:
        model=Ques_Exam
        fields=['exam_id', 'ques_id']
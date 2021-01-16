from django import forms
from .models import Question, Ques_Exam

class QuesForm(forms.ModelForm):
    class Meta:
        model=Question
        fields=['cate_id', 'content', 'type', 'correct_ans', 'a_ans', 'b_ans', 'c_ans', 'd_ans', 'mark']

class QuesExamForm(forms.ModelForm):
    class Meta:
        model=Ques_Exam
        fields=['exam_id', 'ques_id']
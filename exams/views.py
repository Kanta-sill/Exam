from django.shortcuts import render, redirect
from .models import Exam, Category, Question, Ques_Exam
from .forms import QuesForm
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from .serializers import Qu_Ex_serializer

# Create your views here.

@login_required()
def index(request):
    exam_list=Exam.objects.all()
    return render(request, 'exam/index.html', {'exam_list':exam_list})

@login_required()
def detail(request, item_id):
    item=Exam.objects.get(pk=item_id)
    return render(request, 'exam/detail.html', {'item':item})

# question:
@login_required()
def ques_view(request):
    ques_list=Question.objects.all()
    return render(request, 'exam/question.html', {'ques_list':ques_list})

@login_required()
def ques_detail(request, ques_id):
    ques=Question.objects.get(pk=ques_id)
    return render(request, 'exam/ques_detail.html', {'ques':ques})

@login_required()
def ques_delete(request, ques_id):
    ques=Question.objects.get(id=ques_id)
    if request.method=='POST':
        ques.delete()
        return redirect('exam:question')
    return render(request, 'exam/ques_delete.html', {'ques':ques})

@login_required()
def ques_create(request):
    form=QuesForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('exam:question')
    return render(request, 'exam/ques_form.html', {'form':form})

@login_required()
def ques_update(request, ques_id):
    ques=Question.objects.get(id=ques_id)
    form=QuesForm(request.POST or None, instance=ques)
    if form.is_valid():
        form.save()
        return redirect('exam:question')
    return render(request, 'exam/ques_form.html', {'form':form, 'ques':ques})

class Qu_ExViewset(viewsets.ModelViewSet):
    queryset = Ques_Exam.objects.all()
    serializer_class = Qu_Ex_serializer
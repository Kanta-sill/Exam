from django.urls import path, include
from . import views
from rest_framework import routers

router=routers.SimpleRouter()
router.register('ques', views.Qu_ExViewset)

app_name='exam'

urlpatterns = [
    path('quesviewset/', include(router.urls)),
    path('', views.index, name='index'),
    path('<int:item_id>',views.detail, name='detail'),

    path('question/', views.ques_view, name='question'),
    path('question/<int:ques_id>', views.ques_detail, name='ques_detail'),
    path('question/add/', views.ques_create, name='ques_create'),
    path('update/<int:ques_id>', views.ques_update, name='ques_update'),
    path('question/delete/<int:ques_id>', views.ques_delete, name='ques_delete'),
]
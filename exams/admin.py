from django.contrib import admin
from .models import Exam, Category, Question, Ques_Exam

# Register your models here.

admin.site.site_header="Exam Online"
admin.site.site_title="BTEC Exam Online"
admin.site.index_title="Manage Exam"

class ExamAdmin(admin.ModelAdmin):
    list_display = ('admin', 'title', 'duration', 'type')
    search_fields = ('title', )

admin.site.register(Exam, ExamAdmin)
admin.site.register(Category)
admin.site.register(Question)
admin.site.register(Ques_Exam)
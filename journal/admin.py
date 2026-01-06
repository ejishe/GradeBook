from django.contrib import admin

from journal.models import *


@admin.register(Group, Student, Subject, Lesson, LessonResult)
class GroupAdmin(admin.ModelAdmin):
    pass

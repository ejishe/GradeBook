from django.db import models

class Group(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=50)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='students')

    def __str__(self):
        return self.name


class Subject(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Lesson(models.Model):
    lesson_types = [
        ('lecture', 'Лекция'),
        ('practice', 'Практика')
    ]

    date = models.DateField(auto_now_add=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='lessons')
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='lessons')
    lesson_type = models.CharField(max_length=20, choices=lesson_types)

    def __str__(self):
        return str(self.subject)


class LessonResult(models.Model):
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name='results'
    )

    lesson = models.ForeignKey(
        Lesson,
        on_delete=models.CASCADE,
        related_name='results'
    )

    attended = models.BooleanField(default=False)

    practice_score = models.IntegerField(null=True, blank=True)
    lab_score = models.IntegerField(null=True, blank=True)
    homework_score = models.IntegerField(null=True, blank=True)
    card_score = models.IntegerField(null=True, blank=True)

    class Meta:
        unique_together = ('student', 'lesson')

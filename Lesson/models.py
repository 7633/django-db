# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Authorship(models.Model):
    user = models.ForeignKey('User', models.DO_NOTHING)
    course = models.ForeignKey('Course', models.DO_NOTHING)

    class Meta():
        managed = False
        db_table = 'authorship'
        unique_together = (('user', 'course'),)


class Course(models.Model):
    course_name = models.CharField(max_length=45, blank=False, null=True)
    description = models.CharField(max_length=45, blank=False, null=True)
    start = models.DateField(blank=False, null=True)
    finish = models.DateField(blank=False, null=True)
    students = models.ManyToManyField('User', through='Education', related_name='students', blank=True)
    authors = models.ManyToManyField('User', through='Authorship', related_name='authors', blank=False)

    class Meta():
        managed = False
        db_table = 'course'

    def __str__(self):
        return self.course_name


class Discussion(models.Model):
    text = models.CharField(max_length=45, blank=True, null=True)
    lesson = models.ForeignKey('Lesson', models.DO_NOTHING)
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)

    class Meta():
        managed = False
        db_table = 'discussion'


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta():
        managed = False
        db_table = 'django_migrations'


class Education(models.Model):
    user = models.ForeignKey('User', models.DO_NOTHING)
    course = models.ForeignKey(Course, models.DO_NOTHING)

    class Meta():
        managed = False
        db_table = 'education'
        unique_together = (('user', 'course'),)


class Lesson(models.Model):
    name = models.CharField(max_length=45, blank=False, null=True)
    course = models.ForeignKey(Course, models.DO_NOTHING, blank=False)
    lesson_type = models.ForeignKey('LessonType', models.DO_NOTHING, blank=False)
    students = models.ManyToManyField('User', through='UserHasLesson', blank=True)

    class Meta():
        managed = False
        db_table = 'lesson'

    def __str__(self):
        return '[' + self.course.course_name + '] ' + self.name


class LessonType(models.Model):
    type_name = models.CharField(max_length=45, blank=False, null=True)

    class Meta():
        managed = False
        db_table = 'lesson_type'

    def __str__(self):
        return self.type_name


class Submission(models.Model):
    result = models.BooleanField(blank=False)
    #user_has_lesson_id = models.ForeignKey('UserHasLesson', models.DO_NOTHING, related_name='uhl_id')

    class Meta():
        managed = False
        db_table = 'submission'


class User(models.Model):
    first_name = models.CharField(max_length=45, blank=False, null=True)
    last_name = models.CharField(max_length=45, blank=False, null=True)
    email = models.CharField(max_length=45, blank=False, null=True)

    class Meta():
        managed = False
        db_table = 'user'

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class UserHasLesson(models.Model):
    user = models.ForeignKey(User, models.DO_NOTHING)
    lesson = models.ForeignKey(Lesson, models.DO_NOTHING)

    class Meta():
        managed = False
        db_table = 'user_has_lesson'
        unique_together = (('user', 'lesson'),)

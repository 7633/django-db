from django.contrib import admin
from Lesson.models import Course, Lesson, User, LessonType, Discussion, Submission, Authorship, Education, UserHasLesson


class AuthorshipInline(admin.StackedInline):
    model = Authorship
    extra = 1


class AuthorshipUserInline(admin.StackedInline):
    model = Authorship
    extra = 0


class EducationInline(admin.TabularInline):
    model = Education
    extra = 0


class LessonApplyInline(admin.StackedInline):
    model = UserHasLesson
    extra = 0


class LessonInline(admin.TabularInline):
    model = Lesson
    fk_name = "course"
    extra = 2


class CourseAdmin(admin.ModelAdmin):
    inlines = [
        AuthorshipInline,
        EducationInline,
        LessonInline,
    ]


class UserAdmin(admin.ModelAdmin):
    inlines = [
        AuthorshipUserInline,
        EducationInline,
        LessonApplyInline,
    ]


# class LessonAdmin(admin.ModelAdmin):
#     inlines = [
#         LessonApplyInline,
#     ]


# Register your models here.
admin.site.register(Course, CourseAdmin)
admin.site.register(User, UserAdmin)
admin.site.register([LessonType, Discussion])
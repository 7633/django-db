from django.shortcuts import render, get_object_or_404

# Create your views here.
from Lesson.models import Course, Discussion, Lesson
# from Lesson.forms import CommentForm
from django.views.decorators.csrf import csrf_protect

def home(request):
    courses = Course.objects.all()
    context = {
        'courses': courses
    }
    return render(request, 'Lesson/courses.html', context)


def show_course(request, course_id=1):
    course = get_object_or_404(Course, id=course_id)
    return render(request, "Lesson/course.html",
                  {'course': course,
                   'lesson': Lesson.objects.filter(course_id=course_id)})


def show_lesson(request, course_id=1, lesson_id=1):
    return render(request, "Lesson/lesson.html",
                  {
                      'lesson': Lesson.objects.filter(course_id=course_id, id=lesson_id),
                      'discussion': Discussion.objects.filter(lesson_id=lesson_id)
                   })
#
# # def add_comment():

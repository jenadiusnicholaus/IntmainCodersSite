from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.core import serializers

from .models import *


def home(request):
    course_query = Courses.objects.all()
    scheduling_class = SchedulingClass.objects.all()
    course_instructors = CourseInstructor.objects.all()
    events = Events.objects.all()
    context = {
        'courses': course_query,
        'scheduling_class': scheduling_class,
        'course_instructor': course_instructors,
        'events': events
    }
    return render(request, template_name='index.html', context=context)


def about(request):
    return render(request, template_name='about.html')


def contact(request):
    return render(request, template_name='contact.html')


def course(request):
    return render(request, template_name='courses.html')


class CourseDetails(View):
    def get(self, request, pk=None, *args, **kwargs):
        course_details = Courses.objects.get(pk=pk)

        context = {
            'course_details': course_details
        }
        return render(request, template_name='course-details.html', context=context)

    def post(self, request, pk=None, *args, **kwargs):
        pass


def events(request):
    return render(request, template_name='events.html')


def trainers(request):
    return render(request, template_name='trainers.html')


def pricing(request):
    return render(request, template_name='pricing.html')


def boolForClass(request, ):
    if request.method == 'POST':
        # Get product id from request
        id = request.POST.get('id')
        schedulingClass = get_object_or_404(SchedulingClass, pk=id)
        luser = request.user
        if schedulingClass.user.filter(id=luser.pk).exists():
            return JsonResponse({'messages': 'You already booked'}, content_type='application/json')
        else:
            schedulingClass.user.add(luser)
            menuitem = SchedulingClass.objects.filter(id=id).all()
            # Turn query response into JSON
            data = serializers.serialize('json', menuitem)
            data1 = {
                'messages': 'Thanks for Joining the class',
                'sclass': str(menuitem)
            }
            # Return a HttpResponse containing the JSON data
            return JsonResponse(data1, content_type='application/json')
    else:
        return JsonResponse({'Error': 'Error occurred'}, content_type='application/json')

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.core import serializers
from django.views.decorators.csrf import csrf_protect
import pprint


from .models import *


def home(request):
    course_query = Courses.objects.all()[:6]
    scheduling_class = SchedulingClass.objects.all()
    course_instructors = CourseInstructor.objects.all()
    events = Events.objects.all()
    scheduling_day = SchedulingDay.objects.all()
    context = {
        'courses': course_query,
        'scheduling_class': scheduling_class,
        'course_instructor': course_instructors,
        'events': events,
        'scheduling_day': scheduling_day
    }
    return render(request, template_name='intmain.html', context=context)


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


def boolForClass(request):
    if request.method == 'POST':
        # Get product id from request
        sclassid = request.POST.get('id')
        schedulingClass = get_object_or_404(SchedulingClass, pk=sclassid)
        luser = request.user
        if schedulingClass.user.filter(id=luser.pk).exists():
            return JsonResponse({'messages': 'You already booked'}, content_type='application/json')
        else:
            schedulingClass.user.add(luser)
            menuitem = SchedulingClass.objects.filter(id=sclassid).all()
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


def dayClassList(request,):
    if request.method == 'POST':
        # Get product id from request
        id = request.POST.get('id')
        schedulingday = get_object_or_404(SchedulingDay, pk=id)
        classList = []
        for clss in schedulingday.scheduling_class.all():
            data = {
                "class_id": clss.id,
                "scheduling_time": f'{clss.starting_date} - {clss.starting_time}',
                "course": {
                    "title":clss.course.title,
                    "desc": clss.course.description
                },
                "course_instructor": {
                    "name": clss.course.course_instructor.getFullname(),
                    "profile": clss.course.course_instructor.getInstructorProfilePicture(),
                    "profession":clss.course.course_instructor.profession
                }
            }
            classList.append(data)

        data1 = {
            'messages': 'Thanks for Joining the class',
            'sclass':  classList

        }

        # Return a HttpResponse containing the JSON data
        return JsonResponse(classList, content_type='application/json',  safe=False)

    return HttpResponse("It is not  post request")


def news(request):
    return render(request, template_name='news.html')


def news_details(request):
    return render(request, template_name='news-details.html')


def test_ajax(request):
    if rquest.is_ajax and request.method == 'POST':
         return JsonResponse({"instance": 'is an ajax request'}, status=200)
    else:
        return JsonResponse({"error": "is not an ajax request"}, status=400)






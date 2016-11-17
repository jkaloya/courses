from django.shortcuts import render, HttpResponse, redirect
from .models import Courses, Description

def index(request):
    courses = Courses.objects.all()
    descriptions = Description.objects.all()
    context={
        "courses": courses,
        "descriptions": descriptions
    }
    return render(request, 'coursesapp/index.html', context)

def create(request):
    course = Courses.objects.create(name=request.POST['name'])
    Description.objects.create(courses=course, description=request.POST['description'])
    print 'hello'
    return redirect('/')

def remove(request, id):
    course = Courses.objects.get(id=id)
    description = Description.objects.get(courses=course)
    context = {
        'course': course,
        'description': description,
    }
    return render(request, 'coursesapp/remove.html', context)

def delete(request, id):
    Courses.objects.filter(id=id).delete()
    return redirect('/')

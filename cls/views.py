from django.shortcuts import redirect, render
from django.http import HttpResponse

from cls.filters import StudentFilter,CourseFilter
from course.models import Course
from .forms import ClassCreateForm, ClassUpdateForm
from .models import Class
from student.models import student

from django.contrib.admin.views.decorators import staff_member_required

# Create your views here.

@staff_member_required(login_url='/')
def index(request):
    uDept = request.user.department
    # return render()
    return HttpResponse("helo")

@staff_member_required(login_url='/')
def create(request):
    uDept = request.user.department
    # getting students of the department
    s = student.objects.filter(user__department=uDept, cls=None)
    # getting course of the department
    co = Course.objects.filter(dept=uDept)
    filter = StudentFilter(request.GET, queryset=s)
    cfilter = CourseFilter(request.GET, queryset=co)
    form = ClassCreateForm(request.POST or None, students=s,course=co)
    context = {
        'form': form,
        'filter1': filter,
        'cfilter': cfilter
        
    }
    if request.method == 'POST':
        form = ClassCreateForm(request.POST, students=s,course=co)
        if form.is_valid():
            body = request.POST.dict()
            students = dict(request.POST)['students']
            course=dict(request.POST)['course']
            print(course)
            c = Class(class_name=body['name'], department=uDept)
            c.save()
            for obj in students:
                s = student.objects.get(pk=obj)
                s.cls = c
                s.course.add(*course)
                s.save()
    return render(request, 'cls/form.html', context)


@staff_member_required(login_url='/')
def update(request, id):
    uDept = request.user.department
    c = Class.objects.get(pk=id)
    in_class = student.objects.filter(cls=c, user__department=uDept)
    out_class = student.objects.filter(cls=None, user__department=uDept)
    inStudentFilter = StudentFilter(request.GET, queryset=in_class)
    in_class = inStudentFilter.qs

    outStudentFilter = StudentFilter(request.GET, queryset=out_class)
    out_class = outStudentFilter.qs
    
    form = ClassUpdateForm(request.POST or None, instance=c, in_class=in_class, out_class=out_class)
    
    if request.method == 'POST' and form.is_valid():
        form.save()
        in_cstudents = dict(request.POST)['students in class']
        out_cstudents = dict(request.POST)['students not in class']
        for obj in out_cstudents:
            s = student.objects.get(pk=obj)
            # AssignCourse.course_assign(s, c)
            
            s.cls = c
            s.save()
        for obj in in_cstudents:
            s = student.objects.get(pk=obj)
            s.cls = None
            s.save()

    
    context = {
        "form":form,
        "filter1": inStudentFilter
    }
    return render(request, 'cls/form.html', context)
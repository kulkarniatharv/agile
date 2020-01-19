import datetime
import json
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from attendance.models import eDetail, AttendReport
from django.contrib.gis.geos import Point, Polygon
from django.contrib.gis.db.models.functions import Distance

# Create your views here.

def home(request):
    return render(request, 'index.html')

def emp_form(request):
    return render(request, 'emp_form.html')

def about(request):
    return render(request, 'about1.html')

def contact(request):
    return render(request, 'contacts.html')

def check_emp_code(request):
    eCode = request.POST["emp_code"]

    e_detail = eDetail.objects.filter(eID__exact=eCode).all()

    if (e_detail):
       
        for employee in e_detail:
            print(employee)
            context = {
                'employee': employee
            }

        return render(request, 'location.html', context)
    else:
        return HttpResponseRedirect('/attendance/')


def check_location(request):

    fences = {
        'I2IT': Polygon((
            (18.583211,73.737035),
            (18.585046, 73.738399),
            (18.585465, 73.737871),
            (18.584972, 73.737445),
            (18.585641, 73.736537),
            (18.584362,73.735507),
            (18.583211,73.737035)
        )),
    }

    

    eCode = request.POST["employeeID"]
    
    employee_set = eDetail.objects.filter(eID__exact=eCode)

    for employee in employee_set:
        latitude = float(request.POST.get("lat",0.0)) #18.5846382 
        longitude = float(request.POST.get("lon",0.0)) #73.7366744
        print(latitude, longitude)
        user_location = Point(latitude, longitude, srid=4326)

        branch = employee.office_branch
        print(branch)

        if (branch in fences):
            inFence = fences[branch].contains(user_location)
            print('branch found')

            if(inFence):
                today = datetime.date.today()
                now = datetime.datetime.now()
                record = AttendReport(date=today, office_branch=branch, eID=employee, attendStatus='p', time_in=now)
                print('record created!')

                if(AttendReport.objects.filter(eID__exact=employee.eID).count() == 0):
                    record.save()
                    print('record saved!')
                    return render(request, 'attend_success.html')
        
        return render(request, 'attend_failed.html')
    
    





















def get_uloc(request, branch):
    fence = get_object_or_404(GeoPolygon, office_branch=branch)

    if request.method == 'POST':
        
        #Create a form instance and populate it with data from the request
        form = getLocation(request.POST)

        #check if the form is valid
        if form.is_valid():
            #process the data in form.cleaned_data as required
            if (fence.polygon.contains(form.point)):
                return HttpResponseRedirect(reverse('home'))
    
    else:
        form = getLocation()

        context = {
            'form': form,
            'fence': fence,
        }

    return render(request, location.html, context)
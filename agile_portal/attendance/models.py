from django.db import models
from django.contrib.gis.db import models

# Create your models here.

class AttendReport(models.Model):
    date = models.DateField()
    #office_branch = models.ForeignKey('GeoPolygon', on_delete=models.CASCADE, null=True)
    office_branch = models.CharField(max_length=50, default='I2IT')
    eID = models.ForeignKey('eDetail', on_delete=models.CASCADE, null=True)

    ATTEND_VALUES = (
        ('p', 'Present'),
        ('a', 'Absent'),
    )

    attendStatus = models.CharField(max_length=1, choices=ATTEND_VALUES, default='a' ,help_text='Attendance Status',)
    time_in = models.DateTimeField(null=True)

    class Meta:
        ordering = ['date']

    def __str__(self):
        return f'{self.eID} is {self.attendStatus}'

class GeoPolygon(models.Model):
    polygon = models.PolygonField()
    office_branch = models.CharField(primary_key=True, max_length=50)

    def __str__(self):
        return self.office_branch

#class Cur_location(models.Model):
class eDetail(models.Model):
    eID = models.IntegerField(primary_key=True, help_text="Employee ID", default=1)
    Name = models.CharField(max_length=30)
    contact = models.IntegerField()
    mail = models.CharField(max_length=50, blank=True, null=True)
    #office_branch = models.ForeignKey('GeoPolygon', on_delete=models.CASCADE)
    office_branch = models.CharField(max_length=20)

    def __str__(self):
        return self.Name

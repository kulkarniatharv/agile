from django.db import models

# Create your models here.


class aReports(models.Model):
    date = models.DateField()
    geoLocation = models.ForeignKey('GeoLocation', on_delete=models.CASCADE)
    eID = models.ForeignKey('eDetails', on_delete=models.CASCADE)

    ATTEND_VALUES = (
        ('p', 'Present'),
        ('a', 'Absent'),
    )

    attendStatus = models.CharField(max_length=1, choices=ATTEND_VALUES, default='a' ,help_text='Attendance Status',)

    class Meta:
        ordering = ['date']

    def __str__(self):
        return f'{self.eID} is {self.attendStatus}'


class GeoLocation(models.Model):
    lat = models.FloatField()
    lon = models.FloatField()

    office_branch = models.CharField(max_length=50, help_text='Enter the Branch of the office at the location given by latitude and longitude')

    def __str__(self):
        return self.office_branch

class eDetails(models.Model):
    eID = models.CharField(max_length=10)
    name = models.CharField(max_length=30)
    contact = models.IntegerField()
    email = models.CharField(max_length=40)
    office_branch = models.ForeignKey('GeoLocation', on_delete=models.CASCADE)

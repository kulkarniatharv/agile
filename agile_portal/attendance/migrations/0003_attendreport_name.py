# Generated by Django 3.0.2 on 2020-01-19 12:30

from django.db import migrations, models

# def add_polygons(apps, schema_editor):
#     GeoPolygon = apps.get_model('GeoPolygon')

#     poly = (
#         (18.583211,73.737035),
#         (18.585046, 73.738399),
#         (18.585465, 73.737871),
#         (18.584972, 73.737445),
#         (18.585641, 73.736537),
#         (18.584362,73.735507),
#         (18.583211,73.737035)
#     )
#     try:
#         GeoPolygon(polygon=poly, office_branch='i2it').save()
#     except KeyError:
#         pass

class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0002_auto_20200119_1747'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendreport',
            name='name',
            field=models.CharField(blank=True, max_length=20),
        ),
        # migrations.RunPython(add_polygons),
    ]
# Generated by Django 3.1.7 on 2021-03-02 12:47

from django.db import migrations, models
import json
import random


def add_branches(apps, schema_editor):
    with open("objectsgenerator/branches.json", "r") as file:
        data = json.load(file)

    Branch = apps.get_model("mainapp", "Branch")

    for i in data:
        new_obj = Branch(branch_name=i['branch_name'], facade_image=i['facade_image'], latitude=i['latitude'],
                         longitude=i['longitude'])
        new_obj.save()


def add_employees(apps, schema_editor):
    with open("objectsgenerator/persons.json", "r") as file:
        data = json.load(file)

    Employee = apps.get_model("mainapp", "Employee")
    Branch = apps.get_model("mainapp", "Branch")

    for i in data:
        new_obj = Employee(last_name=i['last_name'], first_name=i['first_name'], position_title=i['position_title'],
                           branch_name=Branch.objects.get(id=random.randint(1, 10)))
        new_obj.save()


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_branches),
        migrations.RunPython(add_employees),
    ]

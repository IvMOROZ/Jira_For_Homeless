from django.test import TestCase

# Create your tests here.

import datetime
from django.contrib.auth.models import User
from django.utils import timezone
from base.models import Assignment, Task


class TaskModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test method
        test_user = User.objects.create(username='testuser')
        Task.objects.create(title='test_title', description='test_description', owner=test_user)

    def test_title_label(self):
        task = Task.objects.get(id=1)
        field_label = task._meta.get_field('title').verbose_name
        self.assertEquals(field_label, 'title')

    def test_description_label(self):
        task = Task.objects.get(id=1)
        field_label = task._meta.get_field('description').verbose_name
        self.assertEquals(field_label, 'description')

    def test_title_max_length(self):
        task=Task.objects.get(id=1)
        max_length = task._meta.get_field('title').max_length
        self.assertEquals(max_length,50)

    def test_description_max_length(self):
        task=Task.objects.get(id=1)
        max_length = task._meta.get_field('description').max_length
        self.assertEquals(max_length,500)

    def test_get_current_time(self):
        task=Task.objects.get(id=1)
        created_time = task.created_time
        self.assertEquals(created_time.hour,datetime.datetime.now().hour)

    def test_modified_time(self):
        task=Task.objects.get(id=1)
        modified_time = task.modified_time
        self.assertFalse(modified_time)


class AssignmentTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test method
        test_user = User.objects.create(username='testuser')
        Assignment.objects.create(student=test_user)

    def test_assigment_exist(self):
        sign=Assignment.objects.get(id=1)
        status=sign._meta.get_field('status').verbose_name
        self.assertEquals(status, 'status')

    def test_assigment_value(self):
        sign=Assignment.objects.get(id=1)
        status=sign.status
        self.assertEquals(status, 1)

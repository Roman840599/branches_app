from django.test import TestCase
from .models import Branch, Employee


class BranchTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_branch = Branch.objects.create(
            branch_name='TestBranch', facade_image='default.jpg', latitude='20.123456789', longitude='21.123456789')
        test_branch.save()
        test_employee = Employee.objects.create(
            first_name='TestEmployeeName', last_name='TestEmployeeLastName', position_title='python',
            branch_name=Branch.objects.get(branch_name='TestBranch'))
        test_employee.save()

    def test_branch_content(self):
        inst = Branch.objects.get(branch_name='TestBranch')

        facade_image = f'{inst.facade_image}'
        latitude = f'{inst.latitude}'
        longitude = f'{inst.longitude}'
        self.assertEqual(facade_image, 'default.jpg')
        self.assertEqual(latitude, '20.123456789')
        self.assertEqual(longitude, '21.123456789')

    def test_employee_content(self):
        inst = Employee.objects.get(first_name='TestEmployeeName')

        last_name = f'{inst.last_name}'
        position_title = f'{inst.position_title}'
        branch_name = f'{inst.branch_name}'
        self.assertEqual(last_name, 'TestEmployeeLastName')
        self.assertEqual(position_title, 'python')
        self.assertEqual(branch_name, 'TestBranch')
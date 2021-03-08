from rest_framework import serializers
from mainapp.models import Employee, Branch


class BranchSerializer(serializers.HyperlinkedModelSerializer):
    employees = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='employee-detail')

    class Meta:
        model = Branch
        fields = (
            'url',
            'pk',
            'branch_name',
            'facade_image',
            'latitude',
            'longitude',
            'employees'
        )


# This serializer is designed for displaying branches list without employees field (for comfort displaying
# without thousands of employees).
class BranchSerializerLimited(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = (
            'url',
            'pk',
            'branch_name',
            'facade_image',
        )


class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    branch_name = serializers.SlugRelatedField(queryset=Branch.objects.all(), slug_field='branch_name')

    class Meta:
        model = Employee
        fields = (
            'url',
            'first_name',
            'last_name',
            'position_title',
            'branch_name'
        )

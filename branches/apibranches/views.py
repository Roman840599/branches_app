from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from . import custompermissions
from mainapp.models import Employee, Branch
from .serializers import BranchSerializer, EmployeeSerializer, BranchSerializerLimited
from .geo_script import find_distance


class ClothestBranchList(generics.ListCreateAPIView):
    serializer_class = BranchSerializer

    def get_queryset(self):
        lat0 = float(self.kwargs['lat'])
        lng0 = float(self.kwargs['lng'])
        min_distance = 10000
        queryset = Branch.objects.all()
        for instance in queryset:
            lat1 = float(instance.latitude)
            lng1 = float(instance.longitude)
            distance = find_distance(lat1, lng1, lat0, lng0)
            if distance < min_distance:
                min_distance = distance
                min_distance_id = instance.id
        return Branch.objects.filter(pk=min_distance_id)


class BranchList(generics.ListCreateAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializerLimited
    name = 'branch-list'
    filter_fields = (
        'branch_name',
    )
    permission_classes = (
        custompermissions.IsCurrentUserCEO,
    )


class BranchDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer
    name = 'branch-detail'
    permission_classes = (
        custompermissions.IsCurrentUserCEO,
    )


class EmployeeList(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    name = 'employee-list'
    filter_fields = (
        'branch_name',
    )
    search_fields = (
        '^last_name',
    )
    ordering_fields = (
        'first_name',
        'last_name',
        'position_title',
        'branch_name',
    )


class EmployeeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    name = 'employee-detail'


class ApiRoot(generics.GenericAPIView):
    name = 'api-root'

    def get(self, request, *args, **kwargs):
        return Response({
            'branches': reverse(BranchList.name, request=request),
            'employees': reverse(EmployeeList.name, request=request),
        })

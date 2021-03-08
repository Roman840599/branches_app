from rest_framework import permissions


class IsCurrentUserCEO(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        users_group = request.user.groups.all()
        for i in users_group:
            if str(i) == 'CEO':
                return True

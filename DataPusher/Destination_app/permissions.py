from rest_framework.permissions import BasePermission

class AuthenticateOrNot(BasePermission):

    message = 'You are not allowed here'
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        else:
            return False
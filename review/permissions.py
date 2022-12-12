from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAuthorOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            # if only reading
            return True
        if request.user.is_authenticated:
            # if we have uses
            return True
        # if request.user == obj.author:
        #     # if user(polzovatel) - author comments (reting)
        #     return True
        

    # PUT, PATCH, GET(withbid), DELETE
    def has_object_permission(self, request, view, obj):
        # if result False - 403 Forbidden
        if request.method in SAFE_METHODS:
            # if only reading
            return True
        if not request.user.is_authenticated:
            # if we don't have uses
            return False
        if request.user == obj.author:
            # if user(polzovatel) - author comments (reting)
            return True






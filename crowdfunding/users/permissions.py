# from rest_framework import permissions

# class IsSuperuserOrOwner(permissions.BasePermission):

#     # edit_methods = ("POST")

#     # def has_permission(self, request, view):
#     #     if request.user.is_superuser:
#     #         return True

#     def has_object_permission(self, request, view, obj, pk):
#         if request.user.is_superuser or pk==request.user.pk:
#             return True
        
#         # if request.user.is_authenticated and request.method in self.edit_methods:
#         #     return True
#         return False



# class IsSuperuserOrPostOnly(permissions.BasePermission):

#     edit_methods = ("POST")

#     # def has_permission(self, request, view):
#     #     if request.user.is_superuser:
#     #         return True

#     def has_object_permission(self, request, view, obj):
#         if request.user.is_superuser or (request.user.is_authenticated and request.method in self.edit_methods):
#             return True
        
#         # if request.user.is_authenticated and request.method in self.edit_methods:
#         #     return True
#         return False

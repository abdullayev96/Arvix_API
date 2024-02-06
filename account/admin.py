from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin




class CustomUserAdmin(UserAdmin):

    list_display  = ['id','full_name',"middle_name","number",'username', 'email','password','staff', 'active']
    list_filter = ['email','password', 'staff', 'active']

    # fieldsets = (
    #           (None, {"fields": ("username", "password")}),
    #           ("Permissions", {"fields": ("email", "is_staff", "is_active", "groups", "user_permissions")}),
    # )
    # add_fieldsets = (
    #           (None, {
    #                     "classes": ("wide",),
    #                     "fields": (
    #                               "username", "password1", "password2", "is_staff",
    #                               "email", "is_active", "groups", "user_permissions"
    #                     )}
    #            ),
    # )
    search_fields = ["email","full_name"]
    ordering = ("email",)


admin.site.register(CustomUser, CustomUserAdmin)



from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth.models import User
from users.models import User
from django.contrib.auth.admin import UserAdmin
from .models import TeacherProfile

Desc = 'Add College Email-ID'


class UserAdminConfig(UserAdmin):
    model = User
    search_fields = ('email', 'first_name', 'last_name')
    list_filter = ( 'email', 'is_active', 'is_staff', 'is_superuser')
    ordering = ('email',)
    list_display = ( 'email', 'first_name', 'last_name',
                    'is_active', 'is_staff')
    fieldsets = (
        ('Section 1', {'fields': ('email', 'first_name', 'last_name', 'middle_name','department' ,),
                       'description': '%s' % Desc,

                       }),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_classteacher', 'is_hod', 'is_superuser'),
                         'classes': ('collapse',),
                         }),

    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'middle_name','department' ,'password1', 'password2', )
            }),
            
            ('Permissions', {'fields': ('is_active', 'is_staff', 'is_classteacher', 'is_hod', 'is_superuser',),
            'classes': ('collapse',),
        }),
    )

    search_fields=('email',)
    ordering=('email',)


class Admin(admin.AdminSite):
    site_header = 'SAS'

# admin.site.unregister(User)


admin_site = Admin(name='SAS')

admin.site.register(User, UserAdminConfig)

admin.site.register(TeacherProfile)
# admin_site.register(TeacherProfile)

# class UserTeacherConfig(UserAdminConfig):
#     model = TeacherProfile
#     search_fields = ('teacherID', 'department', 'course', 'semester',)
#     list_filter = ('teacherID','department', 'course', 'is_classteacher')
#     ordering = ('teacherID',)
#     list_display = ('teacherID','department', 'semester',
#                     'course', 'is_classteacher')
#     fieldsets = (
#         ('Section 1', {'fields': ('teacherID', 'department', 'course', 'semester',),


#         }),
#         ('Permissions', {'fields': ('is_classteacher'),
#                          'classes': ('collapse',),
#         }),

#     )

#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('teacherID', 'department',  'semester', 'course','is_classteacher')}
#          ),
#     )
# admin.site.register(TeacherProfile, UserTeacherConfig )

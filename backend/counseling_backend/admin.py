from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, CounselorProfile, ClientProfile, Course, CourseContent, ClientCourseProgress, Session, Payment, BlogPost, ForumPost, ClientFile, Consent, AITriage
from django.apps import AppConfig

class CounselingBackendConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'counseling_backend'
    
class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'role', 'is_staff', 'is_superuser', 'created_at')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('role',)}),
        ('Permissions', {'fields': ('is_staff', 'is_superuser', 'is_deleted', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('created_at', 'updated_at')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'role', 'is_staff', 'is_superuser', 'is_deleted'),
        }),
    )
    search_fields = ('email',)
    ordering = ('email',)

admin.site.register(User, CustomUserAdmin)
admin.site.register(CounselorProfile)
admin.site.register(ClientProfile)
admin.site.register(Course)
admin.site.register(CourseContent)
admin.site.register(ClientCourseProgress)
admin.site.register(Session)
admin.site.register(Payment)
admin.site.register(BlogPost)
admin.site.register(ForumPost)
admin.site.register(ClientFile)
admin.site.register(Consent)
admin.site.register(AITriage)
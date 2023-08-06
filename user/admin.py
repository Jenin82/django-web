from typing import Set
from .models import UserProfile
from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

def is_member(user):
    return user.is_superuser or user.groups.filter(name='admin_cse').exists()

class CustomUserAdmin(UserAdmin):
	def get_form(self, request, obj=None, **kwargs):
		form = super().get_form(request, obj, **kwargs)
		is_superuser = request.user.is_superuser
		disabled_fields = set()  # type: Set[str]

		if not is_member(request.user):
				disabled_fields |= {
						'is_superuser',
						'groups',
						'user_permissions',
				}
    
		if is_member(request.user):
				disabled_fields |= {
						'is_superuser',
						'user_permissions',
				}
    
    
			# Prevent non-superusers from editing their own permissions
		if (
				not is_superuser
				and obj is not None
				and obj == request.user
		):
				disabled_fields |= {
						'is_staff',
						'is_superuser',
						'groups',
						'user_permissions',
				}

		for f in disabled_fields:
				if f in form.base_fields:
						form.base_fields[f].disabled = True

		return form

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'mobile', 'user_class', 'img')

admin.site.register(UserProfile, UserProfileAdmin)



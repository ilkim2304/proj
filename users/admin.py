from django.contrib import admin
from .models import User

class UserAdmin(admin.ModelAdmin):
    search_fields = ["id", "username", "second_name"]

    def id(self, obj):
        return [obj.id]

    def username(self, obj):
        return [obj.username]

    def email(self, obj):
        return obj.email

    list_display = ["id", "username", "email"]

admin.site.register(User, UserAdmin)

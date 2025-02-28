from django.contrib import admin
from .models import UserData  # Import your model

@admin.register(UserData)
class UserDataAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "gender", "mobile")  # Columns to display

# OR just use: admin.site.register(UserData)


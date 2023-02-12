from django.contrib import admin
from .models.current_loans import Current
from .models.loan_history import Log

# Register your models here.
admin.site.register(Log)
admin.site.register(Current)
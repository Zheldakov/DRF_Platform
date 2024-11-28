from django.contrib import admin
from users.models import User
# Регистрируем модель User в административной панели Django
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Отображение в админ панели пользователей"""
    list_display = ('id','email','first_name','last_name', 'is_active',) # Показываем поля в списке модели
    list_filter = ('id','email',) # Фильтрация
    ordering = ('id',)
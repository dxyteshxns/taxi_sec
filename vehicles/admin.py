from django.contrib import admin

from .models import Vehicle


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'car_number', 'car_model', 'driver',
        'seats', 'year', 'color', 'is_active', 'created_at'
    ]
    list_filter = ['is_active', 'seats', 'year', 'created_at']
    search_fields = ['car_number', 'car_model', 'driver__user__email', 'color']
    readonly_fields = ['created_at', 'updated_at']
    list_editable = ['is_active']
    
    fieldsets = (
        ('Driver', {
            'fields': ('driver',)
        }),
        ('Vehicle Information', {
            'fields': ('car_number', 'car_model', 'seats', 'year', 'color', 'photo')
        }),
        ('Status', {
            'fields': ('is_active',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at')
        }),
    )
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.select_related('driver', 'driver__user')

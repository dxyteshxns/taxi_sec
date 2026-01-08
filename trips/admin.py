from django.contrib import admin

from .models import Trip


@admin.register(Trip)
class TripAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'rider', 'driver', 'origin', 'destination',
        'status', 'price', 'created_at'
    ]
    list_filter = ['status', 'created_at']
    search_fields = ['rider__email', 'driver__user__email', 'origin', 'destination']
    readonly_fields = ['created_at', 'updated_at']
    list_editable = ['status']
    
    fieldsets = (
        ('Trip Information', {
            'fields': ('rider', 'driver', 'origin', 'destination', 'comment')
        }),
        ('Status & Price', {
            'fields': ('status', 'price')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at')
        }),
    )
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.select_related('rider', 'driver', 'driver__user')

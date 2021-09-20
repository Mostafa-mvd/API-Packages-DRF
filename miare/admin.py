from django.contrib import admin
from miare.models import Capacity, Area, Courier, Shift, CourierShift


@admin.register(Courier)
class CourierAdmin(admin.ModelAdmin):
    list_display = ['name', ]


@admin.register(Shift)
class ShiftAdmin(admin.ModelAdmin):
    list_display = ['start', 'end']


@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    list_display = ['name', ]


@admin.register(Capacity)
class CapacityAdmin(admin.ModelAdmin):
    list_display = ['id', 'shift', 'area', 'date', 'capacity', ]
    # ordering = ['date', '-area', 'shift']


@admin.register(CourierShift)
class AdminCourierShift(admin.ModelAdmin):
    list_display = ['courier', 'shift', 'area', 'shift_begin', 'shift_end']
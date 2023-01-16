from django.contrib import admin

from django.contrib import admin
from .models import Employee, LeaveRequest

admin.site.site_header = "Manage Leave Requests"
admin.site.site_title = "Manage Leave Requests"

class LeaveRequestAdmin1(admin.ModelAdmin):
    actions = ['approve_leave_request', 'reject_leave_request']
    list_display = ('employee', 'type_of_leave', 'start_date', 'end_date', 'status')
    list_filter = ('status', 'type_of_leave')

    def approve_leave_request(self, request, queryset):
        queryset.update(status='approved')
    approve_leave_request.short_description = "Approve selected leave requests"

    def reject_leave_request(self, request, queryset):
        queryset.update(status='rejected')
    reject_leave_request.short_description = "Reject selected leave requests"





class EmployeeAdmin1(admin.ModelAdmin):
    actions = ['change_employee_status']
    list_display = ('user', 'nom', 'department', 'position')
    # list_filter = ( 'department')
    def change_employee_status(self, request, queryset):
        queryset.update(status='inactive')
    change_employee_status.short_description = "change status of selected employee to inactive"





admin.site.register(Employee,EmployeeAdmin1)

admin.site.register( LeaveRequest,LeaveRequestAdmin1)


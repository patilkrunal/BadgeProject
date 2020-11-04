from django.contrib import admin

from .models import Branch_of_study, Course


class CourseAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    
    def get_changeform_initial_data(self, request):
        get_data = super(CourseAdmin, self).get_changeform_initial_data(request)
        get_data['creator'] = request.user.pk
        return get_data


admin.site.register(Branch_of_study)
admin.site.register(Course, CourseAdmin)

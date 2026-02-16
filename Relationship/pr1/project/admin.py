from django.contrib import admin
from .models import projectVarity, ProjectReview, Store, ProjectCertificate


class ProjectReviewInline(admin.TabularInline):
    model = ProjectReview
    extra = 2

class ProjectVarietyAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'date_added')
    inlines = [ProjectReviewInline]

class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    filter_horizontal = ('project_varieties',)

class ProjectCertificateAdmin(admin.ModelAdmin):
    list_display = ('project', 'certificate_number')

# Register your models here.
admin.site.register(projectVarity, ProjectVarietyAdmin)
admin.site.register(Store, StoreAdmin)
admin.site.register(ProjectCertificate, ProjectCertificateAdmin)

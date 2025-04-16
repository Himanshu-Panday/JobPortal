from django.contrib import admin
from .models import Profile, Post

# Register your models here.
admin.site.register(Profile)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('job_title', 'job_company', 'author', 'created_at')
    search_fields = ('job_title', 'job_company', 'skill', 'author__username')
    list_filter = ('job_company', 'created_at')
    ordering = ('-created_at',)

    def created_at(self, obj):
        return obj.pk
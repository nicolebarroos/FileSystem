from django.contrib import admin

from file_system.models import Files, FileSystem


class FileSytemAdmin(admin.ModelAdmin):
    readonly_fields = ('directory')


admin.site.register(FileSystem)
admin.site.register(Files)

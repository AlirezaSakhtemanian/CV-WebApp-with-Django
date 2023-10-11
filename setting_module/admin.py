from django.contrib import admin

from .models import SiteSetting, Skills, Projects, Degrees

admin.site.register(SiteSetting)
admin.site.register(Degrees)
admin.site.register(Projects)


@admin.register(Skills)
class SkillsAdmin(admin.ModelAdmin):
    list_display = ('title', 'skill_percent')
    list_editable = ('skill_percent',)

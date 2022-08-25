from django.contrib import admin
from topic.models import UserTopic
class TopicAdmin(admin.ModelAdmin):
    list_display = ['__str__']
    search_fields = ['__str__']
    list_per_page = 10
    class Meta:
        model = UserTopic



admin.site.register(UserTopic, TopicAdmin)

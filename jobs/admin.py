from django.contrib import admin
from jobs.models import Company, Experience, Position, Comment
from social_django.models import UserSocialAuth

admin.site.register(Company)
admin.site.register(Experience)
admin.site.register(Position)
admin.site.register(Comment)

# Register your models here.

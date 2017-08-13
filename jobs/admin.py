from django.contrib import admin
from jobs.models import Company, Experience, Position, Comment, Board
from social_django.models import UserSocialAuth

admin.site.register(Company)
admin.site.register(Experience)
admin.site.register(Position)
admin.site.register(Comment)
admin.site.register(Board)
# Register your models here.

from django.contrib import admin
from jobs.models import Company, Experience, Position, Comment, Board, SavedJobs

admin.site.register(Company)
admin.site.register(Experience)
admin.site.register(Position)
admin.site.register(Comment)
admin.site.register(Board)
admin.site.register(SavedJobs)
# Register your models here.

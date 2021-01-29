from django.contrib import admin

# Register your models here.
from .models import Game, Complete, Simulation, User

admin.site.register(Game)
admin.site.register(Complete)
admin.site.register(Simulation)
admin.site.register(User)
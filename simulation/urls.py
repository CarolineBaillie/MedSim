from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.index, name="index"),
    path("guide", views.guide, name="guide"),
    path("create", views.create, name="create"),
    path("mySim", views.mySim, name="mySim"),
    path("browse", views.browse, name="browse"),
    path("current", views.current, name="current"),
    path("completed", views.completed, name="completed"),
    path("play/<int:sim_id>", views.play, name="play"),
    path("reset/<int:sim_id>", views.reset, name="reset"),
    path("affirmed/<int:simID>/<str:a>", views.affirmed, name="affirmed"),
    path("submit", views.submit, name="submit"),
    path("save", views.save, name="save"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register")
]

from django.urls import path

from .views import add_attendee, add_gym, changed, edit_attendee, success

urlpatterns = [
    path("", add_gym),
    path("attendee/<int:attendee_pk>", edit_attendee),
    path("attendee", add_attendee),
    path("success", success),
    path("attendee/changed", changed),
]

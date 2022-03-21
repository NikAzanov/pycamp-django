from django.http import HttpResponseRedirect
from django.shortcuts import render

from apps.gym.models import Attendee, Gym

from .forms import AttendeeModelForm, GymForm
from .tasks import send_notifications


def add_gym(request):
    """Simple view to add gym."""

    if request.method == 'POST':
        form = GymForm(request.POST)
        if form.is_valid():
            gym = Gym(
                name=form.cleaned_data['name'],
                boss=form.cleaned_data['boss'],
                description=form.cleaned_data['description'],
            )
            gym.save()

            return HttpResponseRedirect('success')

    else:
        form = GymForm()
    return render(
        request,
        'gym/add_gym.html',
        {'form': form},
    )


def add_attendee(request):
    """Simple view to add attendee."""
    if request.method == 'POST':
        form = AttendeeModelForm(request.POST)
        if form.is_valid():
            attendee = form.save()
            send_notifications.delay(attendees=[attendee])
            return HttpResponseRedirect('success')
    else:
        form = AttendeeModelForm()
    return render(
        request,
        'gym/add_attendee.html',
        {'title': 'Add attendee', 'form': form},
    )


def edit_attendee(request, attendee_pk):
    """Simple view to edit attendee."""
    attendee = Attendee.objects.get(id=attendee_pk)

    if request.method == 'POST':
        form = AttendeeModelForm(request.POST, instance=attendee)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('changed')
    else:
        form = AttendeeModelForm(instance=attendee)
    return render(
        request,
        'gym/add_attendee.html',
        {'title': 'Edit attendee', 'form': form},
    )


def success(request):
    return render(
        request,
        'gym/success.html',
        {'message': "New instance was added"},
    )


def changed(request):
    return render(
        request,
        'gym/success.html',
        {'message': "Instance was changed"},
    )

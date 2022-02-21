from django.contrib import admin

from ..core.admin import BaseAdmin
from .models import Attendee, Gym, Subscription


@admin.register(Attendee)
class AttendeeAdminModel(BaseAdmin):
    """Admin for `Attendee` model."""
    list_filter = (
        'user',
        'gym',
        'subscription',
    )


@admin.register(Subscription)
class SubscriptionAdminModel(BaseAdmin):
    """Admin for `Subscription` model."""
    list_display = (
        'name',
        'gym',
        '_subscribers_count',
    )
    list_filter = (
        'gym',
    )

    def _subscribers_count(self, obj):
        """Return count of subscribers."""
        return obj.subscribers.count()


class SubscriptionAdminInline(admin.TabularInline):
    """Inline for `Subscription` model."""
    model = Subscription
    extra = 0


@admin.register(Gym)
class GymAdminModel(BaseAdmin):
    """Admin for `Gym` model."""
    list_display = (
        'id',
        'name',
        'boss',
    )
    list_display_links = (
        'name',
    )
    autocomplete_fields = (
        'boss',
    )
    search_fields = (
        'name',
        'boss__email',
    )
    filter_horizontal = (
        'attendees',
    )
    inlines = (SubscriptionAdminInline, )
    fieldsets = (
        (None, {
            'classes': ['wide'],
            'fields': (
                'name',
                'boss',
            ),
        }),
    )

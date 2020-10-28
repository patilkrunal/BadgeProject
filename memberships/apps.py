from django.apps import AppConfig


class MembershipsConfig(AppConfig):
    name = 'memberships'

    def ready(self):
        import Badging_system_krunal.memberships.signals

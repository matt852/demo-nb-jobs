from nautobot.extras.choices import ObjectChangeActionChoices
from nautobot.extras.jobs import JobHookReceiver


class UpdateDeviceInterfaceDescription(JobHookReceiver):
    def receive_job_hook(self, change, action, changed_object):
        if action == ObjectChangeActionChoices.ACTION_UPDATE:
            self.log_warning("Running AWX job to update interface description.")
            return True

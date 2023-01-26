from nautobot.extras.choices import ObjectChangeActionChoices
from nautobot.extras.jobs import JobHookReceiver


class UpdateFirewallObjectGroup(JobHookReceiver):
    def receive_job_hook(self, change, action, changed_object):
        if action == ObjectChangeActionChoices.ACTION_UPDATE:
            self.log_warning("Running Ansible AWX job to update object group on firewall.")
            return True

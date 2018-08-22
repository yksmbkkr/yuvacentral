from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils import six

class EmailConfirmationTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (
            six.text_type(user.pk) + six.text_type(timestamp) + six.text_type(user.user_check.email_confirmation_status)
            )

email_confirmation_token = EmailConfirmationTokenGenerator()

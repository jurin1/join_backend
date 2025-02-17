from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

class EmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(email=username)  # Suche nach Benutzer anhand der E-Mail
        except UserModel.DoesNotExist:
            return None
        if user.check_password(password):
            return user
        return None
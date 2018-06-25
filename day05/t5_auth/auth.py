from django.contrib.auth.backends import ModelBackend
from t5_auth.models import User


class MyBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, ):
        user = None
        try:
            user = User.objects.get(username=username)
        except:
            try:
                user = User.objects.get(phone=username)
            except:
                return None
        if user.check_password(password):
            return user
        else:
            return None

from django.conf.urls import url
from t3 import views

urlpatterns = [
    url(r"^avg-age$", views.get_avg_age)
]
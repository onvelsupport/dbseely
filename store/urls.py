from django.urls import path
from . import views

urlpatterns = [

    path("", views.giveaway, name="giveaway"),

    path(
        "thank-you/",
        views.thank_you,
        name="thank_you"
    ),

]
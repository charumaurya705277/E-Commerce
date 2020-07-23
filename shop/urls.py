from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="ShopeHome"),
    path("aboutus/",views.aboutus, name="AboutUs"),
    path("contactus/",views.contactus, name="ContactUS"),
    path("tracker/",views.tracker, name="TrackerStatus"),
    path("search/",views.search, name=" Search"),
    path("productview/<int:myid>",views.productview, name="ProductView"),
    path("checkout/",views.checkout, name="Checkout"),

]

from django.urls import path, include
from rest_framework import routers
from .views import ProfileViewSet, ProjectViewSet, ContactCreateView, ContactListView

router = routers.DefaultRouter()
router.register(r"profile", ProfileViewSet, basename="profile")
router.register(r"projects", ProjectViewSet, basename="projects")

urlpatterns = [
    path("api/", include(router.urls)),
    path("api/contact/", ContactCreateView.as_view(), name="api-contact"),
    path("api/contacts/", ContactListView.as_view(), name="api-contacts-admin"),  # admin uchun
]

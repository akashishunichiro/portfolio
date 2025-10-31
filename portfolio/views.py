from rest_framework import viewsets, generics, status
from rest_framework.response import Response
from rest_framework.decorators import api_view, action
from .models import Profile, Project, ContactMessage
from .serializers import ProfileSerializer, ProjectSerializer, ContactMessageSerializer

# Profile - odatda bittagina (first) bo‘ladi, shuning uchun List/Detail kerak emas
class ProfileViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Profile.objects.all().order_by("-id")
    serializer_class = ProfileSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all().order_by("order", "-created_at")
    serializer_class = ProjectSerializer
    # Sayt uchun, public GET allowed, admin yaratish uchun token auth kerak bo'lsa permission qo'shish mumkin

class ContactCreateView(generics.CreateAPIView):
    queryset = ContactMessage.objects.all()
    serializer_class = ContactMessageSerializer

    def create(self, request, *args, **kwargs):
        # oddiy server-side validationlar shu yerda bo'lishi mumkin
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        # Bu yerda email yuborishni qo'shish mumkin (celery yoki sync)
        headers = self.get_success_headers(serializer.data)
        return Response({"detail": "Message sent"}, status=status.HTTP_201_CREATED, headers=headers)

# Admin uchun Contact list va mark-as-read endpoint
from rest_framework.permissions import IsAdminUser
class ContactListView(generics.ListAPIView):
    queryset = ContactMessage.objects.all().order_by("-created_at")
    serializer_class = ContactMessageSerializer
    permission_classes = [IsAdminUser]

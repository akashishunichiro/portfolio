from django.db import models

class Profile(models.Model):
    # Bu single-row model bo'lishi mumkin — admin orqali o'zgartirasiz
    full_name = models.CharField(max_length=120)
    title = models.CharField(max_length=120, blank=True)
    bio = models.TextField(blank=True)
    phone = models.CharField(max_length=30, blank=True)
    email = models.EmailField(blank=True)
    instagram = models.URLField(blank=True)
    telegram = models.URLField(blank=True)
    youtube = models.URLField(blank=True)
    # profil rasmi
    avatar = models.ImageField(upload_to="avatars/", null=True, blank=True)

    def __str__(self):
        return self.full_name

class Project(models.Model):
    title = models.CharField(max_length=200)
    short_description = models.CharField(max_length=300, blank=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="projects/", null=True, blank=True)
    demo_url = models.URLField(blank=True)
    repo_url = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

class ContactMessage(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    phone = models.CharField(max_length=30, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} - {self.email}"
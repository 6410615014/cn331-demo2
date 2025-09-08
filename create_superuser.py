import os
import django
from django.contrib.auth import get_user_model

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Airline.settings")  # เปลี่ยนถ้าโปรเจกต์ชื่อไม่ใช่ Airline
django.setup()

User = get_user_model()

username = os.environ.get("DJANGO_SUPERUSER_USERNAME", "admin")
email = os.environ.get("DJANGO_SUPERUSER_EMAIL", "admin@example.com")
password = os.environ.get("DJANGO_SUPERUSER_PASSWORD", "adminpass123")

if not User.objects.filter(username=username).exists():
    print(f"Creating superuser '{username}'...")
    User.objects.create_superuser(username=username, email=email, password=password)
else:
    print(f"Superuser '{username}' already exists. Skipping.")

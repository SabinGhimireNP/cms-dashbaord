
from django.contrib.auth.models import AbstractUser
from django.db import models
# Create your models here.


class User(AbstractUser):
  ROLE_CHOICES=(
    ('admin','Admin'),
    ('cms_user','Cms User')
  )
  role = models.CharField(max_length=20,choices=ROLE_CHOICES,default='cms_user')
  profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
  

class AdminAccount(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='admin_account')
    admin_id = models.CharField(max_length=20, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.admin_id:
            last_admin = AdminAccount.objects.exclude(admin_id='').order_by('-admin_id').first()
            if last_admin and last_admin.admin_id.startswith('adm-'):
                try:
                    last_num = int(last_admin.admin_id.split('-')[1])
                    new_num = last_num + 1
                except ValueError:
                    new_num = 1
            else:
                new_num = 1
            self.admin_id = f"adm-{str(new_num).zfill(3)}"
        super().save(*args, **kwargs)
  



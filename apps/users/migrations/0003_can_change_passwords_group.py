# Generated manually

from django.db import migrations

def create_can_change_passwords_group(apps, schema_editor):
    Group = apps.get_model('auth', 'Group')
    Group.objects.get_or_create(name='can_change_passwords')

def remove_can_change_passwords_group(apps, schema_editor):
    Group = apps.get_model('auth', 'Group')
    Group.objects.filter(name='can_change_passwords').delete()

class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_profile_picture'),
        ('auth', '0012_alter_user_first_name_max_length'), # Typical latest auth migration, but string reference is safer
    ]

    operations = [
        migrations.RunPython(create_can_change_passwords_group, remove_can_change_passwords_group),
    ]

# Generated manually

from django.db import migrations, models

def backfill_admin_id(apps, schema_editor):
    User = apps.get_model('users', 'User')
    users = User.objects.filter(admin_id='')
    for i, user in enumerate(users):
        user.admin_id = f"adm-{str(i+1).zfill(3)}"
        user.save(update_fields=['admin_id'])

class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_can_change_passwords_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='admin_id',
            field=models.CharField(blank=True, max_length=20, unique=True),
        ),
        migrations.RunPython(backfill_admin_id, migrations.RunPython.noop),
    ]

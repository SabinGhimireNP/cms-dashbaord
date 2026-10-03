# Generated manually

from django.db import migrations, models
import django.db.models.deletion

def backfill_admin_accounts(apps, schema_editor):
    User = apps.get_model('users', 'User')
    AdminAccount = apps.get_model('users', 'AdminAccount')
    
    # Create an AdminAccount for every user
    for i, user in enumerate(User.objects.all()):
        admin_id = f"adm-{str(i+1).zfill(3)}"
        AdminAccount.objects.create(user=user, admin_id=admin_id)

class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_can_change_passwords_group'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdminAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admin_id', models.CharField(blank=True, max_length=20, unique=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='admin_account', to='users.user')),
            ],
        ),
        migrations.RunPython(backfill_admin_accounts, migrations.RunPython.noop),
    ]

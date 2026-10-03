# Generated manually

from django.db import migrations, models

def backfill_member_ids(apps, schema_editor):
    Member = apps.get_model('tenure', 'Member')
    for i, member in enumerate(Member.objects.all()):
        member_id = f"MEM-{str(i+1).zfill(4)}"
        member.member_id = member_id
        member.save(update_fields=['member_id'])

class Migration(migrations.Migration):

    dependencies = [
        ('tenure', '0006_remove_member_signature'), 
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='member_id',
            field=models.CharField(blank=True, max_length=20, unique=True),
        ),
        migrations.RunPython(backfill_member_ids, migrations.RunPython.noop),
    ]

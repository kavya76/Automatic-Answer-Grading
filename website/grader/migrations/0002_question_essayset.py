

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grader', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='essaySet',
            field=models.IntegerField(default=0, unique=True),
            preserve_default=False,
        ),
    ]

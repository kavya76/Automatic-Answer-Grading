

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grader', '0006_essay_score'),
    ]

    operations = [
        migrations.AlterField(
            model_name='essay',
            name='score',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]

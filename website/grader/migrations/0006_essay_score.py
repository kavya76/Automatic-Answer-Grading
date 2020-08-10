

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grader', '0005_auto_20180812_1549'),
    ]

    operations = [
        migrations.AddField(
            model_name='essay',
            name='score',
            field=models.IntegerField(null=True),
        ),
    ]



from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grader', '0004_auto_20180812_1546'),
    ]

    operations = [
        migrations.AlterField(
            model_name='essay',
            name='content',
            field=models.TextField(max_length=100000),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_title',
            field=models.TextField(max_length=100000),
        ),
    ]



from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grader', '0002_question_essayset'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='essaySet',
            new_name='set',
        ),
    ]

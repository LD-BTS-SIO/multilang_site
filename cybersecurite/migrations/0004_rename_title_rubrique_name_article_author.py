# cybersecurite/migrations/0004_rename_title_rubrique_name_article_author.py

from django.db import migrations, models

def set_default_author(apps, schema_editor):
    Article = apps.get_model('cybersecurite', 'Article')
    Author = apps.get_model('cybersecurite', 'Author')
    default_author = Author.objects.get(id=1)
    Article.objects.filter(author__isnull=True).update(author=default_author)

class Migration(migrations.Migration):

    dependencies = [
        ('cybersecurite', '0003_author_rubrique'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rubrique',
            old_name='title',
            new_name='name',
        ),
        migrations.AddField(
            model_name='article',
            name='author',
            field=models.ForeignKey(default=1, to='cybersecurite.Author', on_delete=models.CASCADE),
        ),
        migrations.RunPython(set_default_author),
    ]

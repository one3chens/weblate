# Generated by Django 3.1.1 on 2020-10-29 11:51

from django.db import migrations


def update_name(apps, schema_editor):
    Group = apps.get_model("weblate_auth", "Group")
    db_alias = schema_editor.connection.alias
    for group in Group.objects.using(db_alias).filter(
        name__endswith="@Template", internal=True
    ):
        group.name = "{}@Sources".format(group.name.rsplit("@", 1)[0])
        group.save(update_fields=["name"])


class Migration(migrations.Migration):

    dependencies = [
        ("weblate_auth", "0012_auto_20200729_1200"),
    ]

    operations = [
        migrations.RunPython(update_name, migrations.RunPython.noop, elidable=True),
    ]
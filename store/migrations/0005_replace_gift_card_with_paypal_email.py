from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0004_alter_entry_preferred_gift_card"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="entry",
            name="preferred_gift_card",
        ),
        migrations.AddField(
            model_name="entry",
            name="paypal_email",
            field=models.EmailField(default="", max_length=254),
            preserve_default=False,
        ),
    ]

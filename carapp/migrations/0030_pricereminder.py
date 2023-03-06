# Generated by Django 3.2.5 on 2023-02-23 16:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('carapp', '0029_delete_pricereminder'),
    ]

    operations = [
        migrations.CreateModel(
            name='PriceReminder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_address', models.EmailField(max_length=200)),
                ('advert_id_owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='carapp.advert')),
            ],
        ),
    ]

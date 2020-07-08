# Generated by Django 3.0.4 on 2020-04-08 23:46

import collections
from django.db import migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('django_netjsonconfig', '0043_add_indexes_on_ip_fields'),
    ]

    operations = [
        migrations.AddField(
            model_name='template',
            name='default_values',
            field=jsonfield.fields.JSONField(
                blank=True,
                default=dict,
                dump_kwargs={'ensure_ascii': False, 'indent': 4},
                help_text='A dictionary containing the default values for the variables used by this template; these default variables will be used during schema validation.',
                load_kwargs={'object_pairs_hook': collections.OrderedDict},
                verbose_name='Default Values',
            ),
        ),
    ]
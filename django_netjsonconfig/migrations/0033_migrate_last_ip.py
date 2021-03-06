# Generated by Django 2.0.5 on 2018-07-11 11:15

from django.db import migrations, models


def forward(apps, schema_editor):
    device_model = apps.get_model('django_netjsonconfig', 'Device')
    devices = device_model.objects.all().select_related('config')
    for device in devices:
        if not hasattr(device, 'config'):
            continue
        device.last_ip = device.config.last_ip
        device.save()


def backward(apps, schema_editor):
    device_model = apps.get_model('django_netjsonconfig', 'Device')
    devices = device_model.objects.all().select_related('config')
    for device in devices:
        if not hasattr(device, 'config'):
            continue
        device.config.last_ip = device.last_ip
        device.config.save()


class Migration(migrations.Migration):

    dependencies = [
        ('django_netjsonconfig', '0032_internal_notes_label'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='last_ip',
            field=models.GenericIPAddressField(
                blank=True,
                help_text='indicates the IP address logged from the last request coming from the device',
                null=True,
            ),
        ),
        migrations.RunPython(forward, backward),
        migrations.RemoveField(model_name='config', name='last_ip'),
    ]

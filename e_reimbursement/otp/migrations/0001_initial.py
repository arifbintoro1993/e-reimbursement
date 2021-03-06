# Generated by Django 3.0.11 on 2021-01-11 15:52

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('otp_email', '0004_throttling'),
        ('reimbursement', '0002_reimbursement_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailDeviceExtra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('device', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='extra', to='otp_email.EmailDevice')),
                ('reimbursement', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='reimbursement.Reimbursement')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

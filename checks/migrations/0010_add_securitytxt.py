# Generated by Django 3.2.15 on 2022-09-15 15:01

import checks.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("checks", "0009_rpki"),
    ]

    operations = [
        migrations.AddField(
            model_name="domaintestappsecpriv",
            name="securitytxt_enabled",
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name="domaintestappsecpriv",
            name="securitytxt_errors",
            field=checks.models.ListField(default=[]),
        ),
        migrations.AddField(
            model_name="domaintestappsecpriv",
            name="securitytxt_found_host",
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="domaintestappsecpriv",
            name="securitytxt_recommendations",
            field=checks.models.ListField(default=[]),
        ),
        migrations.AddField(
            model_name="domaintestappsecpriv",
            name="securitytxt_score",
            field=models.IntegerField(null=True),
        ),
    ]

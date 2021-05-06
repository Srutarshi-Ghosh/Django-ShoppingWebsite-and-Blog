# Generated by Django 2.2 on 2019-12-30 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blogpost',
            fields=[
                ('post_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=500)),
                ('heading1', models.CharField(max_length=500)),
                ('content_head1', models.CharField(max_length=5000)),
                ('heading2', models.CharField(max_length=500)),
                ('content_head2', models.CharField(max_length=5000)),
                ('heading3', models.CharField(max_length=500)),
                ('content_head3', models.CharField(max_length=5000)),
                ('pub_date', models.DateField()),
                ('thumbnail', models.ImageField(default='', upload_to='blog/images')),
            ],
        ),
    ]

# Generated by Django 4.1.6 on 2023-05-15 15:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('Cid', models.IntegerField(primary_key=True, serialize=False)),
                ('Cname', models.CharField(max_length=20)),
                ('Clink', models.CharField(max_length=100)),
                ('time_initial', models.IntegerField(default=1)),
                ('time_remaining', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Pagetype',
            fields=[
                ('Pid', models.IntegerField(primary_key=True, serialize=False)),
                ('Nlist', models.CharField(max_length=20)),
                ('Nfixed', models.CharField(max_length=20)),
                ('Nname', models.CharField(max_length=20)),
                ('Nlink', models.CharField(max_length=20)),
                ('Ntime', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('Uid', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('phone', models.CharField(max_length=20)),
                ('notice_order', models.CharField(default='123456', max_length=10)),
                ('college', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='college', to='dgunotice.category')),
                ('department', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='department', to='dgunotice.category')),
                ('sub_college', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sub_college', to='dgunotice.category')),
                ('sub_department', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sub_department', to='dgunotice.category')),
            ],
        ),
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('title', models.CharField(max_length=200)),
                ('link', models.CharField(max_length=250, primary_key=True, serialize=False)),
                ('time', models.CharField(max_length=30)),
                ('Cid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dgunotice.category')),
            ],
        ),
        migrations.AddField(
            model_name='category',
            name='Pid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='dgunotice.pagetype'),
        ),
        migrations.CreateModel(
            name='Keyword',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=10)),
                ('Cid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dgunotice.category')),
                ('Uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dgunotice.user')),
            ],
            options={
                'unique_together': {('Uid', 'key', 'Cid')},
            },
        ),
    ]

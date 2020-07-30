# Generated by Django 3.0.7 on 2020-07-30 20:26

import autoslug.fields
import core.models
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth_core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('street', models.CharField(max_length=200)),
                ('suite', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('zipcode', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'address',
                'verbose_name_plural': 'address',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='name')),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Checkout',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'checkout',
            },
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('message', models.CharField(choices=[('Processing Purchase', 'Processing Purchase'), ('Approved Purchase', 'Approved Purchase'), ('Purchase Denied', 'Purchase Denied'), ('Purchase Denied', 'Purchase sent')], max_length=30)),
            ],
            options={
                'verbose_name': 'status',
                'verbose_name_plural': 'status',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=60)),
                ('description', models.TextField(blank=True)),
                ('price', models.FloatField()),
                ('stock', models.IntegerField()),
                ('image', models.ImageField(max_length=255, upload_to=core.models.upload_to)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category_product', to='core.Category')),
            ],
            options={
                'verbose_name': 'product',
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('email', models.CharField(max_length=255, verbose_name='e-mail')),
                ('personal_document', models.CharField(max_length=20, verbose_name='cpf')),
                ('phone', models.CharField(max_length=12)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_client', to='auth_core.UserClient')),
            ],
            options={
                'verbose_name': 'client',
            },
        ),
        migrations.CreateModel(
            name='CheckoutItem',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('quantity', models.PositiveSmallIntegerField(verbose_name='quantity')),
                ('price', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='price')),
                ('checkout', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='checkout_items', to='core.Checkout')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Product')),
            ],
            options={
                'verbose_name': 'checkout item',
            },
        ),
        migrations.AddField(
            model_name='checkout',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_client_checkout', to='core.Customer'),
        ),
    ]

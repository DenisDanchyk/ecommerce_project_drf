# Generated by Django 3.2.8 on 2021-10-13 14:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_products', models.PositiveIntegerField(default=0, verbose_name='Кількість продуктів')),
                ('final_price', models.DecimalField(decimal_places=2, default=0, max_digits=9, verbose_name='Фінальна ціна')),
                ('in_order', models.BooleanField(default=False, verbose_name='В обробці')),
                ('for_anonymos_user', models.BooleanField(default=False, verbose_name='Для не авторизованих користувачів')),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Власник')),
            ],
            options={
                'verbose_name_plural': 'Корзини',
            },
        ),
        migrations.CreateModel(
            name='CartProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField()),
                ('quantity', models.PositiveIntegerField(default=1, verbose_name='Кількість')),
                ('user_size_choice', models.CharField(max_length=255, null=True, verbose_name='Вибраний користовачем розмір')),
                ('final_price', models.DecimalField(blank=True, decimal_places=2, max_digits=9, verbose_name='Ціна')),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_products', to='cart.cart', verbose_name='Корзина')),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Покупець')),
            ],
            options={
                'verbose_name': 'Продукти для корзини',
                'verbose_name_plural': 'Продукт для корзини',
            },
        ),
        migrations.AddField(
            model_name='cart',
            name='products',
            field=models.ManyToManyField(blank=True, related_name='related_cart', to='cart.CartProduct', verbose_name='Продукти'),
        ),
    ]

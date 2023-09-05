# Generated by Django 4.2.5 on 2023-09-05 13:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='IngredientCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('instructions', models.TextField()),
                ('difficulty', models.CharField(max_length=50)),
                ('prep_time', models.IntegerField()),
                ('rating', models.DecimalField(decimal_places=2, default=0.0, max_digits=3)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField()),
                ('text', models.TextField()),
                ('date', models.DateTimeField()),
                ('recipe_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='constructor.recipe')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='constructor.user')),
            ],
        ),
        migrations.CreateModel(
            name='RecipeIngredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.DecimalField(decimal_places=2, max_digits=6)),
                ('ingredient_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='constructor.ingredient')),
                ('recipe_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='constructor.recipe')),
            ],
        ),
        migrations.AddField(
            model_name='ingredient',
            name='IngredientCategory_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='constructor.ingredientcategory'),
        ),
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipe_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='constructor.recipe')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='constructor.user')),
            ],
        ),
    ]
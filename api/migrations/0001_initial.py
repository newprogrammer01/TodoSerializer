from django.db import migrations, models
class Migration(migrations.Migration):


   initial = True

   dependencies = [
   ]

   operations = [
      migrations.CreateModel(
        name ='Todo',
        fields=[
            ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ('task', models.CharField(max_length=100)),
            ('description', models.TextField()),
            ('completed', models.BooleanField(default=False)),
            ('created_at', models.DateTimeField(auto_now_add=True)),
            ('updated_at', models.DateTimeField(auto_now=True)),

        ],
      ),
    ]  
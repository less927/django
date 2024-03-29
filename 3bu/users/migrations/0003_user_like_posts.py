# Generated by Django 4.2.11 on 2024-03-19 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_alter_comment_created_alter_post_content_and_more'),
        ('users', '0002_user_profile_image_user_short_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='like_posts',
            field=models.ManyToManyField(blank=True, related_name='like_users', to='posts.post', verbose_name='좋아요 누른 Post 목록'),
        ),
    ]

from django.db.models import Model, CharField, ImageField


# Create your models here.


# class Post(Model):
#     title = CharField(verbose_name='Sarlavha', max_length=255)
#     body = CharField(verbose_name='Tana', max_length=255)
#     user = ForeignKey('auth.User', on_delete=CASCADE)
#
#
# class Comment(Model):
#     name = CharField(verbose_name='Nomi', max_length=255)
#     email = EmailField(verbose_name='Pochta', max_length=255)
#     body = CharField(verbose_name='Tana', max_length=255)
#     post = ForeignKey('apps.Post', on_delete=CASCADE)
#
#
# class Album(Model):
#     title = CharField(verbose_name='Sarlavha', max_length=255)
#     user = ForeignKey('auth.User', on_delete=CASCADE)
#
#
# class Photo(Model):
#     title = CharField(verbose_name='Sarlavha', max_length=255)
#     url = URLField(verbose_name='Havola', max_length=255)
#     thumbnailUrl = URLField(verbose_name='Havola', max_length=255)
#     album = ForeignKey('apps.Album', on_delete=CASCADE)
#
#
# class Todo(Model):
#     BOOL_CHOICES = ((True, 'Yes'), (False, 'No'))
#
#     title = CharField(verbose_name='Sarlavha', max_length=255)
#     completed = BooleanField(choices=BOOL_CHOICES)
#     user = ForeignKey('auth.User', on_delete=CASCADE)


class CreativeTeam(Model):
    first_name = CharField(max_length=255)
    last_name = CharField(max_length=255)
    photo = ImageField(upload_to='rasm')
    proffession = CharField(max_length=255)


class Director(Model):
    first_name = CharField(max_length=255)
    last_name = CharField(max_length=255)
    photo = ImageField(upload_to='rasm')
    proffession = CharField(max_length=255)


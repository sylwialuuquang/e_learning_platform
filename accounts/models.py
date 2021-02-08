from django.db.models import Model, OneToOneField, CASCADE, ForeignKey, DO_NOTHING
from django.contrib.auth.models import User
from django.db.models import ImageField

# import viewer.models


class Profile(Model):
    user = OneToOneField(User, on_delete=CASCADE, related_name='profile')
    avatar = ImageField(upload_to='avatar', default='default.png')
    team = ForeignKey('viewer.Team', on_delete=DO_NOTHING, null=True, blank=True)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'

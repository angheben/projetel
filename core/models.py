import uuid
from django.db import models
from stdimage.models import StdImageField


def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename


class Base(models.Model):
    creation = models.DateField(name='Creation', auto_now_add=True)
    modification = models.DateField(name='Modification', auto_now=True)
    active = models.BooleanField(name='Active', default=True)

    class Meta:
        abstract = True


class Service(Base):
    ICON_CHOICES = (
        ('lni-cog', 'Gear'),
        ('lni-stats-up', 'Graphic'),
        ('lni-users', 'Users'),
        ('lni-layers', 'Design'),
        ('lni-mobile', 'Mobile'),
        ('lni-rocket', 'Rocket')
    )
    service = models.CharField(name='Service', max_length=100)
    description = models.TextField(name='Description', max_length=200)
    icon = models.CharField(name='Icon', max_length=12, choices=ICON_CHOICES)

    class Meta:
        verbose_name = 'Services'
        verbose_name_plural = 'Services'



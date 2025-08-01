from django.db import models
# For allowing generic relationships
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

# Create your models here.

class Tag(models.Model):

    label = models.CharField( max_length=255 )


class TaggedItem( models.Model ):

    # What tag applied to what object
    tag = models.ForeignKey( Tag, on_delete=models.CASCADE )
    # Identifying the object that this tag will be applied to
    # Type (product, video, article)
    # ID
    content_type = models.ForeignKey( ContentType, on_delete=models.CASCADE )
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey() 
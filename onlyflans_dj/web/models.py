from django.db import models
import uuid

# Create your models here.
class Flan(models.Model):
    flan_uuid = models.UUIDField(default=uuid.uuid4, editable = False, unique = True)
    name = models.CharField(max_length=64)
    description = models.TextField()
    image_url = models.URLField()
    slug = models.SlugField(unique=True)  
    is_private = models.BooleanField(default=False)

class ContactForm(models.Model):
    contact_form_uuid = models.UUIDField(default=uuid.uuid4, editable= False)
    customer_email = models.EmailField()
    customer_name = models.CharField(max_length=64)
    message = models.TextField() 

    
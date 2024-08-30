from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.
# import datetime
# datetime.datetime()

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

class Event(models.Model):
    title                               = models.CharField(max_length=200)
    slug                               = models.SlugField(unique=True)
    description                = models.TextField()
    date                              = models.DateTimeField()
    location                       = models.CharField(max_length=300)
    category                     = models.ForeignKey(Category, on_delete=models.CASCADE)
    organizer                    = models.ForeignKey(User, on_delete=models.CASCADE)
    max_participants    = models.PositiveIntegerField(null=True, blank=True)
    created_at                 = models.DateTimeField(auto_now_add=True)

    # add default slug
    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1
            while Event.objects.filter(slug=slug).exists():
                slug = f'{base_slug}-{counter}'
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.title} >> {self.organizer}'

# Event.objects.create(organizer=User.objects.get(username="dave"),title="Learning Rust", description="Lets come learn rust together!", location="Germany", date=datetime(2024, 10, 25), category=Category.objects.get(name="Technology"))
# Event.objects.create(organizer=User.objects.get(username="Lionel"),title="Navigating the Business world as an Entrepreneur", description="How to survive the harsh and quick changing economy of the business world as an entrepreneur", location="Tunisia", date=datetime(2024, 11, 6, 9), category=Category.objects.get(name="Business"))
# Event.objects.create(organizer=User.objects.get(username="admin"),title="How to increase instagram account reach", description="Webinar giving a fully detailed guide on how to ,make you instagram account reach out to more accounts", location="Virtual", date=datetime(2024, 9, 11), category=Category.objects.get(name="Webinar"))
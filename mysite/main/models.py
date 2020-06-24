from django.db import models
from django.utils import timezone

class TutorialCategory(models.Model):

    tutorial_category = models.CharField(max_length=200)
    category_summary = models.CharField(max_length=200)
    category_slug = models.CharField(max_length=200, default=1)

    class Meta:
        # Gives the proper plural name for admin
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.tutorial_category

class tutorialSeries(models.Model):
    type = models.CharField(max_length=200)
    Series_category = models.ForeignKey(TutorialCategory, default=1, verbose_name="Categories", on_delete=models.SET_DEFAULT)
    series_summary = models.CharField(max_length=200)

    class Meta:
        # otherwise we get "Tutorial Seriess in admin"
        verbose_name_plural = "Series"

    def __str__(self):
        return self.tutorial_series


class Tutorial(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published = models.DateTimeField( 'published date', default=timezone.now)
    tutorial_series = models.ForeignKey(TutorialSeries, default=1, verbose_name="Series", on_delete=models.SET_DEFAULT)
    tutorial_slug = models.CharField(max_length=200, default=1)

    def __str__(self):
        return self.title



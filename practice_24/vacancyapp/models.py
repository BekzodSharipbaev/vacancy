from django.db import models
from django.urls import reverse

# Create your models here.


class Company(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


STATUS_CH = [
    ('junior', 'Junior'),
    ('middle', 'Middle'),
    ('senior', 'Senior'),
]


class Vacancy(models.Model):
    title = models.CharField(max_length=255)
    languages = models.ManyToManyField(Language, related_name='vacancies')
    company = models.ForeignKey(Company, null=True, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=255, choices=STATUS_CH, default='junior')
    salary = models.PositiveIntegerField(null=True)
    description = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ("-id",)

    def get_absolute_url(self):
        return reverse('vacancy', kwargs={'pk': self.pk})

    def __str__(self):
        return f"{self.title} - {self.company} - {self.salary}"

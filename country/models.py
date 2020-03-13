from django.db import models
from model_utils.models import TimeStampedModel


class Country(TimeStampedModel):
    name = models.CharField(max_length=255)
    currency = models.ForeignKey("currency.Currency", on_delete=models.CASCADE)

    class Meta:
        db_table = "country"
        verbose_name_plural = "countries"

    def __str__(self):
        return self.name

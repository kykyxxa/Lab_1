from django.db import models

class CountryPopulation(models.Model):
    country = models.CharField(max_length=100, verbose_name="Страна")
    iso3 = models.CharField(max_length=3, verbose_name="Код ISO3")
    year = models.IntegerField(verbose_name="Год")
    population = models.BigIntegerField(verbose_name="Население")
    population_growth = models.IntegerField(null=True, blank=True, verbose_name="Прирост населения")
    growth_rate = models.DecimalField(
        max_digits=10, 
        decimal_places=6, 
        null=True, 
        blank=True, 
        verbose_name="Темп роста (%)"
    )
    decade = models.CharField(max_length=10, verbose_name="Десятилетие")

    class Meta:
        db_table = "country_population"  # Имя таблицы в БД
        verbose_name = "Население страны"
        verbose_name_plural = "Население стран"
        # Уникальный ключ (страна + год)
        unique_together = ('country', 'year')  

    def __str__(self):
        return f"{self.country} ({self.year}): {self.population}"
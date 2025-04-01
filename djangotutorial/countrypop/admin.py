from django.contrib import admin
from countrypop.models import CountryPopulation

@admin.register(CountryPopulation)
class CountryPopulation(admin.ModelAdmin):
    list_display = [field.name for field in CountryPopulation._meta.get_fields()]  # Какие поля показывать
    search_fields = ("country", "year")  # Поля для поиска
    list_filter = ("population", "year")  # Фильтры сбоку
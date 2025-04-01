from rest_framework import serializers
from countrypop.models import CountryPopulation  # Импортируем модель

class CountryPopulationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CountryPopulation
        fields = [
            'id', 'country', 'iso3', 'year', 'population',
            'population_growth', 'growth_rate', 'decade'
        ]
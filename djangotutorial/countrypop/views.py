from rest_framework.generics import ListAPIView
from rest_framework.renderers import JSONRenderer
from countrypop.models import CountryPopulation
from countrypop.serializers import CountryPopulationSerializer
from countrypop.renderers import CSVRenderer  # Импортируем CSV-рендерер

class CountryPopulationListView(ListAPIView):
    queryset = CountryPopulation.objects.all()
    serializer_class = CountryPopulationSerializer
    renderer_classes = [JSONRenderer, CSVRenderer]  # Добавляем поддержку CSV
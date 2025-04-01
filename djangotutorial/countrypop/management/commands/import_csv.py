import csv
from decimal import Decimal
from django.core.management.base import BaseCommand
from countrypop.models import CountryPopulation  

class Command(BaseCommand):
    help = "Импорт данных о населении стран из CSV-файла в модель CountryPopulation"

    def add_arguments(self, parser):
        parser.add_argument("file_path", type=str, help="Путь к CSV-файлу")

    def handle(self, *args, **options):
        file_path = options["file_path"]

        def parse_value(value, field_type):
            """Преобразует строковые значения из CSV в нужные типы или None, если значение пустое"""
            if value in ("", "NULL", "None", "NaT"):
                return None
            if field_type == int:
                return int(float(value)) if value.replace('.', '', 1).isdigit() else None
            if field_type == float or field_type == Decimal:
                return Decimal(value) if value.replace('.', '', 1).isdigit() else None
            return value

        with open(file_path, newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            records = []

            for row in reader:
                record = CountryPopulation(
                    country=row["Country"],
                    iso3=row["ISO3"],
                    year=parse_value(row["Year"], int),
                    population=parse_value(row["Population"], int),
                    population_growth=parse_value(row["Population Growth"], int),
                    growth_rate=parse_value(row["Growth Rate (%)"], Decimal),
                    decade=row["Decade"]
                )
                records.append(record)

            CountryPopulation.objects.bulk_create(records)
            self.stdout.write(
                self.style.SUCCESS(f"Успешно импортировано {len(records)} записей из {file_path}")
            )
        
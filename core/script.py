import os
import django

from django.contrib.gis.geos import Polygon
from geometry_app.models import Region, District, Canton, Contour


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "my_project.settings")
django.setup()

def fill_database_with_data():
    # Создание региона
    region_geometry = Polygon(((0, 0), (0, 1), (1, 1), (1, 0), (0, 0)))
    region = Region.objects.create(title='Чуй', geometry=region_geometry)

    # Создание районов
    for i in range(1, 4):
        district_geometry = Polygon(((0, 0), (0, 1), (1, 1), (1, 0), (0, 0)))
        district = District.objects.create(region=region, title=f'Район {i}', geometry=district_geometry)

        # Создание айыльных округов
        for j in range(1, 3):
            canton_geometry = Polygon(((0, 0), (0, 1), (1, 1), (1, 0), (0, 0)))
            canton = Canton.objects.create(district=district, title=f'Айыльный округ {j}', geometry=canton_geometry)

            # Создание контуров
            for k in range(1, 11):
                contour_geometry = Polygon(((0, 0), (0, 1), (1, 1), (1, 0), (0, 0)))
                contour = Contour.objects.create(canton=canton, geometry=contour_geometry)

if __name__ == "__main__":
    fill_database_with_data()

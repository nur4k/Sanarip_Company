from django.contrib.gis.db import models


class Region(models.Model):
    title = models.CharField('Название', max_length=155)
    geometry = models.PolygonField('Координаты')

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'Регион'
        verbose_name_plural = 'Регионы'


class District(models.Model):
    region = models.ForeignKey(to=Region, on_delete=models.CASCADE, related_name='district_region')
    title = models.CharField('Название', max_length=155)
    geometry = models.PolygonField('Координаты')

    def __str__(self) -> str:
        return f'{self.title} -- {self.region}'
    
    class Meta:
        verbose_name = 'Район'
        verbose_name_plural = 'Районы'


class Canton(models.Model):
    district = models.ForeignKey(to=District, on_delete=models.CASCADE, related_name='canton_district')
    title = models.CharField('Название', max_length=155)
    geometry = models.PolygonField('Координаты')

    def __str__(self) -> str:
        return f'{self.title} -- {self.district}'
    
    class Meta:
        verbose_name = 'Округ'
        verbose_name_plural = 'Округи'


class Contour(models.Model):
    canton = models.ForeignKey(to=Canton, on_delete=models.CASCADE, related_name='contour_canton')
    geometry = models.PolygonField('Координаты')
    
    def __str__(self) -> str:
        return f'{self.title} -- {self.canton}'
    
    class Meta:
        verbose_name = 'Контур'
        verbose_name_plural = 'Контуры'

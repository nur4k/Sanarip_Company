from django.urls import path

from geometry_app.views import RegionView, DistrictView, CantonView, ContourView


urlpatterns = [
    path('region/', RegionView.as_view()),
    path('district/', DistrictView.as_view()),
    path('canton/', CantonView.as_view()),
    path('contour/', ContourView.as_view()),
]

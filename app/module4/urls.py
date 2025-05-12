from inspect import getmembers, isclass
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework.viewsets import ModelViewSet, ViewSet
from . import views

router = DefaultRouter()

# Automatically find all ViewSets in views.py and register them
for name, cls in getmembers(views, isclass): # isclass checks if the object is a class and returns True if so
    # Checks if the class is a subclass of ViewSet (see CategoryInsertViewSet as an example)
    # Restricts verified classes to only those belonging to the views module and not others imported into views
    if issubclass(cls, ViewSet) and cls.__module__ == views.__name__:
        router.register(
            # Set name to lowercase and remove 'viewset' substring of imported with that prefix
            rf"{name.lower().replace('viewset', '')}", cls, basename=name.lower()
        )

urlpatterns = [
    path("api/mod4/", include(router.urls)), # Register the router under '/api/mod4'
]
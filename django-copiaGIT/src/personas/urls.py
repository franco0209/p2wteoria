
from django.urls import path
from personas.views import (
    personaTestView,
    personaCreateView,
    personasShowObject,
    personasListView,
    personasDeleteView,
    PersonaListView,
    )

app_name= "personas"
urlpatterns = [
    path("add/", personaCreateView, name="adding"),
    path("<int:myID>/",personasShowObject, name="browsing"),
    path("", PersonaListView.as_view(), name="persona-list"),
    path("<int:myID>/delete/", personasDeleteView, name="deleting"),
]

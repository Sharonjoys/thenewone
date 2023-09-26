from django.urls import path
from.import views

app_name='seriesapp'
urlpatterns = [

    path('',views.corp,name='corp'),
    path('series/<int:seriesid>/',views.series,name='series'),
    path('add/',views.add_series,name='add_series'),
    path('update/<int:id>/',views.updatef,name='update'),
    path('delete/<int:id>/',views.delete,name='delete')


]

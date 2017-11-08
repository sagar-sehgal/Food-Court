from django.conf.urls import url
from . import views 
app_name="food"

urlpatterns = [
	url(r'^$',views.index,name="all_plants"),
	# url(r'^$',views.add_food,name="add_food")
]

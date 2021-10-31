from django.urls import path

from crispy.views import PersonCreateView, PersonUpdateView, PersonListView, PersonDeleteView

app_name = 'crispy'

urlpatterns = [
	path('', PersonListView.as_view(), name='list'),
	path('add/', PersonCreateView.as_view(), name='add'),
	path('edit/<int:pk>/', PersonUpdateView.as_view(), name='edit'),
	path('delete/<int:pk>/', PersonDeleteView.as_view(), name='delete'),
]

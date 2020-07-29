from django.urls import path
from . import views
from .views import HomeView,HistoryView,ContactsView,PricesView,HoursView,WelcomePostView

urlpatterns = [
  #  path('', views.home, name="home"),
    path('news.html/', HomeView.as_view(), name="news"),
    path('history.html/', HistoryView.as_view(), name="history"),
    path('contacts.html/', ContactsView.as_view(), name="contacts"),
    path('prices.html/', PricesView.as_view(), name="prices"),
    path('hours.html/' , HoursView.as_view(), name="hours"),
    path('', WelcomePostView.as_view(), name = "home")


]
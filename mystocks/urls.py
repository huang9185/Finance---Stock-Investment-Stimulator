from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name='home'),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register_view, name="register"),
    path("watchlist", views.watchlist, name="watchlist"),
    path("profile", views.profile, name="profile"),
    path("history", views.history, name="history"),

    path("share/<str:quote>", views.share, name="share"),
    path("sell/<str:quote>", views.sell, name="sell"),
    path("search/<str:category>", views.search, name="search"),
    path("stock/<str:quote>", views.stock, name="stock"),
    path("company/<str:quote>", views.company, name="company"),

    # API Route
    path("stock/<str:quote>/watch/<int:is_watched>", views.watch, name="watch"),
]
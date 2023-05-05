from django.urls import path

from . import views

app_name = "polls"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:question_id>/", views.detail, name="detail"),
    path("<int:question_id>/results/", views.results, name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
    path("r2_codes/", views.r2_codes, name="r2_codes"),
    path("r1_codes/", views.r1_codes, name="r1_codes"),
    path("r1_codes/<str:r_1_code>/", views.r1_codes_detail, name="r1_codes_detail"),
]
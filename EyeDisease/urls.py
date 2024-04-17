from EyeDisease import views
from django.urls import path
urlpatterns=[
path('image-upload',views.form_input),
path('image',views.app),
path('result',views.upload_eye_image),
]

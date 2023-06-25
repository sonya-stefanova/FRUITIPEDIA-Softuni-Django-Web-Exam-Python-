from django.urls import include, path
from fruitipedia_app.web.views import show_home, show_dashboard, create_fruit, edit_fruit, details_fruit, delete_fruit, \
    create_profile, details_profile, edit_profile, delete_profile

urlpatterns = (
    path('', show_home, name='index'),
    path('dashboard/', show_dashboard, name='dashboard'),

    path('create/', create_fruit, name='create fruit'),


    path('<int:pk>/details/', details_fruit, name='details fruit'),
    path('<int:pk>/edit/', edit_fruit, name='edit fruit'),
    path('<int:pk>/delete/', delete_fruit, name='delete fruit'),


    path('profile/', include([
        path('create/', create_profile, name='create profile'),
        path('details/', details_profile, name='details profile'),
        path('edit/', edit_profile, name='edit profile'),
        path('delete/', delete_profile, name='delete profile'),
    ])
         ),
)



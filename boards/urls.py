from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter
app_name = 'boards'
t = DefaultRouter()
t.register('boards', views.BoardViewSets, basename='boards')

urlpatterns = [
    # path('', views.home, name='home'),
    # path('', views.boards_list, name='home'),
    # path('', views.BoardList.as_view(), name='home'),
    # path('boards/<int:id>', views.board_topics, name='board_topics'),
    # path('boards/<int:id>', views.BoardTopics.as_view(), name='board_topics'),
    # path('board_detail/<int:id>', views.BoardDetails.as_view(), name='board_details'),

]

urlpatterns += t.urls
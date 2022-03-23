from django.urls import path
from .views import BoardList, BoardDetail, LikeBoard, VoteBoard, HotBoard

urlpatterns = [
    path('', BoardList.as_view()),
    path('<int:pk>/', BoardDetail.as_view()),
    path('<int:pk>/like/', LikeBoard.as_view()),
    path('<int:pk>/vote/', VoteBoard.as_view()),
    path('hot/', HotBoard.as_view()),
]
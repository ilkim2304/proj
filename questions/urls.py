from .views import CreateQuestionAPIView, VoteForAnwser 
from django.urls import path

urlpatterns = [
    path("createQuestion", CreateQuestionAPIView.as_view(), name="CreateQuestion"),
    path("vote", VoteForAnwser.as_view(), name="Vote"),
]

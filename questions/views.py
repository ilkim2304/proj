from rest_framework import status, generics, serializers
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from .serializers import CreateQuestion, VoteForAnswer
from .models import Questions, Answers


class CreateQuestionAPIView(generics.GenericAPIView):
    serializer_class = CreateQuestion
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid()
        question = serializer.data.get("question")
        questions = Questions.objects.create()
        questions.question = question
        questions.save()
        return Response({"Success": "Successfully"}, status=status.HTTP_200_OK)


class VoteForAnwser(generics.GenericAPIView):
    serializer_class = VoteForAnswer
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        user = request.user
        id = serializer.data.get("id")
        answers = Answers.objects.get(id=id)
        answers.voters.add(user)
        answers.save()
        return Response({"Success": "Successfully"}, status=status.HTTP_200_OK)

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import UserModel, TweetModel
from .serializers import UserSerializer, TweetSerializer
from django.db.models import F
from .models import UserModel



@api_view(['GET'])
def get_tweets(request):
    tweets = TweetModel.objects.all()
    serializer = TweetSerializer(tweets, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def create_comment(request):
    serializer = TweetSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


@api_view(['GET'])
def get_tweet(request, pk):
    try:
        tweet = TweetModel.objects.get(pk=pk)
    except TweetModel.DoesNotExist:
        return Response(status=404)

    serializer = TweetSerializer(tweet)
    return Response(serializer.data)


@api_view(['GET'])
def get_ranked_users(request):
    ranked_users = UserModel.objects.exclude(user_rank=0).order_by('-user_rank')
    serializer = UserSerializer(ranked_users, many=True)
    return Response(serializer.data)


class TweetModelViewSet(viewsets.ModelViewSet):
    queryset = TweetModel.objects.all()
    serializer_class = TweetSerializer


class UserModelViewSet(viewsets.ModelViewSet):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer

    @action(detail=True, methods=['post'])
    def create_tweet(self, request, pk=None):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        tweet = serializer.save()

        mentioned_users = tweet.mentioned_users.all()
        for user in mentioned_users:
            if user != tweet.user:
                user.user_rank += 1
                user.save()

        return Response(serializer.data)

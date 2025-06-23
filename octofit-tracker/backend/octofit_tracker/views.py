from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer, TeamSerializer, ActivitySerializer, LeaderboardSerializer, WorkoutSerializer
from .models import User, Team, Activity, Leaderboard, Workout

@api_view(['GET', 'POST'])
def api_root(request, format=None):
    if request.method == 'POST':
        return Response({"message": "POST request received"}, status=status.HTTP_201_CREATED)

    # Dynamically determine the base URL for the API root
    host = request.get_host()
    scheme = 'https' if 'app.github.dev' in host else 'http'
    # Always allow both codespace and localhost URLs in the response
    codespace_url = 'https://silver-funicular-v65wg9rv54v7fp7pv-8000.app.github.dev/'
    localhost_url = 'http://localhost:8000/'
    return Response({
        'users': [codespace_url + 'api/users/?format=api', localhost_url + 'api/users/?format=api'],
        'teams': [codespace_url + 'api/teams/?format=api', localhost_url + 'api/teams/?format=api'],
        'activities': [codespace_url + 'api/activities/?format=api', localhost_url + 'api/activities/?format=api'],
        'leaderboard': [codespace_url + 'api/leaderboard/?format=api', localhost_url + 'api/leaderboard/?format=api'],
        'workouts': [codespace_url + 'api/workouts/?format=api', localhost_url + 'api/workouts/?format=api']
    })

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

class LeaderboardViewSet(viewsets.ModelViewSet):
    queryset = Leaderboard.objects.all()
    serializer_class = LeaderboardSerializer

class WorkoutViewSet(viewsets.ModelViewSet):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer

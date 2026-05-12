# views.py for Octofit Tracker
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': '/users/',
        'teams': '/teams/',
        'activities': '/activities/',
        'leaderboard': '/leaderboard/',
        'workouts': '/workouts/',
    })

# Placeholder views for users, teams, activities, leaderboard, workouts

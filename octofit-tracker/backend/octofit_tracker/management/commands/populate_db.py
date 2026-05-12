from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models



from django.conf import settings

from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Connect to MongoDB directly for index creation
        client = MongoClient('localhost', 27017)
        db = client['octofit_db']

        # Drop collections if they exist
        db.users.drop()
        db.teams.drop()
        db.activities.drop()
        db.leaderboard.drop()
        db.workouts.drop()

        # Create unique index on email for users
        db.users.create_index([('email', 1)], unique=True)

        # Sample data
        users = [
            {'name': 'Clark Kent', 'email': 'superman@dc.com', 'team': 'Team DC'},
            {'name': 'Bruce Wayne', 'email': 'batman@dc.com', 'team': 'Team DC'},
            {'name': 'Diana Prince', 'email': 'wonderwoman@dc.com', 'team': 'Team DC'},
            {'name': 'Tony Stark', 'email': 'ironman@marvel.com', 'team': 'Team Marvel'},
            {'name': 'Steve Rogers', 'email': 'captain@marvel.com', 'team': 'Team Marvel'},
            {'name': 'Natasha Romanoff', 'email': 'blackwidow@marvel.com', 'team': 'Team Marvel'},
        ]
        teams = [
            {'name': 'Team Marvel', 'members': ['Tony Stark', 'Steve Rogers', 'Natasha Romanoff']},
            {'name': 'Team DC', 'members': ['Clark Kent', 'Bruce Wayne', 'Diana Prince']},
        ]
        activities = [
            {'user': 'Clark Kent', 'activity': 'Flight', 'duration': 60},
            {'user': 'Tony Stark', 'activity': 'Suit Training', 'duration': 45},
            {'user': 'Steve Rogers', 'activity': 'Shield Practice', 'duration': 30},
        ]
        leaderboard = [
            {'user': 'Clark Kent', 'points': 100},
            {'user': 'Tony Stark', 'points': 90},
            {'user': 'Steve Rogers', 'points': 80},
        ]
        workouts = [
            {'name': 'Super Strength', 'suggested_for': 'Team DC'},
            {'name': 'Tech Endurance', 'suggested_for': 'Team Marvel'},
        ]

        db.users.insert_many(users)
        db.teams.insert_many(teams)
        db.activities.insert_many(activities)
        db.leaderboard.insert_many(leaderboard)
        db.workouts.insert_many(workouts)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))

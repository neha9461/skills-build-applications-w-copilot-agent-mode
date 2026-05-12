from djongo import models

# User model
class User(models.Model):
	username = models.CharField(max_length=150, unique=True)
	email = models.EmailField(unique=True)
	date_joined = models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return self.username

# Team model
class Team(models.Model):
	name = models.CharField(max_length=100, unique=True)
	members = models.ArrayReferenceField(to=User, on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return self.name

# Activity model
class Activity(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	activity_type = models.CharField(max_length=100)
	duration = models.FloatField()  # in minutes
	calories_burned = models.FloatField()
	date = models.DateField()
	def __str__(self):
		return f"{self.user.username} - {self.activity_type}"

# Workout model
class Workout(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField()
	difficulty = models.CharField(max_length=50)
	def __str__(self):
		return self.name

# Leaderboard model
class Leaderboard(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	score = models.FloatField()
	rank = models.IntegerField()
	def __str__(self):
		return f"{self.user.username} - Rank {self.rank}"

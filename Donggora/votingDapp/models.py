from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=20)


class Category(models.Model):
    name = models.CharField(max_length=20)


class User(models.Model):
    GENDER = [('남', 'Male'), ('여', 'Female')]

    name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    gender = models.CharField(max_length=2, choices=GENDER)
    email = models.EmailField()
    phone = models.CharField(max_length=11)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)


class Comment(models.Model):
    content = models.TextField()
    like = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)
    created_at = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Poll(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    valid_until = models.DateField()
    pros = models.IntegerField(default=0)
    cons = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # candidate


class Vote(models.Model):
    created_at = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
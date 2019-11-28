from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.contrib.postgres.fields import ArrayField

class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('이메일 주소가 필요합니다.')
        
        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password=password)
        user.is_admin = True
        user.save(using=self._db)
        return user

class Department(models.Model):
    college = [("문과대학", "문과대학"),
              ("이과대학", "이과대학"),
              ("불교대학", "불교대학"),
              ("법과대학", "법과대학"),
              ("사회과학대학", "사회과학대학"),
              ("경찰사법대학", "경찰사법대학"),
              ("경영대학", "경영대학"),
              ("바이오시스템대학", "바이오시스템대학"),
              ("공과대학", "공과대학"),
              ("사범대학", "사범대학"),
              ("예술대학", "예술대학"),
              ("약학대학", "약학대학"),
              ("미래융합대학", "미래융합대학")]

    name = models.CharField(max_length=20, choices=college)

    def __str__(self):
        return self.name


class Category(models.Model):        
    category = [("학사제도", "학사제도"),
            ("시설", "시설"),
            ("교직원", "교직원")]

    name = models.CharField(max_length=20, choices=category)

    def __str__(self):
        return self.name


class User(AbstractBaseUser):
    GENDER = [('남', 'Male'), ('여', 'Female')]

    name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    gender = models.CharField(max_length=2, choices=GENDER)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=11)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin


class Poll(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    valid_until = models.DateField()
    pros = models.IntegerField(default=0)
    cons = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    contract = models.CharField(max_length=255, blank=True, null=True)
    # restriction = ArrayField(models.IntegerField(max_length=2, blank=True), size=8)

    def __str__(self):
        return self.title


class Comment(models.Model):
    content = models.TextField()
    like = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)
    created_at = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)

    def __str__(self):
        return self.content


class Vote(models.Model):
    created_at = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)

    def __str__(self):
        return self.poll
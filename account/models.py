from django.db import models

from django.contrib.auth.models import User

class UserInfo(User):
    age=models.IntegerField()
    gender=models.CharField(max_length=30)
    contact=models.CharField(max_length=30)

    class Meta:
        db_table='user_info'


from django.contrib.auth.forms import UserCreationForm

class UserInfoForm(UserCreationForm):
    class Meta:
        model=UserInfo
        fields=['username','first_name','last_name','age','gender','email','contact','password1','password2']

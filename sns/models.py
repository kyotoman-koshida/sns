
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.validators import ValidationError
from django.contrib.auth.models import User



# Messageクラス
class Message(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, \
            related_name='message_owner')
    group = models.ForeignKey('Group', on_delete=models.CASCADE)
    content = models.TextField(max_length=1000)
    share_id = models.IntegerField(default=-1)
    good_count = models.IntegerField(default=0)
    share_count = models.IntegerField(default=0)
    pub_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.content) + ' (' + str(self.owner) + ')'
    
    def get_share(self):
        return Message.objects.get(id=self.share_id)

    class Meta:
        ordering = ('-pub_date',)

# Groupクラス
class Group(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, \
            related_name='group_owner')
    title = models.CharField(max_length=100)
    
    def __str__(self):
        return self.title

# Friendクラス
class Friend(models.Model):

    GENDER_CHOICES = (
         (1,'男性'),
         (2,'女性'),
    )

    owner = models.ForeignKey(User, on_delete=models.CASCADE, \
            related_name='friend_owner')
    user = models.ForeignKey(User, on_delete=models.CASCADE, \
            related_name='friend_user')
    gender = models.IntegerField(verbose_name='性別',choices=GENDER_CHOICES)     
    group = models.ForeignKey(Group, on_delete=models.CASCADE, verbose_name='グループ')
    place = models.CharField(max_length=100, verbose_name='居住地')
    introduce = models.CharField(max_length=250, verbose_name='自己紹介', null=True)

    def senbetu(value):
        if value<150.0 or value>169.9:
            raise ValidationError('身長は150.0cm以上、169.9cm以下でご記入下さい')
    
    men = True
    def gencheck(self):
        if self.gender == 2:
           men = False

    height =models.FloatField(editable=men, validators=[senbetu], verbose_name='身長')

    def __str__(self):
        GENDER = {1:'男性', 2:'女性',}
        return str(self.user) + ' (性別:"' + GENDER[self.gender] + '")'

# Goodクラス
class Good(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, \
            related_name='good_owner')
    message = models.ForeignKey(Message, on_delete=models.CASCADE)

    def __str__(self):
        return 'good for "' + str(self.message) + '" (by ' + \
                str(self.owner) + ')'

class DM(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="dm_owner")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="dm_user")
    content = models.CharField(max_length=250)
    dm_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.owner) + " が " + str(self.user) + " にDM " + \
            str(self.dm_at.month) + "/" + str(self.dm_at.day) + ")"

    class Meta:
        ordering = ["-dm_at"]                

# Create your models here.

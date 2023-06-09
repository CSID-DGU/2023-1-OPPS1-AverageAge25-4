# Create your models here.
from django.db import models

# Create your models here.

class Pagetype(models.Model):
    Pid = models.IntegerField(primary_key=True)
    Nlist = models.CharField(max_length=50)
    Nfixed = models.CharField(max_length=50)
    Nname = models.CharField(max_length=50)
    Nlink = models.CharField(max_length=50)
    Ntime = models.CharField(max_length=50)

    class Meta:
        managed = True
        db_table = 'pagetype'

    def __str__(self):
        return str(self.Pid)


class Category(models.Model):
    Cid = models.IntegerField(primary_key=True)
    Cname = models.CharField(max_length=20)
    Clink = models.CharField(max_length=100)
    Pid = models.ForeignKey(Pagetype, on_delete=models.SET_NULL, null=True)
    time_initial = models.IntegerField(default=1)
    time_remaining = models.IntegerField(default=1)

    class Meta:
        managed = True
        db_table = 'category'

    def __str__(self):
        return f"{self.Cid}.{self.Cname}"


class User(models.Model):
    Uid = models.CharField(max_length=200, primary_key=True)
    password = models.CharField(max_length=100)
    notice_order = models.CharField(max_length=30, default="1/2/3/4/5/6")

    class Meta:
        managed = True
        db_table = 'user'

    def __str__(self):
        return self.Uid

class Verify(models.Model):
    token = models.CharField(max_length=100, primary_key=True)
    temp_id = models.CharField(max_length=200)
    temp_password = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'verify'

    def __str__(self):
        return self.token

class Keyword(models.Model):
    Uid = models.ForeignKey(User, on_delete=models.CASCADE)
    key = models.CharField(max_length=10)
    Cid = models.ForeignKey(Category, on_delete=models.CASCADE)
    similar_on = models.BooleanField(default=True)

    class Meta:
        managed = True
        db_table = 'keyword'
        unique_together = (('Uid', 'key', 'Cid'),)

    def __str__(self):
        return self.key

class Notice(models.Model):
    Cid = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    link = models.CharField(max_length=250, primary_key=True)
    time = models.CharField(max_length=30)
    isSended = models.BooleanField(default=False)
    isTrained = models.BooleanField(default=False)

    class Meta:
        managed = True
        db_table = 'notice'

    def __str__(self):
        return f"{self.Cid.Cid} + {self.Cid.Cname} - {self.title}"

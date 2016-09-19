from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=140)
    last_name = models.CharField(max_length=140)
    user_name = models.CharField(max_length=140)

    def __str__(self):
        return self.first_name


class Desk(models.Model):
    location = models.CharField(max_length=140)
    desk_number = models.CharField(max_length=1)

    def __str__(self):
        return (self.desk_number + ' | ' + self.location)

class Booking(models.Model):
    user = models.ForeignKey(User)
    desk = models.ForeignKey(Desk)
    date = models.DateTimeField()

    def __str__(self):
        return self.user.user_name
        # return (self.desk.desk_number + ' | ' + self.desk.location)




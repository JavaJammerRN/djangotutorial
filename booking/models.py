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
        return (self.location + ' | ' +  self.desk_number )

# default is just cos did some migrations before finished everything so it was confused.
class Booking(models.Model):
    user = models.ForeignKey(User, default='', related_name='user')
    desk = models.ForeignKey(Desk, default='',  related_name='desk')
    date = models.DateTimeField()

    def __str__(self):
        return ( str(self.date.strftime("%Y-%m-%d")) + ' | ' + self.user.user_name + ' | ' + self.desk.location + ': ' + self.desk.desk_number)
        
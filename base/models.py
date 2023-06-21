from django.db import models


class TodaySpecials(models.Model):
    name = models.CharField(max_length=50, db_comment='name of today specials meals')
    short_description = models.TextField(max_length=500, db_comment='short description of today specials meals')
    description = models.TextField(max_length=500, db_comment='description of today specials meals')
    image = models.ImageField(upload_to='menu/today_specials',
                              db_comment='image of today specials meals')

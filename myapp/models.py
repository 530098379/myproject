from __future__ import unicode_literals

from django.db import models


class Book(models.Model):
    book_name = models.CharField(max_length=64)
    add_time = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.book_name


class FcaTimer(models.Model):
    issuer = models.CharField(max_length=16)
    expire_date = models.DateTimeField(auto_now_add=True)
    unique_key_id = models.CharField(max_length=32)
    timer_type = models.CharField(max_length=5)
    message_type = models.CharField(max_length=5)
    message_seq_no = models.CharField(max_length=10)
    return_mq_grp = models.CharField(max_length=5)
    return_mq_que = models.CharField(max_length=5)
    cassette_id = models.CharField(max_length=8)
    ask_key_id = models.CharField(max_length=20)
    time_stamp = models.DateTimeField(auto_now_add=True)
    updater = models.CharField(max_length=16)

    class Meta:
        db_table = "FCA_TIMER"

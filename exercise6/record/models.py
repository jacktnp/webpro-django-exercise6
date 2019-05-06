from django.db import models
from django.contrib.auth.models import User, Permission, Group

# Create your models here.
class Record(models.Model):
    title = models.CharField(max_length=500, null=True, blank=True)
    WORK = '01'
    SICK = '02'
    TYPES = (
        (WORK, 'ลากิจ'),
        (SICK, 'ลาป่วย')
    )

    APPROVE_STATUS_CHOICE = (
        (0, 'Rejected'),
        (1, 'Approve'),
        (2, 'Waiting')
    )
    type = models.CharField(max_length=2, choices=TYPES, default='01')
    approve_status = models.IntegerField(choices=APPROVE_STATUS_CHOICE, default=2)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    create_by = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.title
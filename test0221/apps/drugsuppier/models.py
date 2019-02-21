from django.db import models
from common.BaseModel import  BaseModel


# Create your models here.
class drugsuppier(BaseModel) :
    suppierId=models.CharField(max_length=10,verbose_name="供应商id")
    drugId=models.CharField(max_length=10,verbose_name="药品id")
    price=models.IntegerField(verbose_name="药品单价")
    amount=models.IntegerField(verbose_name="药品数量")
    userId=models.CharField(max_length=10,verbose_name="用户id")
    time=models.DateTimeField()
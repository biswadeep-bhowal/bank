from django.db import models
from django.contrib.auth.models import User


class Customer( models.Model ) : 

    user = models.OneToOneField( User, on_delete = models.CASCADE )
    cust_id = models.BigIntegerField( primary_key = True, default = 100000 )
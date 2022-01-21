from django.db import models
from user.models import Customer

class Transaction( models.Model ) : 

    trans_id = models.BigIntegerField( primary_key = True, default = 1000000 )
    
    sender = models.ManyToManyField( Customer, related_name = 'sender' )
    receiver = models.ManyToManyField( Customer, related_name = 'receiver' )

    def str( self ) : return "{} to {}".format( self.sender.cust_id, self.receiver.cust_id )
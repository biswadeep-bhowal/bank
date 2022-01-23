from django.db import models
from user.models import Customer

class Transaction( models.Model ) : 

    trans_id = models.BigIntegerField( primary_key = True, default = 1000000 )
    amount = models.PositiveBigIntegerField( default = 0 )

    sender = models.PositiveBigIntegerField( null = True )
    receiver = models.PositiveBigIntegerField( null = True )

    def __str__( self ) : return "{} {} {} {}".format( str( self.trans_id ), str( self.sender ), str( self.receiver ), str( self.amount ) )
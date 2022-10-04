from django.db import models
import datetime

# -------------------------------- Mempool --------------------------------
class Mempool(models.Model):
    """
    Mempool refers to a waiting room that collects a valid pending (unconfirmed) transaction until it is processed & added to the block.
    """
    mempool_id = models.AutoField(
        primary_key=True,
    )
    time_stamp = models.DateTimeField(
        auto_now = True,
    )
    token_id = models.CharField(
        max_length=44,                      # Stored as base64, maximum 256 bits
    )
    operator = models.CharField(
        max_length=2,
    )
    amount = models.FloatField()
    address = models.CharField(
        max_length=44,                      # Stored as base64, maximum 256 bits
    )
    bounty = models.FloatField()
    deadline = models.IntegerField()        # Unix timestamps
    def __str__(self) -> str:
        return "{}) {} : {} {} {} {}".format(
            str(self.mempool_id),
            self.token_id,
            self.operator,
            self.operand_1,
            self.operand_2,
            self.operand_3,
        )
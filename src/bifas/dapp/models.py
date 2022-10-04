from django.db import models
from .CONSTANTS import LENGTH_OF_256_BITS_FOR_BASE64

# deadline = models.IntegerField()      # Unix timestamps

# -------------------------------- Account --------------------------------
class Account(models.Model):
    """
    Account
    """
    public_key = models.CharField(          # Pay-to-PubKey (P2PK)
        max_length=LENGTH_OF_256_BITS_FOR_BASE64 // 2,
        unique=True,
        primary_key=True,
    )

# -------------------------------- Token --------------------------------
class Token(models.Model):
    """
    Token
    """
    creator = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
    )

    token_id = models.CharField(
        max_length=LENGTH_OF_256_BITS_FOR_BASE64,
        primary_key=True,
    )
    info_link = models.URLField()
    info_hash = models.CharField(
        max_length=LENGTH_OF_256_BITS_FOR_BASE64,
    )
    info_digital_signature = models.CharField(
        max_length=LENGTH_OF_256_BITS_FOR_BASE64,
    )

# -------------------------------- UTXO --------------------------------
class UTXO(models.Model):
    """
    UTXO
    """
    owner = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
    )
    token = models.ForeignKey(
        Token,
        on_delete=models.CASCADE,
    )

    amount = models.FloatField()

# -------------------------------- Block --------------------------------
class Block(models.Model):
    """
    Block
    """
    miner = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
    )

    block_id = models.AutoField(
        primary_key=True,
    )
    time_stamp = models.DateTimeField()
    previous_hash = models.CharField(
        max_length=LENGTH_OF_256_BITS_FOR_BASE64,
    )
    nonce = models.CharField(
        max_length=LENGTH_OF_256_BITS_FOR_BASE64,
    )
    digital_signature = models.CharField(
        max_length=LENGTH_OF_256_BITS_FOR_BASE64,
    )

# -------------------------------- BlockCommand --------------------------------
class BlockCommand(models.Model):
    """
    BlockCommand
    """
    block = models.ForeignKey(
        Block,
        on_delete=models.CASCADE,
    )

    command_id = models.AutoField(
        primary_key=True,
    )
    time_stamp = models.DateTimeField()
    token_id = models.CharField(
        max_length=LENGTH_OF_256_BITS_FOR_BASE64,
    )
    operator = models.CharField(
        max_length=2,
    )
    amount = models.FloatField()
    address = models.CharField(
        max_length=LENGTH_OF_256_BITS_FOR_BASE64,
    )
    bounty = models.FloatField()
    deadline = models.IntegerField()
    digital_signature = models.CharField(
        max_length=LENGTH_OF_256_BITS_FOR_BASE64,
    )

# -------------------------------- Mempool --------------------------------
class Mempool(models.Model):
    """
    Mempool refers to a waiting room that collects a valid pending (unconfirmed) transaction until it is processed & added to the block.
    Mempool is isolated without any foreign keys because records are unverified by miners.
    """
    mempool_id = models.AutoField(
        primary_key=True,
    )
    time_stamp = models.DateTimeField(
        auto_now = True,
    )
    token_id = models.CharField(
        max_length=LENGTH_OF_256_BITS_FOR_BASE64,
    )
    operator = models.CharField(
        max_length=2,
    )
    amount = models.FloatField()
    address = models.CharField(
        max_length=LENGTH_OF_256_BITS_FOR_BASE64,
    )
    bounty = models.FloatField()
    deadline = models.IntegerField()
    digital_signature = models.CharField(
        max_length=LENGTH_OF_256_BITS_FOR_BASE64,
    )
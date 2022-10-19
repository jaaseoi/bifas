from random import choices
from django.db import models
from .CONSTANTS import (
    LENGTH_OF_256_BITS_TO_BYTES,
)

# -------------------------------- Account --------------------------------
class Account(models.Model):
    """
    Account

    Derived attribute :
        birthblock :
            SELECT birth_block_id
            FROM UTXO
            WHERE sender = {{ Account }}
            LIMIT 1

    Exploratory data analysis :
        no_of_accounts :
            SELECT COUNT(*) FROM Account
    """
    # Pay-to-PubKey (P2PK)
    address = models.BinaryField(
        max_length=LENGTH_OF_256_BITS_TO_BYTES,
        unique=True,
        primary_key=True,
    )

# -------------------------------- Token --------------------------------
class Token(models.Model):
    """
    Token

    Derived attribute :
        creator :
            SELECT sender
            FROM UTXO
            WHERE token = {{ Token }}
            LIMIT 1
    
    Exploratory data analysis :
        no_of_tokens :
            SELECT COUNT(*) FROM Token
    """
    # Hash value of Terms of Services (TOC)
    token_hash = models.BinaryField(
        max_length=LENGTH_OF_256_BITS_TO_BYTES,
        unique=True,
        primary_key=True,
    )

# -------------------------------- UTXO --------------------------------
class UTXO(models.Model):
    """
    UTXO

    Exploratory data analysis :
        debit_ledger :
            SELECT sender, token, amount
            FROM UTXO
            WHERE receiver = {{ Account }}
        credit_ledger :
            SELECT receiver, token, amount
            FROM UTXO
            WHERE sender = {{ Account }}
    """
    sender = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
    )
    receiver = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
    )
    token = models.ForeignKey(
        Token,
        on_delete=models.CASCADE,
    )
    amount = models.FloatField()
    birth_block_id = models.IntegerField()

# -------------------------------- Block --------------------------------
class Block(models.Model):
    """
    Block
    """
    block_id = models.AutoField(
        primary_key=True,
    )
    previous_hash = models.BinaryField(
        max_length=LENGTH_OF_256_BITS_TO_BYTES,
    )
    version_number = models.IntegerField()
    time_stamp = models.DateTimeField()
    nonce = models.BinaryField(
        max_length=LENGTH_OF_256_BITS_TO_BYTES,
    )

# -------------------------------- BlockCommand --------------------------------
class BlockCommand(models.Model):
    """
    BlockCommand
    
    Validation :
        unique (block_id, command_id) :
            SELECT block, command_id
            FROM BlockCommand
            GROUP BY block, command
            HAVING COUNT(*) > 1
        valid operator :
            SELECT block, command_id
            FROM BlockCommand
            WHERE operator < 0
    """
    block = models.ForeignKey(
        Block,
        on_delete=models.CASCADE,
    )
    class Operator(models.IntegerChoices):
        INVALID = -1
        # Create new token = Pay to yourself or others
        PAY = 0, 
        LOCK = 1
        ACQUIRE = 2
    operator = models.IntegerChoices(
        default=Operator.INVALID,
        choices=Operator.choices,
    )
    token_id = models.BinaryField(
        max_length=LENGTH_OF_256_BITS_TO_BYTES,
    )
    sender_address = models.BinaryField(
        max_length=LENGTH_OF_256_BITS_TO_BYTES,
    )
    receiver_address = models.BinaryField(
        max_length=LENGTH_OF_256_BITS_TO_BYTES,
    )
    amount = models.FloatField()
    bounty = models.FloatField()
    # Unix timestamps
    settlement_datetime = models.IntegerField()
    digital_signature = models.BinaryField(
        max_length=LENGTH_OF_256_BITS_TO_BYTES,
    )
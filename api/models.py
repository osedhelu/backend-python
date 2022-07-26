
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.

from django.db import models

class Company(models.Model):
    name=models.CharField(max_length=50)
    website=models.URLField(max_length=100)
    foundation=models.PositiveIntegerField()

class Commerces(models.Model):
    name = models.CharField(max_length=150, blank=True, null=True)
    rif = models.CharField(max_length=10, blank=True, null=True)
    email = models.CharField(max_length=150, blank=True, null=True)
    phone = models.CharField(max_length=10, blank=True, null=True)
    password = models.CharField(max_length=300, blank=True, null=True)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'commerces'

class Lists(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=150, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lists'

class DetLists(models.Model):
    name = models.CharField(max_length=150, blank=True, null=True)
    list = models.ForeignKey('Lists', models.DO_NOTHING)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'det_lists'

class Branches(models.Model):
    name = models.CharField(max_length=150, blank=True, null=True)
    location = models.CharField(max_length=300, blank=True, null=True)
    phone = models.CharField(max_length=10, blank=True, null=True)
    branch_type = models.CharField(max_length=1, blank=True, null=True)
    commerce = models.ForeignKey('Commerces', models.DO_NOTHING)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'branches'
class Affiliates(models.Model):
    affiliate = models.CharField(unique=True, max_length=150, blank=True, null=True)
    commerce = models.ForeignKey('Commerces', models.DO_NOTHING)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'affiliates'

class Terminals(models.Model):
    serial = models.CharField(max_length=150, blank=True, null=True)
    password = models.CharField(max_length=300, blank=True, null=True)
    vuelto = models.IntegerField(blank=True, null=True)
    reversoc2p = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=30, blank=True, null=True)
    mark = models.ForeignKey(DetLists, models.DO_NOTHING,related_name='+')
    model = models.ForeignKey(DetLists, models.DO_NOTHING)
    branch = models.ForeignKey(Branches, models.DO_NOTHING)
    affiliate = models.ForeignKey(Affiliates, models.DO_NOTHING)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'terminals'

class Transactions(models.Model):
    bank = models.CharField(max_length=150, blank=True, null=True)
    client_phone = models.CharField(max_length=9, blank=True, null=True)
    client_affiliate = models.CharField(max_length=9, blank=True, null=True)
    amount = models.CharField(max_length=10, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    hour = models.TimeField(blank=True, null=True)
    reference = models.CharField(max_length=300, blank=True, null=True)
    reason = models.CharField(max_length=150, blank=True, null=True)
    terminal = models.ForeignKey(Terminals, models.DO_NOTHING)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'transactions'

class Profiles(models.Model):
    name = models.CharField(max_length=150, blank=True, null=True)
    description = models.CharField(max_length=150, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'profiles'

class Users(models.Model):
    identification = models.CharField(max_length=255)
    names = models.CharField(max_length=255)
    last_names = models.CharField(max_length=255)
    email = models.CharField(unique=True, max_length=255)
    email_verified_at = models.DateTimeField(blank=True, null=True)
    state = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    date_c = models.DateTimeField(blank=True, null=True)
    profile = models.ForeignKey(Profiles, models.DO_NOTHING, blank=True, null=True)
    remember_token = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'

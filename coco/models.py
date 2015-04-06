import datetime

from django.contrib.auth.models import User
from django.db.models.signals import pre_delete, post_save
from django.db import models

from base_models import CocoModel
from coco.data_log import delete_log, save_log


class FullDownloadStats(models.Model):
    user = models.ForeignKey(User)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()


class ServerLog(models.Model):
    id = models.AutoField(primary_key=True)
    timestamp = models.DateTimeField(default=datetime.datetime.utcnow)
    user = models.ForeignKey(User, related_name="serverlog_user", null=True)
    action = models.IntegerField()
    entry_table = models.CharField(max_length=100)
    model_id = models.IntegerField(null=True)


# class CocoUser(CocoModel):
#     id = models.AutoField(primary_key=True)
#     old_coco_id = models.IntegerField(editable=False, null=True)
#     user = models.OneToOneField(User, related_name="coco_user")
# 
#     def __unicode__(self):
#         return  u'%s' % (self.user.username)


class Country(CocoModel):
    country_name = models.CharField(max_length=100, unique='True')

    def __unicode__(self):
        return self.country_name
post_save.connect(save_log, sender=Country)
pre_delete.connect(delete_log, sender=Country)


class State(CocoModel):
    state_name = models.CharField(max_length=100, unique='True')
    country = models.ForeignKey(Country)

    def __unicode__(self):
        return self.state_name
post_save.connect(save_log, sender=State)
pre_delete.connect(delete_log, sender=State)


class District(CocoModel):
    district_name = models.CharField(max_length=100, unique='True')
    state = models.ForeignKey(State)

    def __unicode__(self):
        return self.district_name
post_save.connect(save_log, sender=District)
pre_delete.connect(delete_log, sender=District)


class Block(CocoModel):
    block_name = models.CharField(max_length=100, unique='True')
    district = models.ForeignKey(District)

    def __unicode__(self):
        return self.block_name
post_save.connect(save_log, sender=Block)
pre_delete.connect(delete_log, sender=Block)


class Sublocation(CocoModel):
    sublocation_name = models.CharField(max_length=100)
    block = models.ForeignKey(Block)

    class Meta:
        unique_together = ("sublocation_name", "block")
post_save.connect(save_log, sender=Sublocation)
pre_delete.connect(delete_log, sender=Sublocation)


class Village(CocoModel):
    village_name = models.CharField(max_length=100)
    sublocation = models.ForeignKey(Sublocation)

    class Meta:
        unique_together = ("village_name", "sublocation")

    def __unicode__(self):
        return self.village_name
post_save.connect(save_log, sender=Village)
pre_delete.connect(delete_log, sender=Village)


class Person(CocoModel):
    person_name = models.CharField(max_length=100)
    spouse_name = models.CharField(max_length=100)
    job_card_number = models.CharField(max_length=100, blank=True)
    voter_card_number = models.CharField(max_length=100)
    village = models.ForeignKey(Village)
    no_of_adults = models.IntegerField()
    no_of_children = models.IntegerField()
    house_hold_per_capita_income = models.IntegerField()
    date_of_entry = models.DateField()
    phone_no = models.CharField(max_length=100, blank=True)

    class Meta:
        unique_together = ("person_name", "spouse_name", "village")

    def __unicode__(self):
        return self.person_name+"("+self.spouse_name+", "+self.village.village_name+")"
post_save.connect(save_log, sender=Person)
pre_delete.connect(delete_log, sender=Person)


### For SHG Level Data Capture
class Cluster(CocoModel):
    cluster_name = models.CharField(max_length=100)
    village = models.ForeignKey(Village)

    class Meta:
        unique_together = ("cluster_name", "village")

    def __unicode__(self):
        return self.cluster_name
post_save.connect(save_log, sender=Cluster)
pre_delete.connect(delete_log, sender=Cluster)


class SHGBaseLine(CocoModel):
    group_name = models.CharField(max_length=100)
    cluster = models.ForeignKey(Cluster)
    date_of_formation = models.DateField()
    LINKAGE_CHOICES = (('Yes', 'yes'), ('No', 'no'))
    bank_linkage = models.CharField(max_length=5, choices=LINKAGE_CHOICES)
    cc_limit = models.CharField(max_length=100)
    drawing_power = models.CharField(max_length=100)
    savings_account_number = models.CharField(max_length=100)
    loan_account_number = models.CharField(max_length=100)
    savings_account_balance = models.CharField(max_length=100)
    loan_account_balance = models.CharField(max_length=100)

    class Meta:
        unique_together = ("group_name", "cluster")

    def __unicode__(self):
        return self.group_name + "( " + self.cluster_name + ")"
post_save.connect(save_log, sender=SHGBaseLine)
pre_delete.connect(delete_log, sender=SHGBaseLine)


class SHGProgram(CocoModel):
    person = models.ForeignKey(Person)
    loan_from_money_lenders = models.IntegerField()
    loan_from_kcc_or_mfis = models.IntegerField()
post_save.connect(save_log, sender=SHGProgram)
pre_delete.connect(delete_log, sender=SHGProgram)


class LoanType(CocoModel):
    type_name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.type_name
post_save.connect(save_log, sender=LoanType)
pre_delete.connect(delete_log, sender=LoanType)


class LoanSubType(CocoModel):
    subtype_name = models.CharField(max_length=100)
    type = models.ForeignKey(LoanType)

    def __unicode__(self):
        return self.subtype_name
post_save.connect(save_log, sender=LoanSubType)
pre_delete.connect(delete_log, sender=LoanSubType)


class Loan(CocoModel):
    type = models.ForeignKey(LoanType)
    subtype = models.ForeignKey(LoanSubType)
    amount = models.FloatField()
post_save.connect(save_log, sender=Loan)
pre_delete.connect(delete_log, sender=Loan)


class ExpectedReceipt(CocoModel):
    expected_savings = models.FloatField()
    expected_general_principle = models.FloatField()
    expected_general_interest = models.FloatField()
    expected_special_principle = models.FloatField()
    expected_special_loan = models.FloatField()
post_save.connect(save_log, sender=ExpectedReceipt)
pre_delete.connect(delete_log, sender=ExpectedReceipt)


class ActualReceipt(CocoModel):
    fixed_deposit_saving = models.FloatField()
    regular_saving = models.FloatField()
    insurance_premium_paid = models.FloatField()
    fees = models.FloatField()
    general_principle = models.FloatField()
    general_interest = models.FloatField()
    special_principle = models.FloatField()
    special_interest = models.FloatField()
post_save.connect(save_log, sender=ActualReceipt)
pre_delete.connect(delete_log, sender=ActualReceipt)

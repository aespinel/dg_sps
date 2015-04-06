# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'FullDownloadStats'
        db.create_table(u'coco_fulldownloadstats', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('start_time', self.gf('django.db.models.fields.DateTimeField')()),
            ('end_time', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'coco', ['FullDownloadStats'])

        # Adding model 'ServerLog'
        db.create_table(u'coco_serverlog', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.utcnow)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='serverlog_user', null=True, to=orm['auth.User'])),
            ('action', self.gf('django.db.models.fields.IntegerField')()),
            ('entry_table', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('model_id', self.gf('django.db.models.fields.IntegerField')(null=True)),
        ))
        db.send_create_signal(u'coco', ['ServerLog'])

        # Adding model 'Country'
        db.create_table(u'coco_country', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user_created', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'coco_country_created', null=True, to=orm['auth.User'])),
            ('time_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, null=True, blank=True)),
            ('user_modified', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'coco_country_related_modified', null=True, to=orm['auth.User'])),
            ('time_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, null=True, blank=True)),
            ('country_name', self.gf('django.db.models.fields.CharField')(unique='True', max_length=100)),
        ))
        db.send_create_signal(u'coco', ['Country'])

        # Adding model 'State'
        db.create_table(u'coco_state', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user_created', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'coco_state_created', null=True, to=orm['auth.User'])),
            ('time_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, null=True, blank=True)),
            ('user_modified', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'coco_state_related_modified', null=True, to=orm['auth.User'])),
            ('time_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, null=True, blank=True)),
            ('state_name', self.gf('django.db.models.fields.CharField')(unique='True', max_length=100)),
            ('country', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['coco.Country'])),
        ))
        db.send_create_signal(u'coco', ['State'])

        # Adding model 'District'
        db.create_table(u'coco_district', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user_created', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'coco_district_created', null=True, to=orm['auth.User'])),
            ('time_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, null=True, blank=True)),
            ('user_modified', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'coco_district_related_modified', null=True, to=orm['auth.User'])),
            ('time_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, null=True, blank=True)),
            ('district_name', self.gf('django.db.models.fields.CharField')(unique='True', max_length=100)),
            ('state', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['coco.State'])),
        ))
        db.send_create_signal(u'coco', ['District'])

        # Adding model 'Block'
        db.create_table(u'coco_block', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user_created', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'coco_block_created', null=True, to=orm['auth.User'])),
            ('time_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, null=True, blank=True)),
            ('user_modified', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'coco_block_related_modified', null=True, to=orm['auth.User'])),
            ('time_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, null=True, blank=True)),
            ('block_name', self.gf('django.db.models.fields.CharField')(unique='True', max_length=100)),
            ('district', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['coco.District'])),
        ))
        db.send_create_signal(u'coco', ['Block'])

        # Adding model 'Sublocation'
        db.create_table(u'coco_sublocation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user_created', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'coco_sublocation_created', null=True, to=orm['auth.User'])),
            ('time_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, null=True, blank=True)),
            ('user_modified', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'coco_sublocation_related_modified', null=True, to=orm['auth.User'])),
            ('time_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, null=True, blank=True)),
            ('sublocation_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('block', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['coco.Block'])),
        ))
        db.send_create_signal(u'coco', ['Sublocation'])

        # Adding unique constraint on 'Sublocation', fields ['sublocation_name', 'block']
        db.create_unique(u'coco_sublocation', ['sublocation_name', 'block_id'])

        # Adding model 'Village'
        db.create_table(u'coco_village', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user_created', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'coco_village_created', null=True, to=orm['auth.User'])),
            ('time_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, null=True, blank=True)),
            ('user_modified', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'coco_village_related_modified', null=True, to=orm['auth.User'])),
            ('time_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, null=True, blank=True)),
            ('village_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('sublocation', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['coco.Sublocation'])),
        ))
        db.send_create_signal(u'coco', ['Village'])

        # Adding unique constraint on 'Village', fields ['village_name', 'sublocation']
        db.create_unique(u'coco_village', ['village_name', 'sublocation_id'])

        # Adding model 'Person'
        db.create_table(u'coco_person', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user_created', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'coco_person_created', null=True, to=orm['auth.User'])),
            ('time_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, null=True, blank=True)),
            ('user_modified', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'coco_person_related_modified', null=True, to=orm['auth.User'])),
            ('time_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, null=True, blank=True)),
            ('person_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('spouse_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('job_card_number', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('voter_card_number', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('village', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['coco.Village'])),
            ('no_of_adults', self.gf('django.db.models.fields.IntegerField')()),
            ('no_of_children', self.gf('django.db.models.fields.IntegerField')()),
            ('house_hold_per_capita_income', self.gf('django.db.models.fields.IntegerField')()),
            ('date_of_entry', self.gf('django.db.models.fields.DateField')()),
            ('phone_no', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
        ))
        db.send_create_signal(u'coco', ['Person'])

        # Adding unique constraint on 'Person', fields ['person_name', 'spouse_name', 'village']
        db.create_unique(u'coco_person', ['person_name', 'spouse_name', 'village_id'])

        # Adding model 'Cluster'
        db.create_table(u'coco_cluster', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user_created', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'coco_cluster_created', null=True, to=orm['auth.User'])),
            ('time_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, null=True, blank=True)),
            ('user_modified', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'coco_cluster_related_modified', null=True, to=orm['auth.User'])),
            ('time_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, null=True, blank=True)),
            ('cluster_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('village', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['coco.Village'])),
        ))
        db.send_create_signal(u'coco', ['Cluster'])

        # Adding unique constraint on 'Cluster', fields ['cluster_name', 'village']
        db.create_unique(u'coco_cluster', ['cluster_name', 'village_id'])

        # Adding model 'SHGBaseLine'
        db.create_table(u'coco_shgbaseline', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user_created', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'coco_shgbaseline_created', null=True, to=orm['auth.User'])),
            ('time_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, null=True, blank=True)),
            ('user_modified', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'coco_shgbaseline_related_modified', null=True, to=orm['auth.User'])),
            ('time_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, null=True, blank=True)),
            ('group_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('cluster', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['coco.Cluster'])),
            ('date_of_formation', self.gf('django.db.models.fields.DateField')()),
            ('bank_linkage', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('cc_limit', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('drawing_power', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('savings_account_number', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('loan_account_number', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('savings_account_balance', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('loan_account_balance', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'coco', ['SHGBaseLine'])

        # Adding unique constraint on 'SHGBaseLine', fields ['group_name', 'cluster']
        db.create_unique(u'coco_shgbaseline', ['group_name', 'cluster_id'])

        # Adding model 'SHGProgram'
        db.create_table(u'coco_shgprogram', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user_created', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'coco_shgprogram_created', null=True, to=orm['auth.User'])),
            ('time_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, null=True, blank=True)),
            ('user_modified', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'coco_shgprogram_related_modified', null=True, to=orm['auth.User'])),
            ('time_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, null=True, blank=True)),
            ('person', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['coco.Person'])),
            ('loan_from_money_lenders', self.gf('django.db.models.fields.IntegerField')()),
            ('loan_from_kcc_or_mfis', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'coco', ['SHGProgram'])

        # Adding model 'LoanType'
        db.create_table(u'coco_loantype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user_created', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'coco_loantype_created', null=True, to=orm['auth.User'])),
            ('time_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, null=True, blank=True)),
            ('user_modified', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'coco_loantype_related_modified', null=True, to=orm['auth.User'])),
            ('time_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, null=True, blank=True)),
            ('type_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'coco', ['LoanType'])

        # Adding model 'LoanSubType'
        db.create_table(u'coco_loansubtype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user_created', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'coco_loansubtype_created', null=True, to=orm['auth.User'])),
            ('time_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, null=True, blank=True)),
            ('user_modified', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'coco_loansubtype_related_modified', null=True, to=orm['auth.User'])),
            ('time_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, null=True, blank=True)),
            ('subtype_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['coco.LoanType'])),
        ))
        db.send_create_signal(u'coco', ['LoanSubType'])

        # Adding model 'Loan'
        db.create_table(u'coco_loan', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user_created', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'coco_loan_created', null=True, to=orm['auth.User'])),
            ('time_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, null=True, blank=True)),
            ('user_modified', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'coco_loan_related_modified', null=True, to=orm['auth.User'])),
            ('time_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, null=True, blank=True)),
            ('type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['coco.LoanType'])),
            ('subtype', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['coco.LoanSubType'])),
            ('amount', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal(u'coco', ['Loan'])

        # Adding model 'ExpectedReceipt'
        db.create_table(u'coco_expectedreceipt', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user_created', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'coco_expectedreceipt_created', null=True, to=orm['auth.User'])),
            ('time_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, null=True, blank=True)),
            ('user_modified', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'coco_expectedreceipt_related_modified', null=True, to=orm['auth.User'])),
            ('time_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, null=True, blank=True)),
            ('expected_savings', self.gf('django.db.models.fields.FloatField')()),
            ('expected_general_principle', self.gf('django.db.models.fields.FloatField')()),
            ('expected_general_interest', self.gf('django.db.models.fields.FloatField')()),
            ('expected_special_principle', self.gf('django.db.models.fields.FloatField')()),
            ('expected_special_loan', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal(u'coco', ['ExpectedReceipt'])

        # Adding model 'ActualReceipt'
        db.create_table(u'coco_actualreceipt', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user_created', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'coco_actualreceipt_created', null=True, to=orm['auth.User'])),
            ('time_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, null=True, blank=True)),
            ('user_modified', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'coco_actualreceipt_related_modified', null=True, to=orm['auth.User'])),
            ('time_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, null=True, blank=True)),
            ('fixed_deposit_saving', self.gf('django.db.models.fields.FloatField')()),
            ('regular_saving', self.gf('django.db.models.fields.FloatField')()),
            ('insurance_premium_paid', self.gf('django.db.models.fields.FloatField')()),
            ('fees', self.gf('django.db.models.fields.FloatField')()),
            ('general_principle', self.gf('django.db.models.fields.FloatField')()),
            ('general_interest', self.gf('django.db.models.fields.FloatField')()),
            ('special_principle', self.gf('django.db.models.fields.FloatField')()),
            ('special_interest', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal(u'coco', ['ActualReceipt'])


    def backwards(self, orm):
        # Removing unique constraint on 'SHGBaseLine', fields ['group_name', 'cluster']
        db.delete_unique(u'coco_shgbaseline', ['group_name', 'cluster_id'])

        # Removing unique constraint on 'Cluster', fields ['cluster_name', 'village']
        db.delete_unique(u'coco_cluster', ['cluster_name', 'village_id'])

        # Removing unique constraint on 'Person', fields ['person_name', 'spouse_name', 'village']
        db.delete_unique(u'coco_person', ['person_name', 'spouse_name', 'village_id'])

        # Removing unique constraint on 'Village', fields ['village_name', 'sublocation']
        db.delete_unique(u'coco_village', ['village_name', 'sublocation_id'])

        # Removing unique constraint on 'Sublocation', fields ['sublocation_name', 'block']
        db.delete_unique(u'coco_sublocation', ['sublocation_name', 'block_id'])

        # Deleting model 'FullDownloadStats'
        db.delete_table(u'coco_fulldownloadstats')

        # Deleting model 'ServerLog'
        db.delete_table(u'coco_serverlog')

        # Deleting model 'Country'
        db.delete_table(u'coco_country')

        # Deleting model 'State'
        db.delete_table(u'coco_state')

        # Deleting model 'District'
        db.delete_table(u'coco_district')

        # Deleting model 'Block'
        db.delete_table(u'coco_block')

        # Deleting model 'Sublocation'
        db.delete_table(u'coco_sublocation')

        # Deleting model 'Village'
        db.delete_table(u'coco_village')

        # Deleting model 'Person'
        db.delete_table(u'coco_person')

        # Deleting model 'Cluster'
        db.delete_table(u'coco_cluster')

        # Deleting model 'SHGBaseLine'
        db.delete_table(u'coco_shgbaseline')

        # Deleting model 'SHGProgram'
        db.delete_table(u'coco_shgprogram')

        # Deleting model 'LoanType'
        db.delete_table(u'coco_loantype')

        # Deleting model 'LoanSubType'
        db.delete_table(u'coco_loansubtype')

        # Deleting model 'Loan'
        db.delete_table(u'coco_loan')

        # Deleting model 'ExpectedReceipt'
        db.delete_table(u'coco_expectedreceipt')

        # Deleting model 'ActualReceipt'
        db.delete_table(u'coco_actualreceipt')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'coco.actualreceipt': {
            'Meta': {'object_name': 'ActualReceipt'},
            'fees': ('django.db.models.fields.FloatField', [], {}),
            'fixed_deposit_saving': ('django.db.models.fields.FloatField', [], {}),
            'general_interest': ('django.db.models.fields.FloatField', [], {}),
            'general_principle': ('django.db.models.fields.FloatField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'insurance_premium_paid': ('django.db.models.fields.FloatField', [], {}),
            'regular_saving': ('django.db.models.fields.FloatField', [], {}),
            'special_interest': ('django.db.models.fields.FloatField', [], {}),
            'special_principle': ('django.db.models.fields.FloatField', [], {}),
            'time_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'time_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'coco_actualreceipt_created'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'user_modified': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'coco_actualreceipt_related_modified'", 'null': 'True', 'to': u"orm['auth.User']"})
        },
        u'coco.block': {
            'Meta': {'object_name': 'Block'},
            'block_name': ('django.db.models.fields.CharField', [], {'unique': "'True'", 'max_length': '100'}),
            'district': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['coco.District']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'time_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'time_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'coco_block_created'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'user_modified': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'coco_block_related_modified'", 'null': 'True', 'to': u"orm['auth.User']"})
        },
        u'coco.cluster': {
            'Meta': {'unique_together': "(('cluster_name', 'village'),)", 'object_name': 'Cluster'},
            'cluster_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'time_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'time_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'coco_cluster_created'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'user_modified': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'coco_cluster_related_modified'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'village': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['coco.Village']"})
        },
        u'coco.country': {
            'Meta': {'object_name': 'Country'},
            'country_name': ('django.db.models.fields.CharField', [], {'unique': "'True'", 'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'time_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'time_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'coco_country_created'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'user_modified': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'coco_country_related_modified'", 'null': 'True', 'to': u"orm['auth.User']"})
        },
        u'coco.district': {
            'Meta': {'object_name': 'District'},
            'district_name': ('django.db.models.fields.CharField', [], {'unique': "'True'", 'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'state': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['coco.State']"}),
            'time_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'time_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'coco_district_created'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'user_modified': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'coco_district_related_modified'", 'null': 'True', 'to': u"orm['auth.User']"})
        },
        u'coco.expectedreceipt': {
            'Meta': {'object_name': 'ExpectedReceipt'},
            'expected_general_interest': ('django.db.models.fields.FloatField', [], {}),
            'expected_general_principle': ('django.db.models.fields.FloatField', [], {}),
            'expected_savings': ('django.db.models.fields.FloatField', [], {}),
            'expected_special_loan': ('django.db.models.fields.FloatField', [], {}),
            'expected_special_principle': ('django.db.models.fields.FloatField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'time_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'time_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'coco_expectedreceipt_created'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'user_modified': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'coco_expectedreceipt_related_modified'", 'null': 'True', 'to': u"orm['auth.User']"})
        },
        u'coco.fulldownloadstats': {
            'Meta': {'object_name': 'FullDownloadStats'},
            'end_time': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start_time': ('django.db.models.fields.DateTimeField', [], {}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'coco.loan': {
            'Meta': {'object_name': 'Loan'},
            'amount': ('django.db.models.fields.FloatField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'subtype': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['coco.LoanSubType']"}),
            'time_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'time_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['coco.LoanType']"}),
            'user_created': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'coco_loan_created'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'user_modified': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'coco_loan_related_modified'", 'null': 'True', 'to': u"orm['auth.User']"})
        },
        u'coco.loansubtype': {
            'Meta': {'object_name': 'LoanSubType'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'subtype_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'time_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'time_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['coco.LoanType']"}),
            'user_created': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'coco_loansubtype_created'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'user_modified': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'coco_loansubtype_related_modified'", 'null': 'True', 'to': u"orm['auth.User']"})
        },
        u'coco.loantype': {
            'Meta': {'object_name': 'LoanType'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'time_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'time_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'type_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'user_created': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'coco_loantype_created'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'user_modified': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'coco_loantype_related_modified'", 'null': 'True', 'to': u"orm['auth.User']"})
        },
        u'coco.person': {
            'Meta': {'unique_together': "(('person_name', 'spouse_name', 'village'),)", 'object_name': 'Person'},
            'date_of_entry': ('django.db.models.fields.DateField', [], {}),
            'house_hold_per_capita_income': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'job_card_number': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'no_of_adults': ('django.db.models.fields.IntegerField', [], {}),
            'no_of_children': ('django.db.models.fields.IntegerField', [], {}),
            'person_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'phone_no': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'spouse_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'time_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'time_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'coco_person_created'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'user_modified': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'coco_person_related_modified'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'village': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['coco.Village']"}),
            'voter_card_number': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'coco.serverlog': {
            'Meta': {'object_name': 'ServerLog'},
            'action': ('django.db.models.fields.IntegerField', [], {}),
            'entry_table': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model_id': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.utcnow'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'serverlog_user'", 'null': 'True', 'to': u"orm['auth.User']"})
        },
        u'coco.shgbaseline': {
            'Meta': {'unique_together': "(('group_name', 'cluster'),)", 'object_name': 'SHGBaseLine'},
            'bank_linkage': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'cc_limit': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'cluster': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['coco.Cluster']"}),
            'date_of_formation': ('django.db.models.fields.DateField', [], {}),
            'drawing_power': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'group_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'loan_account_balance': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'loan_account_number': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'savings_account_balance': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'savings_account_number': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'time_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'time_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'coco_shgbaseline_created'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'user_modified': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'coco_shgbaseline_related_modified'", 'null': 'True', 'to': u"orm['auth.User']"})
        },
        u'coco.shgprogram': {
            'Meta': {'object_name': 'SHGProgram'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'loan_from_kcc_or_mfis': ('django.db.models.fields.IntegerField', [], {}),
            'loan_from_money_lenders': ('django.db.models.fields.IntegerField', [], {}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['coco.Person']"}),
            'time_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'time_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'coco_shgprogram_created'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'user_modified': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'coco_shgprogram_related_modified'", 'null': 'True', 'to': u"orm['auth.User']"})
        },
        u'coco.state': {
            'Meta': {'object_name': 'State'},
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['coco.Country']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'state_name': ('django.db.models.fields.CharField', [], {'unique': "'True'", 'max_length': '100'}),
            'time_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'time_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'coco_state_created'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'user_modified': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'coco_state_related_modified'", 'null': 'True', 'to': u"orm['auth.User']"})
        },
        u'coco.sublocation': {
            'Meta': {'unique_together': "(('sublocation_name', 'block'),)", 'object_name': 'Sublocation'},
            'block': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['coco.Block']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sublocation_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'time_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'time_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'coco_sublocation_created'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'user_modified': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'coco_sublocation_related_modified'", 'null': 'True', 'to': u"orm['auth.User']"})
        },
        u'coco.village': {
            'Meta': {'unique_together': "(('village_name', 'sublocation'),)", 'object_name': 'Village'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sublocation': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['coco.Sublocation']"}),
            'time_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'time_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'coco_village_created'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'user_modified': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'coco_village_related_modified'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'village_name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['coco']
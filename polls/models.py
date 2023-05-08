from django.db import models
from django.utils import timezone
import datetime

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
    
class R1Code(models.Model):
    r_1_code = models.CharField(primary_key=True, max_length=2, db_column='r_1_code')
    r_1_desc_en = models.CharField(max_length=50, db_column='r_1_desc_en', verbose_name="English Description")
    r_1_desc_tr = models.CharField(max_length=50, db_column='r_1_desc_tr', verbose_name="Turkish Description")

    def __str__(self):
        return self.r_1_code

    class Meta:
        managed = False
        db_table = 'r1_code'

class R2Code(models.Model):
    r_1_code = models.CharField(max_length=2, db_column='r_1_code', verbose_name="r1_Code")
    r_2_code = models.CharField(max_length=2, db_column='r_2_code', verbose_name="r2_Code")
    r_2_desc_en = models.CharField(max_length=150, db_column='r_2_desc_en', verbose_name="English Description")
    r_2_desc_tr = models.CharField(max_length=150, db_column='r_2_desc_tr', verbose_name="Turkish Description")
    code_r2 = models.CharField(primary_key=True, max_length=150, db_column='code_r2',editable= False)

    def __str__(self):
        return f"{self.r_1_code}-{self.r_2_code}"

    class Meta:
        managed = False
        db_table = 'r2_code'
        unique_together = ('r_1_code', 'r_2_code')

    def _do_insert(self, manager, using, fields, update_pk, raw):
        fields = [
            f for f in fields if f.attname not in ['code_r2']
        ]
        return super()._do_insert(manager, using, fields, update_pk, raw)
    
class R3Code(models.Model):
    r_1_code = models.CharField(max_length=2, db_column='r_1_code', verbose_name="r1_Code")
    r_2_code = models.CharField(max_length=2, db_column='r_2_code', verbose_name="r2_Code")
    r_3_code = models.CharField(max_length=2, db_column='r_3_code', verbose_name="r3_Code")
    r_3_desc_en = models.CharField(max_length=150, db_column='r_3_desc_en', verbose_name="English Description")
    r_3_desc_tr = models.CharField(max_length=150, db_column='r_3_desc_tr', verbose_name="Turkish Description")
    code_r3 = models.CharField(primary_key=True, max_length=8, db_column='code_r3',editable= False)

    def __str__(self):
        return f"{self.r_1_code}-{self.r_2_code}-{self.r_3_code}"

    class Meta:
        managed = False
        db_table = 'r3_code'
        unique_together = ('r_1_code', 'r_2_code', 'r_3_code')

    def _do_insert(self, manager, using, fields, update_pk, raw):
        fields = [
            f for f in fields if f.attname not in ['code_r3']
        ]
        return super()._do_insert(manager, using, fields, update_pk, raw)
    
    def _do_update(self, base_qs, using, pk_val, values, update_fields, forced_update):
        values = [
            value for value in values if value[0].attname not in ['code_r3']
        ]
        return super()._do_update(base_qs, using, pk_val, values, update_fields, forced_update)
    
class R4Code(models.Model):
    r_1_code = models.CharField(max_length=2, db_column='r_1_code', verbose_name="r1_Code")
    r_2_code = models.CharField(max_length=2, db_column='r_2_code', verbose_name="r2_Code")
    r_3_code = models.CharField(max_length=2, db_column='r_3_code', verbose_name="r3_Code")
    r_4_code = models.CharField(max_length=3, db_column='r_4_code', verbose_name="r4_Code")
    r_4_desc_en = models.CharField(max_length=160, db_column='r_4_desc_en', verbose_name="English Description")
    r_4_desc_tr = models.CharField(max_length=150, db_column='r_4_desc_tr', verbose_name="Turkish Description")
    w_ufe = models.DecimalField(max_digits=7, decimal_places=5)
    w_tufe = models.DecimalField(max_digits=7, decimal_places=5)
    w_inf_usd = models.DecimalField(max_digits=7, decimal_places=5)
    w_inf_eur = models.DecimalField(max_digits=7, decimal_places=5)
    w_metal = models.DecimalField(max_digits=7, decimal_places=5)
    w_petrol = models.DecimalField(max_digits=7, decimal_places=5)
    w_cement = models.DecimalField(max_digits=7, decimal_places=5)
    w_electricity = models.DecimalField(max_digits=7, decimal_places=5)
    currency = models.CharField(max_length=3)
    administration = models.CharField(max_length=50, blank=True, null=True)
    admin_id = models.CharField(max_length=50, blank=True, null=True)
    r_loss = models.DecimalField(max_digits=7, decimal_places=5, blank=True, null=True)
    key_r4_simple = models.CharField(max_length=15, blank=True, null=True,editable= False)
    code_r4 = models.CharField(primary_key=True, max_length=8, db_column='code_r4',editable= False)

    def __str__(self):
        return f"{self.r_1_code}-{self.r_2_code}-{self.r_3_code}-{self.r_4_code}"

    class Meta:
        managed = False
        db_table = 'r4_code'
        unique_together = ('r_1_code', 'r_2_code', 'r_3_code', 'r_4_code')

    def _do_insert(self, manager, using, fields, update_pk, raw):
        fields = [
            f for f in fields if f.attname not in ['code_r4','key_r4_simple']
        ]
        return super()._do_insert(manager, using, fields, update_pk, raw)
    
    def _do_update(self, base_qs, using, pk_val, values, update_fields, forced_update):
        values = [
            value for value in values if value[0].attname not in ['code_r4','key_r4_simple']
        ]
        return super()._do_update(base_qs, using, pk_val, values, update_fields, forced_update)
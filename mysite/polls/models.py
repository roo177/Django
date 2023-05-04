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
    r_1_code = models.ForeignKey(R1Code, on_delete=models.CASCADE, related_name="related_r2_codes_set", verbose_name="R1code",db_column='r_1_code')
    r_2_code = models.CharField(max_length=2, db_column='r_2_code', verbose_name="Code")
    r_2_desc_en = models.CharField(max_length=150, db_column='r_2_desc_en', verbose_name="English Description")
    r_2_desc_tr = models.CharField(max_length=150, db_column='r_2_desc_tr', verbose_name="Turkish Description")
    code_r2 = models.CharField(primary_key=True, max_length=150, db_column='code_r2')

    def __str__(self):
        return f"{self.r_1_code}-{self.r_2_code}"

    class Meta:
        managed = False
        db_table = 'r2_code'
        unique_together = ('r_1_code', 'r_2_code')

class C1Code(models.Model):
    c_l1 = models.CharField(db_column='c_l1', max_length=2)  # Field name made lowercase.
    code_l1 = models.CharField(db_column='code_l1', max_length=2, primary_key=True)
    desc_en_l1 = models.CharField(db_column='desc_en_l1', max_length=255)  # Field name made lowercase.
    desc_tr_l1 = models.CharField(db_column='desc_tr_l1', max_length=255)  # Field name made lowercase.
    # id = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'c1_code'
    
    def __str__(self):
        return "{}".format(self.code_l1)

    def _do_insert(self, manager, using, fields, update_pk, raw):
        fields = [
            f for f in fields if f.attname not in ['code_l1']
        ]
        return super()._do_insert(manager, using, fields, update_pk, raw)


class C2Code(models.Model):
    c_l1 = models.CharField(db_column='c_l1', max_length=2)  # Field name made lowercase.
    c_l2 = models.CharField(db_column='c_l2', max_length=2)  # Field name made lowercase.
    code_l2 = models.CharField(db_column='code_l2', max_length=4, primary_key=True)  # Field name made lowercase.
    desc_tr_l2 = models.CharField(db_column='desc_tr_l2', max_length=255)  # Field name made lowercase.
    desc_en_l2 = models.CharField(db_column='desc_en_l2', max_length=255)  # Field name made lowercase.
    # id = models.IntegerField()
    # parentid = models.ForeignKey(C1Code, models.CASCADE, db_column='parentid')

    class Meta:
        managed = True
        db_table = 'c2_code'
        unique_together = (('c_l1', 'c_l2'),)
    
    def __str__(self):
        return "{}".format(self.code_l2)
    
    def _do_insert(self, manager, using, fields, update_pk, raw):
        fields = [
            f for f in fields if f.attname not in ['code_l2']
        ]
        return super()._do_insert(manager, using, fields, update_pk, raw)


class C3Code(models.Model):
    c_l1 = models.CharField(db_column='c_l1', max_length=2)  # Field name made lowercase.
    c_l2 = models.CharField(db_column='c_l2', max_length=2)  # Field name made lowercase.
    c_l3 = models.CharField(db_column='c_l3', max_length=2)  # Field name made lowercase.
    # code_l2 = models.CharField(db_column='Code_L2', max_length=243, blank=True, null=True)  # Field name made lowercase.
    code_l3 = models.CharField(db_column='code_l3', max_length=243, primary_key=True)  # Field name made lowercase.
    desc_tr_l3 = models.CharField(db_column='desc_tr_l3', max_length=255)  # Field name made lowercase.
    desc_en_l3 = models.CharField(db_column='desc_en_l3', max_length=255)  # Field name made lowercase.
    t_l3 = models.CharField(db_column='t_l3', max_length=7, blank=True, default="")  # Field name made lowercase.
    # id = models.IntegerField()
    # parentid = models.ForeignKey(C2Code, models.CASCADE, db_column='parentid')

    class Meta:
        managed = True
        db_table = 'c3_code'
        unique_together = (('c_l1', 'c_l2', 'c_l3'),)
    
    def __str__(self):
        return "{}".format(self.code_l3)
    
    def _do_insert(self, manager, using, fields, update_pk, raw):
        fields = [
            f for f in fields if f.attname not in ['code_l3']
        ]
        return super()._do_insert(manager, using, fields, update_pk, raw)


class C4Code(models.Model):
    c_l1 = models.CharField(db_column='c_l1', max_length=2)  # Field name made lowercase.
    c_l2 = models.CharField(db_column='c_l2', max_length=2)  # Field name made lowercase.
    c_l3 = models.CharField(db_column='c_l3', max_length=2)  # Field name made lowercase.
    c_l4 = models.CharField(db_column='c_l4', max_length=2)  # Field name made lowercase.
    # code_l3 = models.CharField(db_column='Code_L3', max_length=243, blank=True, null=True)  # Field name made lowercase.
    code_l4 = models.CharField(db_column='code_l4', max_length=243, primary_key=True)  # Field name made lowercase.
    desc_tr_l4 = models.CharField(db_column='desc_tr_l4', max_length=255)  # Field name made lowercase.
    desc_en_l4 = models.CharField(db_column='desc_en_l4', max_length=255)  # Field name made lowercase.
    t_l3 = models.CharField(db_column='t_l3', max_length=7, blank=True, null=True)  # Field name made lowercase.
    t_l4 = models.CharField(db_column='t_l4', max_length=2, blank=True, null=True)  # Field name made lowercase.
    tmpl_l4 = models.CharField(db_column='tmpl_l4', max_length=10, blank=True, null=True)  # Field name made lowercase.
    # id = models.IntegerField()
    # parentid = models.ForeignKey(C3Code, models.CASCADE, db_column='parentid')

    class Meta:
        managed = True
        db_table = 'c4_code'
        unique_together = (('c_l1', 'c_l2', 'c_l3', 'c_l4'),)
    
    def __str__(self):
        return "{}".format(self.code_l4)
    
    def _do_insert(self, manager, using, fields, update_pk, raw):
        fields = [
            f for f in fields if f.attname not in ['code_l4', 'tmpl_l4']
        ]
        return super()._do_insert(manager, using, fields, update_pk, raw)


class C5Code(models.Model):
    c_l1 = models.CharField(db_column='c_l1', max_length=2)  # Field name made lowercase.
    c_l2 = models.CharField(db_column='c_l2', max_length=2)  # Field name made lowercase.
    c_l3 = models.CharField(db_column='c_l3', max_length=2)  # Field name made lowercase.
    c_l4 = models.CharField(db_column='c_l4', max_length=2)  # Field name made lowercase.
    c_l5 = models.CharField(db_column='c_l5', max_length=2)  # Field name made lowercase.
    # code_l4 = models.CharField(db_column='Code_L4', max_length=243, blank=True, null=True)  # Field name made lowercase.
    code_l5 = models.CharField(db_column='code_l5', max_length=243, primary_key=True)  # Field name made lowercase.
    desc_tr_l5 = models.CharField(db_column='desc_tr_l5', max_length=255, blank=True, default="")  # Field name made lowercase.
    desc_en_l5 = models.CharField(db_column='desc_en_l5', max_length=255, blank=True, default="")  # Field name made lowercase.
    t_l3 = models.CharField(db_column='t_l3', max_length=7, blank=True, null=True)  # Field name made lowercase.
    t_l4 = models.CharField(db_column='t_l4', max_length=2, blank=True, null=True)  # Field name made lowercase.
    t_l5 = models.CharField(db_column='t_l5', max_length=2, blank=True, null=True)  # Field name made lowercase.
    unit = models.CharField(db_column='unit', max_length=10, blank=True, null=True)  # Field name made lowercase.
    d_pre_tr = models.CharField(db_column='d_pre_tr', max_length=7, blank=True, null=True)  # Field name made lowercase.
    d_pre_en = models.CharField(db_column='d_pre_en', max_length=255, blank=True, null=True)  # Field name made lowercase.
    templ_l5 = models.CharField(db_column='templ_l5', max_length=243, blank=True, null=True)  # Field name made lowercase.
    # id = models.IntegerField()
    # parentid = models.ForeignKey(C4Code, models.CASCADE, db_column='parentid')

    class Meta:
        managed = True
        db_table = 'c5_code'
        unique_together = (('c_l1', 'c_l2', 'c_l3', 'c_l4', 'c_l5'),)
    
    def __str__(self):
        return "{}".format(self.code_l5)
    
    def _do_insert(self, manager, using, fields, update_pk, raw):
        fields = [
            f for f in fields if f.attname not in ['code_l5', 'templ_l5']
        ]
        return super()._do_insert(manager, using, fields, update_pk, raw)


class C6Code(models.Model):
    c_l1 = models.CharField(db_column='c_l1', max_length=2)  # Field name made lowercase.
    c_l2 = models.CharField(db_column='c_l2', max_length=2)  # Field name made lowercase.
    c_l3 = models.CharField(db_column='c_l3', max_length=2)  # Field name made lowercase.
    c_l4 = models.CharField(db_column='c_l4', max_length=2)  # Field name made lowercase.
    c_l5 = models.CharField(db_column='c_l5', max_length=2)  # Field name made lowercase.
    c_l6 = models.CharField(db_column='c_l6', max_length=3)  # Field name made lowercase.
    # code_l5 = models.CharField(db_column='Code_L5', max_length=243, blank=True, null=True, default="01")  # Field name made lowercase.
    code_l6 = models.CharField(db_column='code_l6', max_length=243, primary_key=True)  # Field name made lowercase.
    desc_tr_l6 = models.CharField(db_column='desc_tr_l6', max_length=150)  # Field name made lowercase.
    desc_en_l6 = models.CharField(db_column='desc_en_l6', max_length=150)  # Field name made lowercase.
    unit = models.CharField(db_column='unit', max_length=10, blank=True, null=True)  # Field name made lowercase.
    t_l3 = models.CharField(db_column='t_l3', max_length=7, blank=True, null=True)  # Field name made lowercase.
    t_l4 = models.CharField(db_column='t_l4', max_length=2, blank=True, null=True)  # Field name made lowercase.
    t_l5 = models.CharField(db_column='t_l5', max_length=2, blank=True, null=True)  # Field name made lowercase.
    t_l6 = models.CharField(db_column='t_l6', max_length=3, blank=True, null=True)  # Field name made lowercase.
    f2_lm = models.CharField(db_column='f2_lm', max_length=6, blank=True, null=True)  # Field name made lowercase.
    # id = models.IntegerField()
    # parentid = models.ForeignKey(C5Code, models.CASCADE, db_column='parentid')

    class Meta:
        managed = True
        db_table = 'c6_code'
        unique_together = (('c_l1', 'c_l2', 'c_l3', 'c_l4', 'c_l5', 'c_l6'),)
    
    def __str__(self):
        return "{}".format(self.code_l6)
    
    def _do_insert(self, manager, using, fields, update_pk, raw):
        fields = [
            f for f in fields if f.attname not in ['code_l6']
        ]
        return super()._do_insert(manager, using, fields, update_pk, raw)
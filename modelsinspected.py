# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Project(models.Model):
    user = models.ForeignKey('Users', models.DO_NOTHING, db_column='user', blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    is_active = models.BooleanField(blank=True, null=True)
    pcode = models.CharField(primary_key=True, max_length=10)

    class Meta:
        managed = False
        db_table = 'Project'


class Table11ExpenseCr(models.Model):
    rep_month = models.CharField(db_column='rep_Month', primary_key=True, max_length=4)  # Field name made lowercase. The composite primary key (rep_Month, p_Code, L1, L2, L3, L4, L5, L6) found, that is not supported. The first column is selected.
    p_code = models.CharField(db_column='p_Code', max_length=3)  # Field name made lowercase.
    l1 = models.CharField(db_column='L1', max_length=1)  # Field name made lowercase.
    l2 = models.CharField(db_column='L2', max_length=2)  # Field name made lowercase.
    l3 = models.CharField(db_column='L3', max_length=2)  # Field name made lowercase.
    l4 = models.CharField(db_column='L4', max_length=2)  # Field name made lowercase.
    l5 = models.CharField(db_column='L5', max_length=2)  # Field name made lowercase.
    l6 = models.CharField(db_column='L6', max_length=3)  # Field name made lowercase.
    unit_price = models.DecimalField(db_column='Unit_Price', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    unit = models.CharField(db_column='Unit', max_length=25, blank=True, null=True)  # Field name made lowercase.
    code_l5 = models.CharField(db_column='Code_L5', max_length=243, blank=True, null=True)  # Field name made lowercase.
    code_l6 = models.CharField(db_column='Code_L6', max_length=243, blank=True, null=True)  # Field name made lowercase.
    ex_1706 = models.DecimalField(db_column='EX_1706', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_1707 = models.DecimalField(db_column='EX_1707', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_1708 = models.DecimalField(db_column='EX_1708', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_1709 = models.DecimalField(db_column='EX_1709', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_1710 = models.DecimalField(db_column='EX_1710', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_1711 = models.DecimalField(db_column='EX_1711', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_1712 = models.DecimalField(db_column='EX_1712', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_1801 = models.DecimalField(db_column='EX_1801', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_1802 = models.DecimalField(db_column='EX_1802', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_1803 = models.DecimalField(db_column='EX_1803', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_1804 = models.DecimalField(db_column='EX_1804', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_1805 = models.DecimalField(db_column='EX_1805', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_1806 = models.DecimalField(db_column='EX_1806', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_1807 = models.DecimalField(db_column='EX_1807', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_1808 = models.DecimalField(db_column='EX_1808', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_1809 = models.DecimalField(db_column='EX_1809', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_1810 = models.DecimalField(db_column='EX_1810', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_1811 = models.DecimalField(db_column='EX_1811', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_1812 = models.DecimalField(db_column='EX_1812', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_1901 = models.DecimalField(db_column='EX_1901', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_1902 = models.DecimalField(db_column='EX_1902', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_1903 = models.DecimalField(db_column='EX_1903', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_1904 = models.DecimalField(db_column='EX_1904', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_1905 = models.DecimalField(db_column='EX_1905', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_1906 = models.DecimalField(db_column='EX_1906', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_1907 = models.DecimalField(db_column='EX_1907', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_1908 = models.DecimalField(db_column='EX_1908', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_1909 = models.DecimalField(db_column='EX_1909', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_1910 = models.DecimalField(db_column='EX_1910', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_1911 = models.DecimalField(db_column='EX_1911', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_1912 = models.DecimalField(db_column='EX_1912', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2001 = models.DecimalField(db_column='EX_2001', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2002 = models.DecimalField(db_column='EX_2002', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2003 = models.DecimalField(db_column='EX_2003', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2004 = models.DecimalField(db_column='EX_2004', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2005 = models.DecimalField(db_column='EX_2005', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2006 = models.DecimalField(db_column='EX_2006', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2007 = models.DecimalField(db_column='EX_2007', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2008 = models.DecimalField(db_column='EX_2008', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2009 = models.DecimalField(db_column='EX_2009', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2010 = models.DecimalField(db_column='EX_2010', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2011 = models.DecimalField(db_column='EX_2011', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2012 = models.DecimalField(db_column='EX_2012', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2101 = models.DecimalField(db_column='EX_2101', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2102 = models.DecimalField(db_column='EX_2102', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2103 = models.DecimalField(db_column='EX_2103', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2104 = models.DecimalField(db_column='EX_2104', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2105 = models.DecimalField(db_column='EX_2105', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2106 = models.DecimalField(db_column='EX_2106', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2107 = models.DecimalField(db_column='EX_2107', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2108 = models.DecimalField(db_column='EX_2108', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2109 = models.DecimalField(db_column='EX_2109', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2110 = models.DecimalField(db_column='EX_2110', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2111 = models.DecimalField(db_column='EX_2111', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2112 = models.DecimalField(db_column='EX_2112', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2201 = models.DecimalField(db_column='EX_2201', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2202 = models.DecimalField(db_column='EX_2202', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2203 = models.DecimalField(db_column='EX_2203', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2204 = models.DecimalField(db_column='EX_2204', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2205 = models.DecimalField(db_column='EX_2205', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2206 = models.DecimalField(db_column='EX_2206', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2207 = models.DecimalField(db_column='EX_2207', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2208 = models.DecimalField(db_column='EX_2208', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2209 = models.DecimalField(db_column='EX_2209', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2210 = models.DecimalField(db_column='EX_2210', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2211 = models.DecimalField(db_column='EX_2211', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2212 = models.DecimalField(db_column='EX_2212', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2301 = models.DecimalField(db_column='EX_2301', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2302 = models.DecimalField(db_column='EX_2302', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2303 = models.DecimalField(db_column='EX_2303', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2304 = models.DecimalField(db_column='EX_2304', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2305 = models.DecimalField(db_column='EX_2305', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2306 = models.DecimalField(db_column='EX_2306', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2307 = models.DecimalField(db_column='EX_2307', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2308 = models.DecimalField(db_column='EX_2308', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2309 = models.DecimalField(db_column='EX_2309', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2310 = models.DecimalField(db_column='EX_2310', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2311 = models.DecimalField(db_column='EX_2311', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2312 = models.DecimalField(db_column='EX_2312', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2401 = models.DecimalField(db_column='EX_2401', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2402 = models.DecimalField(db_column='EX_2402', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2403 = models.DecimalField(db_column='EX_2403', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2404 = models.DecimalField(db_column='EX_2404', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2405 = models.DecimalField(db_column='EX_2405', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2406 = models.DecimalField(db_column='EX_2406', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2407 = models.DecimalField(db_column='EX_2407', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2408 = models.DecimalField(db_column='EX_2408', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2409 = models.DecimalField(db_column='EX_2409', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2410 = models.DecimalField(db_column='EX_2410', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2411 = models.DecimalField(db_column='EX_2411', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2412 = models.DecimalField(db_column='EX_2412', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2501 = models.DecimalField(db_column='EX_2501', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2502 = models.DecimalField(db_column='EX_2502', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2503 = models.DecimalField(db_column='EX_2503', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2504 = models.DecimalField(db_column='EX_2504', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2505 = models.DecimalField(db_column='EX_2505', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2506 = models.DecimalField(db_column='EX_2506', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2507 = models.DecimalField(db_column='EX_2507', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2508 = models.DecimalField(db_column='EX_2508', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2509 = models.DecimalField(db_column='EX_2509', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2510 = models.DecimalField(db_column='EX_2510', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2511 = models.DecimalField(db_column='EX_2511', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2512 = models.DecimalField(db_column='EX_2512', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2601 = models.DecimalField(db_column='EX_2601', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2602 = models.DecimalField(db_column='EX_2602', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2603 = models.DecimalField(db_column='EX_2603', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2604 = models.DecimalField(db_column='EX_2604', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2605 = models.DecimalField(db_column='EX_2605', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2606 = models.DecimalField(db_column='EX_2606', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2607 = models.DecimalField(db_column='EX_2607', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2608 = models.DecimalField(db_column='EX_2608', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2609 = models.DecimalField(db_column='EX_2609', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2610 = models.DecimalField(db_column='EX_2610', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2611 = models.DecimalField(db_column='EX_2611', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2612 = models.DecimalField(db_column='EX_2612', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2701 = models.DecimalField(db_column='EX_2701', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2702 = models.DecimalField(db_column='EX_2702', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2703 = models.DecimalField(db_column='EX_2703', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2704 = models.DecimalField(db_column='EX_2704', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2705 = models.DecimalField(db_column='EX_2705', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2706 = models.DecimalField(db_column='EX_2706', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2707 = models.DecimalField(db_column='EX_2707', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2708 = models.DecimalField(db_column='EX_2708', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2709 = models.DecimalField(db_column='EX_2709', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2710 = models.DecimalField(db_column='EX_2710', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2711 = models.DecimalField(db_column='EX_2711', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2712 = models.DecimalField(db_column='EX_2712', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Table_11_Expense_CR'
        unique_together = (('rep_month', 'p_code', 'l1', 'l2', 'l3', 'l4', 'l5', 'l6'),)


class Table12ExpenseAb(models.Model):
    rep_month = models.CharField(db_column='rep_Month', primary_key=True, max_length=4)  # Field name made lowercase. The composite primary key (rep_Month, p_Code, L1, L2, L3, L4, L5, L6) found, that is not supported. The first column is selected.
    p_code = models.CharField(db_column='p_Code', max_length=3)  # Field name made lowercase.
    l1 = models.CharField(db_column='L1', max_length=1)  # Field name made lowercase.
    l2 = models.CharField(db_column='L2', max_length=2)  # Field name made lowercase.
    l3 = models.CharField(db_column='L3', max_length=2)  # Field name made lowercase.
    l4 = models.CharField(db_column='L4', max_length=2)  # Field name made lowercase.
    l5 = models.CharField(db_column='L5', max_length=2)  # Field name made lowercase.
    l6 = models.CharField(db_column='L6', max_length=3)  # Field name made lowercase.
    ex_1706 = models.DecimalField(db_column='EX_1706', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_1707 = models.DecimalField(db_column='EX_1707', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_1708 = models.DecimalField(db_column='EX_1708', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_1709 = models.DecimalField(db_column='EX_1709', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_1710 = models.DecimalField(db_column='EX_1710', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_1711 = models.DecimalField(db_column='EX_1711', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_1712 = models.DecimalField(db_column='EX_1712', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_1801 = models.DecimalField(db_column='EX_1801', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_1802 = models.DecimalField(db_column='EX_1802', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_1803 = models.DecimalField(db_column='EX_1803', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_1804 = models.DecimalField(db_column='EX_1804', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_1805 = models.DecimalField(db_column='EX_1805', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_1806 = models.DecimalField(db_column='EX_1806', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_1807 = models.DecimalField(db_column='EX_1807', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_1808 = models.DecimalField(db_column='EX_1808', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_1809 = models.DecimalField(db_column='EX_1809', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_1810 = models.DecimalField(db_column='EX_1810', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_1811 = models.DecimalField(db_column='EX_1811', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_1812 = models.DecimalField(db_column='EX_1812', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_1901 = models.DecimalField(db_column='EX_1901', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_1902 = models.DecimalField(db_column='EX_1902', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_1903 = models.DecimalField(db_column='EX_1903', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_1904 = models.DecimalField(db_column='EX_1904', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_1905 = models.DecimalField(db_column='EX_1905', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_1906 = models.DecimalField(db_column='EX_1906', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_1907 = models.DecimalField(db_column='EX_1907', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_1908 = models.DecimalField(db_column='EX_1908', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_1909 = models.DecimalField(db_column='EX_1909', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_1910 = models.DecimalField(db_column='EX_1910', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_1911 = models.DecimalField(db_column='EX_1911', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_1912 = models.DecimalField(db_column='EX_1912', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2001 = models.DecimalField(db_column='EX_2001', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2002 = models.DecimalField(db_column='EX_2002', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2003 = models.DecimalField(db_column='EX_2003', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2004 = models.DecimalField(db_column='EX_2004', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2005 = models.DecimalField(db_column='EX_2005', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2006 = models.DecimalField(db_column='EX_2006', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2007 = models.DecimalField(db_column='EX_2007', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2008 = models.DecimalField(db_column='EX_2008', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2009 = models.DecimalField(db_column='EX_2009', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2010 = models.DecimalField(db_column='EX_2010', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2011 = models.DecimalField(db_column='EX_2011', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2012 = models.DecimalField(db_column='EX_2012', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2101 = models.DecimalField(db_column='EX_2101', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2102 = models.DecimalField(db_column='EX_2102', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2103 = models.DecimalField(db_column='EX_2103', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2104 = models.DecimalField(db_column='EX_2104', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2105 = models.DecimalField(db_column='EX_2105', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2106 = models.DecimalField(db_column='EX_2106', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2107 = models.DecimalField(db_column='EX_2107', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2108 = models.DecimalField(db_column='EX_2108', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2109 = models.DecimalField(db_column='EX_2109', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2110 = models.DecimalField(db_column='EX_2110', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2111 = models.DecimalField(db_column='EX_2111', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2112 = models.DecimalField(db_column='EX_2112', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2201 = models.DecimalField(db_column='EX_2201', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2202 = models.DecimalField(db_column='EX_2202', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2203 = models.DecimalField(db_column='EX_2203', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2204 = models.DecimalField(db_column='EX_2204', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2205 = models.DecimalField(db_column='EX_2205', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2206 = models.DecimalField(db_column='EX_2206', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2207 = models.DecimalField(db_column='EX_2207', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2208 = models.DecimalField(db_column='EX_2208', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2209 = models.DecimalField(db_column='EX_2209', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2210 = models.DecimalField(db_column='EX_2210', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2211 = models.DecimalField(db_column='EX_2211', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2212 = models.DecimalField(db_column='EX_2212', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2301 = models.DecimalField(db_column='EX_2301', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2302 = models.DecimalField(db_column='EX_2302', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2303 = models.DecimalField(db_column='EX_2303', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2304 = models.DecimalField(db_column='EX_2304', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2305 = models.DecimalField(db_column='EX_2305', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2306 = models.DecimalField(db_column='EX_2306', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2307 = models.DecimalField(db_column='EX_2307', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2308 = models.DecimalField(db_column='EX_2308', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2309 = models.DecimalField(db_column='EX_2309', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2310 = models.DecimalField(db_column='EX_2310', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2311 = models.DecimalField(db_column='EX_2311', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2312 = models.DecimalField(db_column='EX_2312', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2401 = models.DecimalField(db_column='EX_2401', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2402 = models.DecimalField(db_column='EX_2402', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2403 = models.DecimalField(db_column='EX_2403', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2404 = models.DecimalField(db_column='EX_2404', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2405 = models.DecimalField(db_column='EX_2405', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2406 = models.DecimalField(db_column='EX_2406', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2407 = models.DecimalField(db_column='EX_2407', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2408 = models.DecimalField(db_column='EX_2408', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2409 = models.DecimalField(db_column='EX_2409', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2410 = models.DecimalField(db_column='EX_2410', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2411 = models.DecimalField(db_column='EX_2411', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2412 = models.DecimalField(db_column='EX_2412', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2501 = models.DecimalField(db_column='EX_2501', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2502 = models.DecimalField(db_column='EX_2502', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2503 = models.DecimalField(db_column='EX_2503', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2504 = models.DecimalField(db_column='EX_2504', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2505 = models.DecimalField(db_column='EX_2505', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2506 = models.DecimalField(db_column='EX_2506', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2507 = models.DecimalField(db_column='EX_2507', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2508 = models.DecimalField(db_column='EX_2508', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2509 = models.DecimalField(db_column='EX_2509', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2510 = models.DecimalField(db_column='EX_2510', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2511 = models.DecimalField(db_column='EX_2511', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2512 = models.DecimalField(db_column='EX_2512', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2601 = models.DecimalField(db_column='EX_2601', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2602 = models.DecimalField(db_column='EX_2602', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2603 = models.DecimalField(db_column='EX_2603', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2604 = models.DecimalField(db_column='EX_2604', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2605 = models.DecimalField(db_column='EX_2605', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2606 = models.DecimalField(db_column='EX_2606', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2607 = models.DecimalField(db_column='EX_2607', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2608 = models.DecimalField(db_column='EX_2608', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2609 = models.DecimalField(db_column='EX_2609', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2610 = models.DecimalField(db_column='EX_2610', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2611 = models.DecimalField(db_column='EX_2611', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2612 = models.DecimalField(db_column='EX_2612', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2701 = models.DecimalField(db_column='EX_2701', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2702 = models.DecimalField(db_column='EX_2702', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2703 = models.DecimalField(db_column='EX_2703', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2704 = models.DecimalField(db_column='EX_2704', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2705 = models.DecimalField(db_column='EX_2705', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2706 = models.DecimalField(db_column='EX_2706', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2707 = models.DecimalField(db_column='EX_2707', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2708 = models.DecimalField(db_column='EX_2708', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2709 = models.DecimalField(db_column='EX_2709', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2710 = models.DecimalField(db_column='EX_2710', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2711 = models.DecimalField(db_column='EX_2711', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ex_2712 = models.DecimalField(db_column='EX_2712', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    code_l5 = models.CharField(db_column='Code_L5', max_length=243, blank=True, null=True)  # Field name made lowercase.
    code_l6 = models.CharField(db_column='Code_L6', max_length=243, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Table_12_Expense_AB'
        unique_together = (('rep_month', 'p_code', 'l1', 'l2', 'l3', 'l4', 'l5', 'l6'),)


class Table13IncomeCr(models.Model):
    rep_month = models.CharField(db_column='rep_Month', primary_key=True, max_length=4)  # Field name made lowercase. The composite primary key (rep_Month, p_Code, L1, L2, L3, L4, L5, L6) found, that is not supported. The first column is selected.
    p_code = models.CharField(db_column='p_Code', max_length=3)  # Field name made lowercase.
    l1 = models.CharField(db_column='L1', max_length=1)  # Field name made lowercase.
    l2 = models.CharField(db_column='L2', max_length=2)  # Field name made lowercase.
    l3 = models.CharField(db_column='L3', max_length=2)  # Field name made lowercase.
    l4 = models.CharField(db_column='L4', max_length=2)  # Field name made lowercase.
    l5 = models.CharField(db_column='L5', max_length=2)  # Field name made lowercase.
    l6 = models.CharField(db_column='L6', max_length=3)  # Field name made lowercase.
    unit_price = models.DecimalField(db_column='Unit_Price', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    unit = models.CharField(db_column='Unit', max_length=25, blank=True, null=True)  # Field name made lowercase.
    task = models.CharField(db_column='Task', max_length=6, blank=True, null=True)  # Field name made lowercase.
    in_1706 = models.DecimalField(db_column='IN_1706', max_digits=15, decimal_places=2)  # Field name made lowercase.
    in_1707 = models.DecimalField(db_column='IN_1707', max_digits=15, decimal_places=2)  # Field name made lowercase.
    in_1708 = models.DecimalField(db_column='IN_1708', max_digits=15, decimal_places=2)  # Field name made lowercase.
    in_1709 = models.DecimalField(db_column='IN_1709', max_digits=15, decimal_places=2)  # Field name made lowercase.
    in_1710 = models.DecimalField(db_column='IN_1710', max_digits=15, decimal_places=2)  # Field name made lowercase.
    in_1711 = models.DecimalField(db_column='IN_1711', max_digits=15, decimal_places=2)  # Field name made lowercase.
    in_1712 = models.DecimalField(db_column='IN_1712', max_digits=15, decimal_places=2)  # Field name made lowercase.
    in_1801 = models.DecimalField(db_column='IN_1801', max_digits=15, decimal_places=2)  # Field name made lowercase.
    in_1802 = models.DecimalField(db_column='IN_1802', max_digits=15, decimal_places=2)  # Field name made lowercase.
    in_1803 = models.DecimalField(db_column='IN_1803', max_digits=15, decimal_places=2)  # Field name made lowercase.
    in_1804 = models.DecimalField(db_column='IN_1804', max_digits=15, decimal_places=2)  # Field name made lowercase.
    in_1805 = models.DecimalField(db_column='IN_1805', max_digits=15, decimal_places=2)  # Field name made lowercase.
    in_1806 = models.DecimalField(db_column='IN_1806', max_digits=15, decimal_places=2)  # Field name made lowercase.
    in_1807 = models.DecimalField(db_column='IN_1807', max_digits=15, decimal_places=2)  # Field name made lowercase.
    in_1808 = models.DecimalField(db_column='IN_1808', max_digits=15, decimal_places=2)  # Field name made lowercase.
    in_1809 = models.DecimalField(db_column='IN_1809', max_digits=15, decimal_places=2)  # Field name made lowercase.
    in_1810 = models.DecimalField(db_column='IN_1810', max_digits=15, decimal_places=2)  # Field name made lowercase.
    in_1811 = models.DecimalField(db_column='IN_1811', max_digits=15, decimal_places=2)  # Field name made lowercase.
    in_1812 = models.DecimalField(db_column='IN_1812', max_digits=15, decimal_places=2)  # Field name made lowercase.
    in_1901 = models.DecimalField(db_column='IN_1901', max_digits=15, decimal_places=2)  # Field name made lowercase.
    in_1902 = models.DecimalField(db_column='IN_1902', max_digits=15, decimal_places=2)  # Field name made lowercase.
    in_1903 = models.DecimalField(db_column='IN_1903', max_digits=15, decimal_places=2)  # Field name made lowercase.
    in_1904 = models.DecimalField(db_column='IN_1904', max_digits=15, decimal_places=2)  # Field name made lowercase.
    in_1905 = models.DecimalField(db_column='IN_1905', max_digits=15, decimal_places=2)  # Field name made lowercase.
    in_1906 = models.DecimalField(db_column='IN_1906', max_digits=15, decimal_places=2)  # Field name made lowercase.
    in_1907 = models.DecimalField(db_column='IN_1907', max_digits=15, decimal_places=2)  # Field name made lowercase.
    in_1908 = models.DecimalField(db_column='IN_1908', max_digits=15, decimal_places=2)  # Field name made lowercase.
    in_1909 = models.DecimalField(db_column='IN_1909', max_digits=15, decimal_places=2)  # Field name made lowercase.
    in_1910 = models.DecimalField(db_column='IN_1910', max_digits=15, decimal_places=2)  # Field name made lowercase.
    in_1911 = models.DecimalField(db_column='IN_1911', max_digits=15, decimal_places=2)  # Field name made lowercase.
    in_1912 = models.DecimalField(db_column='IN_1912', max_digits=15, decimal_places=2)  # Field name made lowercase.
    in_2001 = models.DecimalField(db_column='IN_2001', max_digits=15, decimal_places=2)  # Field name made lowercase.
    in_2002 = models.DecimalField(db_column='IN_2002', max_digits=15, decimal_places=2)  # Field name made lowercase.
    in_2003 = models.DecimalField(db_column='IN_2003', max_digits=15, decimal_places=2)  # Field name made lowercase.
    in_2004 = models.DecimalField(db_column='IN_2004', max_digits=15, decimal_places=2)  # Field name made lowercase.
    in_2005 = models.DecimalField(db_column='IN_2005', max_digits=15, decimal_places=2)  # Field name made lowercase.
    in_2006 = models.DecimalField(db_column='IN_2006', max_digits=15, decimal_places=2)  # Field name made lowercase.
    in_2007 = models.DecimalField(db_column='IN_2007', max_digits=15, decimal_places=2)  # Field name made lowercase.
    in_2008 = models.DecimalField(db_column='IN_2008', max_digits=15, decimal_places=2)  # Field name made lowercase.
    in_2009 = models.DecimalField(db_column='IN_2009', max_digits=15, decimal_places=2)  # Field name made lowercase.
    in_2010 = models.DecimalField(db_column='IN_2010', max_digits=15, decimal_places=2)  # Field name made lowercase.
    in_2011 = models.DecimalField(db_column='IN_2011', max_digits=15, decimal_places=2)  # Field name made lowercase.
    in_2012 = models.DecimalField(db_column='IN_2012', max_digits=15, decimal_places=2)  # Field name made lowercase.
    in_2101 = models.DecimalField(db_column='IN_2101', max_digits=15, decimal_places=2)  # Field name made lowercase.
    in_2102 = models.DecimalField(db_column='IN_2102', max_digits=15, decimal_places=2)  # Field name made lowercase.
    in_2103 = models.DecimalField(db_column='IN_2103', max_digits=15, decimal_places=2)  # Field name made lowercase.
    in_2104 = models.DecimalField(db_column='IN_2104', max_digits=15, decimal_places=2)  # Field name made lowercase.
    in_2105 = models.DecimalField(db_column='IN_2105', max_digits=15, decimal_places=2)  # Field name made lowercase.
    in_2106 = models.DecimalField(db_column='IN_2106', max_digits=15, decimal_places=2)  # Field name made lowercase.
    in_2107 = models.DecimalField(db_column='IN_2107', max_digits=15, decimal_places=2)  # Field name made lowercase.
    in_2108 = models.DecimalField(db_column='IN_2108', max_digits=15, decimal_places=2)  # Field name made lowercase.
    in_2109 = models.DecimalField(db_column='IN_2109', max_digits=15, decimal_places=2)  # Field name made lowercase.
    in_2110 = models.DecimalField(db_column='IN_2110', max_digits=15, decimal_places=2)  # Field name made lowercase.
    in_2111 = models.DecimalField(db_column='IN_2111', max_digits=15, decimal_places=2)  # Field name made lowercase.
    in_2112 = models.DecimalField(db_column='IN_2112', max_digits=15, decimal_places=2)  # Field name made lowercase.
    in_2201 = models.DecimalField(db_column='IN_2201', max_digits=15, decimal_places=2)  # Field name made lowercase.
    in_2202 = models.DecimalField(db_column='IN_2202', max_digits=15, decimal_places=2)  # Field name made lowercase.
    in_2203 = models.DecimalField(db_column='IN_2203', max_digits=15, decimal_places=2)  # Field name made lowercase.
    in_2204 = models.DecimalField(db_column='IN_2204', max_digits=15, decimal_places=2)  # Field name made lowercase.
    in_2205 = models.DecimalField(db_column='IN_2205', max_digits=15, decimal_places=2)  # Field name made lowercase.
    in_2206 = models.DecimalField(db_column='IN_2206', max_digits=15, decimal_places=2)  # Field name made lowercase.
    in_2207 = models.DecimalField(db_column='IN_2207', max_digits=15, decimal_places=2)  # Field name made lowercase.
    in_2208 = models.DecimalField(db_column='IN_2208', max_digits=15, decimal_places=2)  # Field name made lowercase.
    in_2209 = models.DecimalField(db_column='IN_2209', max_digits=15, decimal_places=2)  # Field name made lowercase.
    in_2210 = models.DecimalField(db_column='IN_2210', max_digits=15, decimal_places=2)  # Field name made lowercase.
    in_2211 = models.DecimalField(db_column='IN_2211', max_digits=15, decimal_places=2)  # Field name made lowercase.
    in_2212 = models.DecimalField(db_column='IN_2212', max_digits=15, decimal_places=2)  # Field name made lowercase.
    in_2301 = models.DecimalField(db_column='IN_2301', max_digits=15, decimal_places=2)  # Field name made lowercase.
    in_2302 = models.DecimalField(db_column='IN_2302', max_digits=15, decimal_places=2)  # Field name made lowercase.
    in_2303 = models.DecimalField(db_column='IN_2303', max_digits=15, decimal_places=2)  # Field name made lowercase.
    in_2304 = models.DecimalField(db_column='IN_2304', max_digits=15, decimal_places=2)  # Field name made lowercase.
    in_2305 = models.DecimalField(db_column='IN_2305', max_digits=15, decimal_places=2)  # Field name made lowercase.
    in_2306 = models.DecimalField(db_column='IN_2306', max_digits=15, decimal_places=2)  # Field name made lowercase.
    in_2307 = models.DecimalField(db_column='IN_2307', max_digits=15, decimal_places=2)  # Field name made lowercase.
    in_2308 = models.DecimalField(db_column='IN_2308', max_digits=15, decimal_places=2)  # Field name made lowercase.
    in_2309 = models.DecimalField(db_column='IN_2309', max_digits=15, decimal_places=2)  # Field name made lowercase.
    in_2310 = models.DecimalField(db_column='IN_2310', max_digits=15, decimal_places=2)  # Field name made lowercase.
    in_2311 = models.DecimalField(db_column='IN_2311', max_digits=15, decimal_places=2)  # Field name made lowercase.
    in_2312 = models.DecimalField(db_column='IN_2312', max_digits=15, decimal_places=2)  # Field name made lowercase.
    in_2401 = models.DecimalField(db_column='IN_2401', max_digits=15, decimal_places=2)  # Field name made lowercase.
    in_2402 = models.DecimalField(db_column='IN_2402', max_digits=15, decimal_places=2)  # Field name made lowercase.
    in_2403 = models.DecimalField(db_column='IN_2403', max_digits=15, decimal_places=2)  # Field name made lowercase.
    in_2404 = models.DecimalField(db_column='IN_2404', max_digits=15, decimal_places=2)  # Field name made lowercase.
    in_2405 = models.DecimalField(db_column='IN_2405', max_digits=15, decimal_places=2)  # Field name made lowercase.
    in_2406 = models.DecimalField(db_column='IN_2406', max_digits=15, decimal_places=2)  # Field name made lowercase.
    in_2407 = models.DecimalField(db_column='IN_2407', max_digits=15, decimal_places=2)  # Field name made lowercase.
    in_2408 = models.DecimalField(db_column='IN_2408', max_digits=15, decimal_places=2)  # Field name made lowercase.
    in_2409 = models.DecimalField(db_column='IN_2409', max_digits=15, decimal_places=2)  # Field name made lowercase.
    in_2410 = models.DecimalField(db_column='IN_2410', max_digits=15, decimal_places=2)  # Field name made lowercase.
    in_2411 = models.DecimalField(db_column='IN_2411', max_digits=15, decimal_places=2)  # Field name made lowercase.
    in_2412 = models.DecimalField(db_column='IN_2412', max_digits=15, decimal_places=2)  # Field name made lowercase.
    in_2501 = models.DecimalField(db_column='IN_2501', max_digits=15, decimal_places=2)  # Field name made lowercase.
    in_2502 = models.DecimalField(db_column='IN_2502', max_digits=15, decimal_places=2)  # Field name made lowercase.
    in_2503 = models.DecimalField(db_column='IN_2503', max_digits=15, decimal_places=2)  # Field name made lowercase.
    in_2504 = models.DecimalField(db_column='IN_2504', max_digits=15, decimal_places=2)  # Field name made lowercase.
    in_2505 = models.DecimalField(db_column='IN_2505', max_digits=15, decimal_places=2)  # Field name made lowercase.
    in_2506 = models.DecimalField(db_column='IN_2506', max_digits=15, decimal_places=2)  # Field name made lowercase.
    in_2507 = models.DecimalField(db_column='IN_2507', max_digits=15, decimal_places=2)  # Field name made lowercase.
    in_2508 = models.DecimalField(db_column='IN_2508', max_digits=15, decimal_places=2)  # Field name made lowercase.
    in_2509 = models.DecimalField(db_column='IN_2509', max_digits=15, decimal_places=2)  # Field name made lowercase.
    in_2510 = models.DecimalField(db_column='IN_2510', max_digits=15, decimal_places=2)  # Field name made lowercase.
    in_2511 = models.DecimalField(db_column='IN_2511', max_digits=15, decimal_places=2)  # Field name made lowercase.
    in_2512 = models.DecimalField(db_column='IN_2512', max_digits=15, decimal_places=2)  # Field name made lowercase.
    in_2601 = models.DecimalField(db_column='IN_2601', max_digits=15, decimal_places=2)  # Field name made lowercase.
    in_2602 = models.DecimalField(db_column='IN_2602', max_digits=15, decimal_places=2)  # Field name made lowercase.
    in_2603 = models.DecimalField(db_column='IN_2603', max_digits=15, decimal_places=2)  # Field name made lowercase.
    in_2604 = models.DecimalField(db_column='IN_2604', max_digits=15, decimal_places=2)  # Field name made lowercase.
    in_2605 = models.DecimalField(db_column='IN_2605', max_digits=15, decimal_places=2)  # Field name made lowercase.
    in_2606 = models.DecimalField(db_column='IN_2606', max_digits=15, decimal_places=2)  # Field name made lowercase.
    in_2607 = models.DecimalField(db_column='IN_2607', max_digits=15, decimal_places=2)  # Field name made lowercase.
    in_2608 = models.DecimalField(db_column='IN_2608', max_digits=15, decimal_places=2)  # Field name made lowercase.
    in_2609 = models.DecimalField(db_column='IN_2609', max_digits=15, decimal_places=2)  # Field name made lowercase.
    in_2610 = models.DecimalField(db_column='IN_2610', max_digits=15, decimal_places=2)  # Field name made lowercase.
    in_2611 = models.DecimalField(db_column='IN_2611', max_digits=15, decimal_places=2)  # Field name made lowercase.
    in_2612 = models.DecimalField(db_column='IN_2612', max_digits=15, decimal_places=2)  # Field name made lowercase.
    in_2701 = models.DecimalField(db_column='IN_2701', max_digits=15, decimal_places=2)  # Field name made lowercase.
    in_2702 = models.DecimalField(db_column='IN_2702', max_digits=15, decimal_places=2)  # Field name made lowercase.
    in_2703 = models.DecimalField(db_column='IN_2703', max_digits=15, decimal_places=2)  # Field name made lowercase.
    in_2704 = models.DecimalField(db_column='IN_2704', max_digits=15, decimal_places=2)  # Field name made lowercase.
    in_2705 = models.DecimalField(db_column='IN_2705', max_digits=15, decimal_places=2)  # Field name made lowercase.
    in_2706 = models.DecimalField(db_column='IN_2706', max_digits=15, decimal_places=2)  # Field name made lowercase.
    in_2707 = models.DecimalField(db_column='IN_2707', max_digits=15, decimal_places=2)  # Field name made lowercase.
    in_2708 = models.DecimalField(db_column='IN_2708', max_digits=15, decimal_places=2)  # Field name made lowercase.
    in_2709 = models.DecimalField(db_column='IN_2709', max_digits=15, decimal_places=2)  # Field name made lowercase.
    in_2710 = models.DecimalField(db_column='IN_2710', max_digits=15, decimal_places=2)  # Field name made lowercase.
    in_2711 = models.DecimalField(db_column='IN_2711', max_digits=15, decimal_places=2)  # Field name made lowercase.
    in_2712 = models.DecimalField(db_column='IN_2712', max_digits=15, decimal_places=2)  # Field name made lowercase.
    code_l5 = models.CharField(db_column='Code_L5', max_length=243, blank=True, null=True)  # Field name made lowercase.
    code_l6 = models.CharField(db_column='Code_L6', max_length=243, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Table_13_Income_CR'
        unique_together = (('rep_month', 'p_code', 'l1', 'l2', 'l3', 'l4', 'l5', 'l6'),)


class Table14IncomeAb(models.Model):
    rep_month = models.CharField(db_column='rep_Month', primary_key=True, max_length=4)  # Field name made lowercase. The composite primary key (rep_Month, p_Code, L2, L1, L3, L4, L5, L6) found, that is not supported. The first column is selected.
    p_code = models.CharField(db_column='p_Code', max_length=3)  # Field name made lowercase.
    l1 = models.CharField(db_column='L1', max_length=1)  # Field name made lowercase.
    l2 = models.CharField(db_column='L2', max_length=2)  # Field name made lowercase.
    l3 = models.CharField(db_column='L3', max_length=2)  # Field name made lowercase.
    l4 = models.CharField(db_column='L4', max_length=2)  # Field name made lowercase.
    l5 = models.CharField(db_column='L5', max_length=2)  # Field name made lowercase.
    l6 = models.CharField(db_column='L6', max_length=3)  # Field name made lowercase.
    in_1706 = models.DecimalField(db_column='IN_1706', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    in_1707 = models.DecimalField(db_column='IN_1707', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    in_1708 = models.DecimalField(db_column='IN_1708', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    in_1709 = models.DecimalField(db_column='IN_1709', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    in_1710 = models.DecimalField(db_column='IN_1710', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    in_1711 = models.DecimalField(db_column='IN_1711', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    in_1712 = models.DecimalField(db_column='IN_1712', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    in_1801 = models.DecimalField(db_column='IN_1801', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    in_1802 = models.DecimalField(db_column='IN_1802', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    in_1803 = models.DecimalField(db_column='IN_1803', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    in_1804 = models.DecimalField(db_column='IN_1804', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    in_1805 = models.DecimalField(db_column='IN_1805', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    in_1806 = models.DecimalField(db_column='IN_1806', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    in_1807 = models.DecimalField(db_column='IN_1807', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    in_1808 = models.DecimalField(db_column='IN_1808', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    in_1809 = models.DecimalField(db_column='IN_1809', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    in_1810 = models.DecimalField(db_column='IN_1810', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    in_1811 = models.DecimalField(db_column='IN_1811', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    in_1812 = models.DecimalField(db_column='IN_1812', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    in_1901 = models.DecimalField(db_column='IN_1901', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    in_1902 = models.DecimalField(db_column='IN_1902', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    in_1903 = models.DecimalField(db_column='IN_1903', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    in_1904 = models.DecimalField(db_column='IN_1904', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    in_1905 = models.DecimalField(db_column='IN_1905', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    in_1906 = models.DecimalField(db_column='IN_1906', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    in_1907 = models.DecimalField(db_column='IN_1907', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    in_1908 = models.DecimalField(db_column='IN_1908', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    in_1909 = models.DecimalField(db_column='IN_1909', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    in_1910 = models.DecimalField(db_column='IN_1910', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    in_1911 = models.DecimalField(db_column='IN_1911', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    in_1912 = models.DecimalField(db_column='IN_1912', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    in_2001 = models.DecimalField(db_column='IN_2001', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    in_2002 = models.DecimalField(db_column='IN_2002', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    in_2003 = models.DecimalField(db_column='IN_2003', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    in_2004 = models.DecimalField(db_column='IN_2004', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    in_2005 = models.DecimalField(db_column='IN_2005', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    in_2006 = models.DecimalField(db_column='IN_2006', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    in_2007 = models.DecimalField(db_column='IN_2007', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    in_2008 = models.DecimalField(db_column='IN_2008', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    in_2009 = models.DecimalField(db_column='IN_2009', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    in_2010 = models.DecimalField(db_column='IN_2010', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    in_2011 = models.DecimalField(db_column='IN_2011', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    in_2012 = models.DecimalField(db_column='IN_2012', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    in_2101 = models.DecimalField(db_column='IN_2101', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    in_2102 = models.DecimalField(db_column='IN_2102', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    in_2103 = models.DecimalField(db_column='IN_2103', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    in_2104 = models.DecimalField(db_column='IN_2104', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    in_2105 = models.DecimalField(db_column='IN_2105', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    in_2106 = models.DecimalField(db_column='IN_2106', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    in_2107 = models.DecimalField(db_column='IN_2107', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    in_2108 = models.DecimalField(db_column='IN_2108', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    in_2109 = models.DecimalField(db_column='IN_2109', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    in_2110 = models.DecimalField(db_column='IN_2110', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    in_2111 = models.DecimalField(db_column='IN_2111', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    in_2112 = models.DecimalField(db_column='IN_2112', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    in_2201 = models.DecimalField(db_column='IN_2201', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    in_2202 = models.DecimalField(db_column='IN_2202', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    in_2203 = models.DecimalField(db_column='IN_2203', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    in_2204 = models.DecimalField(db_column='IN_2204', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    in_2205 = models.DecimalField(db_column='IN_2205', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    in_2206 = models.DecimalField(db_column='IN_2206', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    in_2207 = models.DecimalField(db_column='IN_2207', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    in_2208 = models.DecimalField(db_column='IN_2208', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    in_2209 = models.DecimalField(db_column='IN_2209', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    in_2210 = models.DecimalField(db_column='IN_2210', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    in_2211 = models.DecimalField(db_column='IN_2211', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    in_2212 = models.DecimalField(db_column='IN_2212', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    in_2301 = models.DecimalField(db_column='IN_2301', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    in_2302 = models.DecimalField(db_column='IN_2302', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    in_2303 = models.DecimalField(db_column='IN_2303', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    in_2304 = models.DecimalField(db_column='IN_2304', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    in_2305 = models.DecimalField(db_column='IN_2305', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    in_2306 = models.DecimalField(db_column='IN_2306', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    in_2307 = models.DecimalField(db_column='IN_2307', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    in_2308 = models.DecimalField(db_column='IN_2308', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    in_2309 = models.DecimalField(db_column='IN_2309', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    in_2310 = models.DecimalField(db_column='IN_2310', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    in_2311 = models.DecimalField(db_column='IN_2311', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    in_2312 = models.DecimalField(db_column='IN_2312', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    in_2401 = models.DecimalField(db_column='IN_2401', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    in_2402 = models.DecimalField(db_column='IN_2402', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    in_2403 = models.DecimalField(db_column='IN_2403', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    in_2404 = models.DecimalField(db_column='IN_2404', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    in_2405 = models.DecimalField(db_column='IN_2405', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    in_2406 = models.DecimalField(db_column='IN_2406', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    in_2407 = models.DecimalField(db_column='IN_2407', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    in_2408 = models.DecimalField(db_column='IN_2408', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    in_2409 = models.DecimalField(db_column='IN_2409', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    in_2410 = models.DecimalField(db_column='IN_2410', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    in_2411 = models.DecimalField(db_column='IN_2411', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    in_2412 = models.DecimalField(db_column='IN_2412', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    in_2501 = models.DecimalField(db_column='IN_2501', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    in_2502 = models.DecimalField(db_column='IN_2502', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    in_2503 = models.DecimalField(db_column='IN_2503', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    in_2504 = models.DecimalField(db_column='IN_2504', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    in_2505 = models.DecimalField(db_column='IN_2505', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    in_2506 = models.DecimalField(db_column='IN_2506', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    in_2507 = models.DecimalField(db_column='IN_2507', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    in_2508 = models.DecimalField(db_column='IN_2508', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    in_2509 = models.DecimalField(db_column='IN_2509', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    in_2510 = models.DecimalField(db_column='IN_2510', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    in_2511 = models.DecimalField(db_column='IN_2511', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    in_2512 = models.DecimalField(db_column='IN_2512', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    in_2601 = models.DecimalField(db_column='IN_2601', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    in_2602 = models.DecimalField(db_column='IN_2602', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    in_2603 = models.DecimalField(db_column='IN_2603', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    in_2604 = models.DecimalField(db_column='IN_2604', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    in_2605 = models.DecimalField(db_column='IN_2605', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    in_2606 = models.DecimalField(db_column='IN_2606', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    in_2607 = models.DecimalField(db_column='IN_2607', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    in_2608 = models.DecimalField(db_column='IN_2608', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    in_2609 = models.DecimalField(db_column='IN_2609', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    in_2610 = models.DecimalField(db_column='IN_2610', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    in_2611 = models.DecimalField(db_column='IN_2611', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    in_2612 = models.DecimalField(db_column='IN_2612', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    in_2701 = models.DecimalField(db_column='IN_2701', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    in_2702 = models.DecimalField(db_column='IN_2702', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    in_2703 = models.DecimalField(db_column='IN_2703', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    in_2704 = models.DecimalField(db_column='IN_2704', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    in_2705 = models.DecimalField(db_column='IN_2705', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    in_2706 = models.DecimalField(db_column='IN_2706', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    in_2707 = models.DecimalField(db_column='IN_2707', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    in_2708 = models.DecimalField(db_column='IN_2708', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    in_2709 = models.DecimalField(db_column='IN_2709', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    in_2710 = models.DecimalField(db_column='IN_2710', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    in_2711 = models.DecimalField(db_column='IN_2711', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    in_2712 = models.DecimalField(db_column='IN_2712', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Table_14_Income_AB'
        unique_together = (('rep_month', 'p_code', 'l2', 'l1', 'l3', 'l4', 'l5', 'l6'),)


class Table24ExpDiffExplCm(models.Model):
    rep_month = models.CharField(db_column='rep_Month', primary_key=True, max_length=4)  # Field name made lowercase. The composite primary key (rep_Month, p_Code, L1, L2, L3, L4, L5, L6) found, that is not supported. The first column is selected.
    p_code = models.CharField(db_column='p_Code', max_length=3)  # Field name made lowercase.
    l1 = models.CharField(db_column='L1', max_length=1)  # Field name made lowercase.
    l2 = models.CharField(db_column='L2', max_length=2)  # Field name made lowercase.
    l3 = models.CharField(db_column='L3', max_length=2)  # Field name made lowercase.
    l4 = models.CharField(db_column='L4', max_length=2)  # Field name made lowercase.
    l5 = models.CharField(db_column='L5', max_length=2)  # Field name made lowercase.
    l6 = models.CharField(db_column='L6', max_length=3)  # Field name made lowercase.
    explanation = models.CharField(db_column='Explanation', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Table_24_Exp_Diff_Expl_CM'
        unique_together = (('rep_month', 'p_code', 'l1', 'l2', 'l3', 'l4', 'l5', 'l6'),)


class Table34ExpDiffExplRt(models.Model):
    rep_month = models.CharField(db_column='rep_Month', primary_key=True, max_length=4)  # Field name made lowercase. The composite primary key (rep_Month, p_Code, L1, L2, L3, L4, L5, L6) found, that is not supported. The first column is selected.
    p_code = models.CharField(db_column='p_Code', max_length=3)  # Field name made lowercase.
    l1 = models.CharField(db_column='L1', max_length=1)  # Field name made lowercase.
    l2 = models.CharField(db_column='L2', max_length=2)  # Field name made lowercase.
    l3 = models.CharField(db_column='L3', max_length=2)  # Field name made lowercase.
    l4 = models.CharField(db_column='L4', max_length=2)  # Field name made lowercase.
    l5 = models.CharField(db_column='L5', max_length=2)  # Field name made lowercase.
    l6 = models.CharField(db_column='L6', max_length=3)  # Field name made lowercase.
    explanation = models.CharField(db_column='Explanation', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Table_34_Exp_Diff_Expl_RT'
        unique_together = (('rep_month', 'p_code', 'l1', 'l2', 'l3', 'l4', 'l5', 'l6'),)


class Table44IncDiffExplCm(models.Model):
    rep_month = models.CharField(db_column='rep_Month', primary_key=True, max_length=4)  # Field name made lowercase. The composite primary key (rep_Month, p_Code, L1, L2, L3, L4, L5, L6) found, that is not supported. The first column is selected.
    p_code = models.CharField(db_column='p_Code', max_length=3)  # Field name made lowercase.
    l1 = models.CharField(db_column='L1', max_length=1)  # Field name made lowercase.
    l2 = models.CharField(db_column='L2', max_length=2)  # Field name made lowercase.
    l3 = models.CharField(db_column='L3', max_length=2)  # Field name made lowercase.
    l4 = models.CharField(db_column='L4', max_length=2)  # Field name made lowercase.
    l5 = models.CharField(db_column='L5', max_length=2)  # Field name made lowercase.
    l6 = models.CharField(db_column='L6', max_length=3)  # Field name made lowercase.
    explanation = models.TextField(db_column='Explanation', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Table_44_Inc_Diff_Expl_CM'
        unique_together = (('rep_month', 'p_code', 'l1', 'l2', 'l3', 'l4', 'l5', 'l6'),)


class Table54IncDiffExplRt(models.Model):
    rep_month = models.CharField(db_column='rep_Month', primary_key=True, max_length=4)  # Field name made lowercase. The composite primary key (rep_Month, p_Code, L1, L2, L3, L4, L5, L6) found, that is not supported. The first column is selected.
    p_code = models.CharField(db_column='p_Code', max_length=3)  # Field name made lowercase.
    l1 = models.CharField(db_column='L1', max_length=1)  # Field name made lowercase.
    l2 = models.CharField(db_column='L2', max_length=2)  # Field name made lowercase.
    l3 = models.CharField(db_column='L3', max_length=2)  # Field name made lowercase.
    l4 = models.CharField(db_column='L4', max_length=2)  # Field name made lowercase.
    l5 = models.CharField(db_column='L5', max_length=2)  # Field name made lowercase.
    l6 = models.CharField(db_column='L6', max_length=3)  # Field name made lowercase.
    explanation = models.CharField(db_column='Explanation', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Table_54_Inc_Diff_Expl_RT'
        unique_together = (('rep_month', 'p_code', 'l1', 'l2', 'l3', 'l4', 'l5', 'l6'),)


class AccountsUserprofile(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=50, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    zip = models.CharField(max_length=5, blank=True, null=True)
    photo = models.CharField(max_length=100, blank=True, null=True)
    user = models.OneToOneField('Users', models.DO_NOTHING, blank=True, null=True)
    emplotment_start_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'accounts_userprofile'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class C1Code(models.Model):
    c_l1 = models.CharField(primary_key=True, max_length=1)
    desc_en_l1 = models.CharField(max_length=255)
    desc_tr_l1 = models.CharField(max_length=255)
    code_l1 = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'c1_code'


class C2Code(models.Model):
    c_l1 = models.CharField(primary_key=True, max_length=1)  # The composite primary key (c_l1, c_l2) found, that is not supported. The first column is selected.
    c_l2 = models.CharField(max_length=2)
    desc_tr_l2 = models.CharField(max_length=255)
    desc_en_l2 = models.CharField(max_length=255)
    code_l2 = models.CharField(max_length=6, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'c2_code'
        unique_together = (('c_l1', 'c_l2'),)


class C3Code(models.Model):
    c_l1 = models.CharField(primary_key=True, max_length=1)  # The composite primary key (c_l1, c_l2, c_l3) found, that is not supported. The first column is selected.
    c_l2 = models.CharField(max_length=2)
    c_l3 = models.CharField(max_length=2)
    desc_tr_l3 = models.CharField(max_length=255)
    desc_en_l3 = models.CharField(max_length=255)
    t_l3 = models.CharField(max_length=7)
    code_l2 = models.CharField(max_length=6, blank=True, null=True)
    code_l3 = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'c3_code'
        unique_together = (('c_l1', 'c_l2', 'c_l3'),)


class C4Code(models.Model):
    c_l1 = models.CharField(primary_key=True, max_length=1)  # The composite primary key (c_l1, c_l2, c_l3, c_l4) found, that is not supported. The first column is selected.
    c_l2 = models.CharField(max_length=2)
    c_l3 = models.CharField(max_length=2)
    c_l4 = models.CharField(max_length=2)
    desc_tr_l4 = models.CharField(max_length=255)
    desc_en_l4 = models.CharField(max_length=255)
    t_l3 = models.CharField(max_length=7)
    t_l4 = models.CharField(max_length=2)
    code_l3 = models.CharField(max_length=10, blank=True, null=True)
    code_l4 = models.CharField(max_length=12, blank=True, null=True)
    tmpl_14 = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'c4_code'
        unique_together = (('c_l1', 'c_l2', 'c_l3', 'c_l4'),)


class C5Code(models.Model):
    c_l1 = models.CharField(primary_key=True, max_length=1)  # The composite primary key (c_l1, c_l2, c_l3, c_l4, c_l5) found, that is not supported. The first column is selected.
    c_l2 = models.CharField(max_length=2)
    c_l3 = models.CharField(max_length=2)
    c_l4 = models.CharField(max_length=2)
    c_l5 = models.CharField(max_length=2)
    desc_tr_l5 = models.CharField(max_length=255)
    desc_en_l5 = models.CharField(max_length=255)
    t_l3 = models.CharField(max_length=7)
    t_l4 = models.CharField(max_length=2)
    t_l5 = models.CharField(max_length=2)
    unit = models.CharField(max_length=10, blank=True, null=True)
    d_pre_tr = models.CharField(max_length=7, blank=True, null=True)
    d_pre_en = models.CharField(max_length=255, blank=True, null=True)
    code_l4 = models.CharField(max_length=12, blank=True, null=True)
    code_l5 = models.CharField(max_length=16, blank=True, null=True)
    templ_15 = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'c5_code'
        unique_together = (('c_l1', 'c_l2', 'c_l3', 'c_l4', 'c_l5'),)


class C6Code(models.Model):
    c_l1 = models.CharField(max_length=1)
    c_l2 = models.CharField(max_length=2)
    c_l3 = models.CharField(max_length=2)
    c_l4 = models.CharField(max_length=2)
    c_l5 = models.CharField(max_length=2)
    c_l6 = models.CharField(max_length=3)
    desc_tr_l6 = models.CharField(max_length=150)
    desc_en_l6 = models.CharField(max_length=150)
    unit = models.CharField(max_length=10, blank=True, null=True)
    t_l3 = models.CharField(max_length=7)
    t_l4 = models.CharField(max_length=2)
    t_l5 = models.CharField(max_length=2)
    t_l6 = models.CharField(max_length=3)
    f2_lm = models.CharField(max_length=6, blank=True, null=True)
    code_l5 = models.CharField(max_length=18, blank=True, null=True)
    code_l6 = models.CharField(unique=True, max_length=18, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'c6_code'


class CriticalLogs(models.Model):
    created_at = models.DateTimeField()
    id = models.BigAutoField(primary_key=True)
    error_type = models.CharField(max_length=60, blank=True, null=True)
    log_detail = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'critical_logs'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class ExportTest(models.Model):
    c_l1 = models.CharField(max_length=255, blank=True, null=True)
    c_l2 = models.CharField(max_length=255, blank=True, null=True)
    c_l3 = models.CharField(max_length=255, blank=True, null=True)
    c_l4 = models.CharField(max_length=255, blank=True, null=True)
    c_l5 = models.CharField(max_length=255, blank=True, null=True)
    c_l6 = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'export_test'


class GlobalVariables(models.Model):
    key = models.CharField(primary_key=True, max_length=255)
    value = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'global_variables'


class MonCurrRates(models.Model):
    rep_month = models.CharField(primary_key=True, max_length=4)  # The composite primary key (rep_month, month) found, that is not supported. The first column is selected.
    month = models.DateField()
    r_eur_try = models.DecimalField(max_digits=12, decimal_places=6, blank=True, null=True)
    r_usd_try = models.DecimalField(max_digits=12, decimal_places=6, blank=True, null=True)
    r_try_try = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)
    r_usd_usd = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)
    r_eur_eur = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)
    r_eur_usd = models.DecimalField(max_digits=12, decimal_places=6, blank=True, null=True)
    r_try_eur = models.DecimalField(max_digits=12, decimal_places=6, blank=True, null=True)
    r_usd_eur = models.DecimalField(max_digits=12, decimal_places=6, blank=True, null=True)
    r_try_usd = models.DecimalField(max_digits=12, decimal_places=6, blank=True, null=True)
    id = models.AutoField()

    class Meta:
        managed = False
        db_table = 'mon_curr_rates'
        unique_together = (('rep_month', 'month'),)


class PollsChoice(models.Model):
    id = models.BigAutoField(primary_key=True)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField()
    question = models.ForeignKey('PollsQuestion', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'polls_choice'


class PollsPencil(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'polls_pencil'


class PollsQuestion(models.Model):
    id = models.BigAutoField(primary_key=True)
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'polls_question'


class R1Code(models.Model):
    r_1_code = models.CharField(primary_key=True, max_length=2)
    r_1_desc_en = models.CharField(max_length=150, blank=True, null=True)
    r_1_desc_tr = models.CharField(max_length=150, blank=True, null=True)
    code_r1 = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'r1_code'


class R2Code(models.Model):
    r_1_code = models.OneToOneField(R1Code, models.DO_NOTHING, db_column='r_1_code', primary_key=True)  # The composite primary key (r_1_code, r_2_code) found, that is not supported. The first column is selected.
    r_2_code = models.CharField(max_length=2)
    r_2_desc_en = models.CharField(max_length=150, blank=True, null=True)
    r_2_desc_tr = models.CharField(max_length=150, blank=True, null=True)
    code_r2 = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'r2_code'
        unique_together = (('r_1_code', 'r_2_code'),)


class R3Code(models.Model):
    r_1_code = models.OneToOneField(R2Code, models.DO_NOTHING, db_column='r_1_code', primary_key=True)  # The composite primary key (r_1_code, r_2_code, r_3_code) found, that is not supported. The first column is selected.
    r_2_code = models.CharField(max_length=2)
    r_3_code = models.CharField(max_length=2)
    r_3_desc_en = models.CharField(max_length=150, blank=True, null=True)
    r_3_desc_tr = models.CharField(max_length=150, blank=True, null=True)
    code_r3 = models.CharField(max_length=8, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'r3_code'
        unique_together = (('r_1_code', 'r_2_code', 'r_3_code'),)


class R4Code(models.Model):
    r_1_code = models.CharField(max_length=2)
    r_2_code = models.CharField(max_length=2)
    r_3_code = models.CharField(max_length=2)
    r_4_code = models.CharField(max_length=3)
    unit = models.CharField(max_length=25)
    r_4_desc_en = models.CharField(max_length=160)
    r_4_desc_tr = models.CharField(max_length=160)
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
    key_r4_simple = models.CharField(max_length=15, blank=True, null=True)
    code_r4 = models.CharField(unique=True, max_length=12, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'r4_code'


class SpBgtAllJsn(models.Model):
    curr = models.CharField(blank=True, null=True)
    desc_tr = models.TextField(blank=True, null=True)
    mylink = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'sp_bgt_all_jsn'


class SpBgtApt(models.Model):
    rep_month = models.CharField(max_length=4, blank=True, null=True)
    p_code = models.CharField(max_length=3, blank=True, null=True)
    curr = models.CharField(blank=True, null=True)
    code_l6 = models.CharField(max_length=50, blank=True, null=True)
    code_l5 = models.TextField(blank=True, null=True)
    code_l4 = models.TextField(blank=True, null=True)
    code_l3 = models.TextField(blank=True, null=True)
    code_l2 = models.TextField(blank=True, null=True)
    code_l1 = models.TextField(blank=True, null=True)
    desc_tr_l6 = models.CharField(max_length=255, blank=True, null=True)
    desc_tr_l5 = models.CharField(max_length=255, blank=True, null=True)
    desc_tr_l4 = models.CharField(max_length=255, blank=True, null=True)
    desc_tr_l3 = models.CharField(max_length=255, blank=True, null=True)
    desc_tr_l2 = models.CharField(max_length=255, blank=True, null=True)
    desc_tr_l1 = models.CharField(max_length=255, blank=True, null=True)
    act_inc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    act_exp = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    act_prf = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    pln_inc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    pln_exp = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    pln_prf = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    ttl_inc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    ttl_exp = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    ttl_prf = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sp_bgt_apt'


class SpBgtMon(models.Model):
    rep_month = models.CharField(max_length=255, blank=True, null=True)
    p_code = models.CharField(max_length=255, blank=True, null=True)
    cost_type = models.CharField(max_length=255, blank=True, null=True)
    code_l6 = models.CharField(max_length=255, blank=True, null=True)
    code_l5 = models.TextField(blank=True, null=True)
    code_l4 = models.TextField(blank=True, null=True)
    code_l3 = models.TextField(blank=True, null=True)
    code_l2 = models.TextField(blank=True, null=True)
    code_l1 = models.TextField(blank=True, null=True)
    curr = models.TextField(blank=True, null=True)
    desc_tr_l1 = models.CharField(max_length=255, blank=True, null=True)
    desc_tr_l2 = models.CharField(max_length=255, blank=True, null=True)
    desc_tr_l3 = models.CharField(max_length=255, blank=True, null=True)
    desc_tr_l4 = models.CharField(max_length=255, blank=True, null=True)
    desc_tr_l5 = models.CharField(max_length=255, blank=True, null=True)
    desc_tr_l6 = models.CharField(max_length=255, blank=True, null=True)
    m_21_03 = models.FloatField(blank=True, null=True)
    m_21_04 = models.FloatField(blank=True, null=True)
    m_21_05 = models.FloatField(blank=True, null=True)
    m_21_06 = models.FloatField(blank=True, null=True)
    m_21_07 = models.FloatField(blank=True, null=True)
    m_21_08 = models.FloatField(blank=True, null=True)
    m_21_09 = models.FloatField(blank=True, null=True)
    m_21_10 = models.FloatField(blank=True, null=True)
    m_21_11 = models.FloatField(blank=True, null=True)
    m_21_12 = models.FloatField(blank=True, null=True)
    m_22_01 = models.FloatField(blank=True, null=True)
    m_22_02 = models.FloatField(blank=True, null=True)
    m_22_03 = models.FloatField(blank=True, null=True)
    m_22_04 = models.FloatField(blank=True, null=True)
    m_22_05 = models.FloatField(blank=True, null=True)
    m_22_06 = models.FloatField(blank=True, null=True)
    m_22_07 = models.FloatField(blank=True, null=True)
    m_22_08 = models.FloatField(blank=True, null=True)
    m_22_09 = models.FloatField(blank=True, null=True)
    m_22_10 = models.FloatField(blank=True, null=True)
    m_22_11 = models.FloatField(blank=True, null=True)
    m_22_12 = models.FloatField(blank=True, null=True)
    m_23_01 = models.FloatField(blank=True, null=True)
    m_23_02 = models.FloatField(blank=True, null=True)
    m_23_03 = models.FloatField(blank=True, null=True)
    m_23_04 = models.FloatField(blank=True, null=True)
    m_23_05 = models.FloatField(blank=True, null=True)
    m_23_06 = models.FloatField(blank=True, null=True)
    m_23_07 = models.FloatField(blank=True, null=True)
    m_23_08 = models.FloatField(blank=True, null=True)
    m_23_09 = models.FloatField(blank=True, null=True)
    m_23_10 = models.FloatField(blank=True, null=True)
    m_23_11 = models.FloatField(blank=True, null=True)
    m_23_12 = models.FloatField(blank=True, null=True)
    m_24_01 = models.FloatField(blank=True, null=True)
    m_24_02 = models.FloatField(blank=True, null=True)
    m_24_03 = models.FloatField(blank=True, null=True)
    m_24_04 = models.FloatField(blank=True, null=True)
    m_24_05 = models.FloatField(blank=True, null=True)
    m_24_06 = models.FloatField(blank=True, null=True)
    m_24_07 = models.FloatField(blank=True, null=True)
    m_24_08 = models.FloatField(blank=True, null=True)
    m_24_09 = models.FloatField(blank=True, null=True)
    m_24_10 = models.FloatField(blank=True, null=True)
    m_24_11 = models.FloatField(blank=True, null=True)
    m_24_12 = models.FloatField(blank=True, null=True)
    m_25_01 = models.FloatField(blank=True, null=True)
    m_25_02 = models.FloatField(blank=True, null=True)
    m_25_03 = models.FloatField(blank=True, null=True)
    m_25_04 = models.FloatField(blank=True, null=True)
    m_25_05 = models.FloatField(blank=True, null=True)
    m_25_06 = models.FloatField(blank=True, null=True)
    m_25_07 = models.FloatField(blank=True, null=True)
    m_25_08 = models.FloatField(blank=True, null=True)
    m_25_09 = models.FloatField(blank=True, null=True)
    m_25_10 = models.FloatField(blank=True, null=True)
    m_25_11 = models.FloatField(blank=True, null=True)
    m_25_12 = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sp_bgt_mon'


class SpBgtMon2212(models.Model):
    cost_type = models.CharField(max_length=255, blank=True, null=True)
    p_code = models.CharField(max_length=255, blank=True, null=True)
    code_l6 = models.CharField(max_length=255, blank=True, null=True)
    code_l5 = models.TextField(blank=True, null=True)
    code_l4 = models.TextField(blank=True, null=True)
    code_l3 = models.TextField(blank=True, null=True)
    code_l2 = models.TextField(blank=True, null=True)
    code_l1 = models.TextField(blank=True, null=True)
    curr = models.TextField(blank=True, null=True)
    desc_tr_l1 = models.CharField(max_length=255, blank=True, null=True)
    desc_tr_l2 = models.CharField(max_length=255, blank=True, null=True)
    desc_tr_l3 = models.CharField(max_length=255, blank=True, null=True)
    desc_tr_l4 = models.CharField(max_length=255, blank=True, null=True)
    desc_tr_l5 = models.CharField(max_length=255, blank=True, null=True)
    desc_tr_l6 = models.CharField(max_length=255, blank=True, null=True)
    m_21_03 = models.FloatField(blank=True, null=True)
    m_21_04 = models.FloatField(blank=True, null=True)
    m_21_05 = models.FloatField(blank=True, null=True)
    m_21_06 = models.FloatField(blank=True, null=True)
    m_21_07 = models.FloatField(blank=True, null=True)
    m_21_08 = models.FloatField(blank=True, null=True)
    m_21_09 = models.FloatField(blank=True, null=True)
    m_21_10 = models.FloatField(blank=True, null=True)
    m_21_11 = models.FloatField(blank=True, null=True)
    m_21_12 = models.FloatField(blank=True, null=True)
    m_22_01 = models.FloatField(blank=True, null=True)
    m_22_02 = models.FloatField(blank=True, null=True)
    m_22_03 = models.FloatField(blank=True, null=True)
    m_22_04 = models.FloatField(blank=True, null=True)
    m_22_05 = models.FloatField(blank=True, null=True)
    m_22_06 = models.FloatField(blank=True, null=True)
    m_22_07 = models.FloatField(blank=True, null=True)
    m_22_08 = models.FloatField(blank=True, null=True)
    m_22_09 = models.FloatField(blank=True, null=True)
    m_22_10 = models.FloatField(blank=True, null=True)
    m_22_11 = models.FloatField(blank=True, null=True)
    m_22_12 = models.FloatField(blank=True, null=True)
    m_23_01 = models.FloatField(blank=True, null=True)
    m_23_02 = models.FloatField(blank=True, null=True)
    m_23_03 = models.FloatField(blank=True, null=True)
    m_23_04 = models.FloatField(blank=True, null=True)
    m_23_05 = models.FloatField(blank=True, null=True)
    m_23_06 = models.FloatField(blank=True, null=True)
    m_23_07 = models.FloatField(blank=True, null=True)
    m_23_08 = models.FloatField(blank=True, null=True)
    m_23_09 = models.FloatField(blank=True, null=True)
    m_23_10 = models.FloatField(blank=True, null=True)
    m_23_11 = models.FloatField(blank=True, null=True)
    m_23_12 = models.FloatField(blank=True, null=True)
    m_24_01 = models.FloatField(blank=True, null=True)
    m_24_02 = models.FloatField(blank=True, null=True)
    m_24_03 = models.FloatField(blank=True, null=True)
    m_24_04 = models.FloatField(blank=True, null=True)
    m_24_05 = models.FloatField(blank=True, null=True)
    m_24_06 = models.FloatField(blank=True, null=True)
    m_24_07 = models.FloatField(blank=True, null=True)
    m_24_08 = models.FloatField(blank=True, null=True)
    m_24_09 = models.FloatField(blank=True, null=True)
    m_24_10 = models.FloatField(blank=True, null=True)
    m_24_11 = models.FloatField(blank=True, null=True)
    m_24_12 = models.FloatField(blank=True, null=True)
    m_25_01 = models.FloatField(blank=True, null=True)
    m_25_02 = models.FloatField(blank=True, null=True)
    m_25_03 = models.FloatField(blank=True, null=True)
    m_25_04 = models.FloatField(blank=True, null=True)
    m_25_05 = models.FloatField(blank=True, null=True)
    m_25_06 = models.FloatField(blank=True, null=True)
    m_25_07 = models.FloatField(blank=True, null=True)
    m_25_08 = models.FloatField(blank=True, null=True)
    m_25_09 = models.FloatField(blank=True, null=True)
    m_25_10 = models.FloatField(blank=True, null=True)
    m_25_11 = models.FloatField(blank=True, null=True)
    m_25_12 = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sp_bgt_mon_2212'


class SpBgtMon2212Jsn(models.Model):
    code = models.CharField(max_length=3, blank=True, null=True)
    cost_type = models.CharField(max_length=255, blank=True, null=True)
    curr = models.TextField(blank=True, null=True)
    desc_tr = models.CharField(max_length=100, blank=True, null=True)
    mylink = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'sp_bgt_mon_2212_jsn'


class SpBgtMonJsn(models.Model):
    rep_month = models.CharField(max_length=255, blank=True, null=True)
    code = models.CharField(max_length=3, blank=True, null=True)
    cost_type = models.CharField(max_length=255, blank=True, null=True)
    curr = models.TextField(blank=True, null=True)
    desc_tr = models.CharField(max_length=100, blank=True, null=True)
    mylink = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'sp_bgt_mon_jsn'


class SpBgtPrjJsn(models.Model):
    code = models.CharField(max_length=3, blank=True, null=True)
    curr = models.CharField(blank=True, null=True)
    desc_tr = models.CharField(max_length=100, blank=True, null=True)
    mylink = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'sp_bgt_prj_jsn'


class SpCmpAllJsn(models.Model):
    code = models.TextField(blank=True, null=True)
    desc_tr = models.TextField(blank=True, null=True)
    mylink = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'sp_cmp_all_jsn'


class SpCmpJsn(models.Model):
    code = models.TextField(blank=True, null=True)
    desc_tr = models.TextField(blank=True, null=True)
    mylink = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'sp_cmp_jsn'


class Sup0Projects(models.Model):
    p_code = models.CharField(primary_key=True, max_length=3)
    s_name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'sup_0_projects'


class T001Projects(models.Model):
    r01_p_order = models.SmallIntegerField()
    p_code = models.CharField(primary_key=True, max_length=3)
    r03_s_name = models.CharField(max_length=150)
    r04_l_name = models.CharField(max_length=255, blank=True, null=True)
    r05_employer = models.CharField(max_length=255, blank=True, null=True)
    r06_contractor = models.CharField(max_length=255, blank=True, null=True)
    r07_owners_engineer = models.CharField(max_length=255, blank=True, null=True)
    r08_location = models.CharField(max_length=150, blank=True, null=True)
    r09_cont_date = models.DateTimeField(blank=True, null=True)
    r11_update_date = models.DateTimeField(blank=True, null=True)
    r12_dd_cb = models.DateTimeField(blank=True, null=True)
    r13_dd_ab = models.DateTimeField(blank=True, null=True)
    r14_pm = models.CharField(max_length=30, blank=True, null=True)
    r15_pm_tel = models.CharField(max_length=25, blank=True, null=True)
    r20_cont_type = models.CharField(max_length=50, blank=True, null=True)
    r21_cont_pr_1 = models.FloatField(blank=True, null=True)
    r22_cont_pr_1_cr = models.CharField(max_length=255, blank=True, null=True)
    r23_cont_pr_2 = models.FloatField(blank=True, null=True)
    r24_cont_pr_2_cr = models.CharField(max_length=255, blank=True, null=True)
    r25_cont_pr_3 = models.FloatField(blank=True, null=True)
    r26_cont_pr_3_cr = models.CharField(max_length=255, blank=True, null=True)
    r31_addw_pr_1 = models.FloatField(blank=True, null=True)
    r32_addw_pr_1_cr = models.CharField(max_length=255, blank=True, null=True)
    r33_addw_pr_2 = models.FloatField(blank=True, null=True)
    r34_addw_pr_2_cr = models.CharField(max_length=255, blank=True, null=True)
    r35_addw_pr_3 = models.FloatField(blank=True, null=True)
    r36_addw_pr_3_cr = models.CharField(max_length=255, blank=True, null=True)
    r40_ntp_date = models.DateTimeField(blank=True, null=True)
    r41_dur_project = models.SmallIntegerField(blank=True, null=True)
    r42_dur_project_int = models.CharField(max_length=10, blank=True, null=True)
    r43_dur_te = models.SmallIntegerField(blank=True, null=True)
    r44_dur_te_int = models.CharField(max_length=10, blank=True, null=True)
    r45_dur_oa = models.SmallIntegerField(blank=True, null=True)
    r46_dur_oa_int = models.CharField(max_length=10, blank=True, null=True)
    r47_dur_maintenance = models.SmallIntegerField(blank=True, null=True)
    r48_dur_maint_int = models.CharField(max_length=10, blank=True, null=True)
    r49_date_cur_end = models.DateTimeField(blank=True, null=True)
    r50_date_cur_oa = models.DateTimeField(blank=True, null=True)
    r51_mw_name_1 = models.CharField(max_length=255, blank=True, null=True)
    r52_mw_expln_1 = models.CharField(max_length=255, blank=True, null=True)
    r53_mw_name_2 = models.CharField(max_length=255, blank=True, null=True)
    r54_mw_expln_2 = models.CharField(max_length=255, blank=True, null=True)
    r55_mw_name_3 = models.CharField(max_length=255, blank=True, null=True)
    r56_mw_expln_3 = models.CharField(max_length=255, blank=True, null=True)
    r57_mw_name_4 = models.CharField(max_length=255, blank=True, null=True)
    r58_mw_expln_4 = models.CharField(max_length=255, blank=True, null=True)
    r59_mw_name_5 = models.CharField(max_length=255, blank=True, null=True)
    r60_mw_expln_5 = models.CharField(max_length=255, blank=True, null=True)
    r61_mw_name_6 = models.CharField(max_length=255, blank=True, null=True)
    r62_mw_expln_6 = models.CharField(max_length=255, blank=True, null=True)
    r63_mw_name_7 = models.CharField(max_length=255, blank=True, null=True)
    r64_mw_expln_7 = models.CharField(max_length=255, blank=True, null=True)
    r65_mw_name_8 = models.CharField(max_length=255, blank=True, null=True)
    r66_mw_expln_8 = models.CharField(max_length=255, blank=True, null=True)
    r71_designer_1 = models.CharField(max_length=255, blank=True, null=True)
    r72_designer_2 = models.CharField(max_length=255, blank=True, null=True)
    r73_designer_3 = models.CharField(max_length=255, blank=True, null=True)
    r75_perc_adv = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    r76_perc_cmp = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    r77_perc_opa = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    r81_sec_dep_1 = models.DecimalField(max_digits=18, decimal_places=0, blank=True, null=True)
    r82_sec_dep_1_cr = models.CharField(max_length=5, blank=True, null=True)
    r83_sec_dep_2 = models.DecimalField(max_digits=18, decimal_places=0, blank=True, null=True)
    r84_sec_dep_2_cr = models.CharField(max_length=5, blank=True, null=True)
    r85_sec_dep_3 = models.DecimalField(max_digits=18, decimal_places=0, blank=True, null=True)
    r86_sec_dep_3_cr = models.CharField(max_length=5, blank=True, null=True)
    r91_password = models.CharField(max_length=10, blank=True, null=True)
    r92_g_maps = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_001_projects'


class T101Milestones(models.Model):
    rep_month = models.CharField(db_column='rep_Month', primary_key=True, max_length=4)  # Field name made lowercase. The composite primary key (rep_Month, p_Code, mls_Code) found, that is not supported. The first column is selected.
    p_code = models.CharField(db_column='p_Code', max_length=3)  # Field name made lowercase.
    mls_code = models.CharField(db_column='mls_Code', max_length=50)  # Field name made lowercase.
    mls_desc = models.CharField(db_column='mls_Desc', max_length=255)  # Field name made lowercase.
    mls_date_target = models.DateField(db_column='mls_Date_Target', blank=True, null=True)  # Field name made lowercase.
    mls_date_current = models.DateField(db_column='mls_Date_Current', blank=True, null=True)  # Field name made lowercase.
    mls_progress = models.DecimalField(db_column='mls_Progress', max_digits=8, decimal_places=4)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_101_Milestones'
        unique_together = (('rep_month', 'p_code', 'mls_code'),)


class T102PhysicalPrg(models.Model):
    rep_month = models.CharField(db_column='rep_Month', primary_key=True, max_length=4)  # Field name made lowercase. The composite primary key (rep_Month, p_Code, php_Month) found, that is not supported. The first column is selected.
    p_code = models.CharField(db_column='p_Code', max_length=3)  # Field name made lowercase.
    php_month = models.DateTimeField(db_column='php_Month')  # Field name made lowercase.
    php_pl_progress = models.DecimalField(db_column='php_PL_Progress', max_digits=10, decimal_places=6)  # Field name made lowercase.
    php_ac_progress = models.DecimalField(db_column='php_AC_Progress', max_digits=10, decimal_places=6)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_102_Physical_Prg'
        unique_together = (('rep_month', 'p_code', 'php_month'),)


class T103ImpTopics(models.Model):
    rep_month = models.CharField(db_column='rep_Month', primary_key=True, max_length=4)  # Field name made lowercase. The composite primary key (rep_Month, p_Code, tpc_No) found, that is not supported. The first column is selected.
    p_code = models.CharField(db_column='p_Code', max_length=3)  # Field name made lowercase.
    tpc_no = models.SmallIntegerField(db_column='tpc_No')  # Field name made lowercase.
    tpc_short = models.CharField(db_column='tpc_Short', max_length=255)  # Field name made lowercase.
    tpc_long = models.TextField(db_column='tpc_Long')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_103_Imp_Topics'
        unique_together = (('rep_month', 'p_code', 'tpc_no'),)


class T104ClaimsAndPnts(models.Model):
    rep_month = models.CharField(db_column='rep_Month', primary_key=True, max_length=4)  # Field name made lowercase. The composite primary key (rep_Month, p_Code, cap_Code) found, that is not supported. The first column is selected.
    p_code = models.CharField(db_column='p_Code', max_length=3)  # Field name made lowercase.
    cap_code = models.CharField(db_column='cap_Code', max_length=25)  # Field name made lowercase.
    cap_doc_type = models.CharField(db_column='cap_Doc_Type', max_length=255)  # Field name made lowercase.
    cap_name = models.CharField(db_column='cap_Name', max_length=255)  # Field name made lowercase.
    cap_explaination = models.TextField(db_column='cap_Explaination')  # Field name made lowercase.
    cap_status = models.CharField(db_column='cap_Status', max_length=255)  # Field name made lowercase.
    cap_doc_date = models.DateTimeField(db_column='cap_Doc_Date', blank=True, null=True)  # Field name made lowercase.
    cap_cost = models.IntegerField(db_column='cap_Cost', blank=True, null=True)  # Field name made lowercase.
    cap_curr = models.CharField(db_column='cap_Curr', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_104_Claims_and_Pnts'
        unique_together = (('rep_month', 'p_code', 'cap_code'),)


class T105PersPlan(models.Model):
    rep_month = models.CharField(db_column='rep_Month', primary_key=True, max_length=4)  # Field name made lowercase. The composite primary key (rep_Month, p_Code, ppl_Month) found, that is not supported. The first column is selected.
    p_code = models.CharField(db_column='p_Code', max_length=3)  # Field name made lowercase.
    ppl_month = models.DateTimeField(db_column='ppl_Month')  # Field name made lowercase.
    ppl_cur_dir_ict = models.IntegerField(db_column='ppl_Cur_Dir_Ict', blank=True, null=True)  # Field name made lowercase.
    ppl_cur_dir_sbc = models.IntegerField(db_column='ppl_Cur_Dir_Sbc', blank=True, null=True)  # Field name made lowercase.
    ppl_cur_ind_ict = models.IntegerField(db_column='ppl_Cur_Ind_Ict', blank=True, null=True)  # Field name made lowercase.
    ppl_cur_ind_sbc = models.IntegerField(db_column='ppl_Cur_Ind_Sbc', blank=True, null=True)  # Field name made lowercase.
    ppl_pln_dir_ict = models.IntegerField(db_column='ppl_Pln_Dir_Ict', blank=True, null=True)  # Field name made lowercase.
    ppl_pln_dir_sbc = models.IntegerField(db_column='ppl_Pln_Dir_Sbc', blank=True, null=True)  # Field name made lowercase.
    ppl_pln_ind_ict = models.IntegerField(db_column='ppl_Pln_Ind_Ict', blank=True, null=True)  # Field name made lowercase.
    ppl_pln_ind_sbc = models.IntegerField(db_column='ppl_Pln_Ind_Sbc', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_105_Pers_Plan'
        unique_together = (('rep_month', 'p_code', 'ppl_month'),)


class T106MachPlan(models.Model):
    rep_month = models.CharField(db_column='rep_Month', primary_key=True, max_length=4)  # Field name made lowercase. The composite primary key (rep_Month, p_Code, mpl_M_Owner, mpl_M_Type) found, that is not supported. The first column is selected.
    p_code = models.CharField(db_column='p_Code', max_length=3)  # Field name made lowercase.
    mpl_m_owner = models.CharField(db_column='mpl_M_Owner', max_length=50)  # Field name made lowercase.
    mpl_m_type = models.CharField(db_column='mpl_M_Type', max_length=100)  # Field name made lowercase.
    mpl_m_count = models.IntegerField(db_column='mpl_M_Count', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_106_Mach_Plan'
        unique_together = (('rep_month', 'p_code', 'mpl_m_owner', 'mpl_m_type'),)


class T121TaskDesc(models.Model):
    project = models.CharField(db_column='Project', max_length=3, blank=True, null=True)  # Field name made lowercase.
    task_1 = models.CharField(db_column='Task_1', max_length=61, blank=True, null=True)  # Field name made lowercase.
    task_2 = models.CharField(db_column='Task_2', max_length=61, blank=True, null=True)  # Field name made lowercase.
    task_3 = models.CharField(db_column='Task_3', max_length=61, blank=True, null=True)  # Field name made lowercase.
    task_4 = models.CharField(db_column='Task_4', max_length=61, blank=True, null=True)  # Field name made lowercase.
    task_5 = models.CharField(db_column='Task_5', max_length=61, blank=True, null=True)  # Field name made lowercase.
    task_9 = models.CharField(db_column='Task_9', max_length=61, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_121_Task_Desc'


class TAcModExp(models.Model):
    rep_month = models.CharField(primary_key=True, max_length=4)  # The composite primary key (rep_month, user_id, session_id, pc, l_1, l_2, l_3, l_4, l_5, l_6, exp_ac_mon, exp_ac_exp, curr, ccode) found, that is not supported. The first column is selected.
    user_id = models.CharField(max_length=6)
    session_id = models.CharField(max_length=20)
    pc = models.CharField(max_length=3)
    l_1 = models.CharField(max_length=1)
    l_2 = models.CharField(max_length=2)
    l_3 = models.CharField(max_length=2)
    l_4 = models.CharField(max_length=2)
    l_5 = models.CharField(max_length=2)
    l_6 = models.CharField(max_length=3)
    exp_ac_mon = models.DateField()
    exp_ac_exp = models.DecimalField(max_digits=25, decimal_places=15)
    curr = models.CharField(max_length=3)
    key_r_pc_l6 = models.CharField(max_length=50, blank=True, null=True)
    ccode = models.CharField(max_length=18)
    pkey = models.CharField(max_length=60, blank=True, null=True)
    jkey = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_ac_mod_exp'
        unique_together = (('rep_month', 'user_id', 'session_id', 'pc', 'l_1', 'l_2', 'l_3', 'l_4', 'l_5', 'l_6', 'exp_ac_mon', 'exp_ac_exp', 'curr', 'ccode'),)


class TActionBookmarks(models.Model):
    username = models.CharField(max_length=255)
    action_date = models.DateTimeField()
    action_min = models.IntegerField()
    action_form = models.CharField(max_length=255, blank=True, null=True)
    action_sform_01 = models.CharField(max_length=255, blank=True, null=True)
    action_sform_01_param_01 = models.CharField(max_length=255, blank=True, null=True)
    action_sform_01_param_01_value = models.CharField(max_length=255, blank=True, null=True)
    action_sform_01_param_02 = models.CharField(max_length=255, blank=True, null=True)
    action_sform_01_param_02_value = models.CharField(max_length=255, blank=True, null=True)
    action_sform_01_param_03 = models.CharField(max_length=255, blank=True, null=True)
    action_sform_01_param_03_value = models.CharField(max_length=255, blank=True, null=True)
    action_sform_01_param_04 = models.CharField(max_length=255, blank=True, null=True)
    action_sform_01_param_04_value = models.CharField(max_length=255, blank=True, null=True)
    action_sform_01_param_05 = models.CharField(max_length=255, blank=True, null=True)
    action_sform_01_param_05_value = models.CharField(max_length=255, blank=True, null=True)
    form_level = models.IntegerField(blank=True, null=True)
    action_sform_01_param_06 = models.CharField(max_length=255, blank=True, null=True)
    action_sform_01_param_06_value = models.CharField(max_length=255, blank=True, null=True)
    action_sform_01_param_07 = models.CharField(max_length=255, blank=True, null=True)
    action_sform_01_param_07_value = models.CharField(max_length=255, blank=True, null=True)
    action_sform_01_param_08 = models.CharField(max_length=255, blank=True, null=True)
    action_sform_01_param_08_value = models.CharField(max_length=255, blank=True, null=True)
    action_sform_01_param_09 = models.CharField(max_length=255, blank=True, null=True)
    action_sform_01_param_09_value = models.CharField(max_length=255, blank=True, null=True)
    action_sform_01_param_10 = models.CharField(max_length=255, blank=True, null=True)
    action_sform_01_param_10_value = models.CharField(max_length=255, blank=True, null=True)
    action_sform_01_param_11 = models.CharField(max_length=255, blank=True, null=True)
    action_sform_01_param_11_value = models.CharField(max_length=255, blank=True, null=True)
    action_sform_01_param_12 = models.CharField(max_length=255, blank=True, null=True)
    action_sform_01_param_12_value = models.CharField(max_length=255, blank=True, null=True)
    action_sform_01_param_13 = models.CharField(max_length=255, blank=True, null=True)
    action_sform_01_param_13_value = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_action_bookmarks'


class TActionLog(models.Model):
    username = models.CharField(max_length=255, blank=True, null=True)
    action = models.CharField(max_length=255, blank=True, null=True)
    action_document = models.CharField(max_length=255, blank=True, null=True)
    action_date = models.DateField(blank=True, null=True)
    action_time = models.TimeField(blank=True, null=True)
    action_type = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_action_log'


class TActionMostUsedTime(models.Model):
    username = models.CharField(max_length=255)
    action_date = models.DateField()
    action_min = models.IntegerField()
    action_form = models.CharField(max_length=255, blank=True, null=True)
    action_sform_01 = models.CharField(max_length=255, blank=True, null=True)
    action_sform_01_param_01 = models.CharField(max_length=255, blank=True, null=True)
    action_sform_01_param_01_value = models.CharField(max_length=255, blank=True, null=True)
    action_sform_01_param_02 = models.CharField(max_length=255, blank=True, null=True)
    action_sform_01_param_02_value = models.CharField(max_length=255, blank=True, null=True)
    action_sform_01_param_03 = models.CharField(max_length=255, blank=True, null=True)
    action_sform_01_param_03_value = models.CharField(max_length=255, blank=True, null=True)
    action_sform_01_param_04 = models.CharField(max_length=255, blank=True, null=True)
    action_sform_01_param_04_value = models.CharField(max_length=255, blank=True, null=True)
    action_sform_01_param_05 = models.CharField(max_length=255, blank=True, null=True)
    action_sform_01_param_05_value = models.CharField(max_length=255, blank=True, null=True)
    form_level = models.IntegerField(blank=True, null=True)
    action_sform_01_param_06 = models.CharField(max_length=255, blank=True, null=True)
    action_sform_01_param_06_value = models.CharField(max_length=255, blank=True, null=True)
    action_sform_01_param_07 = models.CharField(max_length=255, blank=True, null=True)
    action_sform_01_param_07_value = models.CharField(max_length=255, blank=True, null=True)
    action_sform_01_param_08 = models.CharField(max_length=255, blank=True, null=True)
    action_sform_01_param_08_value = models.CharField(max_length=255, blank=True, null=True)
    action_sform_01_param_09 = models.CharField(max_length=255, blank=True, null=True)
    action_sform_01_param_09_value = models.CharField(max_length=255, blank=True, null=True)
    action_sform_01_param_10 = models.CharField(max_length=255, blank=True, null=True)
    action_sform_01_param_10_value = models.CharField(max_length=255, blank=True, null=True)
    action_sform_01_param_11 = models.CharField(max_length=255, blank=True, null=True)
    action_sform_01_param_11_value = models.CharField(max_length=255, blank=True, null=True)
    action_sform_01_param_12 = models.CharField(max_length=255, blank=True, null=True)
    action_sform_01_param_12_value = models.CharField(max_length=255, blank=True, null=True)
    action_sform_01_param_13 = models.CharField(max_length=255, blank=True, null=True)
    action_sform_01_param_13_value = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_action_most_used_time'


class TActionTime(models.Model):
    username = models.CharField(max_length=255)
    action_date = models.DateField()
    action_min = models.IntegerField()

    class Meta:
        managed = False
        db_table = 't_action_time'


class TBbAnalysis(models.Model):
    pc = models.CharField(primary_key=True, max_length=3)  # The composite primary key (pc, l_1, l_2, l_3, l_4, l_5, l_6, rs_l1, rs_l2, rs_l3, rs_l4, rep_month) found, that is not supported. The first column is selected.
    l_1 = models.CharField(max_length=1)
    l_2 = models.CharField(max_length=2)
    l_3 = models.CharField(max_length=2)
    l_4 = models.CharField(max_length=2)
    l_5 = models.CharField(max_length=2)
    l_6 = models.CharField(max_length=3)
    rs_l1 = models.CharField(max_length=2)
    rs_l2 = models.CharField(max_length=2)
    rs_l3 = models.CharField(max_length=2)
    rs_l4 = models.CharField(max_length=3)
    an_rs_quantity = models.DecimalField(max_digits=18, decimal_places=9, blank=True, null=True)
    rep_month = models.CharField(max_length=4)
    r_loss = models.DecimalField(max_digits=7, decimal_places=5, blank=True, null=True)
    key_r_pc_l6 = models.CharField(max_length=50, blank=True, null=True)
    key_r4_simple = models.CharField(max_length=15, blank=True, null=True)
    key_r4 = models.CharField(max_length=25, blank=True, null=True)
    key_full = models.CharField(max_length=50, blank=True, null=True)
    l_comb = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_bb_analysis'
        unique_together = (('pc', 'l_1', 'l_2', 'l_3', 'l_4', 'l_5', 'l_6', 'rs_l1', 'rs_l2', 'rs_l3', 'rs_l4', 'rep_month'),)


class TBbExp(models.Model):
    rep_month = models.CharField(primary_key=True, max_length=4)  # The composite primary key (rep_month, pc, l_1, l_2, l_3, l_4, l_5, l_6, curr, exp_ac_mon) found, that is not supported. The first column is selected.
    pc = models.CharField(max_length=3)
    l_1 = models.CharField(max_length=1)
    l_2 = models.CharField(max_length=2)
    l_3 = models.CharField(max_length=2)
    l_4 = models.CharField(max_length=2)
    l_5 = models.CharField(max_length=2)
    l_6 = models.CharField(max_length=3)
    exp_ac_mon = models.DateField()
    exp_ac_exp = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    curr = models.CharField(max_length=3)
    key_r_pc_l6 = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_bb_exp'
        unique_together = (('rep_month', 'pc', 'l_1', 'l_2', 'l_3', 'l_4', 'l_5', 'l_6', 'curr', 'exp_ac_mon'),)


class TBbExpEscRatesL6(models.Model):
    rep_month = models.CharField(primary_key=True, max_length=4)  # The composite primary key (rep_month, pc, l_1, l_2, l_3, l_4, l_5, l_6, month) found, that is not supported. The first column is selected.
    pc = models.CharField(max_length=3)
    l_1 = models.CharField(max_length=1)
    l_2 = models.CharField(max_length=2)
    l_3 = models.CharField(max_length=2)
    l_4 = models.CharField(max_length=2)
    l_5 = models.CharField(max_length=2)
    l_6 = models.CharField(max_length=3)
    month = models.DateField()
    exp_rate = models.DecimalField(max_digits=18, decimal_places=9, blank=True, null=True)
    key_r_pc_l6 = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_bb_exp_esc_rates_l6'
        unique_together = (('rep_month', 'pc', 'l_1', 'l_2', 'l_3', 'l_4', 'l_5', 'l_6', 'month'),)


class TBbExpEurSt(models.Model):
    rep_month = models.CharField(max_length=4, blank=True, null=True)
    pc = models.CharField(max_length=3, blank=True, null=True)
    j_code = models.CharField(max_length=50, blank=True, null=True)
    desc_tr_l2 = models.CharField(max_length=255, blank=True, null=True)
    desc_tr_l3 = models.CharField(max_length=255, blank=True, null=True)
    month = models.DateField(blank=True, null=True)
    eur_expense = models.FloatField(blank=True, null=True)
    up_curr_conv = models.CharField(max_length=3, blank=True, null=True)
    l_1 = models.CharField(max_length=1, blank=True, null=True)
    l_2 = models.CharField(max_length=2, blank=True, null=True)
    l_3 = models.CharField(max_length=2, blank=True, null=True)
    l_4 = models.CharField(max_length=2, blank=True, null=True)
    l_5 = models.CharField(max_length=2, blank=True, null=True)
    l_6 = models.CharField(max_length=3, blank=True, null=True)
    key_r_pc_l6 = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_bb_exp_eur_st'


class TBbExpSt(models.Model):
    rep_month = models.CharField(max_length=4, blank=True, null=True)
    pc = models.CharField(max_length=3, blank=True, null=True)
    j_code = models.CharField(max_length=50, blank=True, null=True)
    desc_tr_l2 = models.CharField(max_length=255, blank=True, null=True)
    desc_tr_l3 = models.CharField(max_length=255, blank=True, null=True)
    month = models.DateField(blank=True, null=True)
    total_expense = models.FloatField(blank=True, null=True)
    curr = models.CharField(max_length=3, blank=True, null=True)
    l_1 = models.CharField(max_length=1, blank=True, null=True)
    l_2 = models.CharField(max_length=2, blank=True, null=True)
    l_3 = models.CharField(max_length=2, blank=True, null=True)
    l_4 = models.CharField(max_length=2, blank=True, null=True)
    l_5 = models.CharField(max_length=2, blank=True, null=True)
    l_6 = models.CharField(max_length=3, blank=True, null=True)
    key_r_pc_l6 = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_bb_exp_st'


class TBbExpTrySt(models.Model):
    rep_month = models.CharField(max_length=4, blank=True, null=True)
    pc = models.CharField(max_length=3, blank=True, null=True)
    j_code = models.CharField(max_length=50, blank=True, null=True)
    desc_tr_l2 = models.CharField(max_length=255, blank=True, null=True)
    desc_tr_l3 = models.CharField(max_length=255, blank=True, null=True)
    month = models.DateField(blank=True, null=True)
    try_expense = models.FloatField(blank=True, null=True)
    up_curr_conv = models.CharField(max_length=3, blank=True, null=True)
    l_1 = models.CharField(max_length=1, blank=True, null=True)
    l_2 = models.CharField(max_length=2, blank=True, null=True)
    l_3 = models.CharField(max_length=2, blank=True, null=True)
    l_4 = models.CharField(max_length=2, blank=True, null=True)
    l_5 = models.CharField(max_length=2, blank=True, null=True)
    l_6 = models.CharField(max_length=3, blank=True, null=True)
    key_r_pc_l6 = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_bb_exp_try_st'


class TBbExpUsdSt(models.Model):
    rep_month = models.CharField(max_length=4, blank=True, null=True)
    pc = models.CharField(max_length=3, blank=True, null=True)
    j_code = models.CharField(max_length=50, blank=True, null=True)
    desc_tr_l2 = models.CharField(max_length=255, blank=True, null=True)
    desc_tr_l3 = models.CharField(max_length=255, blank=True, null=True)
    month = models.DateField(blank=True, null=True)
    usd_expense = models.FloatField(blank=True, null=True)
    up_curr_conv = models.CharField(max_length=3, blank=True, null=True)
    l_1 = models.CharField(max_length=1, blank=True, null=True)
    l_2 = models.CharField(max_length=2, blank=True, null=True)
    l_3 = models.CharField(max_length=2, blank=True, null=True)
    l_4 = models.CharField(max_length=2, blank=True, null=True)
    l_5 = models.CharField(max_length=2, blank=True, null=True)
    l_6 = models.CharField(max_length=3, blank=True, null=True)
    key_r_pc_l6 = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_bb_exp_usd_st'


class TBbIncEscRatesL6(models.Model):
    rep_month = models.CharField(primary_key=True, max_length=4)  # The composite primary key (rep_month, pc, l_1, l_2, l_3, l_4, l_5, l_6, month) found, that is not supported. The first column is selected.
    pc = models.CharField(max_length=3)
    l_1 = models.CharField(max_length=1)
    l_2 = models.CharField(max_length=2)
    l_3 = models.CharField(max_length=2)
    l_4 = models.CharField(max_length=2)
    l_5 = models.CharField(max_length=2)
    l_6 = models.CharField(max_length=3)
    month = models.DateField()
    inc_rate = models.DecimalField(max_digits=18, decimal_places=9, blank=True, null=True)
    key_r_pc_l6 = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_bb_inc_esc_rates_l6'
        unique_together = (('rep_month', 'pc', 'l_1', 'l_2', 'l_3', 'l_4', 'l_5', 'l_6', 'month'),)


class TBbIncEscRatesPcode(models.Model):
    rep_month = models.CharField(primary_key=True, max_length=4)  # The composite primary key (rep_month, pc, month) found, that is not supported. The first column is selected.
    pc = models.CharField(max_length=3)
    month = models.DateField()
    inc_rate_pcode = models.DecimalField(max_digits=18, decimal_places=9, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_bb_inc_esc_rates_pcode'
        unique_together = (('rep_month', 'pc', 'month'),)


class TBbIncEurSt(models.Model):
    rep_month = models.CharField(max_length=4, blank=True, null=True)
    pc = models.CharField(max_length=3, blank=True, null=True)
    j_code = models.CharField(max_length=255, blank=True, null=True)
    desc_tr_l2 = models.CharField(max_length=255, blank=True, null=True)
    desc_tr_l3 = models.CharField(max_length=255, blank=True, null=True)
    month = models.DateField(blank=True, null=True)
    eur_income = models.FloatField(blank=True, null=True)
    up_curr_conv = models.CharField(max_length=255, blank=True, null=True)
    l_1 = models.CharField(max_length=1, blank=True, null=True)
    l_2 = models.CharField(max_length=2, blank=True, null=True)
    l_3 = models.CharField(max_length=2, blank=True, null=True)
    l_4 = models.CharField(max_length=2, blank=True, null=True)
    l_5 = models.CharField(max_length=2, blank=True, null=True)
    l_6 = models.CharField(max_length=3, blank=True, null=True)
    desc_tr_l6 = models.CharField(max_length=150, blank=True, null=True)
    key_r_pc_l6 = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_bb_inc_eur_st'


class TBbIncQty(models.Model):
    rep_month = models.CharField(primary_key=True, max_length=4)  # The composite primary key (rep_month, pc, l_1, l_2, l_3, l_4, l_5, l_6, inc_base_mon) found, that is not supported. The first column is selected.
    pc = models.CharField(max_length=3)
    l_1 = models.CharField(max_length=1)
    l_2 = models.CharField(max_length=2)
    l_3 = models.CharField(max_length=2)
    l_4 = models.CharField(max_length=2)
    l_5 = models.CharField(max_length=2)
    l_6 = models.CharField(max_length=3)
    inc_base_mon = models.DateField()
    inc_base_qty = models.DecimalField(max_digits=18, decimal_places=9, blank=True, null=True)
    key_r_pc_l6 = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_bb_inc_qty'
        unique_together = (('rep_month', 'pc', 'l_1', 'l_2', 'l_3', 'l_4', 'l_5', 'l_6', 'inc_base_mon'),)


class TBbIncSt(models.Model):
    rep_month = models.CharField(max_length=4, blank=True, null=True)
    pc = models.CharField(max_length=3, blank=True, null=True)
    j_code = models.CharField(max_length=255, blank=True, null=True)
    desc_tr_l2 = models.CharField(max_length=255, blank=True, null=True)
    desc_tr_l3 = models.CharField(max_length=255, blank=True, null=True)
    inc_base_mon = models.DateField(blank=True, null=True)
    inc_total = models.FloatField(blank=True, null=True)
    curr = models.CharField(max_length=3, blank=True, null=True)
    l_1 = models.CharField(max_length=1, blank=True, null=True)
    l_2 = models.CharField(max_length=2, blank=True, null=True)
    l_3 = models.CharField(max_length=2, blank=True, null=True)
    l_4 = models.CharField(max_length=2, blank=True, null=True)
    l_5 = models.CharField(max_length=2, blank=True, null=True)
    l_6 = models.CharField(max_length=3, blank=True, null=True)
    desc_tr_l6 = models.CharField(max_length=150, blank=True, null=True)
    key_r_pc_l6 = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_bb_inc_st'


class TBbIncTrySt(models.Model):
    rep_month = models.CharField(max_length=4, blank=True, null=True)
    pc = models.CharField(max_length=3, blank=True, null=True)
    j_code = models.CharField(max_length=255, blank=True, null=True)
    desc_tr_l2 = models.CharField(max_length=255, blank=True, null=True)
    desc_tr_l3 = models.CharField(max_length=255, blank=True, null=True)
    month = models.DateField(blank=True, null=True)
    try_income = models.FloatField(blank=True, null=True)
    up_curr_conv = models.CharField(max_length=255, blank=True, null=True)
    l_1 = models.CharField(max_length=1, blank=True, null=True)
    l_2 = models.CharField(max_length=2, blank=True, null=True)
    l_3 = models.CharField(max_length=2, blank=True, null=True)
    l_4 = models.CharField(max_length=2, blank=True, null=True)
    l_5 = models.CharField(max_length=2, blank=True, null=True)
    l_6 = models.CharField(max_length=3, blank=True, null=True)
    desc_tr_l6 = models.CharField(max_length=150, blank=True, null=True)
    key_r_pc_l6 = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_bb_inc_try_st'


class TBbIncUsdSt(models.Model):
    rep_month = models.CharField(max_length=4, blank=True, null=True)
    pc = models.CharField(max_length=3, blank=True, null=True)
    j_code = models.CharField(max_length=255, blank=True, null=True)
    desc_tr_l2 = models.CharField(max_length=255, blank=True, null=True)
    desc_tr_l3 = models.CharField(max_length=255, blank=True, null=True)
    month = models.DateField(blank=True, null=True)
    usd_income = models.FloatField(blank=True, null=True)
    up_curr_conv = models.CharField(max_length=255, blank=True, null=True)
    l_1 = models.CharField(max_length=1, blank=True, null=True)
    l_2 = models.CharField(max_length=2, blank=True, null=True)
    l_3 = models.CharField(max_length=2, blank=True, null=True)
    l_4 = models.CharField(max_length=2, blank=True, null=True)
    l_5 = models.CharField(max_length=2, blank=True, null=True)
    l_6 = models.CharField(max_length=3, blank=True, null=True)
    desc_tr_l6 = models.CharField(max_length=150, blank=True, null=True)
    key_r_pc_l6 = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_bb_inc_usd_st'


class TBbIncWbs(models.Model):
    rep_month = models.CharField(primary_key=True, max_length=4)  # The composite primary key (rep_month, pc, l_1, l_2, l_3, l_4, l_5, l_6, curr) found, that is not supported. The first column is selected.
    pc = models.CharField(max_length=3)
    l_1 = models.CharField(max_length=1)
    l_2 = models.CharField(max_length=2)
    l_3 = models.CharField(max_length=2)
    l_4 = models.CharField(max_length=2)
    l_5 = models.CharField(max_length=2)
    l_6 = models.CharField(max_length=3)
    curr = models.CharField(max_length=3)
    up = models.DecimalField(max_digits=18, decimal_places=9, blank=True, null=True)
    key_r_pc_l6 = models.CharField(max_length=50, blank=True, null=True)
    unit = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_bb_inc_wbs'
        unique_together = (('rep_month', 'pc', 'l_1', 'l_2', 'l_3', 'l_4', 'l_5', 'l_6', 'curr'),)


class TBbIndexes(models.Model):
    month = models.DateField(primary_key=True)  # The composite primary key (month, pc, rep_month) found, that is not supported. The first column is selected.
    r_ufe = models.DecimalField(max_digits=18, decimal_places=10, blank=True, null=True)
    r_tufe = models.DecimalField(max_digits=18, decimal_places=10, blank=True, null=True)
    r_inf_usd = models.DecimalField(max_digits=18, decimal_places=10, blank=True, null=True)
    r_inf_eur = models.DecimalField(max_digits=18, decimal_places=10, blank=True, null=True)
    r_metal = models.DecimalField(max_digits=18, decimal_places=10, blank=True, null=True)
    r_petrol = models.DecimalField(max_digits=18, decimal_places=10, blank=True, null=True)
    r_cement = models.DecimalField(max_digits=18, decimal_places=10, blank=True, null=True)
    r_electricity = models.DecimalField(max_digits=18, decimal_places=10, blank=True, null=True)
    pc = models.CharField(max_length=3)
    rep_month = models.CharField(max_length=4)

    class Meta:
        managed = False
        db_table = 't_bb_indexes'
        unique_together = (('month', 'pc', 'rep_month'),)


class TBbIndexesImported(models.Model):
    rep_month = models.TextField(primary_key=True)  # The composite primary key (rep_month, bb_month) found, that is not supported. The first column is selected.
    bb_month = models.DateField()
    bb_pc = models.TextField()
    bb_ufe = models.DecimalField(max_digits=18, decimal_places=10, blank=True, null=True)
    bb_tufe = models.DecimalField(max_digits=18, decimal_places=10, blank=True, null=True)
    bb_inf_usd = models.DecimalField(max_digits=18, decimal_places=10, blank=True, null=True)
    bb_inf_eur = models.DecimalField(max_digits=18, decimal_places=10, blank=True, null=True)
    bb_metal = models.DecimalField(max_digits=18, decimal_places=10, blank=True, null=True)
    bb_electricity = models.DecimalField(max_digits=18, decimal_places=10, blank=True, null=True)
    bb_cement = models.DecimalField(max_digits=18, decimal_places=10, blank=True, null=True)
    bb_petrol = models.DecimalField(max_digits=18, decimal_places=10, blank=True, null=True)
    bb_usdtry = models.DecimalField(max_digits=18, decimal_places=10, blank=True, null=True)
    bb_eurtry = models.DecimalField(max_digits=18, decimal_places=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_bb_indexes_imported'
        unique_together = (('rep_month', 'bb_month'),)


class TBbIndexesInput(models.Model):
    bb_year = models.CharField(primary_key=True, max_length=4)
    bb_pc = models.CharField(max_length=3)
    bb_ufe = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    bb_tufe = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    bb_inf_usd = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    bb_inf_eur = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    bb_metal = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    bb_electricity = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    bb_cement = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    bb_petrol = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    bb_usdtry = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    bb_eurtry = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_bb_indexes_input'


class TBbIndexesMonthlyInput(models.Model):
    bb_month = models.DateField(primary_key=True)
    bb_pc = models.CharField(max_length=3)
    bb_ufe = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    bb_tufe = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    bb_inf_usd = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    bb_inf_eur = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    bb_metal = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    bb_electricity = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    bb_cement = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    bb_petrol = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    bb_usdtry = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    bb_eurtry = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_bb_indexes_monthly_input'


class TBbMonCurrRates(models.Model):
    rep_month = models.CharField(primary_key=True, max_length=4)  # The composite primary key (rep_month, pc, month) found, that is not supported. The first column is selected.
    pc = models.CharField(max_length=3)
    month = models.DateField()
    r_eur_try = models.DecimalField(max_digits=12, decimal_places=6, blank=True, null=True)
    r_usd_try = models.DecimalField(max_digits=12, decimal_places=6, blank=True, null=True)
    r_eur_eur = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)
    r_try_eur = models.DecimalField(max_digits=12, decimal_places=6, blank=True, null=True)
    r_try_try = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)
    r_usd_usd = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)
    r_try_usd = models.DecimalField(max_digits=12, decimal_places=6, blank=True, null=True)
    r_eur_usd = models.DecimalField(max_digits=12, decimal_places=6, blank=True, null=True)
    r_usd_eur = models.DecimalField(max_digits=12, decimal_places=6, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_bb_mon_curr_rates'
        unique_together = (('rep_month', 'pc', 'month'),)


class TBbProfitEurSt(models.Model):
    rep_month = models.CharField(max_length=4, blank=True, null=True)
    pc = models.CharField(max_length=3, blank=True, null=True)
    j_code = models.CharField(max_length=50, blank=True, null=True)
    desc_tr_l2 = models.CharField(max_length=255, blank=True, null=True)
    desc_tr_l3 = models.CharField(max_length=255, blank=True, null=True)
    expense = models.FloatField(blank=True, null=True)
    income = models.FloatField(blank=True, null=True)
    month = models.DateField(blank=True, null=True)
    curr = models.CharField(max_length=3, blank=True, null=True)
    l_1 = models.CharField(max_length=1, blank=True, null=True)
    l_2 = models.CharField(max_length=2, blank=True, null=True)
    l_3 = models.CharField(max_length=2, blank=True, null=True)
    l_4 = models.CharField(max_length=2, blank=True, null=True)
    l_5 = models.CharField(max_length=2, blank=True, null=True)
    l_6 = models.CharField(max_length=3, blank=True, null=True)
    profit = models.FloatField(blank=True, null=True)
    desc_tr_l6 = models.CharField(max_length=255, blank=True, null=True)
    key_r_pc_l6 = models.CharField(max_length=50, blank=True, null=True)
    unit = models.CharField(max_length=50, blank=True, null=True)
    desc_tr_l4 = models.CharField(max_length=255, blank=True, null=True)
    desc_tr_l5 = models.CharField(max_length=255, blank=True, null=True)
    desc_tr_l1 = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_bb_profit_eur_st'


class TBbProfitSt(models.Model):
    rep_month = models.CharField(max_length=4, blank=True, null=True)
    pc = models.CharField(max_length=3, blank=True, null=True)
    j_code = models.CharField(max_length=50, blank=True, null=True)
    desc_tr_l2 = models.CharField(max_length=255, blank=True, null=True)
    desc_tr_l3 = models.CharField(max_length=255, blank=True, null=True)
    month = models.DateField(blank=True, null=True)
    expense = models.FloatField(blank=True, null=True)
    income = models.FloatField(blank=True, null=True)
    curr = models.CharField(max_length=3, blank=True, null=True)
    l_1 = models.CharField(max_length=1, blank=True, null=True)
    l_2 = models.CharField(max_length=2, blank=True, null=True)
    l_3 = models.CharField(max_length=2, blank=True, null=True)
    l_4 = models.CharField(max_length=2, blank=True, null=True)
    l_5 = models.CharField(max_length=2, blank=True, null=True)
    l_6 = models.CharField(max_length=3, blank=True, null=True)
    profit = models.FloatField(blank=True, null=True)
    desc_tr_l6 = models.CharField(max_length=255, blank=True, null=True)
    key_r_pc_l6 = models.CharField(max_length=50, blank=True, null=True)
    unit = models.CharField(max_length=50, blank=True, null=True)
    desc_tr_l4 = models.CharField(max_length=255, blank=True, null=True)
    desc_tr_l5 = models.CharField(max_length=255, blank=True, null=True)
    desc_tr_l1 = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_bb_profit_st'


class TBbProfitTrySt(models.Model):
    rep_month = models.CharField(max_length=4, blank=True, null=True)
    pc = models.CharField(max_length=3, blank=True, null=True)
    j_code = models.CharField(max_length=50, blank=True, null=True)
    desc_tr_l2 = models.CharField(max_length=255, blank=True, null=True)
    desc_tr_l3 = models.CharField(max_length=255, blank=True, null=True)
    expense = models.FloatField(blank=True, null=True)
    income = models.FloatField(blank=True, null=True)
    month = models.DateField(blank=True, null=True)
    curr = models.CharField(max_length=3, blank=True, null=True)
    l_1 = models.CharField(max_length=1, blank=True, null=True)
    l_2 = models.CharField(max_length=2, blank=True, null=True)
    l_3 = models.CharField(max_length=2, blank=True, null=True)
    l_4 = models.CharField(max_length=2, blank=True, null=True)
    l_5 = models.CharField(max_length=2, blank=True, null=True)
    l_6 = models.CharField(max_length=3, blank=True, null=True)
    profit = models.FloatField(blank=True, null=True)
    desc_tr_l6 = models.CharField(max_length=255, blank=True, null=True)
    key_r_pc_l6 = models.CharField(max_length=50, blank=True, null=True)
    unit = models.CharField(max_length=50, blank=True, null=True)
    desc_tr_l4 = models.CharField(max_length=255, blank=True, null=True)
    desc_tr_l5 = models.CharField(max_length=255, blank=True, null=True)
    desc_tr_l1 = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_bb_profit_try_st'


class TBbProfitUsdSt(models.Model):
    rep_month = models.CharField(max_length=4, blank=True, null=True)
    pc = models.CharField(max_length=3, blank=True, null=True)
    j_code = models.CharField(max_length=50, blank=True, null=True)
    desc_tr_l2 = models.CharField(max_length=255, blank=True, null=True)
    desc_tr_l3 = models.CharField(max_length=255, blank=True, null=True)
    expense = models.FloatField(blank=True, null=True)
    income = models.FloatField(blank=True, null=True)
    month = models.DateField(blank=True, null=True)
    curr = models.CharField(max_length=3, blank=True, null=True)
    l_1 = models.CharField(max_length=1, blank=True, null=True)
    l_2 = models.CharField(max_length=2, blank=True, null=True)
    l_3 = models.CharField(max_length=2, blank=True, null=True)
    l_4 = models.CharField(max_length=2, blank=True, null=True)
    l_5 = models.CharField(max_length=2, blank=True, null=True)
    l_6 = models.CharField(max_length=3, blank=True, null=True)
    profit = models.FloatField(blank=True, null=True)
    desc_tr_l6 = models.CharField(max_length=255, blank=True, null=True)
    key_r_pc_l6 = models.CharField(max_length=50, blank=True, null=True)
    unit = models.CharField(max_length=50, blank=True, null=True)
    desc_tr_l4 = models.CharField(max_length=255, blank=True, null=True)
    desc_tr_l5 = models.CharField(max_length=255, blank=True, null=True)
    desc_tr_l1 = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_bb_profit_usd_st'


class TBbQty(models.Model):
    rep_month = models.CharField(primary_key=True, max_length=4)  # The composite primary key (rep_month, pc, l_1, l_2, l_3, l_4, l_5, l_6, exp_base_mon) found, that is not supported. The first column is selected.
    pc = models.CharField(max_length=3)
    l_1 = models.CharField(max_length=1)
    l_2 = models.CharField(max_length=2)
    l_3 = models.CharField(max_length=2)
    l_4 = models.CharField(max_length=2)
    l_5 = models.CharField(max_length=2)
    l_6 = models.CharField(max_length=3)
    exp_base_mon = models.DateField()
    exp_base_qty = models.DecimalField(max_digits=15, decimal_places=9, blank=True, null=True)
    key_r_pc_l6 = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_bb_qty'
        unique_together = (('rep_month', 'pc', 'l_1', 'l_2', 'l_3', 'l_4', 'l_5', 'l_6', 'exp_base_mon'),)


class TBbResUp(models.Model):
    pc = models.CharField(primary_key=True, max_length=3)  # The composite primary key (pc, rs_l1, rs_l2, rs_l3, rs_l4, rep_month) found, that is not supported. The first column is selected.
    rs_l1 = models.CharField(max_length=2)
    rs_l2 = models.CharField(max_length=2)
    rs_l3 = models.CharField(max_length=2)
    rs_l4 = models.CharField(max_length=3)
    up_cost = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    rep_month = models.CharField(max_length=4)
    key_r4_simple = models.CharField(max_length=15, blank=True, null=True)
    key_r4 = models.CharField(max_length=25, blank=True, null=True)
    price_month = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_bb_res_up'
        unique_together = (('pc', 'rs_l1', 'rs_l2', 'rs_l3', 'rs_l4', 'rep_month'),)


class TCbAnalysis(models.Model):
    pc = models.CharField(primary_key=True, max_length=3)  # The composite primary key (pc, rs_l1, rs_l2, rs_l3, rs_l4, l_1, l_2, l_3, l_4, l_5, l_6, rep_month) found, that is not supported. The first column is selected.
    rs_l1 = models.CharField(max_length=2)
    rs_l2 = models.CharField(max_length=2)
    rs_l3 = models.CharField(max_length=2)
    rs_l4 = models.CharField(max_length=3)
    an_rs_quantity = models.DecimalField(max_digits=18, decimal_places=9, blank=True, null=True)
    l_1 = models.CharField(max_length=1)
    l_2 = models.CharField(max_length=2)
    l_3 = models.CharField(max_length=2)
    l_4 = models.CharField(max_length=2)
    l_5 = models.CharField(max_length=2)
    l_6 = models.CharField(max_length=3)
    rep_month = models.CharField(max_length=4)
    r_loss = models.DecimalField(max_digits=7, decimal_places=5, blank=True, null=True)
    key_r_pc_l6 = models.CharField(max_length=50, blank=True, null=True)
    key_r4_simple = models.CharField(max_length=15, blank=True, null=True)
    key_r4 = models.CharField(max_length=25, blank=True, null=True)
    key_full = models.CharField(max_length=50, blank=True, null=True)
    l_comb = models.CharField(max_length=50, blank=True, null=True)
    ccode = models.CharField(max_length=18, blank=True, null=True)
    rcode = models.CharField(max_length=12, blank=True, null=True)
    pkey = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_cb_analysis'
        unique_together = (('pc', 'rs_l1', 'rs_l2', 'rs_l3', 'rs_l4', 'l_1', 'l_2', 'l_3', 'l_4', 'l_5', 'l_6', 'rep_month'),)


class TCbExp(models.Model):
    rep_month = models.CharField(primary_key=True, max_length=4)  # The composite primary key (rep_month, pc, l_1, l_2, l_3, l_4, l_5, l_6, exp_ac_mon, curr) found, that is not supported. The first column is selected.
    pc = models.CharField(max_length=3)
    l_1 = models.CharField(max_length=1)
    l_2 = models.CharField(max_length=2)
    l_3 = models.CharField(max_length=2)
    l_4 = models.CharField(max_length=2)
    l_5 = models.CharField(max_length=2)
    l_6 = models.CharField(max_length=3)
    exp_ac_mon = models.DateField()
    exp_ac_exp = models.DecimalField(max_digits=25, decimal_places=15, blank=True, null=True)
    curr = models.CharField(max_length=3)
    key_r_pc_l6 = models.CharField(max_length=50, blank=True, null=True)
    ccode = models.CharField(max_length=18, blank=True, null=True)
    pkey = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_cb_exp'
        unique_together = (('rep_month', 'pc', 'l_1', 'l_2', 'l_3', 'l_4', 'l_5', 'l_6', 'exp_ac_mon', 'curr'),)


class TCbExpEscRatesL6(models.Model):
    rep_month = models.CharField(primary_key=True, max_length=4)  # The composite primary key (rep_month, pc, l_1, l_2, l_3, l_4, l_5, l_6, month) found, that is not supported. The first column is selected.
    pc = models.CharField(max_length=3)
    l_1 = models.CharField(max_length=1)
    l_2 = models.CharField(max_length=2)
    l_3 = models.CharField(max_length=2)
    l_4 = models.CharField(max_length=2)
    l_5 = models.CharField(max_length=2)
    l_6 = models.CharField(max_length=3)
    month = models.DateField()
    exp_rate = models.DecimalField(max_digits=25, decimal_places=15, blank=True, null=True)
    key_r_pc_l6 = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_cb_exp_esc_rates_l6'
        unique_together = (('rep_month', 'pc', 'l_1', 'l_2', 'l_3', 'l_4', 'l_5', 'l_6', 'month'),)


class TCbExpEurSt(models.Model):
    rep_month = models.CharField(max_length=4, blank=True, null=True)
    pc = models.CharField(max_length=3, blank=True, null=True)
    j_code = models.CharField(max_length=50, blank=True, null=True)
    desc_tr_l2 = models.CharField(max_length=255, blank=True, null=True)
    desc_tr_l3 = models.CharField(max_length=255, blank=True, null=True)
    month = models.DateField(blank=True, null=True)
    eur_expense = models.FloatField(blank=True, null=True)
    up_curr_conv = models.CharField(max_length=3, blank=True, null=True)
    l_1 = models.CharField(max_length=1, blank=True, null=True)
    l_2 = models.CharField(max_length=2, blank=True, null=True)
    l_3 = models.CharField(max_length=2, blank=True, null=True)
    l_4 = models.CharField(max_length=2, blank=True, null=True)
    l_5 = models.CharField(max_length=2, blank=True, null=True)
    l_6 = models.CharField(max_length=3, blank=True, null=True)
    key_r_pc_l6 = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_cb_exp_eur_st'


class TCbExpMod(models.Model):
    rep_month = models.CharField(primary_key=True, max_length=4)  # The composite primary key (rep_month, user_id, session_id, pc, l_1, l_2, l_3, l_4, l_5, l_6, exp_ac_mon, exp_ac_exp, curr, ccode) found, that is not supported. The first column is selected.
    user_id = models.CharField(max_length=6)
    session_id = models.CharField(max_length=20)
    pc = models.CharField(max_length=3)
    l_1 = models.CharField(max_length=1)
    l_2 = models.CharField(max_length=2)
    l_3 = models.CharField(max_length=2)
    l_4 = models.CharField(max_length=2)
    l_5 = models.CharField(max_length=2)
    l_6 = models.CharField(max_length=3)
    exp_ac_mon = models.DateField()
    exp_ac_exp = models.DecimalField(max_digits=25, decimal_places=15)
    curr = models.CharField(max_length=3)
    key_r_pc_l6 = models.CharField(max_length=50, blank=True, null=True)
    ccode = models.CharField(max_length=18)
    pkey = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_cb_exp_mod'
        unique_together = (('rep_month', 'user_id', 'session_id', 'pc', 'l_1', 'l_2', 'l_3', 'l_4', 'l_5', 'l_6', 'exp_ac_mon', 'exp_ac_exp', 'curr', 'ccode'),)


class TCbExpSt(models.Model):
    rep_month = models.CharField(max_length=4, blank=True, null=True)
    pc = models.CharField(max_length=3, blank=True, null=True)
    j_code = models.CharField(max_length=50, blank=True, null=True)
    desc_tr_l2 = models.CharField(max_length=255, blank=True, null=True)
    desc_tr_l3 = models.CharField(max_length=255, blank=True, null=True)
    month = models.DateField(blank=True, null=True)
    total_expense = models.FloatField(blank=True, null=True)
    curr = models.CharField(max_length=3, blank=True, null=True)
    l_1 = models.CharField(max_length=1, blank=True, null=True)
    l_2 = models.CharField(max_length=2, blank=True, null=True)
    l_3 = models.CharField(max_length=2, blank=True, null=True)
    l_4 = models.CharField(max_length=2, blank=True, null=True)
    l_5 = models.CharField(max_length=2, blank=True, null=True)
    l_6 = models.CharField(max_length=3, blank=True, null=True)
    key_r_pc_l6 = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_cb_exp_st'


class TCbExpTrySt(models.Model):
    rep_month = models.CharField(max_length=4, blank=True, null=True)
    pc = models.CharField(max_length=3, blank=True, null=True)
    j_code = models.CharField(max_length=50, blank=True, null=True)
    desc_tr_l2 = models.CharField(max_length=255, blank=True, null=True)
    desc_tr_l3 = models.CharField(max_length=255, blank=True, null=True)
    month = models.DateTimeField(blank=True, null=True)
    try_expense = models.FloatField(blank=True, null=True)
    up_curr_conv = models.CharField(max_length=3, blank=True, null=True)
    l_1 = models.CharField(max_length=1, blank=True, null=True)
    l_2 = models.CharField(max_length=2, blank=True, null=True)
    l_3 = models.CharField(max_length=2, blank=True, null=True)
    l_4 = models.CharField(max_length=2, blank=True, null=True)
    l_5 = models.CharField(max_length=2, blank=True, null=True)
    l_6 = models.CharField(max_length=3, blank=True, null=True)
    key_r_pc_l6 = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_cb_exp_try_st'


class TCbExpUsdSt(models.Model):
    rep_month = models.CharField(max_length=4, blank=True, null=True)
    pc = models.CharField(max_length=3, blank=True, null=True)
    j_code = models.CharField(max_length=50, blank=True, null=True)
    desc_tr_l2 = models.CharField(max_length=255, blank=True, null=True)
    desc_tr_l3 = models.CharField(max_length=255, blank=True, null=True)
    month = models.DateField(blank=True, null=True)
    usd_expense = models.FloatField(blank=True, null=True)
    up_curr_conv = models.CharField(max_length=3, blank=True, null=True)
    l_1 = models.CharField(max_length=1, blank=True, null=True)
    l_2 = models.CharField(max_length=2, blank=True, null=True)
    l_3 = models.CharField(max_length=2, blank=True, null=True)
    l_4 = models.CharField(max_length=2, blank=True, null=True)
    l_5 = models.CharField(max_length=2, blank=True, null=True)
    l_6 = models.CharField(max_length=3, blank=True, null=True)
    key_r_pc_l6 = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_cb_exp_usd_st'


class TCbIncEscRatesL6(models.Model):
    rep_month = models.CharField(primary_key=True, max_length=4)  # The composite primary key (rep_month, pc, l_1, l_2, l_3, l_4, l_5, l_6, month) found, that is not supported. The first column is selected.
    pc = models.CharField(max_length=3)
    l_1 = models.CharField(max_length=1)
    l_2 = models.CharField(max_length=2)
    l_3 = models.CharField(max_length=2)
    l_4 = models.CharField(max_length=2)
    l_5 = models.CharField(max_length=2)
    l_6 = models.CharField(max_length=3)
    month = models.DateField()
    inc_rate = models.DecimalField(max_digits=25, decimal_places=15, blank=True, null=True)
    key_r_pc_l6 = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_cb_inc_esc_rates_l6'
        unique_together = (('rep_month', 'pc', 'l_1', 'l_2', 'l_3', 'l_4', 'l_5', 'l_6', 'month'),)


class TCbIncEscRatesPcode(models.Model):
    rep_month = models.CharField(primary_key=True, max_length=4)  # The composite primary key (rep_month, pc, month) found, that is not supported. The first column is selected.
    pc = models.CharField(max_length=3)
    month = models.DateField()
    inc_rate_pcode = models.DecimalField(max_digits=25, decimal_places=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_cb_inc_esc_rates_pcode'
        unique_together = (('rep_month', 'pc', 'month'),)


class TCbIncEurSt(models.Model):
    rep_month = models.CharField(max_length=4, blank=True, null=True)
    pc = models.CharField(max_length=3, blank=True, null=True)
    j_code = models.CharField(max_length=255, blank=True, null=True)
    desc_tr_l2 = models.CharField(max_length=255, blank=True, null=True)
    desc_tr_l3 = models.CharField(max_length=255, blank=True, null=True)
    month = models.DateField(blank=True, null=True)
    eur_income = models.FloatField(blank=True, null=True)
    up_curr_conv = models.CharField(max_length=255, blank=True, null=True)
    l_1 = models.CharField(max_length=1, blank=True, null=True)
    l_2 = models.CharField(max_length=2, blank=True, null=True)
    l_3 = models.CharField(max_length=2, blank=True, null=True)
    l_4 = models.CharField(max_length=2, blank=True, null=True)
    l_5 = models.CharField(max_length=2, blank=True, null=True)
    l_6 = models.CharField(max_length=3, blank=True, null=True)
    desc_tr_l6 = models.CharField(max_length=150, blank=True, null=True)
    key_r_pc_l6 = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_cb_inc_eur_st'


class TCbIncQty(models.Model):
    rep_month = models.CharField(primary_key=True, max_length=4)  # The composite primary key (rep_month, pc, l_1, l_2, l_3, l_4, l_5, l_6, inc_base_mon) found, that is not supported. The first column is selected.
    pc = models.CharField(max_length=3)
    l_1 = models.CharField(max_length=1)
    l_2 = models.CharField(max_length=2)
    l_3 = models.CharField(max_length=2)
    l_4 = models.CharField(max_length=2)
    l_5 = models.CharField(max_length=2)
    l_6 = models.CharField(max_length=3)
    inc_base_mon = models.DateField()
    inc_base_qty = models.DecimalField(max_digits=25, decimal_places=15, blank=True, null=True)
    key_r_pc_l6 = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_cb_inc_qty'
        unique_together = (('rep_month', 'pc', 'l_1', 'l_2', 'l_3', 'l_4', 'l_5', 'l_6', 'inc_base_mon'),)


class TCbIncSt(models.Model):
    rep_month = models.CharField(primary_key=True, max_length=4)  # The composite primary key (rep_month, pc, key_r_pc_l6, inc_base_mon) found, that is not supported. The first column is selected.
    pc = models.CharField(max_length=3)
    j_code = models.CharField(max_length=255, blank=True, null=True)
    desc_tr_l2 = models.CharField(max_length=255, blank=True, null=True)
    desc_tr_l3 = models.CharField(max_length=255, blank=True, null=True)
    inc_base_mon = models.DateField()
    inc_total = models.FloatField(blank=True, null=True)
    curr = models.CharField(max_length=3, blank=True, null=True)
    l_1 = models.CharField(max_length=1, blank=True, null=True)
    l_2 = models.CharField(max_length=2, blank=True, null=True)
    l_3 = models.CharField(max_length=2, blank=True, null=True)
    l_4 = models.CharField(max_length=2, blank=True, null=True)
    l_5 = models.CharField(max_length=2, blank=True, null=True)
    l_6 = models.CharField(max_length=3, blank=True, null=True)
    desc_tr_l6 = models.CharField(max_length=150, blank=True, null=True)
    key_r_pc_l6 = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 't_cb_inc_st'
        unique_together = (('rep_month', 'pc', 'key_r_pc_l6', 'inc_base_mon'),)


class TCbIncTrySt(models.Model):
    rep_month = models.CharField(max_length=4, blank=True, null=True)
    pc = models.CharField(max_length=3, blank=True, null=True)
    j_code = models.CharField(max_length=255, blank=True, null=True)
    desc_tr_l2 = models.CharField(max_length=255, blank=True, null=True)
    desc_tr_l3 = models.CharField(max_length=255, blank=True, null=True)
    month = models.DateField(blank=True, null=True)
    try_income = models.FloatField(blank=True, null=True)
    up_curr_conv = models.CharField(max_length=255, blank=True, null=True)
    l_1 = models.CharField(max_length=1, blank=True, null=True)
    l_2 = models.CharField(max_length=2, blank=True, null=True)
    l_3 = models.CharField(max_length=2, blank=True, null=True)
    l_4 = models.CharField(max_length=2, blank=True, null=True)
    l_5 = models.CharField(max_length=2, blank=True, null=True)
    l_6 = models.CharField(max_length=3, blank=True, null=True)
    desc_tr_l6 = models.CharField(max_length=150, blank=True, null=True)
    key_r_pc_l6 = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_cb_inc_try_st'


class TCbIncUsdSt(models.Model):
    rep_month = models.CharField(max_length=4, blank=True, null=True)
    pc = models.CharField(max_length=3, blank=True, null=True)
    j_code = models.CharField(max_length=255, blank=True, null=True)
    desc_tr_l2 = models.CharField(max_length=255, blank=True, null=True)
    desc_tr_l3 = models.CharField(max_length=255, blank=True, null=True)
    month = models.DateField(blank=True, null=True)
    usd_income = models.FloatField(blank=True, null=True)
    up_curr_conv = models.CharField(max_length=255, blank=True, null=True)
    l_1 = models.CharField(max_length=1, blank=True, null=True)
    l_2 = models.CharField(max_length=2, blank=True, null=True)
    l_3 = models.CharField(max_length=2, blank=True, null=True)
    l_4 = models.CharField(max_length=2, blank=True, null=True)
    l_5 = models.CharField(max_length=2, blank=True, null=True)
    l_6 = models.CharField(max_length=3, blank=True, null=True)
    desc_tr_l6 = models.CharField(max_length=150, blank=True, null=True)
    key_r_pc_l6 = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_cb_inc_usd_st'


class TCbIncWbs(models.Model):
    rep_month = models.CharField(primary_key=True, max_length=4)  # The composite primary key (rep_month, pc, l_1, l_2, l_4, l_3, l_5, curr, l_6) found, that is not supported. The first column is selected.
    pc = models.CharField(max_length=3)
    l_1 = models.CharField(max_length=1)
    l_2 = models.CharField(max_length=2)
    l_3 = models.CharField(max_length=2)
    l_4 = models.CharField(max_length=2)
    l_5 = models.CharField(max_length=2)
    l_6 = models.CharField(max_length=3)
    curr = models.CharField(max_length=3)
    up = models.DecimalField(max_digits=18, decimal_places=9, blank=True, null=True)
    key_r_pc_l6 = models.CharField(max_length=50, blank=True, null=True)
    unit = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_cb_inc_wbs'
        unique_together = (('rep_month', 'pc', 'l_1', 'l_2', 'l_4', 'l_3', 'l_5', 'curr', 'l_6'),)


class TCbIndexes(models.Model):
    rep_month = models.CharField(primary_key=True, max_length=4)  # The composite primary key (rep_month, month) found, that is not supported. The first column is selected.
    month = models.DateField()
    bb_metal = models.DecimalField(max_digits=18, decimal_places=10, blank=True, null=True)
    bb_electricity = models.DecimalField(max_digits=18, decimal_places=10, blank=True, null=True)
    bb_cement = models.DecimalField(max_digits=18, decimal_places=10, blank=True, null=True)
    bb_petrol = models.DecimalField(max_digits=18, decimal_places=10, blank=True, null=True)
    bb_inf_usd = models.DecimalField(max_digits=18, decimal_places=10, blank=True, null=True)
    bb_inf_eur = models.DecimalField(max_digits=18, decimal_places=10, blank=True, null=True)
    bb_ufe = models.DecimalField(max_digits=18, decimal_places=10, blank=True, null=True)
    bb_tufe = models.DecimalField(max_digits=18, decimal_places=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_cb_indexes'
        unique_together = (('rep_month', 'month'),)


class TCbIndexesBudget(models.Model):
    rep_month = models.CharField(primary_key=True, max_length=4)  # The composite primary key (rep_month, cb_month) found, that is not supported. The first column is selected.
    cb_month = models.DateField()
    cb_ufe = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    cb_tufe = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    cb_inf_usd = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    cb_inf_eur = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    cb_metal = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    cb_electricity = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    cb_cement = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    cb_petrol = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    cb_usdtry = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    cb_eurtry = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_cb_indexes_budget'
        unique_together = (('rep_month', 'cb_month'),)


class TCbIndexesImported(models.Model):
    rep_month = models.CharField(primary_key=True, max_length=4)  # The composite primary key (rep_month, cb_month) found, that is not supported. The first column is selected.
    cb_month = models.DateTimeField()
    cb_ufe = models.DecimalField(max_digits=18, decimal_places=10, blank=True, null=True)
    cb_tufe = models.DecimalField(max_digits=18, decimal_places=10, blank=True, null=True)
    cb_inf_usd = models.DecimalField(max_digits=18, decimal_places=10, blank=True, null=True)
    cb_inf_eur = models.DecimalField(max_digits=18, decimal_places=10, blank=True, null=True)
    cb_metal = models.DecimalField(max_digits=18, decimal_places=10, blank=True, null=True)
    cb_electricity = models.DecimalField(max_digits=18, decimal_places=10, blank=True, null=True)
    cb_cement = models.DecimalField(max_digits=18, decimal_places=10, blank=True, null=True)
    cb_petrol = models.DecimalField(max_digits=18, decimal_places=10, blank=True, null=True)
    cb_usdtry = models.DecimalField(max_digits=18, decimal_places=10, blank=True, null=True)
    cb_eurtry = models.DecimalField(max_digits=18, decimal_places=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_cb_indexes_imported'
        unique_together = (('rep_month', 'cb_month'),)


class TCbIndexesInput(models.Model):
    cb_year = models.CharField(primary_key=True, max_length=4)
    cb_ufe = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    cb_tufe = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    cb_inf_usd = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    cb_inf_eur = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    cb_metal = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    cb_electricity = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    cb_cement = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    cb_petrol = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    cb_usdtry = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    cb_eurtry = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_cb_indexes_input'


class TCbIndexesMonthlyInput(models.Model):
    cb_month = models.DateField(primary_key=True)
    cb_ufe = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    cb_tufe = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    cb_inf_usd = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    cb_inf_eur = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    cb_metal = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    cb_electricity = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    cb_cement = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    cb_petrol = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    cb_usdtry = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    cb_eurtry = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_cb_indexes_monthly_input'


class TCbModExpEurSt(models.Model):
    user_id = models.TextField()
    session_id = models.TextField()
    rep_month = models.CharField(max_length=4, blank=True, null=True)
    pc = models.CharField(max_length=3, blank=True, null=True)
    j_code = models.CharField(max_length=50, blank=True, null=True)
    desc_tr_l2 = models.CharField(max_length=255, blank=True, null=True)
    desc_tr_l3 = models.CharField(max_length=255, blank=True, null=True)
    month = models.DateField(blank=True, null=True)
    eur_expense = models.FloatField(blank=True, null=True)
    up_curr_conv = models.CharField(max_length=3, blank=True, null=True)
    l_1 = models.CharField(max_length=1, blank=True, null=True)
    l_2 = models.CharField(max_length=2, blank=True, null=True)
    l_3 = models.CharField(max_length=2, blank=True, null=True)
    l_4 = models.CharField(max_length=2, blank=True, null=True)
    l_5 = models.CharField(max_length=2, blank=True, null=True)
    l_6 = models.CharField(max_length=3, blank=True, null=True)
    key_r_pc_l6 = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_cb_mod_exp_eur_st'


class TCbModExpSt(models.Model):
    user_id = models.TextField()
    session_id = models.TextField()
    rep_month = models.CharField(max_length=4, blank=True, null=True)
    pc = models.CharField(max_length=3, blank=True, null=True)
    j_code = models.CharField(max_length=50, blank=True, null=True)
    desc_tr_l2 = models.CharField(max_length=255, blank=True, null=True)
    desc_tr_l3 = models.CharField(max_length=255, blank=True, null=True)
    month = models.DateField(blank=True, null=True)
    total_expense = models.FloatField(blank=True, null=True)
    curr = models.CharField(max_length=3, blank=True, null=True)
    l_1 = models.CharField(max_length=1, blank=True, null=True)
    l_2 = models.CharField(max_length=2, blank=True, null=True)
    l_3 = models.CharField(max_length=2, blank=True, null=True)
    l_4 = models.CharField(max_length=2, blank=True, null=True)
    l_5 = models.CharField(max_length=2, blank=True, null=True)
    l_6 = models.CharField(max_length=3, blank=True, null=True)
    key_r_pc_l6 = models.CharField(max_length=50, blank=True, null=True)
    jkey = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_cb_mod_exp_st'


class TCbModExpTrySt(models.Model):
    user_id = models.TextField()
    session_id = models.TextField()
    rep_month = models.CharField(max_length=4, blank=True, null=True)
    pc = models.CharField(max_length=3, blank=True, null=True)
    j_code = models.CharField(max_length=50, blank=True, null=True)
    desc_tr_l2 = models.CharField(max_length=255, blank=True, null=True)
    desc_tr_l3 = models.CharField(max_length=255, blank=True, null=True)
    month = models.DateField(blank=True, null=True)
    try_expense = models.FloatField(blank=True, null=True)
    up_curr_conv = models.CharField(max_length=3, blank=True, null=True)
    l_1 = models.CharField(max_length=1, blank=True, null=True)
    l_2 = models.CharField(max_length=2, blank=True, null=True)
    l_3 = models.CharField(max_length=2, blank=True, null=True)
    l_4 = models.CharField(max_length=2, blank=True, null=True)
    l_5 = models.CharField(max_length=2, blank=True, null=True)
    l_6 = models.CharField(max_length=3, blank=True, null=True)
    key_r_pc_l6 = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_cb_mod_exp_try_st'


class TCbModExpUsdSt(models.Model):
    user_id = models.TextField()
    session_id = models.TextField()
    rep_month = models.CharField(max_length=4, blank=True, null=True)
    pc = models.CharField(max_length=3, blank=True, null=True)
    j_code = models.CharField(max_length=50, blank=True, null=True)
    desc_tr_l2 = models.CharField(max_length=255, blank=True, null=True)
    desc_tr_l3 = models.CharField(max_length=255, blank=True, null=True)
    month = models.DateField(blank=True, null=True)
    usd_expense = models.FloatField(blank=True, null=True)
    up_curr_conv = models.CharField(max_length=3, blank=True, null=True)
    l_1 = models.CharField(max_length=1, blank=True, null=True)
    l_2 = models.CharField(max_length=2, blank=True, null=True)
    l_3 = models.CharField(max_length=2, blank=True, null=True)
    l_4 = models.CharField(max_length=2, blank=True, null=True)
    l_5 = models.CharField(max_length=2, blank=True, null=True)
    l_6 = models.CharField(max_length=3, blank=True, null=True)
    key_r_pc_l6 = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_cb_mod_exp_usd_st'


class TCbModIncEurSt(models.Model):
    user_id = models.TextField()
    session_id = models.TextField()
    rep_month = models.CharField(max_length=4, blank=True, null=True)
    pc = models.CharField(max_length=3, blank=True, null=True)
    j_code = models.CharField(max_length=255, blank=True, null=True)
    desc_tr_l2 = models.CharField(max_length=255, blank=True, null=True)
    desc_tr_l3 = models.CharField(max_length=255, blank=True, null=True)
    month = models.DateField(blank=True, null=True)
    eur_income = models.FloatField(blank=True, null=True)
    up_curr_conv = models.CharField(max_length=255, blank=True, null=True)
    l_1 = models.CharField(max_length=1, blank=True, null=True)
    l_2 = models.CharField(max_length=2, blank=True, null=True)
    l_3 = models.CharField(max_length=2, blank=True, null=True)
    l_4 = models.CharField(max_length=2, blank=True, null=True)
    l_5 = models.CharField(max_length=2, blank=True, null=True)
    l_6 = models.CharField(max_length=3, blank=True, null=True)
    desc_tr_l6 = models.CharField(max_length=150, blank=True, null=True)
    key_r_pc_l6 = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_cb_mod_inc_eur_st'


class TCbModIncSt(models.Model):
    user_id = models.TextField()
    session_id = models.TextField()
    rep_month = models.CharField(max_length=4, blank=True, null=True)
    pc = models.CharField(max_length=3, blank=True, null=True)
    j_code = models.CharField(max_length=50, blank=True, null=True)
    desc_tr_l2 = models.CharField(max_length=255, blank=True, null=True)
    desc_tr_l3 = models.CharField(max_length=255, blank=True, null=True)
    inc_base_mon = models.DateField(blank=True, null=True)
    inc_total = models.FloatField(blank=True, null=True)
    curr = models.CharField(max_length=3, blank=True, null=True)
    l_1 = models.CharField(max_length=1, blank=True, null=True)
    l_2 = models.CharField(max_length=2, blank=True, null=True)
    l_3 = models.CharField(max_length=2, blank=True, null=True)
    l_4 = models.CharField(max_length=2, blank=True, null=True)
    l_5 = models.CharField(max_length=2, blank=True, null=True)
    l_6 = models.CharField(max_length=3, blank=True, null=True)
    desc_tr_l6 = models.CharField(max_length=150, blank=True, null=True)
    key_r_pc_l6 = models.CharField(max_length=50, blank=True, null=True)
    jkey = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_cb_mod_inc_st'


class TCbModIncTrySt(models.Model):
    user_id = models.TextField()
    session_id = models.TextField()
    rep_month = models.CharField(max_length=4, blank=True, null=True)
    pc = models.CharField(max_length=3, blank=True, null=True)
    j_code = models.CharField(max_length=255, blank=True, null=True)
    desc_tr_l2 = models.CharField(max_length=255, blank=True, null=True)
    desc_tr_l3 = models.CharField(max_length=255, blank=True, null=True)
    month = models.DateField(blank=True, null=True)
    try_income = models.FloatField(blank=True, null=True)
    up_curr_conv = models.CharField(max_length=255, blank=True, null=True)
    l_1 = models.CharField(max_length=1, blank=True, null=True)
    l_2 = models.CharField(max_length=2, blank=True, null=True)
    l_3 = models.CharField(max_length=2, blank=True, null=True)
    l_4 = models.CharField(max_length=2, blank=True, null=True)
    l_5 = models.CharField(max_length=2, blank=True, null=True)
    l_6 = models.CharField(max_length=3, blank=True, null=True)
    desc_tr_l6 = models.CharField(max_length=150, blank=True, null=True)
    key_r_pc_l6 = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_cb_mod_inc_try_st'


class TCbModIncUsdSt(models.Model):
    user_id = models.TextField()
    session_id = models.TextField()
    rep_month = models.CharField(max_length=4, blank=True, null=True)
    pc = models.CharField(max_length=3, blank=True, null=True)
    j_code = models.CharField(max_length=255, blank=True, null=True)
    desc_tr_l2 = models.CharField(max_length=255, blank=True, null=True)
    desc_tr_l3 = models.CharField(max_length=255, blank=True, null=True)
    month = models.DateField(blank=True, null=True)
    usd_income = models.FloatField(blank=True, null=True)
    up_curr_conv = models.CharField(max_length=255, blank=True, null=True)
    l_1 = models.CharField(max_length=1, blank=True, null=True)
    l_2 = models.CharField(max_length=2, blank=True, null=True)
    l_3 = models.CharField(max_length=2, blank=True, null=True)
    l_4 = models.CharField(max_length=2, blank=True, null=True)
    l_5 = models.CharField(max_length=2, blank=True, null=True)
    l_6 = models.CharField(max_length=3, blank=True, null=True)
    desc_tr_l6 = models.CharField(max_length=150, blank=True, null=True)
    key_r_pc_l6 = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_cb_mod_inc_usd_st'


class TCbModIndexes(models.Model):
    user_id = models.CharField(primary_key=True, max_length=6)  # The composite primary key (user_id, session_id, rep_month, month) found, that is not supported. The first column is selected.
    session_id = models.CharField(max_length=20)
    rep_month = models.CharField(max_length=4)
    month = models.DateField()
    bb_ufe = models.DecimalField(max_digits=18, decimal_places=10, blank=True, null=True)
    bb_tufe = models.DecimalField(max_digits=18, decimal_places=10, blank=True, null=True)
    bb_inf_usd = models.DecimalField(max_digits=18, decimal_places=10, blank=True, null=True)
    bb_inf_eur = models.DecimalField(max_digits=18, decimal_places=10, blank=True, null=True)
    bb_metal = models.DecimalField(max_digits=18, decimal_places=10, blank=True, null=True)
    bb_petrol = models.DecimalField(max_digits=18, decimal_places=10, blank=True, null=True)
    bb_cement = models.DecimalField(max_digits=18, decimal_places=10, blank=True, null=True)
    bb_electricity = models.DecimalField(max_digits=18, decimal_places=10, blank=True, null=True)
    rm_month = models.CharField(max_length=150, blank=True, null=True)
    jkey_curr_index = models.CharField(max_length=150, blank=True, null=True)
    rep_month_userid_sessionid = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_cb_mod_indexes'
        unique_together = (('user_id', 'session_id', 'rep_month', 'month'),)


class TCbModMonCurrRates(models.Model):
    user_id = models.CharField(primary_key=True, max_length=6)  # The composite primary key (user_id, session_id, rep_month, month) found, that is not supported. The first column is selected.
    session_id = models.CharField(max_length=20)
    rep_month = models.CharField(max_length=4)
    month = models.DateField()
    r_eur_try = models.DecimalField(max_digits=12, decimal_places=6, blank=True, null=True)
    r_usd_try = models.DecimalField(max_digits=12, decimal_places=6, blank=True, null=True)
    r_try_try = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)
    r_usd_usd = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)
    r_eur_eur = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)
    r_eur_usd = models.DecimalField(max_digits=12, decimal_places=6, blank=True, null=True)
    r_try_eur = models.DecimalField(max_digits=12, decimal_places=6, blank=True, null=True)
    r_usd_eur = models.DecimalField(max_digits=12, decimal_places=6, blank=True, null=True)
    r_try_usd = models.DecimalField(max_digits=12, decimal_places=6, blank=True, null=True)
    rm_month = models.CharField(max_length=150, blank=True, null=True)
    jkey_curr_index = models.CharField(max_length=150, blank=True, null=True)
    rep_month_userid_sessionid = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_cb_mod_mon_curr_rates'
        unique_together = (('user_id', 'session_id', 'rep_month', 'month'),)


class TCbModProfitEurSt(models.Model):
    user_id = models.TextField()
    session_id = models.TextField()
    rep_month = models.CharField(max_length=4, blank=True, null=True)
    pc = models.CharField(max_length=3, blank=True, null=True)
    j_code = models.CharField(max_length=50, blank=True, null=True)
    desc_tr_l2 = models.CharField(max_length=255, blank=True, null=True)
    desc_tr_l3 = models.CharField(max_length=255, blank=True, null=True)
    expense = models.FloatField(blank=True, null=True)
    income = models.FloatField(blank=True, null=True)
    month = models.DateField(blank=True, null=True)
    curr = models.CharField(max_length=3, blank=True, null=True)
    l_1 = models.CharField(max_length=1, blank=True, null=True)
    l_2 = models.CharField(max_length=2, blank=True, null=True)
    l_3 = models.CharField(max_length=2, blank=True, null=True)
    l_4 = models.CharField(max_length=2, blank=True, null=True)
    l_5 = models.CharField(max_length=2, blank=True, null=True)
    l_6 = models.CharField(max_length=3, blank=True, null=True)
    profit = models.FloatField(blank=True, null=True)
    desc_tr_l6 = models.CharField(max_length=255, blank=True, null=True)
    unit = models.CharField(max_length=50, blank=True, null=True)
    desc_tr_l4 = models.CharField(max_length=255, blank=True, null=True)
    desc_tr_l5 = models.CharField(max_length=255, blank=True, null=True)
    desc_tr_l1 = models.CharField(max_length=255, blank=True, null=True)
    key_r_pc_l6 = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_cb_mod_profit_eur_st'


class TCbModProfitSt(models.Model):
    user_id = models.TextField()
    session_id = models.TextField()
    rep_month = models.CharField(max_length=4, blank=True, null=True)
    pc = models.CharField(max_length=3, blank=True, null=True)
    desc_tr_l2 = models.CharField(max_length=255, blank=True, null=True)
    desc_tr_l3 = models.CharField(max_length=255, blank=True, null=True)
    month = models.DateField(blank=True, null=True)
    expense = models.FloatField(blank=True, null=True)
    income = models.FloatField(blank=True, null=True)
    curr = models.CharField(max_length=3, blank=True, null=True)
    l_1 = models.CharField(max_length=1, blank=True, null=True)
    l_2 = models.CharField(max_length=2, blank=True, null=True)
    l_3 = models.CharField(max_length=2, blank=True, null=True)
    l_4 = models.CharField(max_length=2, blank=True, null=True)
    l_5 = models.CharField(max_length=2, blank=True, null=True)
    l_6 = models.CharField(max_length=3, blank=True, null=True)
    profit = models.FloatField(blank=True, null=True)
    desc_tr_l6 = models.CharField(max_length=255, blank=True, null=True)
    unit = models.CharField(max_length=50, blank=True, null=True)
    desc_tr_l4 = models.CharField(max_length=255, blank=True, null=True)
    desc_tr_l5 = models.CharField(max_length=255, blank=True, null=True)
    desc_tr_l1 = models.CharField(max_length=255, blank=True, null=True)
    key_r_pc_l6 = models.CharField(max_length=50, blank=True, null=True)
    j_code = models.CharField(max_length=50, blank=True, null=True)
    jkey = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_cb_mod_profit_st'


class TCbModProfitTrySt(models.Model):
    user_id = models.TextField()
    session_id = models.TextField()
    rep_month = models.CharField(max_length=4, blank=True, null=True)
    pc = models.CharField(max_length=3, blank=True, null=True)
    j_code = models.CharField(max_length=50, blank=True, null=True)
    desc_tr_l2 = models.CharField(max_length=255, blank=True, null=True)
    desc_tr_l3 = models.CharField(max_length=255, blank=True, null=True)
    expense = models.FloatField(blank=True, null=True)
    income = models.FloatField(blank=True, null=True)
    month = models.DateField(blank=True, null=True)
    curr = models.CharField(max_length=3, blank=True, null=True)
    l_1 = models.CharField(max_length=1, blank=True, null=True)
    l_2 = models.CharField(max_length=2, blank=True, null=True)
    l_3 = models.CharField(max_length=2, blank=True, null=True)
    l_4 = models.CharField(max_length=2, blank=True, null=True)
    l_5 = models.CharField(max_length=2, blank=True, null=True)
    l_6 = models.CharField(max_length=3, blank=True, null=True)
    profit = models.FloatField(blank=True, null=True)
    desc_tr_l6 = models.CharField(max_length=255, blank=True, null=True)
    unit = models.CharField(max_length=50, blank=True, null=True)
    desc_tr_l4 = models.CharField(max_length=255, blank=True, null=True)
    desc_tr_l5 = models.CharField(max_length=255, blank=True, null=True)
    desc_tr_l1 = models.CharField(max_length=255, blank=True, null=True)
    key_r_pc_l6 = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_cb_mod_profit_try_st'


class TCbModProfitUsdSt(models.Model):
    user_id = models.TextField()
    session_id = models.TextField()
    rep_month = models.CharField(max_length=4, blank=True, null=True)
    pc = models.CharField(max_length=3, blank=True, null=True)
    j_code = models.CharField(max_length=50, blank=True, null=True)
    desc_tr_l2 = models.CharField(max_length=255, blank=True, null=True)
    desc_tr_l3 = models.CharField(max_length=255, blank=True, null=True)
    expense = models.FloatField(blank=True, null=True)
    income = models.FloatField(blank=True, null=True)
    month = models.DateField(blank=True, null=True)
    curr = models.CharField(max_length=3, blank=True, null=True)
    l_1 = models.CharField(max_length=1, blank=True, null=True)
    l_2 = models.CharField(max_length=2, blank=True, null=True)
    l_3 = models.CharField(max_length=2, blank=True, null=True)
    l_4 = models.CharField(max_length=2, blank=True, null=True)
    l_5 = models.CharField(max_length=2, blank=True, null=True)
    l_6 = models.CharField(max_length=3, blank=True, null=True)
    profit = models.FloatField(blank=True, null=True)
    desc_tr_l6 = models.CharField(max_length=255, blank=True, null=True)
    unit = models.CharField(max_length=50, blank=True, null=True)
    desc_tr_l4 = models.CharField(max_length=255, blank=True, null=True)
    desc_tr_l5 = models.CharField(max_length=255, blank=True, null=True)
    desc_tr_l1 = models.CharField(max_length=255, blank=True, null=True)
    key_r_pc_l6 = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_cb_mod_profit_usd_st'


class TCbProfitCrosstabUnionAll01(models.Model):
    tablo_tipi = models.CharField(max_length=255, blank=True, null=True)
    j_key_comb = models.CharField(max_length=255, blank=True, null=True)
    rep_month = models.CharField(max_length=255, blank=True, null=True)
    pc = models.CharField(max_length=255, blank=True, null=True)
    j_code = models.CharField(max_length=255, blank=True, null=True)
    l_1 = models.CharField(max_length=255, blank=True, null=True)
    l_2 = models.CharField(max_length=255, blank=True, null=True)
    l_3 = models.CharField(max_length=255, blank=True, null=True)
    l_4 = models.CharField(max_length=255, blank=True, null=True)
    l_5 = models.CharField(max_length=255, blank=True, null=True)
    l_6 = models.CharField(max_length=255, blank=True, null=True)
    key_r_pc_l6 = models.CharField(max_length=255, blank=True, null=True)
    unit = models.CharField(max_length=255, blank=True, null=True)
    desc_tr_l1 = models.CharField(max_length=255, blank=True, null=True)
    desc_tr_l2 = models.CharField(max_length=255, blank=True, null=True)
    desc_tr_l3 = models.CharField(max_length=255, blank=True, null=True)
    desc_tr_l4 = models.CharField(max_length=255, blank=True, null=True)
    desc_tr_l5 = models.CharField(max_length=255, blank=True, null=True)
    desc_tr_l6 = models.CharField(max_length=255, blank=True, null=True)
    tutar_tipi = models.CharField(max_length=255, blank=True, null=True)
    number_1_06_2017 = models.FloatField(db_column='1_06_2017', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1_07_2017 = models.FloatField(db_column='1_07_2017', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1_08_2017 = models.FloatField(db_column='1_08_2017', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1_09_2017 = models.FloatField(db_column='1_09_2017', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1_10_2017 = models.FloatField(db_column='1_10_2017', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1_11_2017 = models.FloatField(db_column='1_11_2017', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1_12_2017 = models.FloatField(db_column='1_12_2017', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1_01_2018 = models.FloatField(db_column='1_01_2018', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1_02_2018 = models.FloatField(db_column='1_02_2018', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1_03_2018 = models.FloatField(db_column='1_03_2018', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1_04_2018 = models.FloatField(db_column='1_04_2018', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1_05_2018 = models.FloatField(db_column='1_05_2018', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1_06_2018 = models.FloatField(db_column='1_06_2018', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1_07_2018 = models.FloatField(db_column='1_07_2018', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1_08_2018 = models.FloatField(db_column='1_08_2018', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1_09_2018 = models.FloatField(db_column='1_09_2018', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1_10_2018 = models.FloatField(db_column='1_10_2018', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1_11_2018 = models.FloatField(db_column='1_11_2018', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1_12_2018 = models.FloatField(db_column='1_12_2018', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1_01_2019 = models.FloatField(db_column='1_01_2019', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1_02_2019 = models.FloatField(db_column='1_02_2019', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1_03_2019 = models.FloatField(db_column='1_03_2019', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1_04_2019 = models.FloatField(db_column='1_04_2019', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1_05_2019 = models.FloatField(db_column='1_05_2019', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1_06_2019 = models.FloatField(db_column='1_06_2019', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1_07_2019 = models.FloatField(db_column='1_07_2019', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1_08_2019 = models.FloatField(db_column='1_08_2019', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1_09_2019 = models.FloatField(db_column='1_09_2019', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1_10_2019 = models.FloatField(db_column='1_10_2019', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1_11_2019 = models.FloatField(db_column='1_11_2019', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1_12_2019 = models.FloatField(db_column='1_12_2019', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1_01_2020 = models.FloatField(db_column='1_01_2020', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1_02_2020 = models.FloatField(db_column='1_02_2020', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1_03_2020 = models.FloatField(db_column='1_03_2020', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1_04_2020 = models.FloatField(db_column='1_04_2020', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1_05_2020 = models.FloatField(db_column='1_05_2020', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1_06_2020 = models.FloatField(db_column='1_06_2020', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1_07_2020 = models.FloatField(db_column='1_07_2020', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1_08_2020 = models.FloatField(db_column='1_08_2020', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1_09_2020 = models.FloatField(db_column='1_09_2020', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1_10_2020 = models.FloatField(db_column='1_10_2020', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1_11_2020 = models.FloatField(db_column='1_11_2020', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1_12_2020 = models.FloatField(db_column='1_12_2020', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1_01_2021 = models.FloatField(db_column='1_01_2021', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1_02_2021 = models.FloatField(db_column='1_02_2021', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1_03_2021 = models.FloatField(db_column='1_03_2021', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1_04_2021 = models.FloatField(db_column='1_04_2021', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1_05_2021 = models.FloatField(db_column='1_05_2021', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1_06_2021 = models.FloatField(db_column='1_06_2021', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1_07_2021 = models.FloatField(db_column='1_07_2021', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1_08_2021 = models.FloatField(db_column='1_08_2021', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1_09_2021 = models.FloatField(db_column='1_09_2021', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1_10_2021 = models.FloatField(db_column='1_10_2021', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1_11_2021 = models.FloatField(db_column='1_11_2021', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1_12_2021 = models.FloatField(db_column='1_12_2021', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1_01_2022 = models.FloatField(db_column='1_01_2022', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1_02_2022 = models.FloatField(db_column='1_02_2022', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1_03_2022 = models.FloatField(db_column='1_03_2022', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1_04_2022 = models.FloatField(db_column='1_04_2022', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1_05_2022 = models.FloatField(db_column='1_05_2022', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1_06_2022 = models.FloatField(db_column='1_06_2022', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.

    class Meta:
        managed = False
        db_table = 't_cb_profit_crosstab_union_all_01'


class TCbProfitCrosstabUnionAll02(models.Model):
    tablo_tipi = models.CharField(max_length=255, blank=True, null=True)
    j_key_comb = models.CharField(max_length=255, blank=True, null=True)
    rep_month = models.CharField(max_length=255, blank=True, null=True)
    pc = models.CharField(max_length=255, blank=True, null=True)
    j_code = models.CharField(max_length=255, blank=True, null=True)
    l_1 = models.CharField(max_length=255, blank=True, null=True)
    l_2 = models.CharField(max_length=255, blank=True, null=True)
    l_3 = models.CharField(max_length=255, blank=True, null=True)
    l_4 = models.CharField(max_length=255, blank=True, null=True)
    l_5 = models.CharField(max_length=255, blank=True, null=True)
    l_6 = models.CharField(max_length=255, blank=True, null=True)
    key_r_pc_l6 = models.CharField(max_length=255, blank=True, null=True)
    unit = models.CharField(max_length=255, blank=True, null=True)
    desc_tr_l1 = models.CharField(max_length=255, blank=True, null=True)
    desc_tr_l2 = models.CharField(max_length=255, blank=True, null=True)
    desc_tr_l3 = models.CharField(max_length=255, blank=True, null=True)
    desc_tr_l4 = models.CharField(max_length=255, blank=True, null=True)
    desc_tr_l5 = models.CharField(max_length=255, blank=True, null=True)
    desc_tr_l6 = models.CharField(max_length=255, blank=True, null=True)
    tutar_tipi = models.CharField(max_length=255, blank=True, null=True)
    number_1_07_2022 = models.FloatField(db_column='1_07_2022', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1_08_2022 = models.FloatField(db_column='1_08_2022', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1_09_2022 = models.FloatField(db_column='1_09_2022', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1_10_2022 = models.FloatField(db_column='1_10_2022', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1_11_2022 = models.FloatField(db_column='1_11_2022', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1_12_2022 = models.FloatField(db_column='1_12_2022', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1_01_2023 = models.FloatField(db_column='1_01_2023', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1_02_2023 = models.FloatField(db_column='1_02_2023', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1_03_2023 = models.FloatField(db_column='1_03_2023', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1_04_2023 = models.FloatField(db_column='1_04_2023', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1_05_2023 = models.FloatField(db_column='1_05_2023', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1_06_2023 = models.FloatField(db_column='1_06_2023', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1_07_2023 = models.FloatField(db_column='1_07_2023', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1_08_2023 = models.FloatField(db_column='1_08_2023', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1_09_2023 = models.FloatField(db_column='1_09_2023', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1_10_2023 = models.FloatField(db_column='1_10_2023', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1_11_2023 = models.FloatField(db_column='1_11_2023', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1_12_2023 = models.FloatField(db_column='1_12_2023', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1_01_2024 = models.FloatField(db_column='1_01_2024', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1_02_2024 = models.FloatField(db_column='1_02_2024', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1_03_2024 = models.FloatField(db_column='1_03_2024', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1_04_2024 = models.FloatField(db_column='1_04_2024', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1_05_2024 = models.FloatField(db_column='1_05_2024', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1_06_2024 = models.FloatField(db_column='1_06_2024', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1_07_2024 = models.FloatField(db_column='1_07_2024', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1_08_2024 = models.FloatField(db_column='1_08_2024', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1_09_2024 = models.FloatField(db_column='1_09_2024', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1_10_2024 = models.FloatField(db_column='1_10_2024', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1_11_2024 = models.FloatField(db_column='1_11_2024', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1_12_2024 = models.FloatField(db_column='1_12_2024', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1_01_2025 = models.FloatField(db_column='1_01_2025', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1_02_2025 = models.FloatField(db_column='1_02_2025', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1_03_2025 = models.FloatField(db_column='1_03_2025', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1_04_2025 = models.FloatField(db_column='1_04_2025', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1_05_2025 = models.FloatField(db_column='1_05_2025', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1_06_2025 = models.FloatField(db_column='1_06_2025', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1_07_2025 = models.FloatField(db_column='1_07_2025', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1_08_2025 = models.FloatField(db_column='1_08_2025', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1_09_2025 = models.FloatField(db_column='1_09_2025', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1_10_2025 = models.FloatField(db_column='1_10_2025', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1_11_2025 = models.FloatField(db_column='1_11_2025', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1_12_2025 = models.FloatField(db_column='1_12_2025', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1_01_2026 = models.FloatField(db_column='1_01_2026', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1_02_2026 = models.FloatField(db_column='1_02_2026', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1_03_2026 = models.FloatField(db_column='1_03_2026', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1_04_2026 = models.FloatField(db_column='1_04_2026', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1_05_2026 = models.FloatField(db_column='1_05_2026', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1_06_2026 = models.FloatField(db_column='1_06_2026', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1_07_2026 = models.FloatField(db_column='1_07_2026', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1_08_2026 = models.FloatField(db_column='1_08_2026', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1_09_2026 = models.FloatField(db_column='1_09_2026', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1_10_2026 = models.FloatField(db_column='1_10_2026', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1_11_2026 = models.FloatField(db_column='1_11_2026', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1_12_2026 = models.FloatField(db_column='1_12_2026', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1_01_2027 = models.FloatField(db_column='1_01_2027', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1_02_2027 = models.FloatField(db_column='1_02_2027', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1_03_2027 = models.FloatField(db_column='1_03_2027', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1_04_2027 = models.FloatField(db_column='1_04_2027', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1_05_2027 = models.FloatField(db_column='1_05_2027', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1_06_2027 = models.FloatField(db_column='1_06_2027', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.

    class Meta:
        managed = False
        db_table = 't_cb_profit_crosstab_union_all_02'


class TCbProfitCrosstabUnionAll03(models.Model):
    tablo_tipi = models.CharField(max_length=255, blank=True, null=True)
    j_key_comb = models.CharField(max_length=255, blank=True, null=True)
    rep_month = models.CharField(max_length=255, blank=True, null=True)
    pc = models.CharField(max_length=255, blank=True, null=True)
    j_code = models.CharField(max_length=255, blank=True, null=True)
    l_1 = models.CharField(max_length=255, blank=True, null=True)
    l_2 = models.CharField(max_length=255, blank=True, null=True)
    l_3 = models.CharField(max_length=255, blank=True, null=True)
    l_4 = models.CharField(max_length=255, blank=True, null=True)
    l_5 = models.CharField(max_length=255, blank=True, null=True)
    l_6 = models.CharField(max_length=255, blank=True, null=True)
    key_r_pc_l6 = models.CharField(max_length=255, blank=True, null=True)
    unit = models.CharField(max_length=255, blank=True, null=True)
    desc_tr_l1 = models.CharField(max_length=255, blank=True, null=True)
    desc_tr_l2 = models.CharField(max_length=255, blank=True, null=True)
    desc_tr_l3 = models.CharField(max_length=255, blank=True, null=True)
    desc_tr_l4 = models.CharField(max_length=255, blank=True, null=True)
    desc_tr_l5 = models.CharField(max_length=255, blank=True, null=True)
    desc_tr_l6 = models.CharField(max_length=255, blank=True, null=True)
    tutar_tipi = models.CharField(max_length=255, blank=True, null=True)
    number_1_07_2027 = models.FloatField(db_column='1_07_2027', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1_08_2027 = models.FloatField(db_column='1_08_2027', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1_09_2027 = models.FloatField(db_column='1_09_2027', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1_10_2027 = models.FloatField(db_column='1_10_2027', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1_11_2027 = models.FloatField(db_column='1_11_2027', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1_12_2027 = models.FloatField(db_column='1_12_2027', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.

    class Meta:
        managed = False
        db_table = 't_cb_profit_crosstab_union_all_03'


class TCbProfitEurSt(models.Model):
    rep_month = models.CharField(max_length=4, blank=True, null=True)
    pc = models.CharField(max_length=3, blank=True, null=True)
    j_code = models.CharField(max_length=50, blank=True, null=True)
    desc_tr_l2 = models.CharField(max_length=255, blank=True, null=True)
    desc_tr_l3 = models.CharField(max_length=255, blank=True, null=True)
    expense = models.FloatField(blank=True, null=True)
    income = models.FloatField(blank=True, null=True)
    month = models.DateField(blank=True, null=True)
    curr = models.CharField(max_length=3, blank=True, null=True)
    l_1 = models.CharField(max_length=1, blank=True, null=True)
    l_2 = models.CharField(max_length=2, blank=True, null=True)
    l_3 = models.CharField(max_length=2, blank=True, null=True)
    l_4 = models.CharField(max_length=2, blank=True, null=True)
    l_5 = models.CharField(max_length=2, blank=True, null=True)
    l_6 = models.CharField(max_length=3, blank=True, null=True)
    profit = models.FloatField(blank=True, null=True)
    desc_tr_l6 = models.CharField(max_length=255, blank=True, null=True)
    key_r_pc_l6 = models.CharField(max_length=50, blank=True, null=True)
    unit = models.CharField(max_length=50, blank=True, null=True)
    desc_tr_l4 = models.CharField(max_length=255, blank=True, null=True)
    desc_tr_l5 = models.CharField(max_length=255, blank=True, null=True)
    desc_tr_l1 = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_cb_profit_eur_st'


class TCbProfitSt(models.Model):
    rep_month = models.CharField(max_length=4, blank=True, null=True)
    pc = models.CharField(max_length=3, blank=True, null=True)
    j_code = models.CharField(max_length=50, blank=True, null=True)
    desc_tr_l2 = models.CharField(max_length=255, blank=True, null=True)
    desc_tr_l3 = models.CharField(max_length=255, blank=True, null=True)
    month = models.DateField(blank=True, null=True)
    expense = models.FloatField(blank=True, null=True)
    income = models.FloatField(blank=True, null=True)
    curr = models.CharField(max_length=3, blank=True, null=True)
    l_1 = models.CharField(max_length=1, blank=True, null=True)
    l_2 = models.CharField(max_length=2, blank=True, null=True)
    l_3 = models.CharField(max_length=2, blank=True, null=True)
    l_4 = models.CharField(max_length=2, blank=True, null=True)
    l_5 = models.CharField(max_length=2, blank=True, null=True)
    l_6 = models.CharField(max_length=3, blank=True, null=True)
    profit = models.FloatField(blank=True, null=True)
    desc_tr_l6 = models.CharField(max_length=255, blank=True, null=True)
    key_r_pc_l6 = models.CharField(max_length=50, blank=True, null=True)
    unit = models.CharField(max_length=50, blank=True, null=True)
    desc_tr_l4 = models.CharField(max_length=255, blank=True, null=True)
    desc_tr_l5 = models.CharField(max_length=255, blank=True, null=True)
    desc_tr_l1 = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_cb_profit_st'


class TCbProfitTrySt(models.Model):
    rep_month = models.CharField(max_length=4, blank=True, null=True)
    pc = models.CharField(max_length=3, blank=True, null=True)
    j_code = models.CharField(max_length=50, blank=True, null=True)
    desc_tr_l2 = models.CharField(max_length=255, blank=True, null=True)
    desc_tr_l3 = models.CharField(max_length=255, blank=True, null=True)
    expense = models.FloatField(blank=True, null=True)
    income = models.FloatField(blank=True, null=True)
    month = models.DateField(blank=True, null=True)
    curr = models.CharField(max_length=3, blank=True, null=True)
    l_1 = models.CharField(max_length=1, blank=True, null=True)
    l_2 = models.CharField(max_length=2, blank=True, null=True)
    l_3 = models.CharField(max_length=2, blank=True, null=True)
    l_4 = models.CharField(max_length=2, blank=True, null=True)
    l_5 = models.CharField(max_length=2, blank=True, null=True)
    l_6 = models.CharField(max_length=3, blank=True, null=True)
    profit = models.FloatField(blank=True, null=True)
    desc_tr_l6 = models.CharField(max_length=255, blank=True, null=True)
    key_r_pc_l6 = models.CharField(max_length=50, blank=True, null=True)
    unit = models.CharField(max_length=50, blank=True, null=True)
    desc_tr_l4 = models.CharField(max_length=255, blank=True, null=True)
    desc_tr_l5 = models.CharField(max_length=255, blank=True, null=True)
    desc_tr_l1 = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_cb_profit_try_st'


class TCbProfitUsdSt(models.Model):
    rep_month = models.CharField(max_length=4, blank=True, null=True)
    pc = models.CharField(max_length=3, blank=True, null=True)
    j_code = models.CharField(max_length=50, blank=True, null=True)
    desc_tr_l2 = models.CharField(max_length=255, blank=True, null=True)
    desc_tr_l3 = models.CharField(max_length=255, blank=True, null=True)
    expense = models.FloatField(blank=True, null=True)
    income = models.FloatField(blank=True, null=True)
    month = models.DateField(blank=True, null=True)
    curr = models.CharField(max_length=3, blank=True, null=True)
    l_1 = models.CharField(max_length=1, blank=True, null=True)
    l_2 = models.CharField(max_length=2, blank=True, null=True)
    l_3 = models.CharField(max_length=2, blank=True, null=True)
    l_4 = models.CharField(max_length=2, blank=True, null=True)
    l_5 = models.CharField(max_length=2, blank=True, null=True)
    l_6 = models.CharField(max_length=3, blank=True, null=True)
    profit = models.FloatField(blank=True, null=True)
    desc_tr_l6 = models.CharField(max_length=255, blank=True, null=True)
    key_r_pc_l6 = models.CharField(max_length=50, blank=True, null=True)
    unit = models.CharField(max_length=50, blank=True, null=True)
    desc_tr_l4 = models.CharField(max_length=255, blank=True, null=True)
    desc_tr_l5 = models.CharField(max_length=255, blank=True, null=True)
    desc_tr_l1 = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_cb_profit_usd_st'


class TCbQty(models.Model):
    rep_month = models.CharField(primary_key=True, max_length=4)  # The composite primary key (rep_month, pc, l_1, l_2, l_3, l_4, l_5, l_6, exp_cb_mon) found, that is not supported. The first column is selected.
    pc = models.CharField(max_length=3)
    l_1 = models.CharField(max_length=1)
    l_2 = models.CharField(max_length=2)
    l_3 = models.CharField(max_length=2)
    l_4 = models.CharField(max_length=2)
    l_5 = models.CharField(max_length=2)
    l_6 = models.CharField(max_length=3)
    exp_cb_mon = models.DateField()
    exp_cb_qty = models.DecimalField(max_digits=25, decimal_places=15, blank=True, null=True)
    ccode = models.CharField(max_length=18)
    pkey = models.CharField(max_length=60)
    key_r_pc_l6 = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_cb_qty'
        unique_together = (('rep_month', 'pc', 'l_1', 'l_2', 'l_3', 'l_4', 'l_5', 'l_6', 'exp_cb_mon'),)


class TCbResUp(models.Model):
    rep_month = models.CharField(primary_key=True, max_length=4)  # The composite primary key (rep_month, pc, rs_l1, rs_l2, rs_l3, rs_l4) found, that is not supported. The first column is selected.
    pc = models.CharField(max_length=3)
    rs_l1 = models.CharField(max_length=2)
    rs_l2 = models.CharField(max_length=2)
    rs_l3 = models.CharField(max_length=2)
    rs_l4 = models.CharField(max_length=3)
    up_cost = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    key_r4_simple = models.CharField(max_length=15, blank=True, null=True)
    key_r4 = models.CharField(max_length=25, blank=True, null=True)
    rcode = models.CharField(max_length=12, blank=True, null=True)
    pkey = models.CharField(max_length=30, blank=True, null=True)
    price_month = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_cb_res_up'
        unique_together = (('rep_month', 'pc', 'rs_l1', 'rs_l2', 'rs_l3', 'rs_l4'),)


class TChat(models.Model):
    username = models.CharField(max_length=255, blank=True, null=True)
    message = models.CharField(max_length=255, blank=True, null=True)
    user_type = models.CharField(max_length=255, blank=True, null=True)
    action_date = models.DateField(blank=True, null=True)
    action_time = models.TimeField(blank=True, null=True)
    action_time_with_zone = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_chat'


class TCoeffDesc(models.Model):
    order_no = models.SmallIntegerField(blank=True, null=True)
    coefficient = models.CharField(primary_key=True, max_length=30)
    description = models.CharField(max_length=30, blank=True, null=True)
    initial_value = models.DecimalField(max_digits=25, decimal_places=10, blank=True, null=True)
    unit = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_coeff_desc'


class TMonths(models.Model):
    month = models.DateField(primary_key=True)
    year = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_months'


class TPictures(models.Model):
    username = models.CharField(primary_key=True, max_length=255)  # The composite primary key (username, pic_name) found, that is not supported. The first column is selected.
    pic_name = models.CharField(max_length=255)
    picture = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_pictures'
        unique_together = (('username', 'pic_name'),)


class TRepMonth(models.Model):
    rep_month = models.CharField(primary_key=True, max_length=4)
    rep_month_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_rep_month'


class TSapInput(models.Model):
    masraf_cesidi = models.CharField(max_length=255, blank=True, null=True)
    masraf_cesidi_tanimi = models.CharField(max_length=255, blank=True, null=True)
    pyp_ogesi = models.CharField(max_length=255, blank=True, null=True)
    nesne_tanimi = models.CharField(max_length=255, blank=True, null=True)
    belge_tarihi = models.DateTimeField(blank=True, null=True)
    belge_numarasi = models.CharField(max_length=255, blank=True, null=True)
    tanim = models.CharField(max_length=255, blank=True, null=True)
    deger_nesne_pb = models.FloatField(blank=True, null=True)
    nesne_para_birimi = models.CharField(max_length=255, blank=True, null=True)
    karsit_kayit_hesabi = models.CharField(max_length=255, blank=True, null=True)
    karsit_hesap_tanimi = models.CharField(max_length=255, blank=True, null=True)
    deger_rapor_pb = models.FloatField(blank=True, null=True)
    rapor_para_birimi = models.CharField(max_length=255, blank=True, null=True)
    deger_ipb = models.FloatField(blank=True, null=True)
    islem_para_birimi = models.CharField(max_length=255, blank=True, null=True)
    deger_kkpb = models.FloatField(blank=True, null=True)
    kk_para_birimi = models.CharField(max_length=255, blank=True, null=True)
    ters_kayit_belgesi = models.CharField(max_length=255, blank=True, null=True)
    ters_kaydi_yapildi = models.CharField(max_length=255, blank=True, null=True)
    ters_kayit_ref_no = models.CharField(max_length=255, blank=True, null=True)
    ters_kayit_org = models.CharField(max_length=255, blank=True, null=True)
    pc = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 't_sap_input'


class TTest(models.Model):
    rep_month = models.CharField(primary_key=True, max_length=4)  # The composite primary key (rep_month, pc) found, that is not supported. The first column is selected.
    pc = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 't_test'
        unique_together = (('rep_month', 'pc'),)


class TUnits(models.Model):
    unit = models.CharField(primary_key=True, max_length=20)

    class Meta:
        managed = False
        db_table = 't_units'


class TUserNotes(models.Model):
    username = models.CharField(primary_key=True, max_length=255)  # The composite primary key (username, note_time) found, that is not supported. The first column is selected.
    notes = models.CharField(max_length=255, blank=True, null=True)
    note_time = models.CharField(max_length=255)
    note_time_new = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_user_notes'
        unique_together = (('username', 'note_time'),)


class TUsersOnline(models.Model):
    username = models.CharField(primary_key=True, max_length=255)  # The composite primary key (username, status) found, that is not supported. The first column is selected.
    status = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 't_users_online'
        unique_together = (('username', 'status'),)


class TmC3Code(models.Model):
    t_l3 = models.CharField(primary_key=True, max_length=7)
    desc_tr_l3 = models.CharField(max_length=255, blank=True, null=True)
    desc_en_l3 = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tm_c3_code'


class TmC4Code(models.Model):
    t_l3 = models.CharField(primary_key=True, max_length=7)  # The composite primary key (t_l3, t_l4) found, that is not supported. The first column is selected.
    t_l4 = models.CharField(max_length=2)
    code = models.CharField(max_length=243, blank=True, null=True)
    desc_tr_l4 = models.CharField(max_length=255, blank=True, null=True)
    desc_en_l4 = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tm_c4_code'
        unique_together = (('t_l3', 't_l4'),)


class TmC5Code(models.Model):
    t_l3 = models.CharField(primary_key=True, max_length=7)  # The composite primary key (t_l3, t_l4, t_l5) found, that is not supported. The first column is selected.
    t_l4 = models.CharField(max_length=2)
    t_l5 = models.CharField(max_length=2)
    code_l5 = models.CharField(max_length=255, blank=True, null=True)
    desc_tr_l5 = models.CharField(max_length=255, blank=True, null=True)
    desc_en_l5 = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tm_c5_code'
        unique_together = (('t_l3', 't_l4', 't_l5'),)


class TmC6Code(models.Model):
    t_l3 = models.CharField(primary_key=True, max_length=7)  # The composite primary key (t_l3, t_l4, t_l5, t_l6) found, that is not supported. The first column is selected.
    t_l4 = models.CharField(max_length=2)
    t_l5 = models.CharField(max_length=2)
    t_l6 = models.CharField(max_length=3)
    code_l5 = models.CharField(max_length=30, blank=True, null=True)
    code_l6 = models.CharField(max_length=30, blank=True, null=True)
    desc_tr_l6 = models.CharField(max_length=255, blank=True, null=True)
    desc_en_l6 = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tm_c6_code'
        unique_together = (('t_l3', 't_l4', 't_l5', 't_l6'),)


class Users(models.Model):
    id = models.BigAutoField(primary_key=True)
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    username = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(unique=True, max_length=254)

    class Meta:
        managed = False
        db_table = 'users'

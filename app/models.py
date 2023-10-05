from django.db import models
import datetime
from django.db import models, transaction
# Create your models here.
'''写一个类，并且继承models.Model中的类   用此种方式来创建表'''


class UserInfo(models.Model):
    name = models.CharField(max_length=32)
    password = models.CharField(max_length=64)


class CustomInfo(models.Model):
    name = models.CharField(max_length=64, verbose_name='姓名')
    age = models.IntegerField(verbose_name='年龄')
    phone = models.CharField(max_length=64, verbose_name='手机号')
    address = models.CharField(max_length=128, verbose_name='地址')
    mate = models.CharField(max_length=32, verbose_name='配偶')
    custom = models.CharField(max_length=32, verbose_name='客户')
    scale = models.CharField(max_length=64, verbose_name='规模')  # 规模
    property = models.CharField(max_length=64, verbose_name='资产')  # 资产
    debt = models.CharField(max_length=64, verbose_name='负债')  # 负债
    BreedingAddress = models.CharField(max_length=128, verbose_name='养殖地址')  # 养殖地址
    account = models.CharField(max_length=64, verbose_name='银行账户')  # 银行账户
    type = models.CharField(max_length=32, verbose_name='客户类型')  # 客户类型
    area = models.CharField(max_length=32, verbose_name='所在区域')  # 所在区域
    credit = models.IntegerField(verbose_name='授信额度')  # 授信金额
    credit_date = models.DateTimeField(verbose_name='授信日期')
    use_credit = models.FloatField(verbose_name='使用额度')
    lirun = models.FloatField(verbose_name='利润',default='0')



'''添加一行数据'''


# UserInfo.objects.create(name='狄帅旗',password='666666')

class Custom_xiangqing(models.Model):
    # 级联删除
    xingming = models.CharField(max_length=64, verbose_name='姓名')
    #
    hezuo_guimo = models.CharField(max_length=64, verbose_name='初始规模')
    shangmiao_count = models.IntegerField(verbose_name='上苗数量')
    lilun_count = models.FloatField(verbose_name='理论提货量')
    hezuo_date=models.DateTimeField(verbose_name='合作日期')
    shangmiao_date=models.DateTimeField(verbose_name='上苗日期')
    maimiao_date=models.DateTimeField(verbose_name='卖苗日期')
    shiji_count = models.FloatField(verbose_name='理论提货量')
    hezuo_moshi=models.CharField(max_length=64, verbose_name='合作模式',default='保底合同')
    #
    # today_use = models.IntegerField(verbose_name='今日支用')
    # today_siliao = models.IntegerField(verbose_name='今日提货量')
    #
    # hezuo_date = models.DateTimeField(verbose_name='合作初始时间')
    # shangmiao_date = models.DateTimeField(verbose_name='上苗日期')
    #
    # maimiao_date = models.DateTimeField(verbose_name='卖苗日期')


    # chuangjian_date = models.DateTimeField(verbose_name='提货日期',default=datetime.datetime.now())


class Tihuo(models.Model):
    id = models.AutoField(primary_key=True)
    ren=models.CharField(max_length=64,verbose_name='提货人',default='zhangsan')
    today_use = models.FloatField(verbose_name='今日支用')
    today_siliao = models.FloatField(verbose_name='今日提货量')
    today=models.DateTimeField(verbose_name='提货日期',default=datetime.datetime.now())

    class Meta:
        ordering=['ren','today']

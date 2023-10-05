from django.shortcuts import render, HttpResponse,redirect

from app.models import CustomInfo, UserInfo
from django import forms

from app import models
from django.http import JsonResponse


# Create your views here.
import time
import datetime
#开始界面
def home(request):
    return render(request, 'home.html')

#登录
def login(request):
    if request.method == 'GET':

        return render(request, 'login.html')
    else:
        user = request.POST.get('username')
        pwd = request.POST.get('pwd')

        if user == '脱继昭' and pwd == '666666':

            request.session['info']={'id':1,'name':'脱继昭'}

            return redirect('/user/list/')

        else:
            return render(request, 'login.html', {'error_message': '用户名或密码错误'})

#添加数据
def orm(request):
    # name = models.CharField(max_length=64)
    # age = models.IntegerField()
    # phone = models.CharField(max_length=64)
    # address = models.CharField(max_length=128)
    # mate = models.CharField(max_length=32) #配偶姓名
    # custom = models.CharField(max_length=32) #客户
    # scale = models.CharField(max_length=64)  # 规模
    # property = models.CharField(max_length=64)  # 资产
    # debt = models.CharField(max_length=64)  # 负债
    # BreedingAddress = models.CharField(max_length=128)  # 养殖地址
    # account = models.CharField(max_length=64)  # 银行账户
    # type = models.CharField(max_length=32)  # 客户类型
    # area = models.CharField(max_length=32)  # 所在区域
    # credit = models.IntegerField()  # 授信金额
    # credit_date = models.DateTimeField(auto_now_add=True)
    # use_credit = models.IntegerField()
    # CustomInfo.objects.create(name='朱元璋',age=30,phone='13030650891',address='山东省临沂市临沭县城关镇人民路10号',mate='马皇后',
    #                           custom='张三',scale='1000只',property='1000万',debt='20万',BreedingAddress='临沭县城关镇王庄',
    #                           account='xxxxxxxxxxxxxxxxxxx',type='肉鸡',area='临沂市',credit=100000000,use_credit=500000)

    # CustomInfo.objects.create(name='李世民', age=30, phone='13030650891', address='山东省临沂市临沭县城关镇人民路10号', mate='马皇后',
    #                           custom='张三', scale='1000只', property='1000万', debt='20万', BreedingAddress='临沭县城关镇王庄',
    #                           account='xxxxxxxxxxxxxxxxxxx', type='肉鸡', area='临沂市', credit=100000000, use_credit=500000)
    # CustomInfo.objects.create(name='刘邦', age=30, phone='13030650891', address='山东省临沂市临沭县城关镇人民路10号', mate='马皇后',
    #                           custom='张三', scale='1000只', property='1000万', debt='20万', BreedingAddress='临沭县城关镇王庄',
    #                           account='xxxxxxxxxxxxxxxxxxx', type='肉鸡', area='临沂市', credit=100000000, use_credit=500000)

    # hezuo_guimo = models.CharField(max_length=64, verbose_name='初始规模')
    # shangmiao_count = models.IntegerField(verbose_name='上苗数量')
    # lilun_count = models.IntegerField(verbose_name='理论提货量')
    # hezuo_date = models.DateTimeField(verbose_name='合作日期')
    # shangmiao_date = models.DateTimeField(verbose_name='上苗日期')
    # maimiao_date = models.DateTimeField(verbose_name='卖苗日期')
    # shiji_count = models.IntegerField(verbose_name='理论提货量')
    # models.Custom_xiangqing.objects.create(xingming='李四',hezuo_guimo=10000,shangmiao_count=100000,lilun_count=100,hezuo_date='2023-9-10',
    #                                        shangmiao_date='2023-9-10',maimiao_date='2023-10-9',shiji_count=100)
    # models.Custom_xiangqing.objects.create(xingming='zhangsan', hezuo_guimo=10000, shangmiao_count=100000, lilun_count=100,
    #                                        hezuo_date='2023-9-10',shangmiao_date='2023-9-10', maimiao_date='2023-10-9', shiji_count=100)


    # models.Tihuo.objects.create(today_use=100000,today_siliao=20)
    #
    #
    # # 1.添加数据
    # UserInfo.objects.create(name='root',password='666666')
    # UserInfo.objects.create(name='王六',password='666666')
    # UserInfo.objects.create(name='赵匡胤',password='666666')
    # UserInfo.objects.create(name='秦始皇',password='666666')

    # 2.删除数据    原理是先筛选，后加入delete删除
    # UserInfo.objects.filter(id=2).delete()  #删除id=2的数据
    # UserInfo.objects.all().delete()  #删除表中的所有的数据

    # 3.获取数据

    # data_list=UserInfo.objects.all() #获取表中的所有数据，本质是一个数据列表[行,行,行]，QuerySet类型  每一行是一个对象，里面封装了表中的数据。
    #
    # for obj in data_list:
    #     print(obj.id,obj.name,obj.password)

    # 获取第一行数据

    # data1=UserInfo.objects.filter(id=1).first()  #若是不加first 则获取的依然是QuerySet类型
    # print(data1.id,data1.name,data1.password)

    # 4.修改数据

    # UserInfo.objects.filter(id=2).update(name='张飞')



    return render(request, 'login.html')

#展示界面用户
def user_list(request):
    # 比较原始的筛选方式
    q1 = request.GET.get('q1')
    q2 = request.GET.get('q2')
    q3 = request.GET.get('q3')
    data_list=CustomInfo.objects.all()

    if q1:
        data_list = CustomInfo.objects.filter(name=q1)

    if q2:
        data_list=CustomInfo.objects.filter(type=q2)

    if q3:
        data_list = CustomInfo.objects.filter(area=q3)

    # 进化
    filter_fileds={}
    # for field in CustomInfo._meta.fields:
    #     print(field.name)
    #     params=request.GET.get(field.name)
    #     if params:
    #         filter_fileds[field.name]=params
    # print(filter_fileds)
    # quryset=CustomInfo.objects.filter(**filter_fileds)
    # print(quryset)
    name=[]
    for i in data_list.values('name'):
        name.append(i['name'])

    all_thing = models.Tihuo.objects.all().values('ren')
    all_people = list(set([i['ren'] for i in all_thing]))

    all_tihuo = []
    all_shiyong = []
    for i in all_people:
        select_data = models.Tihuo.objects.filter(ren=i)

        all_siliao = models.Tihuo.objects.filter(ren=i).values('today_siliao', 'today_use')

        all_tihuo.append(sum([i['today_siliao'] for i in all_siliao]))
        all_shiyong.append(sum([i['today_use'] for i in all_siliao]))

    name_dict={}
    for i in range(len(all_people)):
        name_dict[all_people[i]]=all_shiyong[i]



    d = [y for y in (name + all_people) if y not in all_people]
    print(name_dict)
    for i in d:
        name_dict[i]=0
    print(name_dict)



    return render(request, 'userlist.html', {'data': data_list,'data1':name_dict})

# 添加用户功能
class Myform(forms.ModelForm):
    class Meta:
        model=CustomInfo
        fields=['name','age','phone','address','mate',
                'custom','scale','property','debt','BreedingAddress',
                'account','type','area','credit','use_credit','credit_date','lirun']

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

        for name,field in self.fields.items():
            print(name,field)
            field.widget.attrs={'class':'form-control','step':'0.01'}

def user_add(request):
    # data=request.POST.get()
    if request.method=='GET':
        form=Myform()

        return render(request,'user_add.html',{'list_name':form,})

    #用户提交数据，并进行校验
    form=Myform(data=request.POST)

    if form.is_valid():
        #如果数据合法，保存到数据库
        form.save()
        return redirect('/user/list/')
    else:

        return render(request, 'user_add.html', {'list_name': form,})

def user_edit(request):
    nid = request.GET.get("nid")
    row_object = models.CustomInfo.objects.filter(id=nid).first()
    if request.method == 'GET':
        form = Myform(instance=row_object)

        return render(request, 'xiangqing_edit.html', {'list_name': form, })

    form = Myform(data=request.POST, instance=row_object)

    if form.is_valid():
        # 如果数据合法，保存到数据库
        form.save()
        return redirect('/user/list/')
    else:

        return render(request, 'user_edit.html', {'list_name': form, })



#删除用户功能
def user_delete(request):

    nid=request.GET.get("nid")
    print(nid)
    CustomInfo.objects.filter(id=nid).delete()


    return redirect('/user/list/')

#筛选日期功能
def select_date(request):

    return render(request,'date_filter.html')


#展示客户详情界面

def user_xiangqing(request):
    data_list=models.Custom_xiangqing.objects.all()
    print(data_list.first())
    for i in data_list:
        print(i.lilun_count,i.shangmiao_count)






    return render(request, 'user_xiangqing.html', {'data': data_list})


def user_xiangqing_delete(request):
    nid = request.GET.get("nid")
    models.Custom_xiangqing.objects.filter(id=nid).delete()
    return redirect('/user/xiangqing/')

class xiangqingForm(forms.ModelForm):
    class Meta:
        model=models.Custom_xiangqing
        fields=['xingming','hezuo_guimo','shangmiao_count','lilun_count','hezuo_date','shangmiao_date','maimiao_date','shiji_count','hezuo_moshi']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            # print(name, field)
            field.widget.attrs = {'class': 'form-control','step':'0.01'}


def user_xiangqing_add(request):
    if request.method=='GET':
        form=xiangqingForm()

        return render(request,'xiangqing_add.html',{'list_name':form,})

    #用户提交数据，并进行校验
    form=xiangqingForm(data=request.POST)

    if form.is_valid():
        #如果数据合法，保存到数据库
        form.save()
        return redirect('/user/xiangqing/')
    else:

        return render(request, 'xiangqing_add.html', {'list_name': form,})

def user_xiangqing_edit(request):
    nid = request.GET.get("nid")
    row_object = models.Custom_xiangqing.objects.filter(id=nid).first()
    if request.method == 'GET':
        form = xiangqingForm(instance=row_object)

        return render(request, 'xiangqing_edit.html', {'list_name': form, })

    form = xiangqingForm(data=request.POST,instance=row_object)

    if form.is_valid():
        # 如果数据合法，保存到数据库
        form.save()
        return redirect('/user/xiangqing/')
    else:

        return render(request, 'xiangqing_add.html', {'list_name': form,})



def tihuo_zhanshi(request):
    data_list = models.Tihuo.objects.all()
    q1 = request.GET.get('q1')
    q2=request.GET.get('q2')
    q3=request.GET.get('q3')

    if q1:
        data_list = models.Tihuo.objects.filter(ren=q1)

    # if q2:
    #     data_list = models.Tihuo.objects.filter(todaye=q2)
    if q3 and q2:
        data_list = models.Tihuo.objects.filter(today__range=(q2, q3))

    all_use=data_list.values('today_use')
    all_shiyong=[]
    for i in all_use:
        all_shiyong.append(i['today_use'])

    all_siliao=data_list.values('today_siliao')
    all_tihuo=[]
    for i in all_siliao:
        all_tihuo.append(i['today_siliao'])



    print(all_tihuo)
    return render(request, 'tihuo_list.html', {'data': data_list,'all_use':sum(all_shiyong),'all_tihuo':sum(all_tihuo)})

class TihuoForm(forms.ModelForm):
    class Meta:
        model=models.Tihuo
        fields=['ren','today_siliao','today_use','today']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            # print(name, field)
            field.widget.attrs = {'class': 'form-control','step':'0.01','placeholder':field.label}



def tihuo_add(request):
    if request.method=='GET':
        form=TihuoForm()

        return render(request,'tihuo_add.html',{'list_name':form,})

    #用户提交数据，并进行校验
    form=TihuoForm(data=request.POST)

    if form.is_valid():
        #如果数据合法，保存到数据库
        form.save()
        return redirect('/tihuo/zhanshi/')
    else:

        return render(request, 'tihuo_add.html', {'list_name': form,})

def tihuo_delete(request):
    nid = request.GET.get("nid")
    models.Tihuo.objects.filter(id=nid).delete()
    return redirect('/tihuo/zhanshi/')

def tihuo_edit(request):
    nid= request.GET.get("nid")
    row_object=models.Tihuo.objects.filter(id=nid).first()
    if request.method=='GET':
        form=TihuoForm(instance=row_object)

        return render(request,'tihuo_edit.html',{'list_name':form,})

    form = TihuoForm(data=request.POST,instance=row_object)

    if form.is_valid():
        # 如果数据合法，保存到数据库
        form.save()
        return redirect('/tihuo/zhanshi/')
    else:

        return render(request, 'tihuo_add.html', {'list_name': form, })


def shuju_zhanshi(request):
    all_credit=models.CustomInfo.objects.all().values('credit')

    all_jine=[]
    for i in all_credit:

        all_jine.append(i['credit'])

    all_jine=sum(all_jine)

    all_lirun=models.CustomInfo.objects.all().values('lirun')

    all_lirun=sum([i['lirun'] for i in all_lirun])

    #今日的饲料和提货金额
    import datetime

    today=datetime.datetime.now()
    today=str(today).split(' ')[0]


    todayuse=models.Tihuo.objects.filter(today__gte=today).values('today_use','today_siliao')



    today_use_list=[]
    today_siliao_list=[]
    for i in todayuse:
        today_use_list.append(i['today_use'])
        today_siliao_list.append(i['today_siliao'])

    jin_use=sum(today_use_list)
    jin_siliao=sum(today_siliao_list)

    #总的金额和提货量
    AllUse=models.Tihuo.objects.filter().values('today_use','today_siliao')

    all_use_list=[]
    all_siliao_list = []
    for i in AllUse:
        all_use_list.append(i['today_use'])
        all_siliao_list.append(i['today_siliao'])
    all_use=sum(all_use_list)
    all_siliao=sum(all_siliao_list)


    print(all_jine)
    print(all_use)
    print("%.2f"%(all_jine-all_use))
    data_list={
        '总授信':all_jine,
        '今日支用':jin_use,
        '总支用':all_use,
        '今日提货量':jin_siliao,
        '总提货量':all_siliao,
        '总余额':"%.2f"%(all_jine-all_use),
        '总利润':all_lirun
    }
    day1=today.split('-')
    year=int(day1[0])
    month=int(day1[1])
    day=int(day1[2])
    start_date=datetime.date(year,month,day)

    end_date=start_date+datetime.timedelta(days=1)

    data1=models.Custom_xiangqing.objects.filter(maimiao_date__range=(start_date,end_date)).values()










    return render(request, 'shujuzhanshi.html', {'data': data_list,'data1':data1,})


def shuju_tu(request):
    all_thing = models.Tihuo.objects.all().values('ren')
    all_people = list(set([i['ren'] for i in all_thing]))
    print(all_people)

    all_tihuo = []
    all_shiyong = []
    for i in all_people:
        select_data = models.Tihuo.objects.filter(ren=i)

        all_siliao = models.Tihuo.objects.filter(ren=i).values('today_siliao', 'today_use')

        all_tihuo.append(sum([i['today_siliao'] for i in all_siliao]))
        all_shiyong.append(sum([i['today_use'] for i in all_siliao]))

    # 构造柱状图
    legend = ['总支用', '总提货量']
    series_list = [
        {
            'name': '总支用',
            'type': 'bar',
            'data': all_shiyong
        },
        {
            'name': '总提货量',
            'type': 'bar',
            'data': all_tihuo
        },

    ]
    x_axis = all_people
    result = {
        'status': True,
        'data': {
            'legend': legend,
            'series_list': series_list,
            'x_axis': x_axis

        }
    }

    return JsonResponse(result)


def logout(request):

    request.session.clear()

    return redirect('/login/')
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User
from dataDeal.models import picData,picDataSet
from django.utils import timezone

# 查询给用户的全部数据集
def get_data_list(request):
    setlist = picDataSet.objects.filter(user=request.user)
    return setlist


# 查询特定的数据集的全部信息
def get_list_all_info(request,list_id):
    listInfo = picDataSet.objects.filter(pk = list_id)
    return listInfo[0]


# 查询特定数据的全部数据
def get_data_list_by_set(request,list_id):
    datalist = picData.objects.filter(setSource=list_id)
    return datalist


# 查询特定的数据
def get_specific_data(request,data_id):
    data = picData.objects.get(pk=data_id)[0]
    return data


# 给某个数据集中插入数据
def create_data_by_user(request,data,list_id):
    try:
        if data.log != 0 and data.lat != 0:
            log = data.log
            lat = data.lat
        if len(data.typeData) > 0:
            typeData = data.typeData
        else:
            typeData = ";"
        if len(data.wordData) > 0:
            wordData = data.wordData
        else:
            wordData = ";"
        pD = picData(setSource=list_id, log=log, lat=lat, typeData=typeData, wordData=wordData)
        pD.save()
        pSD = picDataSet.objects.get(pk=list_id)
        pSD.dataNum += 1
        pSD.save()
    except:
        pass


# 创建一个数据集
def create_list_by_user(request,name):
    try:
        pDS = picDataSet(user=request.user, dataName=name)
        pDS.save()
    except:
        pass



# 删除用户的一个数据集
def delete_data_list(request,list_key):
    try:
        pDS = picDataSet.objects.get(pk = list_key)
        if pDS.dataName > 0:
            pD = picData.objects.filter(setSource=pDS.pk)
            for pd in pD:
                pd.delete()
        pDS.delete()
    except:
        pass


# 删除数据集中的一个数据
def delete_data_in_list(request,data_id,list_id):
    try:
        pDS = picDataSet.objects.get(pk = list_id)
        pD = picData.objects.get(pk = data_id)
        pD.delete()
        pDS.dataNum -= 1
        pDS.save()
    except:
        pass

# 删除数据集中的一系列数据
def delete_datas_in_list(request,datas_id,list_id):
    try:
        pDS = picDataSet.objects.get(pk=list_id)
        for data_id in datas_id:
            pD = picData.objects.get(pk=data_id)
            pD.delete()
            pDS.dataNum -= 1
        pDS.save()
    except:
        pass
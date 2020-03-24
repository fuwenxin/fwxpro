from django.shortcuts import render
from fwxpro import utils
# Create your views here.


def User_detail(request):
    setlist = utils.get_data_list(request)
    context = {'user':request.user,
               'datasets':setlist}
    response = render(request,'userhome.html',context)
    return response


def Data_list(request,list_pk):
    datalist = utils.get_data_list_by_set(request,list_pk)
    listinfo = utils.get_list_all_info(request,list_pk)
    context = {'datalist':datalist,'listinfo':listinfo}
    response = render(request,'datalist.html',context)
    return response


def User_info(request):
    return render(request,'userinfo.html',{})
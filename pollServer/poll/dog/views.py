from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.

from django.http import HttpResponse
from . import MongoConnection


def index(request):
    return render(request, "dog/index.html")


def index2(request):
    return HttpResponse("hello")


def logo(request):
    return HttpResponse()


def db_insert(request):
    mc = MongoConnection.MongoConnection()
    mc.set_db()
    mc.set_collection()
    mc.insert_doc()
    return HttpResponse(True)


def db_get(request):
    mc = MongoConnection.MongoConnection()
    mc.set_db()
    mc.set_collection()
    if     mc.get_doc() is None:
        return HttpResponse("null")
    else:
        return HttpResponse(str(mc.get_doc()))


def create_user(request):
    id = request.GET["id"]
    pw = request.GET["pw"]
    mg = MongoConnection.MongoConnection()
    mg.set_db()
    mg.set_collection()

    if mg.check_tag(id) is True:
        result = mg.insert_id(id, pw)
        if result is not None:
            return HttpResponse(True)
        else:
            return HttpResponse(False)
    else:
        return HttpResponse(False)


def check_tag(self, id):
    if self.get_doc(id) is None:
        return True
    else:
        return False

@csrf_exempt
def request_post(request):
    c = {}
   # val = request.POST.get('valuekjoiigv')

    val = request.POST['value']

    return HttpResponse(val)

def request_get(request):
    c = {}
   # val = request.POST.get('valuekjoiigv')

    val = request.GET['value']

    return HttpResponse(val)




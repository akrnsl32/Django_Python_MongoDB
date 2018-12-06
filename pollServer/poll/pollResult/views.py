from django.http import HttpResponse
from django.http import *
# Create your views here.
from . import MongoConnection
import json as js
from bson import ObjectId,json_util


def index(request):
    return HttpResponse("poll server test!")


def check_tag(request):
    tag = request.GET["tag"]
    mg = MongoConnection.MongoConnection()
    mg.set_db("poll")
    mg.set_collection("tag")
    result = mg.check_tag(tag)
    return HttpResponse(result)


def create_user(request):
    tag = request.GET["tag"]
    pw = request.GET["pw"]
    mg = MongoConnection.MongoConnection()
    mg.set_db("poll")
    mg.set_collection("tag")

    if mg.check_tag(tag) is True:
        result = mg.insert_tag(tag, pw)
        if result is not None:
            return HttpResponse(True)
        else:
            return HttpResponse(False)
    else:
        return HttpResponse(False)


def login(request):
    tag = request.GET["tag"]
    pw = request.GET["pw"]
    mg = MongoConnection.MongoConnection()
    mg.set_db("poll")
    mg.set_collection("tag")

    result = mg.check_tag(tag)
    # result is False == tag is exist..
    if result is True:
        return HttpResponse("tag_null")
    else:
        result = mg.get_doc(tag)

        result = JSONEncoder().encode(result)
        #converting json to python dictionary
        json_str = js.loads(result)

#        converting dictionary to json
#        result = json_util.dumps(result)

        j_tag = json_str["tag"]
        j_pw = json_str["password"]
        if tag == j_tag:
            if pw == j_pw:
                return HttpResponse(tag)
            else:
                return HttpResponse("pw_null")
        return HttpResponse("tag_null")


def getDoc(request):
    tag = request.GET["tag"]
    mg = MongoConnection.MongoConnection()
    mg.set_db("poll")
    mg.set_collection("tag")
    result = mg.get_dc(tag)
    return HttpResponse(str(result))


class JSONEncoder(js.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return js.JSONEncoder.default(self, o)

import json

from datetime import datetime
from django.contrib.auth.models import User
from django.core import serializers
from django.db.models import get_model
from django.forms.models import model_to_dict
from django.http import HttpResponse

class TimestampException(Exception):
    pass

class UserDoesNotExist(Exception):
    pass


def save_log(sender, **kwargs ):
    instance = kwargs["instance"]
    action = kwargs["created"]
    sender = sender.__name__    # get the name of the table which sent the request
    model_dict = model_to_dict(instance)
    previous_time_stamp = get_latest_timestamp()
    try:
        user = User.objects.get(id=instance.user_modified_id) if instance.user_modified_id else User.objects.get(id=instance.user_created_id)
    except Exception, ex:
        user = None

    ServerLog = get_model('coco', 'ServerLog')
    log = ServerLog(user=user, action=action, entry_table=sender, model_id=instance.id)
    log.save()
    ###Raise an exception if timestamp of latest entry is less than the previously saved data timestamp
    if previous_time_stamp:
        if previous_time_stamp.timestamp > log.timestamp:
            raise TimestampException('timestamp error: Latest entry data time created is less than previous data timecreated')


def delete_log(sender, **kwargs):
    instance = kwargs["instance"]
    sender = sender.__name__    # get the name of the table which sent the request
    user = None
    if instance.user_created_id:
        if instance.user_modified_id:
            user = User.objects.get(id=instance.user_modified_id) 
        else:
            user = User.objects.get(id=instance.user_created_id)
    ServerLog = get_model('coco', 'ServerLog')
    try:
        log = ServerLog(user=user, action=-1, entry_table=sender, model_id=instance.id)
        log.save()
    except Exception as ex:
        pass


def send_updated_log(request):
    timestamp = request.GET.get('timestamp', None)
    print timestamp
    if timestamp:
        ServerLog = get_model('coco', 'ServerLog')
        rows = ServerLog.objects.filter(timestamp__gte=timestamp)
        if rows:
            data = serializers.serialize('json', rows, fields=('action','entry_table','model_id', 'timestamp'))
            return HttpResponse(data, mimetype="application/json")
    return HttpResponse("0")

def get_latest_timestamp():
    ServerLog = get_model('coco', 'ServerLog')
    try:
        timestamp = ServerLog.objects.latest('id')
    except Exception as e:
        timestamp = None
    return timestamp

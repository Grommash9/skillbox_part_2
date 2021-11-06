import json
import time

from django.core.exceptions import PermissionDenied


class IpLogger:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        data_dict = {
            "Time": time.ctime(time.time()),
            "PATH_INFO": request.META['PATH_INFO'],
            "REQUEST_METHOD": request.META['REQUEST_METHOD'],
            "REMOTE_ADDR": request.META['REMOTE_ADDR'],
            "HTTP_USER_AGENT": request.META['HTTP_USER_AGENT'],

        }

        with open('D:/python/skillbox_part_2/module_3/users_log.txt', 'a') as logs_file:
            logs_file.write(f"{str(data_dict)}\n")

        response = self.get_response(request)

        return response
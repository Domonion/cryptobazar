import time
import datetime

from django.shortcuts import render

def main(request):
    return render(request, "index.html")


def output(request):
    print(request.POST)
    context = {
        "name": request.POST["name"],
        "abb": request.POST["abb"],
        "token_count": request.POST["token_count"],
        "start": int(time.mktime(datetime.datetime.strptime(request.POST["start_d"], r"%Y-%m-%d").timetuple())),
        "period": request.POST["time_ico"],
        "restricted": request.POST["restricted"],
        "percent": request.POST["percent"],
    }
    return render(request, "output.html", context, content_type="text/plain")

from django.shortcuts import render

def main(request):
    return render(request, "index.html")


def output(request):
    context = {
        "name": request.POST["name"],
        "abb": request.POST["abb"],
        "token_count": request.POST["token_count"],
        "start": request.POST["start_d"],
        "period": request.POST["time_ico"],
        "restricted": request.POST["restricted"],
        "percent": request.POST["percent"],
    }
    return render(request, "output.html", context)
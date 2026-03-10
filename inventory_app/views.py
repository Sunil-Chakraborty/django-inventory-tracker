import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import SheetData

@csrf_exempt
def receive_sheet_data(request):

    if request.method == "POST":
        data = json.loads(request.body)

        SheetData.objects.create(
            name=data.get("name"),
            department=data.get("department"),
            date=data.get("date")
        )

        return JsonResponse({"status": "success"})

    return JsonResponse({"status": "invalid request"})
 
def dashboard(request):
    data = SheetData.objects.all().order_by('-id')
    return render(request,"dashboard.html",{"data":data})    
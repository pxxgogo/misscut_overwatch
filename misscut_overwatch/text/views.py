from django.shortcuts import render
from django.http import JsonResponse
from text.ops import split_text, fetch_text
from text.models import TextFile
from django.utils.timezone import now
from django.core.files.base import ContentFile
import traceback
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def submit_text(request):
    if request.method == "POST":
        try:
            text: str = request.POST["text"]
            if text == "":
                return JsonResponse({"return_code": 0}, safe=False)
            paras: list[str] = split_text(text)
            for para in paras:
                text_model: TextFile = TextFile()
                text_model.save()
                text_model.file.save("%s-%d.txt" % (str(now()), text_model.id), ContentFile(para))
                text_model.save()
            return JsonResponse({"return_code": 0}, safe=False)
        except:
            ex = traceback.format_exc()
            print(ex)
            return JsonResponse({"return_code": 2}, safe=False)
    return JsonResponse({"return_code": 1}, safe=False)


@csrf_exempt
def get_text(request):
    if request.method == "POST":
        try:
            username: str = request.POST.get("username", "")
            if len(username) == 0:
                return JsonResponse({"return_code": 3}, safe=False)
            content, model_id = fetch_text(username)
            return JsonResponse({"return_code": 0, "text": content, "model_id": model_id}, safe=False)
        except:
            ex = traceback.format_exc()
            print(ex)
            return JsonResponse({"return_code": 2}, safe=False)
    else:
        return JsonResponse({"return_code": 1}, safe=False)

@csrf_exempt
def next_text(request):
    if request.method == "POST":
        try:
            username: str = request.POST.get("username", "")
            model_id: int = int(request.POST.get("model_id", "-1"))
            ret_content: str = request.POST.get("ret_content", "")
            if len(username) == 0 or model_id < 0:
                return JsonResponse({"return_code": 3}, safe=False)
            text_model = TextFile.objects.get(id=model_id)
            text_model.finish_flag = 2
            text_model.ret_file.save("%s-%d.txt" % (str(now()), text_model.id), ContentFile(ret_content))
            text_model.save()
            content, model_id = fetch_text(username)
            return JsonResponse({"return_code": 0, "text": content, "model_id": model_id}, safe=False)
        except:
            ex = traceback.format_exc()
            print(ex)
            return JsonResponse({"return_code": 2}, safe=False)
    else:
        return JsonResponse({"return_code": 1}, safe=False)

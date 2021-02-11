from text.models import TextFile
from django.utils.timezone import now

SOFT_MAX_LENGTH: int = 300


def split_text(text: str):
    tmp_paras: list[str] = text.split("\n")
    merged_paras: list[str] = []
    current_para: str = ""
    for tmp_para in tmp_paras:
        current_para += tmp_para
        if len(current_para) > SOFT_MAX_LENGTH:
            merged_paras.append(current_para)
            current_para = ""
    if len(current_para) > 0:
        merged_paras.append(current_para)
    return merged_paras


def fetch_text(username: str):
    text_models = TextFile.objects.filter(finish_flag=1, username=username)
    if len(text_models) > 0:
        text_model = text_models.first()
        text_model.operate_time = now()
        text_model.save()
        with open(text_model.file.path) as handle:
            content = handle.read()
            model_id = text_model.id
    else:
        text_models = TextFile.objects.filter(finish_flag=0)
        text_model = text_models.first()
        text_model.finish_flag = 1
        text_model.username = username
        text_model.operate_time = now()
        text_model.save()
        with open(text_model.file.path) as handle:
            content = handle.read()
            model_id = text_model.id
    return content, model_id

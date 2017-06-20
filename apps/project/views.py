import re
import json
from datetime import datetime

from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

from .models import Scheme, DraftBase
from users.models import UserProfile
# Create your views here.


class SchemeQueryView(View):

    """
    宣传方案查询
    """

    def get(self, request):
        return render(request, 'Scheme_query.html', {})


class SchemeDraftView(View):
    """
    宣传方案起草
    """

    def get(self, request):
        return render(request, 'xc_ scheme.html', {
            "add_time": datetime.now()
        })

    def post(self, request):
        if request.is_ajax():
            title = request.POST.get('title', '')
            category = request.POST.get('category', '')
            principal = request.POST.get('principal', '')
            member = request.POST.get('member', '')
            budget = request.POST.get('budget', '')
            actual_cost = request.POST.get('actual_cost', '')
            start_time = request.POST.get('start_time', '')
            end_time = request.POST.get('end_time', '')
            remark = request.POST.get('remark', '')
            status = request.POST.get('status', '')
            style = "宣传方案申请"
            accept_user = request.POST.get('accept_user[]', [])

            # 修改时间格式
            time = request.POST.get('add_time', '')
            patten = '年|月'
            time = re.sub(patten, '-', time)
            time = re.sub('日', '', time)

            draft_base = DraftBase()
            draft_base.title = title
            draft_base.status = status
            draft_base.add_time = time
            draft_base.draft_user = request.user
            draft_base.style = style
            draft_base.save()

            scheme = Scheme()
            scheme.category = category
            scheme.principal = principal
            scheme.member = member
            scheme.budget = budget
            scheme.actual_cost = actual_cost
            scheme.start_time = start_time
            scheme.end_time = end_time
            scheme.remark = remark
            scheme.main = draft_base
            scheme.save()

            for a in accept_user:
                accept_user = UserProfile.objects.get(id=a)
                if accept_user:
                    draft_base.accept_user.add(accept_user)

            recall = {"status": "success", "lis_id": scheme.id}
            return HttpResponse(json.dumps(recall))
        return HttpResponse('{"status": "fail"}', content_type="application/json")


class SchemeFileUploadView(View):

    """
    保存宣传方案起草表附件
    """

    def post(self, request, *args, **kwargs):

        lis_id = request.POST.get('lis_id', '')
        file = request.FILES.get("file", None)

        if file:
            scheme = Scheme.objects.get(id=lis_id)
            scheme.file = file
            scheme.save()

            return HttpResponse('{"status": "success"}', content_type="application/json")

        return HttpResponse('{"status": "fail"}', content_type="application/json")

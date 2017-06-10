from datetime import datetime
import json
import re

from django.shortcuts import render, render_to_response
from django.views.generic import View
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.http import HttpResponse

from .models import MessageDraft, ObjMedia, Category
from .forms import MessageDraftFileUploadForm, MessageDraftIdForm
from users.models import UserProfile, Team


class MessageDraftView(View):
    """
    宣传管理信息起草
    """

    def get(self, request):
        add_time = datetime.now()

        all_category = Category.objects.all()
        all_media = ObjMedia.objects.all()
        all_team = Team.objects.all()

        return render(request, 'xc_draft.html', {
            "add_time": add_time,
            "all_category": all_category,
            "all_media": all_media,
            "all_team": all_team,
        })


    def post(self, request):

        if request.is_ajax():

            title = request.POST.get('title', '')
            status = request.POST.get('state', '')

            # 修改时间格式
            time = request.POST.get('time', '')
            patten = '年|月'
            time = re.sub(patten, '-', time)
            time = re.sub('日', '', time)

            start_time = request.POST.get('start_time', '')
            end_time = request.POST.get('end_time', '')
            content = request.POST.get('content', '')
            remark = request.POST.get('remark', '')
            style = request.POST.getlist('style[]', [])
            media = request.POST.getlist('media[]', [])
            accept_user = request.POST.getlist('accept_user[]', [])
            file = request.POST.get('file', '')

            message_draft = MessageDraft()
            message_draft.draft_user = request.user
            message_draft.title = title
            message_draft.status = status
            message_draft.add_time = time
            message_draft.start_time = start_time
            message_draft.end_time = end_time
            message_draft.content = content
            message_draft.remark = remark

            # 保存文件 ！

            message_draft.save()

            lis = MessageDraft.objects.get(id=message_draft.id)
            # 保存类型
            for c in style:
                category = Category(name=c)
                lis.category.add(category)
            # # 保存媒体对象
            for m in media:
                media = ObjMedia(name=m)
                lis.media.add(media)

            # # 修改   保存接受人的id
            # for a in accept_user:
            #     accept_user = UserProfile(id=a)
            #     if accept_user:
            #        lis.accept_user.add(accept_user)

            recall = {"status": "success", "lis_id": message_draft.id}

            return HttpResponse(json.dumps(recall))

        return HttpResponse('{"status": "fail"}', content_type="application/json")


class MessageDraftFileUploadView(View):

    def post(self, request):
        lis_id = request.POST.get("lis_id", '')
        file = request.FILES.get("file", None)
        if file:
            message_draft = MessageDraft.objects.get(id=lis_id)
            message_draft.file = file
            message_draft.save()

            return HttpResponse('{"status": "success"}', content_type="application/json")

        return HttpResponse('{"status": "fail"}', content_type="application/json")

class MessageInfoView(View):
    """
    宣传信息统计页面
    """
    def get(self, request):

        return render(request, 'information_count.html', {

        })

class MessageManagementView(View):
    """
    宣传信息管理页面
    """
    def get(self, request):
        return render(request, 'Publicity_management.html', {

        })

class MessageSearchView(View):
    """
    宣传信息查询页面
    """
    def get(self, request):
        return render(request, 'Publish_query.html', {

        })

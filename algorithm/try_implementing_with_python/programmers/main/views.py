from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http    import JsonResponse
from django.views   import View

import json

def index(request):
    return render(request, 'main/index.html')

@csrf_exempt
def login(request):
    return render(request, 'main/login.html')

@csrf_exempt
def test(request):
    json_object = json.loads(request.body)
    print('ID : ',json_object.get('id'))
    print('PASSWORD : ' ,json_object.get('paswd'))
    return JsonResponse(json_object)


@csrf_exempt
def recruit(request):
    template = 'main/recruit.html'
    tag = ''
    if request.GET:
        tag = request.GET.get('tag')

    return render(request, template, {
        'tag_name' : tag
    })


# def search(request):
#     json_object = json.loads(request.body)
#     tag = json_object.get('tag')
#
#     return JsonResponse(tag)




    # def get(self, request):
    #     json_object = json.loads(request.body)
    #     tag = json_object.get('tag')
    #
    #     company_list = {
    #         'python' : ['매스프레소', '휴머스온'],
    #         'node.js' : ['패스트캠퍼스랭귀지', '리디', '딥바이오','모두싸인'],
    #         'java' : ['투믹스', '리비', '동화기업', '쓰리아이']
    #     }
    #     print(tag)
    #     return JsonResponse({'company' : company_list[tag]}, status=200)


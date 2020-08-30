from django.shortcuts import render

from .models import MovieComment as comment


# Create your views here.
def index(request):
    # 获取请求get方法参数q值
    q_value = request.GET.get('q')

    condition = {'n_star__gt': 3}

    if q_value:
       condition['short__icontains'] = q_value

    show_data = comment.objects.all().filter(**condition)

    return render(request, 'index.html', locals())
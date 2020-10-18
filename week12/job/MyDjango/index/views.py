from django.shortcuts import render
from django.db.models import Avg

from .models import Sentiment as S

# Create your views here.
def data_show(request):
    """
    从数据库获取数据传给templates
    """
    # 获取全部评论数据
    comments = S.objects.all()
    # 评论总数
    counter = S.objects.all().count()

    star_avg = 33

    # 情感倾向
    sentiment_avg = f"{S.objects.aggregate(Avg('sentiment'))['sentiment__avg']:0.2f}"

    # 正向数量
    queryset = S.objects.values('sentiment')
    condtions = {'sentiment__gte': 0.5}
    plus = queryset.filter(**condtions).count()

    # 负向数量
    queryset = S.objects.values('sentiment')
    condtions = {'sentiment__lt': 0.5}
    minus = queryset.filter(**condtions).count()

    return render(request, 'result.html', locals())
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Q
from .models import NetdiskResource

class SearchView(APIView):
    def get(self, request):
        keyword = request.query_params.get('keyword', '').strip()
        category = request.query_params.get('category', 'all')
        page = int(request.query_params.get('page', 1))
        page_size = 20 # 开源演示版，一页20条就够了

        if not keyword:
            return Response({"count": 0, "results": []})

        # 极简 MySQL 模糊查询
        queryset = NetdiskResource.objects.filter(
            Q(title__icontains=keyword)
        )

        if category != 'all':
            queryset = queryset.filter(category=category)

        total = queryset.count()
        start = (page - 1) * page_size
        results = queryset[start:start + page_size]

        # 组装返回数据
        data_list = []
        for item in results:
            data_list.append({
                'id': item.id,
                'title': item.title,
                'download_url': item.download_url,
                'category': item.category,
                'desc': item.desc
            })

        return Response({
            "count": total,
            "results": data_list
        })
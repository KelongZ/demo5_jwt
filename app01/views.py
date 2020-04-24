from django.shortcuts import render, HttpResponse
from rest_framework.views import APIView
# Create your views here.


class IndexView(APIView):
    """
    首页
    """
    authentication_classes = []
    permission_classes = []

    def get(self, request):
        print(request)
        return HttpResponse('首页')

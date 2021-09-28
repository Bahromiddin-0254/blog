from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import render
from .serializers import PersonSerializer
# Create your views here.

def index(request):
    return render(request, 'index.html')
def about(request):
    return render(request,'about.html')
def blog(request):
    return render(request,'blog.html')
def contact(request):
    return render(request,'contact.html')
def portfolio(request):
    return render(request,'portfolio.html')
def services(request):
    return render(request,'services.html')
def teams(request):
    return render(request,'teams.html')
class testView(APIView):
    def get(self,request,*args,**kwargs):
        serializer = PersonSerializer()
        return Response(serializer.data)
    def post(self,request,*args,**kwargs):
        serializer =PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
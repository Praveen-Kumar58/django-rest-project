from django.shortcuts import render

from app.serializers import *
from app.models import*
from rest_framework import viewsets #1) model viewset
from rest_framework.viewsets import ViewSet # 2)Viewset
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser



#model Viewset

class ProductCrudActions(viewsets.ModelViewSet):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
  

#viewSet
class ProductVS(ViewSet):
    permission_classes=[IsAdminUser]
    def list(self,request):
        QPO=Product.objects.all()
        JPO=ProductSerializer(QPO,many=True)
        return Response(JPO.data)
     
    def retrieve(self,request,pk):
        PO=Product.objects.filter(pk=pk)
        if PO:
            JO=ProductSerializer(PO[0])
            return Response(JO.data)
        return Response({"message":"not found"})
        
    
    def create(self,request):
        PSF=ProductSerializer(data=request.data)
        if PSF.is_valid():
            PSF.save()
            return Response({"message":"Successfully created"})
        return Response({"message":"not created"})
    
    def update(self,request,pk):
        PO=Product.objects.get(pk=pk)
        UPO=ProductSerializer(PO,data=request.data)
        if UPO.is_valid():
            UPO.save()
            return Response({"message":"Successfully updated"})
        return Response({"message":"not updated"})
    
    def partial_update(self,request,pk):
        PO=Product.objects.get(pk=pk)
        UPO=ProductSerializer(PO,data=request.data,partial=True)
        if UPO.is_valid():
            UPO.save()
            return Response({"message":"Successfully partial_update"})
        return Response({"message":"not partially_updated"})
    
    def destroy(self,request,pk):
        PO=Product.objects.get(pk=pk)
        PO.delete()
        return Response({"message":"Successfully deleted"})
    
    
    
        
    
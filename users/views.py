from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

# Create your views here.
import users.models as models
import users.serializers as serializers

class SignUpView(APIView):
   
    def post(self, request, format=None):
        print(request.data)
        serializer = serializers.SignUpCustomSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            user_account = serializer.data
            user = models.User.objects.get(email=user_account["email"])

            return Response(
                {
                    "message": f'An activation link has been sent to {user_account["email"]}',
                },
                status=status.HTTP_205_RESET_CONTENT,
            )

        
        return Response(
            {"stauts": "error", "data": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST,
        )

from rest_framework import serializers
import users.models as models
from django.contrib.auth.hashers import make_password



class SignUpCustomSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.User
        # fields = "__all__"
        fields = [
            "email",
            "password",
        ]

    def save(self):
        password = self.validated_data["password"]
        # check for confirm password match
        hash_password = make_password(self.validated_data["password"])
        print("hash_password", hash_password)
        register = models.User(
            email=self.validated_data["email"], password=hash_password,
        )
        register.save()
        print("register",register)

        return register

    
   

   

   
       

   
      
from rest_framework import generics
from rest_framework.response import Response

from rest_framework_simplejwt.tokens import RefreshToken

from user_account.models import BaseUser
from user_account.api.serializers import BaseUserSerializer


class UserLoginView(generics.CreateAPIView):

    def post(self, request, *args, **kwargs):
        username = request.data['username']
        password = request.data['password']

        users = BaseUser.objects.filter(username=username)
        if not users.exists():
            return Response({'user': 'does not exist'})
        user = users.first()
        print(user.password)
        if user.check_password(password):
            refresh = RefreshToken.for_user(user)
            return Response({'user': 'logged in',
                             'access': str(refresh.access_token),
                             'refresh': str(refresh)},
                            status=200)
        return Response({'user': 'wrong password'})


class CustomerUserCreateView(generics.CreateAPIView):
    serializer_class = BaseUserSerializer
    queryset = BaseUser

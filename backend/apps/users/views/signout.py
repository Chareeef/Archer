from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class SignoutView(APIView):
    """Signout view
    """

    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except KeyError:
            return Response({'detail': 'Refresh token is required'},
                            status=status.HTTP_400_BAD_REQUEST)
        except TokenError:
            return Response({'detail': 'Invalid or expired token'},
                            status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'detail': 'Something went wrong'},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

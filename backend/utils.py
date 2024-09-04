from rest_framework_simplejwt.tokens import RefreshToken


def get_token_for_user(user):
    """Generate and return a JWT access token for a given user."""
    refresh = RefreshToken.for_user(user)
    return str(refresh.access_token)

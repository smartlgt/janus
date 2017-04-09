from django.http import JsonResponse, HttpResponse
from oauth2_provider.exceptions import OAuthToolkitError
from oauth2_provider.views import ProtectedResourceView


class ProfileView(ProtectedResourceView):
    def get(self, request, *args, **kwargs):
        if request.resource_owner:
            user = request.resource_owner
            return JsonResponse(
            {
             'id': user.username,
             'first_name': user.first_name,
             'last_name': user.last_name,
             'name': user.first_name + ' ' + user.last_name,
             'email': user.email,
             #ToDo: check the emails
             'email_verifyed': 'True',
             }
            )
        return self.error_response(OAuthToolkitError("No resource owner"))

def index(request):
    return HttpResponse("hello from janus")

def not_authorized(request):
    return HttpResponse("Sorry, you are not authorized to access this application. Contact an admin if you think this is a mistake.")
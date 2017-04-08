from oauth2_provider.models import Grant
from oauth2_provider.oauth2_validators import OAuth2Validator


class OAuth2Validator(OAuth2Validator):

    def validate_code(self, client_id, code, client, request, *args, **kwargs):
        valid = super(OAuth2Validator, self).validate_code(client_id, code, client, request, *args, **kwargs)
        # the request has now a user object if valid is true
        if valid and request.user.profile:

            permitted = False
            user = request.user

            #check if user can autenticate for this app
            for group in user.profile.group.all():
                permits = group.grouppermission_set.all()
                for permit in permits:
                    if permit.can_authenticate:
                        permitted = True

            if not permitted:
                #not permited to access this application
                # ToDo: redirect to different site, and explain this to the user? (if possible at this point)
                return False

        return valid
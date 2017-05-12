# Janus

Janus is a Single sign-on (SSO) system based on django.

The janus services, exposes a OAuth2 interface and can handle the authentication via internal django database or external ldap authentication.

For this project exists a variety of ready to use OAuth2 plugins for commonly used services like Sentry, Sharelatex, Django, Etherpad-lite.

## Installation

### Docker
- You can use the provided `docker-complese.yml`
- !change the `MYSQL_ROOT_PASSWORD`
- copy the `main/config/local_settings.py.dist` to `main/config/local_settings.py`
- !change the `local_settings.py` config to match your docker settings
- start the project `docker-compose up -d`
- execute the migrations `./manage.sh migrate`
- create a superuser `./manage.sh createsuperuser`


## Configuration
- navigate to `http://yourserver/admin/` to setup the OAuth2 uids and secrets.

# Janus

Janus is a Single sign-on (SSO) system based on django.

## Find the right repo
#### This repo (SSO)
This is a standalone version that includes a ready-to-user docker-compose.yml for quick deployment.
#### Module (SSO)
If you only need the janus module for including the sso backend into your existing django-deployment, you can find it here:
https://github.com/smartlgt/django-janus
#### The receiver module
If you want to use janus as a login provider within your django-project, you can find the module here:
https://github.com/smartlgt/janus-allauth-provider

## About Janus
The janus services, exposes a OAuth2 interface and can handle the authentication via internal django database or external ldap authentication.

For this project exists a variety of ready to use OAuth2 plugins for commonly used services like Sentry, Sharelatex, Django, Etherpad-lite.

## Installation

### Docker
- You can use the provided `docker-compose.yml`
- Copy the env.env.dist file to env.env and adjust settings
- copy the `main/config/local_settings.py.dist` to `main/config/local_settings.py`
- change the `local_settings.py` config to match your docker settings
- start the project `docker-compose up -d`
- execute the migrations `./manage.sh migrate`
- create a superuser `./manage.sh createsuperuser`

### Adjusting templates
You can adjust templates within the template folder.

## Configuration
- navigate to `http://yourserver/admin/` to setup the OAuth2 uids and secrets.

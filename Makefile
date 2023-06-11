
.PHONY: all
all:
	python manage.py makemigrations
	python manage.py migrate
	python manage.py shell -c "from django.contrib.auth.models import User; \
		User.objects.filter(username='admin').exists() or \
		User.objects.create_superuser('admin', 'admin@example.com', 'admin')"
	python manage.py runserver 80

# Create env
.PHONY: env
env:
	pip install -r requirements.txt

# Create superuser
.PHONY: admin
admin:
	python manage.py shell -c "from django.contrib.auth.models import User; \
	User.objects.filter(username='admin').exists() or \
	User.objects.create_superuser('admin', 'admin@example.com', 'admin')"

	
# Create new app
ifeq (app,$(firstword $(MAKECMDGOALS)))
  ARGS := $(wordlist 2,$(words $(MAKECMDGOALS)),$(MAKECMDGOALS))
  $(eval $(ARGS):;@:)
endif

.PHONY: app
app:
	mkdir apps\$(ARGS)
	django-admin startapp $(ARGS) apps\$(ARGS)
	echo from configs.settings import INSTALLED_APPS > apps\$(ARGS)\settings.py
	echo. >> apps\$(ARGS)\settings.py
	echo INSTALLED_APPS += ['$(ARGS)',] >> apps\$(ARGS)\settings.py

# Push
.PHONY: git
git:
	git add .
	git commit -m up
	git push
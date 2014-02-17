gogame-newsite-rebuild
======================

A simplified rebuild of the gogame-newsite

#### Setup
    mkdir site
    cd site
    virtualenv --distribute --no-site-packages env
    source env/bin/activate
    git clone git@github.com:orInge/gogame-newsite-rebuild.git project
    pip install -U -r main/requirements.txt
    cd project

#### temporary example db
    python manage.py createdb
    # follow instructions to create a superuser
    # specify 'rebuild:8000' for domain:port
    # opt to install demo pages (yes)

#### collecttemplates
    python manage.py collecttemplates
    # copies all mezzanine default templates into project dir
    mv templates ../templates
    # move out of project dir so as to not override app/templates
    # copy individually to app/templates and modify as needed

#### run dev server
    python manage.py runserver
    visit http://127.0.0.1:8000


#### collectstatic (for deploy)
    # collects to STATIC_ROOT as defined in local_settings.py or settings.py
    python manage.py collectstatic


#### bpython (optional)
    pip install bpython
    bpython manage.py shell

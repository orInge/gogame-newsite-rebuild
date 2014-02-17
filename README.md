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

#### run dev server
    python manage.py runserver
    visit http://127.0.0.1:8000


#### collect static assets & templates
    python manage.py collectstatic


#### bpython (optional)
    pip install bpython
    bpython manage.py shell

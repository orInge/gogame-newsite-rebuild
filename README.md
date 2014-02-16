gogame-newsite-rebuild
======================

A simplified rebuild of the gogame-newsite

#### Setup

    mkdir site
    cd site
    git clone git@github.com:orInge/gogame-newsite-rebuild.git main
    virtualenv --distribute --no-site-packages env
    source env/bin/activate
    pip install -U -r main/requirements.txt
    cd main
    python manage.py runserver
    visit http://127.0.0.1:8000


#### collect static assets & templates
    python manage.py collectstatic


#### bpython (optional)
    pip install bpython
    bpython manage.py shell

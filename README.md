gogame-newsite-rebuild
======================

A simplified rebuild of the gogame-newsite

### Setup

    mkdir site
    cd site
    virtualenv --distribute --no-site-packages env
    source env/bin/activate
    pip install -U -r requirements.txt

    git clone git@github.com:orInge/gogame-newsite-rebuild.git main
    cd main
    python manage.py runserver
    visit http://127.0.0.1:8000

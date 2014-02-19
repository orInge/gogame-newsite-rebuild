gogame-newsite-rebuild
======================

From the ground up

v0.3

#### Setup
    mkdir site
    cd site
    virtualenv --distribute --no-site-packages env
    source env/bin/activate
    git clone git@github.com:orInge/gogame-newsite-rebuild.git project
    pip install -U -r main/requirements.txt
    cd project


#### Temporary sqlite example db
    python manage.py createdb
    # follow instructions to create a superuser
    # use default domain:port
    # opt to install demo pages (yes)
#### Run dev server
    python manage.py runserver
    visit http://127.0.0.1:8000


#### Create mySQL database
    
    # log in to mysql shell as root
    mysql -uroot
    
        (in mysql shell)
        create database newsite_rebuild default character set utf8 collate utf8_general_ci;
        use newsite_rebuild;
        create user 'admin'@'localhost' identified by 'admin';
        grant all privileges on newsite_rebuild.* to 'admin'@'localhost';
        quit;

    python manage.py syncdb
        username: admin
        email: info@thegogame.com
        password: admin
        Site record: 'localhost:8000'  (include quotes)

#### run gunicorn wsgi server
    python manage.py run_gunicorn
    visit http://localhost:8000


#### collecttemplates
    python manage.py collecttemplates
    # copies all mezzanine default templates into project dir
    mv templates ../templates
    # move out of project dir so as to not override app/templates
    # copy individually to app/templates and modify as needed

#### collectstatic 
    # collects to STATIC_ROOT 
    python manage.py collectstatic


#### bpython (optional)
    pip install bpython
    bpython manage.py shell

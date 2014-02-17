from django_assets import Bundle, register

# js = Bundle('common/jquery.js', 'site/base.js', 'site/widgets.js',
#             filters='jsmin', output='gen/packed.js')
# register('js_all', js)

app_sass = Bundle(
    'sass/style.scss',
    filters='scss',
    output='gen/style.css')
register('app_sass', app_sass)

# bootstrap_sass = Bundle(
#     'sass/bootstrap.scss',
#     filters='scss',
#     output='gen/bootstrap.css')
# register('bootstrap_sass', bootstrap_sass)
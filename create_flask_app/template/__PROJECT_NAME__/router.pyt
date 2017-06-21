from ${{ PROJECT_NAME }} import app
from ${{ PROJECT_NAME }}.controller import index


app.add_url_rule('/', 'index', index)

from app import app

@app.route('/')
def index():
    return '<h1>It works!</h1>'

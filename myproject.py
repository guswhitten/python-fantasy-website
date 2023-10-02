from flask import Flask
from views import views
import os

app = Flask(__name__)
app.register_blueprint(views, url_prefix="/")

port = int(os.environ.get('PORT', 8000))
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=port)
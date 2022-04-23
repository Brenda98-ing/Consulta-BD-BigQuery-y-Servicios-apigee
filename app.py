from flask import request, jsonify, Blueprint
from flask import Flask
from datetime import datetime
from resources.paths import v

app = Flask(__name__)

#

app.register_blueprint(v)


if __name__ == '__main__':
    app.run(debug=True)     # Para que el archivo corra
    


# Para pasar datos a url se usan argumentoss
# En método put http://127.0.0.1:5000/tasks?id=2
from flask import Flask, make_response, jsonify, request, Blueprint
from utilities.credentials import Credential
from services.generate_2fa import Generate2FA

app = Flask(__name__)

api_name = '/api'

auth = Blueprint('auth', __name__, url_prefix=f'{api_name}/auth')

def create_app():
    app.register_blueprint(auth)

@app.route('/', methods=['GET'])
def route_root():
    response = dict(
        ApiName='/api',
        AppName='2FA Flask APP',
        Description='Aplicación DEMO - 2FA Python Flask',
        Port=5000
    )
    return make_response(jsonify(response), 200)

@auth.route('/login/', methods=['POST'])
def login():
    data = request.json
    response, status_code = Credential.verify_user(data=data)
    return make_response(jsonify(response), status_code)

@auth.route('/authenticate/2fa/', methods=['POST'])
def authenticate_2fa():
    data = request.json
    response, status_code = Generate2FA.verify(data=data)
    return make_response(jsonify(response), status_code)

@auth.route('/generate/qrcode/', methods=['POST'])
def generate_qrcode():
    data = request.json
    response, status_code = Generate2FA.generated_qrcode(data=data)
    return make_response(jsonify(response), status_code)

@auth.route('/2fa/activated/', methods=['POST'])
def activated_2fa():
    data = request.json
    response, status_code = Generate2FA.activated(data=data)
    return make_response(jsonify(response), status_code)


create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
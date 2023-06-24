import pyotp
from utilities.credentials import Credential
from .qrcode_generate import QRCode


class Generate2FA:
    # Generar una KEY (32 caracteres)
    # __KEY = pyotp.random_base32()
    __KEY = 'ApplicationPythonFlask2FATesting'
    
    @staticmethod
    def activated(data: dict):
        _exist = Credential.activated_2fa(username=data['username'])
        if not _exist:
            return {
                'message': 'username not found!'
            }, 404
        uri = pyotp.totp.TOTP(Generate2FA.__KEY).provisioning_uri(name=data['username'],
                                                                  issuer_name='2FA Flask APP')
        QRCode.generate_qrcode(uri=uri, username=data['username'])
        return {'ok': 'Doble autenticación se encuentra activa.'}, 200
    
    @staticmethod
    def generated_qrcode(data: dict):
        resp = Credential.validate_username(username=data['username'])
        if not resp:
            return {'message': 'El usuario no tiene habilitado la autenticación 2FA'}, 400
        uri = pyotp.totp.TOTP(Generate2FA.__KEY).provisioning_uri(name=data['username'],
                                                                  issuer_name='2FA Flask APP')
        QRCode.generate_qrcode(uri=uri, username=data['username'])
        return {'ok': 'Se generó el QRCODE de manera correcta.'}, 200
    
    @staticmethod
    def verify(data: dict):
        code = '000000' if not 'code' in data else data['code']
        totp = pyotp.TOTP(Generate2FA.__KEY)
        try:
            if totp.verify(code):
                return {
                    'message': 'Has iniciado sesión con 2FA'
                }, 200
            else:
                return {
                    'message': 'Code no valid!'
                }, 403
        except Exception as e:
            print(e)
            return {
                    'message': 'Error al tratar de verificar el código!'
                }, 500


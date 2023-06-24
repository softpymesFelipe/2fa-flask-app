import qrcode

class QRCode:
    
    @staticmethod
    def generate_qrcode(uri: str, username: str):
        qrcode.make(uri).save(f'{username}_2fa_flask.png')

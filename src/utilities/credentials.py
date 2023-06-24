
class Credential:
    
    __USERNAMES = [
        {'username': 'chelispipe', 'password': 'Admin*5', '2FA': False}, 
        {'username': 'laquiceno', 'password': 'Sofia81', '2FA': False}
    ]
    
    @staticmethod
    def verify_user(data: dict):
        is_valid = validate_properties(data=data)
        if not 'ok' in is_valid:
            return is_valid
        _2fa = ''
        _is_ok = False
        for user in Credential.__USERNAMES:
            if data['username'] == user['username'] and data['password'] == user['password']:
                if not user['2FA']:
                    _2fa = ', ¿desea activar la autenticación doble factor 2FA?'
                _is_ok = True
                break
        if _is_ok:
            return {
                'message': f'Bienvenido, {data["username"]}{_2fa}'
            }, 200
        else:
            return {
                'message': 'Los datos ingresados no son correctos.',
            }, 403
    
    @staticmethod
    def activated_2fa(username: str):
        exist = False
        for user in Credential.__USERNAMES:
            if username == user['username']:
                user['2FA'] = True
                exist = True
                break
        
        return exist
    
    @staticmethod
    def validate_username(username: str):
        result = False
        for user in Credential.__USERNAMES:
            if username == user['username'] and user['2FA']:
                result = True
                break
        return result
        
    
def validate_properties(data: dict):
    __is_error = False
    if not 'username' in data or not 'password' in data:
        __is_error = True
    
    if __is_error:
        return {
            'message': 'params invalid!',
        }, 400
    else:
        return {'ok': True}
    



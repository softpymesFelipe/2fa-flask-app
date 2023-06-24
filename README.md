# Application Python Flask - 2FA

```Proyecto educativo``` El objetivo de esta API, es el poder simular el inicio de sesión teniendo en cuenta la doble autenticación 2FA, con el fin de enseñar el uso de la misma  desde el backend.

## Requisitos

- Python
- virtualenv
- Aplicación autenticación 2FA

## Construir el proyecto

1. Obtener una copia del reporsitorio
2. Crear el entorno virtual ```python -m venv venv```
3. Instalar las dependencias ```pip install -r  requirements.txt```

## Ejecutar el proyecto

En el archivo ```run.py``` ubicarse en la parte final del archivo, se encontrará la siguiente linea:
```python
app.run(host='0.0.0.0', port=5000, debug=True)
```
Si se desea se puede cambiar el valor del puerto y cambiar el ```True``` por ```False``` en caso que se desee tener una ejecucón sin el modo ```DEBUG``` activo.

## Uso del API

Para utilizar el API, se debe tener en cuenta que se cuenta con una petición ```GET``` y todas las demás son ```POST```

### Obtener información  del API

Hacer el llamado a la ruta raíz

```bash
http://localhost:5000/
```

para utilizar los demás servicios, se debe tener en cuenta el **APINAME** ```api/``` y para el caso de los servicios a utilizar se debe concatenar el **NAME** ```auth/``` quedando de la siguiente forma:

- ```http://localhost:5000/api/auth/login/``` Este servicio ```POST``` es el tradicional inicio de sesión usuario y contraseña, se debe enviar el siguiente body:

```json
{
    "username": "chelispipe",
    "password": "Admin*5"
}
``` 

- ```http://localhost:5000/api/auth/2fa/activated/``` Este servicio ```POST``` permite activar a los usuarios la generación del QRCODE para la autenticación 2FA y genera el código QR en formato PNG, se debe enviar el siguiente body:

```json
{
    "username": "chelispipe"
}
``` 

- ```http://localhost:5000/api/auth/generate/qrcode/``` Este servicio ```POST``` permite generar el QRCODE en formato PNG solamente si el usuario ya está activo para esta autenticación, se debe enviar el siguiente body:

```json
{
    "username": "chelispipe"
}
``` 

- ```http://localhost:5000/api/auth/authenticate/2fa/``` Este servicio ```POST``` permite validar el código generado por alguna aplicación de autenticación 2FA, se debe enviar el siguiente body:

```json
{
    "code": "123456"
}
``` 

# Desarrollado por

- Felipe Medel
- luispipemedel@gmail.com

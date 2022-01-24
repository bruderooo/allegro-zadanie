import argparse

from flask import Flask

from apis import api

app = Flask(__name__)
app.config.SWAGGER_SUPPORTED_SUBMIT_METHODS = ["get"]
api.init_app(app)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Uruchamia aplikację API stworzoną na zaliczenie zadania.')
    parser.add_argument('--ip', dest='ip', default='127.0.0.1',
                        help='Adres IP do uruchomienia serwera (domyślnie przyjmuje adres 127.0.0.1)')
    parser.add_argument('--port', dest='port', default='5000',
                        help='Port na którym ma działać serwer (domyślnie przyjmuje port 5000)')
    args = parser.parse_args()

    app.run(host=args.ip, port=args.port)

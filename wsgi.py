#
# Aquest fitxer el busca automaticament la comanda flask run
#
from wannapop import create_app

create_app()

# if __name__ == "__main__":
#     app.run(host="127.0.0.1", port=5000, debug=True)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)  # Aunque esta línea no se usará con Gunicorn, es buena práctica definirla.

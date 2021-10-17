import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or\
        b'\xa5\x8b.\x95}\xc9\xcf\xfc\xe3&\x8f,3\xf1\x9cd'


# python -c "import os; print(os.urandom(16))" imprime clave

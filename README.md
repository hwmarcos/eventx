# Eventx

Sistema de eventos

## Como desenvolver

1. Clone o repositótio
2. Crie um virtualenv com Python 3.5
3. Ative o virtualenv
4. Instale as dependências
5. Configure a instância com o .env
6. Execute os testes

```console
git clone git@github.com:hwmarcos/eventx.git wttd
cd wttd
python -m venv .wttd
source .wttd/bin/activate
pip install -r requirements.txt
cp contrib/env-sample .env
python manage.py test
```

## Como fazer o deply

1. Crie uma instância do heroku
2. Envie as configurações para heroku
3. Define uma SECRET_KEY segura para a instância
4. Define DEBUG=False
5. Configure um serviço de e-maio
6. Envie o código para o heroku

```console
heroku create minhainstancia
heroku config:push
heroku config:set SECRET_KEY:`python contrib/secret_gen.py`
heroku config:set DEBUG:False
# configuro o email
git push heroku master --force
```
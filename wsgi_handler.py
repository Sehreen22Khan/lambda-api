# wsgi_handler.py
from mangum import Mangum
from app import app  # assuming your provided Flask code is in app.py
handler = Mangum(app)
def lambda_handler(event, context):
    return handler(event, context)

from flask_restful import Api
from .controllers import AccountListResource, AccountResource

def register_routes(api: Api):
    api.add_resource(AccountListResource, '/accounts')
    api.add_resource(AccountResource, '/accounts/<string:account_id>')

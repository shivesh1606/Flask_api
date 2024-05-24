from flask import request, jsonify
from flask_restful import Resource
import uuid
from datetime import datetime
from .. import db
from .models import Account
from flask import Response

from sqlalchemy.sql import text
from sqlalchemy import inspect


def check_sort_list(sort):
    sort_list = ['id', 'first_name', 'last_name', 'company', 'age', 'city', 'state', 'zip', 'email', 'web', 'created', 'updated']
    if sort not in sort_list:
        return False
    return True
class AccountListResource(Resource):
    def get(self):
        page = int(request.args.get('page', 1))
        limit = int(request.args.get('limit', 5))
        search = request.args.get('search', '')
        sort = request.args.get('sort', '')

        query = Account.query

        # Search functionality
        if search:
            search = f"%{search}%"
            query = query.filter((Account.first_name.ilike(search)) | (Account.last_name.ilike(search)))
        
        # Sorting functionality
        if sort:
            if sort.startswith('-'):
                sort_field = sort[1:]
                print(sort_field)
                if check_sort_list( sort_field):
                    query = query.order_by(text(f"{sort_field} desc"))
                else:
                    return jsonify({"error": f"Invalid sort field: {sort}"})

            else:
                if check_sort_list(sort):
                    query = query.order_by(text(f"{sort} asc"))
                else:
                    return jsonify({"error": f"Invalid sort field: {sort}"})

        # Pagination functionality
        paginated_query = query.paginate(page=page, per_page=limit, error_out=False)

        accounts = paginated_query.items

        response = [account.toDict() for account in accounts]

        # Removing 'created' and 'updated' fields from the response
        for account in response:
            del account['created']
            del account['updated']
        next_page = paginated_query.next_num if paginated_query.has_next else None
        # response.append({'next_page': next_page})
        data={}
        data['next_page'] = next_page
        data['total'] = paginated_query.total
        # next_page_link
        if next_page:
            data['next_page_link'] = f"{request.base_url}?page={next_page}&limit={limit}&search={search}&sort={sort}"
        else:
            data['next_page_link'] = None

        data['accounts'] = response
 
        return jsonify(data)  # Convert response to JSON format

    def post(self):
        request_data = {**request.form.to_dict(), **request.args.to_dict()}
        
        required_fields = ['first_name', 'last_name', 'email']
        for field in required_fields:
            if field not in request_data:
                return jsonify({"error": f"Missing required field: {field}"}), 400
        
        id = str(uuid.uuid4())
        new_account = Account(
            id=id,
            first_name=request_data['first_name'],
            last_name=request_data['last_name'],
            company=request_data.get('company', ''),
            age=int(request_data.get('age', 0)),
            city=request_data.get('city', ''),
            state=request_data.get('state', ''),
            zip=request_data.get('zip', ''),
            email=request_data['email'],
            web=request_data.get('web', '')
        )
        
        db.session.add(new_account)
        db.session.commit()
        
        response = Account.query.get(id).toDict()
        return jsonify(response)

class AccountResource(Resource):
    def get(self, account_id):
        account = Account.query.get(account_id)
        if account:
            response = account.toDict()
            return jsonify(response)
        return jsonify({"error": "Account not found"}), 404
    
    def put(self, account_id):
        request_data = {**request.form.to_dict(), **request.args.to_dict()}
        account = Account.query.get(account_id)
        
        if account:
            # Update only the fields that are present in the request data
            if 'first_name' in request_data:
                account.first_name = request_data['first_name']
            if 'last_name' in request_data:
                account.last_name = request_data['last_name']
            if 'company' in request_data:
                account.company = request_data.get('company', '')
            if 'age' in request_data:
                account.age = int(request_data.get('age', 0))
            if 'city' in request_data:
                account.city = request_data.get('city', '')
            if 'state' in request_data:
                account.state = request_data.get('state', '')
            if 'zip' in request_data:
                account.zip = request_data.get('zip', '')
            if 'email' in request_data:
                account.email = request_data['email']
            if 'web' in request_data:
                account.web = request_data.get('web', '')
            account.updated = datetime.now()
            
            db.session.commit()
            
            response = account.toDict()
            return jsonify(response)
        return jsonify({"error": "Account not found"}), 404
    
    def delete(self, account_id):
        account = Account.query.filter_by(id=account_id).first()
        if account:
            db.session.delete(account)
            db.session.commit()
            return jsonify({"message": f"Account with Id \"{account_id}\" deleted successfully!"})
        return jsonify({"error": "Account not found"}), 404

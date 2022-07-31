from flask import Flask, request, jsonify
from flask_cors import CORS

from .auth.auth import AuthError, requires_auth
from .database.models import setup_db, Drink, db_drop_and_create_all
from .services.drink_service import create_drink_or_abort, update_drink_or_abort, \
    delete_drink_or_abort
from .utils.validator import validate, partial_validate
from .utils.validator_response import json_abort_422

app = Flask(__name__)
# app.config['AUTH0_DOMAIN'] = 'dev-0mmekwpe.us.auth0.com'
# app.config['ALGORITHMS'] = ['RS256']
# app.config['API_AUDIENCE'] = 'coffees'
setup_db(app)
CORS(app)

'''
@TODO uncomment the following line to initialize the datbase
!! NOTE THIS WILL DROP ALL RECORDS AND START YOUR DB FROM SCRATCH
!! NOTE THIS MUST BE UNCOMMENTED ON FIRST RUN
!! Running this function will add one
'''
# db_drop_and_create_all()

# ROUTES
'''
@TODO implement endpoint
    GET /drinks
        it should be a public endpoint
        it should contain only the drink.short() data representation
    returns status code 200 and json {"success": True, "drinks": drinks} where drinks is the list of drinks
        or appropriate status code indicating reason for failure
'''


@app.route('/api/drinks', methods=['GET'])
def get_short_drinks():
    return jsonify({
        'success': True,
        'drinks': [drink.short() for drink in Drink.query.all()]
    })


'''
@TODO implement endpoint
    POST /drinks
        it should create a new row in the drinks table
        it should require the 'post:drinks' permission
        it should contain the drink.long() data representation
    returns status code 200 and json {"success": True, "drinks": drink} where drink anes the created drink
        or appropriate status code indicating reason for failure
'''


@app.route('/api/drinks', methods=['POST'])
@requires_auth('post:drinks')
def create_drink(payload):
    body = request.get_json()

    # validate request body data
    violations = validate(body, ['title', 'recipe'])

    # if there are violations, abort 422 error
    if len(violations) > 0:
        return json_abort_422('Invalid request body', violations)

    # here, we're sure that the request body is valid
    drink = create_drink_or_abort(body)

    return jsonify({
        'success': True,
        'drink': drink.long()
    })


'''
@TODO implement endpoint
    GET /drinks-detail
        it should require the 'get:drinks-detail' permission
        it should contain the drink.long() data representation
    returns status code 200 and json {"success": True, "drinks": drinks} where drinks is the list of drinks
        or appropriate status code indicating reason for failure
'''


@app.route('/api/drinks-detail', methods=['GET'])
@requires_auth('get:drinks-detail')
def get_drinks_detail(payload):
    return jsonify({
        'success': True,
        'drinks': [drink.long() for drink in Drink.query.all()]
    })


'''
@TODO implement endpoint
    PATCH /drinks/<drink_id>
        where <drink_id> is the existing model drink_id
        it should respond with a 404 error if <drink_id> is not found
        it should update the corresponding row for <drink_id>
        it should require the 'patch:drinks' permission
        it should contain the drink.long() data representation
    returns status code 200 and json {"success": True, "drinks": drink} where drink an array containing only the updated drink
        or appropriate status code indicating reason for failure
'''


@app.route('/api/drinks/<int:drink_id>', methods=['PATCH'])
@requires_auth('patch:drinks')
def update_drink(payload, drink_id):
    # here, we're sure that the drink exists
    body = request.get_json()

    # validate request body data
    violations = partial_validate(body, ['title', 'recipe'])

    # if there are violations, abort 422 error
    if len(violations) > 0:
        return json_abort_422('Invalid request body', violations)

    # here, we're sure that the request body is valid
    drink_long = update_drink_or_abort(drink_id, body)

    return jsonify({
        'success': True,
        'drink': drink_long.long()
    })


'''
@TODO implement endpoint
    DELETE /drinks/<drink_id>
        where <drink_id> is the existing model drink_id
        it should respond with a 404 error if <drink_id> is not found
        it should delete the corresponding row for <drink_id>
        it should require the 'delete:drinks' permission
    returns status code 200 and json {"success": True, "delete": drink_id} where drink_id is the drink_id of the deleted record
        or appropriate status code indicating reason for failure
'''


@app.route('/api/drinks/<int:drink_id>', methods=['DELETE'])
@requires_auth('delete:drinks')
def delete_drink(payload, drink_id):
    delete_drink_or_abort(drink_id)
    return jsonify({
        'success': True,
        'delete': drink_id
    })


# Error Handling

'''
@TODO implement error handlers using the @app.errorhandler(error) decorator
    each error handler should return (with appropriate messages):
             jsonify({
                    "success": False,
                    "error": 404,
                    "message": "resource not found"
                    }), 404

'''


@app.errorhandler(401)
def unauthorized(error):
    return jsonify({
        "success": False,
        "error": 401,
        "message": error.description if 'description' in dir(error) else 'Forbidden'
    }), 401


@app.errorhandler(403)
def forbidden(error):
    return jsonify({
        "success": False,
        "error": 403,
        "message": error.description if 'description' in dir(error) else 'Forbidden'
    }), 403


@app.errorhandler(404)
def not_found(error):
    return jsonify({
        "success": False,
        "error": 404,
        "message": "resource not found"
    }), 404


'''
@TODO implement error handler for 404
    error handler should conform to general task above
'''


@app.errorhandler(400)
def bad_request(error):
    return jsonify({
        "success": False,
        "error": 400,
        "message": "Bad request"
    }), 400


'''
Example error handling for unprocessable entity
'''


@app.errorhandler(422)
def unprocessable(error):
    return jsonify({
        "success": False,
        "error": 422,
        "message": "Unprocessable entity"
    }), 422


@app.errorhandler(500)
def server_error(error):
    return jsonify({
        "success": False,
        "error": 500,
        "message": "server error"
    }), 500


'''
@TODO implement error handler for AuthError
    error handler should conform to general task above
'''


@app.errorhandler(AuthError)
def auth_error(error):
    return jsonify({
        "success": False,
        "error": error.status_code,
        "message": error.error['description']
    }), error.status_code

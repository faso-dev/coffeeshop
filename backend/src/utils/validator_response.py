from flask import jsonify, abort

"""
Custom json error handler for 422 errors.
This function is used to create a custom error response for 422 errors with the failed validation violations.
"""


def json_abort_422(error, violations=None):
    """
    Create a JSON error response.
    """
    return jsonify({
        'success': False,
        'error': error,
        'message': 'Unprocessable Entity',
        'violations': violations
    }), 422

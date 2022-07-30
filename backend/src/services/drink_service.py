import json

from flask import abort

from ..database.models import Drink


def create_drink_or_abort(data):
    """
    Create a new drink.
    """
    try:
        drink = Drink(
            title=data['title'],
            recipe=json.dumps(data['recipe'])
        )
        drink.insert()
        return drink
    except Exception as e:
        print(e)
        abort(500)


def get_drink_or_abort_not_found(drink_id):
    """
    Get a drink by id.
    """
    return Drink.query.get_or_404(drink_id)


def update_drink_or_abort(drink_id, data):
    """
    Update a drink.
    """
    drink = get_drink_or_abort_not_found(drink_id)

    try:
        if 'title' in data:
            drink.title = data['title']
        if 'recipe' in data and len(data['recipe']) > 0:
            drink.recipe = json.dumps(data['recipe'])
        drink.update()
        return drink
    except Exception as e:
        print(e)
        abort(500)


def delete_drink_or_abort(drink_id):
    """
    Delete a drink.
    """
    drink = get_drink_or_abort_not_found(drink_id)
    try:
        drink.delete()
    except Exception as e:
        print(e)
        abort(500)

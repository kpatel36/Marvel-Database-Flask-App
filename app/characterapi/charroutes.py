from flask import Blueprint, jsonify, request, render_template,redirect

from app.models import User, db, Character

api = Blueprint('api', __name__, url_prefix='/api')

# route for getting all characters
@api.route('/characters',methods=['GET'])
def getCharacters():
    """
    [GET] return json data on all characters in our database
    """
    characters =[a.to_dict() for a in Character.query.all()]
    return jsonify(characters)

# route for getting one character
@api.route('/characters/name/<string:name>', methods = ['GET'])
def getCharacter(name):
    """
    [GET] that accepts series name jthrough url and either gets series in our database or returns that we dont have that series in our database
    """
    name = Character.query.filter_by(name=name.title()).first()
    if name:
        return jsonify(name.to_dict()),200
    else:
        return jsonify({'Request failed': 'No character with that name in our database'}),404

# route for creating a new character
@api.route('/create/character', methods=['POST'])
def create_character():
    """
    [POST] creates new char in our db with data provided in the request body expected data format:
    expected dict structure:
    {
        'name': <str>,
        'description':<str>
        'comics_number':<int>
        'superpower':<str>
        'alias':<str>,
        'datecreated':<str>
     }
    """
    try:
        data=request.get_json()
        new_char=Character(data)
        db.session.add(new_char)
        db.session.commit()
        return jsonify({'Created': new_char.to_dict()})
    except:
        return jsonify({'Create Character Rejected': 'Character already exists in Database'})


# route for updating a character
@api.route('/character/update/<string:id>', methods=['PUT'])
def updateChar(id):
    pass


# route for deleting a character
@api.route('/character/remove/<string:id>', methods=['DELETE'])
def deleteCharacter(id):
    character = Character.query.get(id)
    if not character:
        return jsonify({'remove failed':'no characters with that name in our database'}), 404
    else:
        db.session.delete(character)
        db.session.commit()
        return jsonify({'Character Deleted from Database': character.to_dict()}), 200
    
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/persons',methods=['POST'])
def flights_create():
    body = request.get_json()
    new_flight = person_dao.Person(body['name'], body['gender'], body['dob'], body['location'])
    id = persons.insert_row(new_flight)
    person = persons.search_row(id)
    person_dict = {'id':person.id, 'name':person.name, 'gender':person.gender, 'dob':person.dob, 'location': person.location}
    return jsonify(person_dict)


@app.route('/persons/<id>',methods=['GET'])
def persons_read_by_id(id):
    person = persons.search_row(id)
    print(person)
    print(type(person))
    if person == None:
        return jsonify("flight not found")
    person_dict = {'id':person.id, 'name':person.name, 'gender':person.gender, 'dob':person.dob, 'location': person.location}
    return jsonify(person_dict)

@app.route('/persons',methods=['GET'])
def persons_read_all():
    persons_list = persons.list_all_rows()
    persons_dict = []
    for person in persons_list:
        persons_dict.append({'id':person.id, 'name':person.name, 'gender':person.gender, 'dob':person.dob, 'location': person.location})
    return jsonify(persons_dict)

@app.route('/persons/<id>',methods=['PUT'])
def persons_update(id):
    body = request.get_json()
    old_person_obj = persons.search_row(id)
    if not old_person_obj:
        return jsonify({'message': 'person not found'})
    old_person_obj.name = body['name']
    old_person_obj.gender = body['gender']
    old_person_obj.dob = body['dob']
    old_person_obj.location = body['location']
    id = body['id']
    persons.update_row(old_person_obj, id)
    person = persons.search_row(id)
    person = {'id':person.id, 'name':person.name, 'gender':person.gender, 'dob':person.dob, 'location': person.location}
    return jsonify(person_dict)

@app.route('/perosns/<id>',methods=['DELETE'])
def persons_delete(id):
    old_person_obj = persons.search_row(id)
    if not old_person_obj:
        return jsonify({'message': 'person not found', 'is_error': 1})
    delete_flight(id)
    return jsonify({'message': 'Flight is deleted', 'is_error': 0})

app.run(debug=True)
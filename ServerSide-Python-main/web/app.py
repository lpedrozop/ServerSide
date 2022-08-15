from flask import Flask, render_template, request, redirect
from flask_bootstrap import Bootstrap
from logic.person import Person

app = Flask(__name__)
bootstrap = Bootstrap(app)
model = []


@app.route("/")
def index():
    return render_template('index.html')


@app.route('/person', methods=['GET'])
def person():
    return render_template('person.html')


@app.route('/person_detail', methods=['POST'])
def person_detail():
    id_person = request.form['id_person']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    p = Person(id_person=id_person, name=first_name, last_name=last_name)
    model.append(p)
    return render_template('person_detail.html', value=p)


@app.route('/people')
def people():
    data = [(i.id_person, i.name, i.last_name) for i in model]
    print(data)
    return render_template('people.html', value=data)

@app.route('/person_delete/<string:id>')
def person_delete(id):
    for person in model:
        if person.id_person == id:
            model.remove(person)

    return redirect('/people')

@app.route('/perupdate', methods=['POST'])
def perupdate():
    for person in model:
        if person.id_person == request.form['id_person']:
            model.remove(person)

    id_person = request.form['id_person']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    p = Person(id_person=id_person, name=first_name, last_name=last_name)
    model.append(p)
    return render_template('person_detail.html', value=p)


@app.route('/person_update/<string:id>', methods=['GET'])
def person_update(id):
    data = 0
    for person in model:
        if person.id_person == id:
            data = person

    return render_template('person_update.html', data=data)





if __name__ == '__main__':
    app.run()

from pprint import pprint
from flask_app import app, render_template, redirect, request, session
from flask_app.model.dojo_model import Dojo
from flask_app.model.ninja_model import Ninja

# display all ninjas
@app.get('/ninjas')
def all_ninjas():
    ninjas = Ninja.find_all()
    print(f'**** FOUND - ALL NINJAS: ****')
    pprint(ninjas)
    return render_template('all_dojos.html', ninjas = ninjas)

# display one ninja by id
@app.get('/ninjas/<int:ninja_id>')
def one_ninja(ninja_id):
    data = {
        'id': ninja_id
    }
    ninja = Ninja.find_by_id(data)
    print(f'**** FOUND - NINJA ID: {ninja.id} ****')
    return render_template('one_ninja.html', ninja = ninja)

# display form to create a ninja
@app.get('/ninjas/new')
def new_ninja():
    dojos = Dojo.find_all()
    return render_template('new_ninja.html',dojos = dojos)

# process form and create a ninja
@app.post('/ninjas')
def create_ninja():
    ninja_id = Ninja.save(request.form)
    print(f'**** CREATED - NINJA ID: {ninja_id} ****')
    return redirect('/ninjas')

# display form to edit a ninja by id
@app.get('/ninjas/<int:ninja_id>/edit')
def edit_ninja(ninja_id):
    data = {
        'id': ninja_id
    }
    ninja = Ninja.find_by_id(data)
    print(f'**** FOUND - NINJA ID: {ninja.id} ****')
    return render_template('edit_ninja.html', ninja = ninja)

# process form and update a ninja by id
@app.post('/ninjas/<int:ninja_id>/update')
def update_ninja(ninja_id):
    Ninja.find_by_id_and_update(request.form)
    print(f'**** UPDATED - NINJA ID: {ninja_id} ****')
    return redirect(f'/ninjas/{ninja_id}')

# delete one ninja by id
@app.get('/ninjas/<int:ninja_id>/delete')
def delete_ninja(ninja_id):
    data = {
        'id': ninja_id
    }
    Ninja.find_by_id_and_delete(data)
    print(f'**** DELETED - NINJA ID: {ninja_id} ****')
    return redirect('/ninjas')
from flask import Blueprint, render_template, request
from ..models.user import User
from ..models.machine import Machine
from ..forms.new_machine_form import NewMachineForm
from ..models.exercise import ExerciseTemplate
from ..forms.new_exercise_template_form import NewExerciseTemplateForm

bp = Blueprint('admin', __name__, url_prefix='/admin')


@bp.route('/')
def admin():
    return render_template('admin/index.html')


@bp.route('/users')
def users():
    """
    This route list of all users in the database,
    and allows and admin to manage them.
    """
    users = User.query.all()
    return render_template('admin/users.html', users=users)


@bp.route('/user/<int:user_id>')
def user(user_id):
    """
    This route is used to access a specific user.
    """
    user = User.query.get(user_id)
    if user is None:
        return render_template('404.html'), 404
    return render_template('admin/user_detail.html', user=user)


@bp.route('/machines')
def machines():
    """
    This route is used to access
    the list of machines in the database.
    """
    machines = Machine.query.all()
    return render_template('admin/machines.html', machines=machines)


@bp.route('/machine/<int:machine_id>')
def machine(machine_id):
    """
    This route is used to access a specific machine.
    """
    machine = Machine.query.get(machine_id)
    if machine is None:
        return render_template('404.html'), 404
    return render_template('admin/machine_detail.html', machine=machine)


@bp.route('/machine/new', methods=['GET', 'POST'])
def new_machine():
    """
    This route is used to create a new machine.
    """
    form = NewMachineForm()
    if form.validate_on_submit():
        machine = Machine.query.filter_by(name=form.name.data).first()
        if machine is None:
            machine = Machine(
                name=form.name.data,
                description=form.description.data,
                image=form.image.data
                )
            machine.add()
            return render_template(
                'admin/machine_detail.html',
                machine=machine
                )
        else:
            pass  # DECIDE WHAT TO DO HERE
    return render_template('admin/new_machine.html', form=form)


@bp.route('/machines/api', methods=['GET', 'POST', 'PUT', 'DELETE'])
def machines_api():
    """
    This are REST API for the machines database.
    """
    update_machine = False
    form = NewMachineForm()

    if request.method == 'POST':
        machine = Machine.query.filter_by(name=form.name.data).first()
        if machine is None:
            machine = Machine(
                name=form.name.data,
                description=form.description.data,
                image=form.image.data
                )
            machine.add()
        else:
            update_machine = True
    elif request.method == 'PUT':
        update_machine = True
    elif request.method == 'DELETE':
        deleted_machine = Machine.query.filter_by(name=form.name.data).first()
        if deleted_machine is not None:
            deleted_machine.delete()
        else:
            return render_template('404.html'), 404

    if update_machine:
        machine = Machine.query.filter_by(name=form.name.data).first()
        if machine is not None:
            machine.name = form.name.data
            machine.description = form.description.data
            machine.image = form.image.data
            machine.update()
        else:
            return render_template('404.html'), 404

    machines = Machine.query.all()
    return machines


@bp.route('/exercises')
def exercises():
    """
    This route is used to access
    the list of exercises templates in the database.
    """
    exercises = ExerciseTemplate.query.all()
    return render_template('admin/exercises.html', exercises=exercises)


@bp.route('/exercise/<int:exercise_id>')
def exercise(exercise_id):
    """
    This route is used to access a specific exercise template.
    """
    exercise = ExerciseTemplate.query.get(exercise_id)
    if exercise is None:
        return render_template('404.html'), 404
    return render_template('admin/exercise_detail.html', exercise=exercise)


@bp.route('/excercise/new', methods=['GET', 'POST'])
def new_exercise():
    """
    This route is used to create a new exercise template.
    """
    form = NewExerciseTemplateForm()
    if form.validate_on_submit():
        exercise = ExerciseTemplate.query.filter_by(
            name=form.name.data
            ).first()
        if exercise is None:
            exercise = ExerciseTemplate(
                name=form.name.data,
                description=form.description.data,
                image=form.image.data
                )
            exercise.add()
            return render_template(
                'admin/exercise_detail.html',
                exercise=exercise
                )
        else:
            pass  # DECIDE WHAT TO DO HERE
    return render_template('admin/new_exercise.html', form=form)


@bp.route('/exercises/api', methods=['GET', 'POST', 'PUT', 'DELETE'])
def exercises_api():
    """
    This are REST API for the exercises database.
    """
    update_exercise = False
    form = NewExerciseTemplateForm()

    if request.method == 'POST':
        exercise = ExerciseTemplate.query.filter_by(
            name=form.name.data
            ).first()
        if exercise is None:
            exercise = ExerciseTemplate(
                name=form.name.data,
                description=form.description.data,
                image=form.image.data
                )
            exercise.add()
        else:
            update_exercise = True
    elif request.method == 'PUT':
        update_exercise = True
    elif request.method == 'DELETE':
        deleted_exercise = ExerciseTemplate.query.filter_by(
            name=form.name.data
            ).first()
        if deleted_exercise is not None:
            deleted_exercise.delete()
        else:
            return render_template('404.html'), 404

    if update_exercise:
        exercise = ExerciseTemplate.query.filter_by(
            name=form.name.data
            ).first()
        if exercise is not None:
            exercise.name = form.name.data
            exercise.description = form.description.data
            exercise.image = form.image.data
            exercise.update()
        else:
            return render_template('404.html'), 404

    exercises = ExerciseTemplate.query.all()
    return exercises

from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from services.note_service import NoteService, NoteDeleteService

note_controller = Blueprint('note_controller', __name__)


@note_controller.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        note_data = request.form.get('note')
        success, message = NoteService.add_note(note_data)
        if not success:
            flash(message, category='error')
        else:
            flash(message, category='success')

    return render_template("home.html", user=current_user)


@note_controller.route('/delete-note/<int:note_id>', methods=['POST'])
@login_required
def delete_note(note_id):
    success, message = NoteDeleteService.delete_note(note_id)
    if not success:
        flash(message, category='error')
    else:
        flash(message, category='success')
    return redirect(url_for('note_controller.home'))

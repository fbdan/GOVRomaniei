from flask import request, url_for,render_template
from flask.ext.api import FlaskAPI, status, exceptions

#static and templates folders

app = FlaskAPI(__name__)


notes = {
    0: 'Executori judecatoresti',
    1: 'Traducatori avizati',
    2: 'TODO',
    3: 'Parc Auto',
    4: 'Informatii diverse',
    5: 'TODO NEXT',
}

def note_repr(key):
    return {
        'url': request.host_url.rstrip('/') + url_for('notes_detail', key=key),
        'text': notes[key]
    }


@app.route("/", methods=['GET', 'POST'])
def notes_list():
    """
    List or create notes
    """
    if request.method == 'POST':
        note = str(request.data.get('text', ''))
        idx = max(notes.keys()) + 1
        notes[idx] = note
        return note_repr(idx), status.HTTP_201_CREATED

    else:
        request.method == 'GET'
        return [note_repr(idx) for idx in sorted(notes.keys())]


@app.route("/<int:key>/", methods=['GET', 'PUT', 'DELETE'])
def notes_detail(key):
    """
    Retrieve, update or delete note instances.
    """
    if request.method == 'PUT':
        note = str(request.data.get('text', ''))
        notes[key] = note
        return note_repr(key)

    elif request.method == 'DELETE':
        notes.pop(key, None)
        return '', status.HTTP_204_NO_CONTENT

    # request.method == 'GET'
    if key not in notes:
        raise exceptions.NotFound()
    return note_repr(key)

@app.route("/index", methods = ["GET","POST"])
def index():
    if request.method == "GET":
        return "<h2>proiectepebune.ro</h2>"
    else:
        return "Acum probabil folosesti metoda POST"

@app.route("/profile/<name>")
def profile(name):
    return render_template("profile.html", name=name)



if __name__ == "__main__":
    app.run(debug=True)

from app import db, app
from app.models import Grocery

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Grocery': Grocery}

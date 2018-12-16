from app import create_app, db
from app.models.user import User
from app.models.cdr import Cdr
import click

app = create_app()

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Cdr': Cdr}

@app.cli.command(with_appcontext=False)
def initdb():
    """Initialize the database."""
    # Flask pushes an application context, which brings current_app and g to life.
    # When the request is complete, the context is removed, along with these variables
    app.app_context().push()
    u = User(username='admin@alochym.com', role='admin')
    u.set_password('password')
    try:
        db.session.add(u)
        db.session.commit()
        click.echo('Create User/Password successful with admin/password')
    except Exception as e:
        pass
        print(str(e))
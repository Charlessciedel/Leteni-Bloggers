# Import db from app factory
from app import create_app
from app import db
from flask_script import Manager,Server
# Connect to models
from app.models import User,Blog,Comment
# Set up migrations
from flask_migrate import Migrate,MigrateCommand

# Creating app instance
# app = create_app('test')
# app = create_app('development')
app = create_app('production')


# Create manager instance 
manager = Manager(app)

# Create migrate instance
migrate = Migrate(app,db)

manager.add_command('server',Server)
manager.add_command('db',MigrateCommand)

@manager.command
def test():
    '''
    Run the unit tests
    '''
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


@manager.shell
def make_shell_context():
    return dict( app=app, db=db, User=User, Review=Review, Role=Role)


# # if __name__ == '__main__':
#     # manager.run()# Import db from app factory
# from app import create_app
# from flask_script import Manager,Server
# # Connect to models
# from app.models import User,Blog,Comment
# # Set up migrations
# from flask_migrate import Migrate,MigrateCommand

# # Creating app instance
# # app = create_app('test')
# # app = create_app('development')
# app = create_app('production')


# # Create manager instance 
# manager = Manager(app)

# # Create migrate instance
# migrate = Migrate(app,db)

# manager.add_command('server',Server)
# manager.add_command('db',MigrateCommand)

# @manager.command
# def test():
#     '''
#     Run the unit tests
#     '''
#     import unittest
#     tests = unittest.TestLoader().discover('tests')
#     unittest.TextTestRunner(verbosity=2).run(tests)


# @manager.shell
# def make_shell_context():
#     return dict( app=app, db=db, User=User, Comment=Comment, Blog=Blog)


if __name__ == '__main__':
#     app.secret_key = 'qwerty12345' 
    manager.run()
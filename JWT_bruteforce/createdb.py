from application import db, app

# Create tables within the app context
with app.app_context():
    db.create_all()

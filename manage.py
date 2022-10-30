from app import app,db


if __name__ == '__main__':
    db.create_all()
    from app.views import *
    app.run(debug=True)
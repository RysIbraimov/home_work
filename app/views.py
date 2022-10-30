from flask import render_template,request,redirect,url_for
from .models import Transactions
from . import app,db

@app.route('/view')
def get_trans():
    transaction = Transactions.query.all()
    return render_template('transaction.html',transaction=transaction)

@app.route('/create')
def add_trans():
    value = request.args.get('value')
    status = request.args.get('status')
    unit = request.args.get('unit')
    comment = request.args.get('comment')
    if value and status and unit and comment:
        new_transacion = Transactions(value=value,status=status,unit=unit,comment=comment)
        db.session.add(new_transacion)
        db.session.commit()
        return redirect(url_for('get_trans'))
    transaction = Transactions.query.all()
    return render_template('add_trans.html',transaction=transaction)





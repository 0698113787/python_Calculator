from flask import Flask, render_template, request, session
import math
import os

app = Flask(__name__)
app.secret_key = 'Ntshangase@2010'  # Change this to a random secret key

@app.route('/', methods=['GET', 'POST'])
def calculator():
    if 'display' not in session:
        session['display'] = '0'
        session['history'] = ''
    
    if request.method == 'POST':
        action = request.form.get('action')
        
        if action == 'clear':
            session['display'] = '0'
            session['history'] = ''
        
        elif action == 'delete':
            if len(session['display']) > 1:
                session['display'] = session['display'][:-1]
            else:
                session['display'] = '0'
        
        elif action == 'append':
            value = request.form.get('value')
            if session['display'] == '0' and value not in ['+', '-', '*', '/', '%', '.']:
                session['display'] = value
            else:
                session['display'] += value
        
        elif action == 'calculate':
            try:
                expression = session['display']
                # Replace display symbols with Python operators
                expression = expression.replace('×', '*').replace('÷', '/')
                
                # Handle percentage
                if '%' in expression:
                    parts = expression.split('%')
                    if len(parts) == 2:
                        base = eval(parts[0])
                        result = base * (eval(parts[1]) / 100)
                    else:
                        result = eval(expression.replace('%', '/100'))
                else:
                    result = eval(expression)
                
                session['history'] = session['display'] + ' ='
                session['display'] = str(result)
            except:
                session['display'] = 'Error'
                session['history'] = ''
        
        elif action == 'square':
            try:
                num = float(session['display'])
                session['history'] = f'{session["display"]}²'
                session['display'] = str(num ** 2)
            except:
                session['display'] = 'Error'
        
        elif action == 'sqrt':
            try:
                num = float(session['display'])
                if num < 0:
                    session['display'] = 'Error'
                else:
                    session['history'] = f'√{session["display"]}'
                    session['display'] = str(math.sqrt(num))
            except:
                session['display'] = 'Error'
        
        elif action == 'toggle_sign':
            try:
                num = float(session['display'])
                session['display'] = str(-num)
            except:
                session['display'] = 'Error'
        
        elif action == 'parenthesis':
            value = request.form.get('value')
            if session['display'] == '0':
                session['display'] = value
            else:
                session['display'] += value
    
    return render_template('calculator.html', 
                         display=session.get('display', '0'),
                         history=session.get('history', ''))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
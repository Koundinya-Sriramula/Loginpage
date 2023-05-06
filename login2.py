@app.route('/login', methods=['POST'])
def login():
  email = request.form['email']
  password = request.form['password']
  cursor = db.cursor()
  cursor.execute("SELECT * FROM users WHERE email=%s AND password=%s", (email, password))
  user = cursor.fetchone()
  if user is None:
    return jsonify({'success': False, 'message': 'Invalid email or password'})
  else:
    return jsonify({'success': True, 'message': 'Login successful'})

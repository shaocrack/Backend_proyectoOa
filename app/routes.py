from flask import jsonify, request
from app import app, db
from app.models import User, Course, Module, Role
from werkzeug.security import generate_password_hash, check_password_hash
from flask_cors import CORS, cross_origin

# Agregar un nuevo usuario
@cross_origin
@app.route('/users', methods=['POST'])
def add_user():
    data = request.get_json()

    
    required_fields = ['username', 'email', 'password', 'role_id']
    for field in required_fields:
        if field not in data:
            return jsonify({'error': f'Missing required field: {field}'}), 400
    username = request.json['username']
    email = request.json['email']
    password = request.json['password']
    role_id = data['role_id']

    hashed_password = generate_password_hash(password)

    new_user = User(username=username, email=email, password=hashed_password, role_id=role_id)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User added successfully'}), 201

# Obtener todos los usuarios
@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    users_list = [{'id': user.id, 'username': user.username, 'email': user.email} for user in users]
    return jsonify(users_list), 200

# Obtener un usuario por su ID
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get_or_404(user_id)
    user_info = {'id': user.id, 'username': user.username, 'email': user.email}
    return jsonify(user_info), 200

# Actualizar un usuario por su ID
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = User.query.get_or_404(user_id)
    username = request.json['username']
    email = request.json['email']
    password = request.json['password']
    role_id = request.json['role_id']

    hashed_password = generate_password_hash(password)

    user.username = username
    user.email = email
    user.password = hashed_password
    user.role_id = role_id

    db.session.commit()

    return jsonify({'message': 'User updated successfully'}), 200

# Eliminar un usuario por su ID
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()

    return jsonify({'message': 'User deleted successfully'}), 200

# Agregar un nuevo curso
@app.route('/courses', methods=['POST'])
def add_course():
    name = request.json['name']
    description = request.json['description']

    new_course = Course(name=name, description=description)
    db.session.add(new_course)
    db.session.commit()

    return jsonify({'message': 'Course added successfully'}), 201

# Obtener todos los cursos
@app.route('/courses', methods=['GET'])
def get_courses():
    courses = Course.query.all()
    courses_list = [{'id': course.id, 'name': course.name, 'description': course.description} for course in courses]
    return jsonify(courses_list), 200

# Obtener un curso por su ID
@app.route('/courses/<int:course_id>', methods=['GET'])
def get_course(course_id):
    course = Course.query.get_or_404(course_id)
    course_info = {'id': course.id, 'name': course.name, 'description': course.description}
    return jsonify(course_info), 200

# Actualizar un curso por su ID
@app.route('/courses/<int:course_id>', methods=['PUT'])
def update_course(course_id):
    course = Course.query.get_or_404(course_id)
    name = request.json['name']
    description = request.json['description']

    course.name = name
    course.description = description

    db.session.commit()

    return jsonify({'message': 'Course updated successfully'}), 200

# Eliminar un curso por su ID
@app.route('/courses/<int:course_id>', methods=['DELETE'])
def delete_course(course_id):
    course = Course.query.get_or_404(course_id)
    db.session.delete(course)
    db.session.commit()

    return jsonify({'message': 'Course deleted successfully'}), 200

# Agregar un nuevo módulo
@app.route('/modules', methods=['POST'])
def add_module():
    title = request.json['title']
    content = request.json['content']
    course_id = request.json['course_id']

    new_module = Module(title=title, content=content, course_id=course_id)
    db.session.add(new_module)
    db.session.commit()

    return jsonify({'message': 'Module added successfully'}), 201

# Obtener todos los módulos de un curso específico
@app.route('/courses/<int:course_id>/modules', methods=['GET'])
def get_course_modules(course_id):
    course = Course.query.get_or_404(course_id)
    modules = Module.query.filter_by(course_id=course_id).all()
    modules_list = [{'id': module.id, 'title': module.title, 'content': module.content} for module in modules]
    return jsonify(modules_list), 200

# Obtener todos los roles
@app.route('/roles', methods=['GET'])
def get_roles():
    roles = Role.query.all()
    roles_list = [{'id': role.id, 'name': role.name} for role in roles]
    return jsonify(roles_list), 200

# Login de usuario
@app.route('/login', methods=['POST'])
def login():
    username = request.json['username']
    password = request.json['password']

    user = User.query.filter_by(username=username).first()

    if user and check_password_hash(user.password, password):
        # Aquí puedes generar un token JWT u otra lógica de autenticación según tus necesidades
        return jsonify({'message': 'Login successful'}), 200
    else:
        return jsonify({'message': 'Invalid username or password'}), 401

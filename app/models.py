from app import db
from sqlalchemy.orm import relationship

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'), nullable=False)
    role = relationship('Role', back_populates='users')
    test_results = relationship('TestResult', back_populates='user')

    def __repr__(self):
        return f'<User {self.username}>'

class Course(db.Model):
    __tablename__ = 'course'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    modules = relationship('Module', back_populates='course')
    test_results = relationship('TestResult', back_populates='course')

    def __repr__(self):
        return f'<Course {self.name}>'

class Module(db.Model):
    __tablename__ = 'module'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=True)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)
    course = relationship('Course', back_populates='modules')
    test_results = relationship('TestResult', back_populates='module')

    def __repr__(self):
        return f'<Module {self.title}>'

class Role(db.Model):
    __tablename__ = 'role'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    users = relationship('User', back_populates='role')

    def __repr__(self):
        return f'<Role {self.name}>'

class TestResult(db.Model):
    __tablename__ = 'test_result'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    module_id = db.Column(db.Integer, db.ForeignKey('module.id'), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)
    attempt = db.Column(db.Integer, nullable=False)
    test_score = db.Column(db.Float, nullable=False)
    user = relationship('User', back_populates='test_results')
    module = relationship('Module', back_populates='test_results')
    course = relationship('Course', back_populates='test_results')

    def __repr__(self):
        return f'<TestResult for User {self.user_id}, Module {self.module_id}, Course {self.course_id}: {self.test_score}>'

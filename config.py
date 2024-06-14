from app import app, db
from app.models import User, Course, Module, TestResult

# Función para llenar datos iniciales en la base de datos
def seed_data():
    # Crear usuarios
    admin = User(username='admin', email='admin@example.com', password='123', role_id=2)
    jimmy = User(username='jimmy guajan', email='jimmy@example.com', password='123', role_id=1)
    ander = User(username='ander lema', email='ander@example.com', password='123', role_id=1)
    mary = User(username='Mary Claudio', email='mary@example.com', password='123', role_id=1)

    # Crear cursos
    curso_programacion = Course(name='Curso de Fundamentos de programacion', description='Se aprenderan la logica de programacion')

    # Crear modulos
    modulo1 = Module(title='modulo1', content='Contenido del módulo1', course_id=1)
    modulo2 = Module(title='modulo2', content='Contenido del módulo2', course_id=1)

    # Crear notas
    nota1 = TestResult(user_id=2, module_id=1, course_id=1, test_score=100)
    nota2 = TestResult(user_id=2, module_id=2, course_id=1, test_score=100)
    nota3 = TestResult(user_id=3, module_id=1, course_id=1, test_score=100)
    nota4 = TestResult(user_id=3, module_id=2, course_id=1, test_score=100)
    nota5 = TestResult(user_id=4, module_id=1, course_id=1, test_score=100)
    nota6 = TestResult(user_id=4, module_id=2, course_id=1, test_score=100)

    # Agregar los objetos creados a la sesión de la base de datos
    db.session.add(admin)
    db.session.add(jimmy)
    db.session.add(ander)
    db.session.add(mary)
    db.session.add(curso_programacion)
    db.session.add(modulo1)
    db.session.add(modulo2)
    db.session.add(nota1)
    db.session.add(nota2)
    db.session.add(nota3)
    db.session.add(nota4)
    db.session.add(nota5)
    db.session.add(nota6)

    # Confirmar los cambios en la base de datos
    db.session.commit()

# Ejecutar la función para llenar datos al iniciar la aplicación
if __name__ == '__main__':
    with app.app_context():
        seed_data()

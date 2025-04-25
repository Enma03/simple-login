# Simple Login App

Una aplicación web simple de inicio de sesión construida con Flask, SQLAlchemy y PyMySQL, conectada a una base de datos MySQL hospedada en Azure.

## 📦 Características

- Registro e inicio de sesión de usuarios
- Almacenamiento seguro de contraseñas con hash
- Conexión a base de datos MySQL (Azure)
- Arquitectura clara y modular

## ⚙️ Requisitos

- Python 3.9 o superior
- Cuenta en Azure con una base de datos MySQL creada
- Virtualenv (opcional pero recomendado)

## 📁 Estructura del proyecto

```
simple_login_app/
│
├── app.py               # Punto de entrada principal
├── models.py            # Modelos de SQLAlchemy
├── config.py            # Configuración de la app (incluye URI de la base de datos)
├── templates/           # HTMLs de Flask
│   ├── login.html
│   └── register.html
├── static/              # Archivos estáticos (CSS, JS)
├── .venv/               # Entorno virtual (si está en el repo)
└── README.md            # Este archivo
```

## 🔐 Configuración

Edita el archivo `config.py` para añadir tu URI de conexión de MySQL en Azure:

```python
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://<usuario>:<contraseña>@mysql-prd-emanuel.mysql.database.azure.com/<nombre_db>'
```

Asegúrate de que:
- Tu servidor MySQL en Azure permite conexiones desde tu IP pública
- Estás usando el puerto `3306`
- El usuario tenga los permisos necesarios

## 🚀 Cómo ejecutar

1. Clona el repositorio:
   ```bash
   git clone https://github.com/tu_usuario/simple_login_app.git
   cd simple_login_app
   ```

2. Crea y activa el entorno virtual:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate    # En Windows
   ```

3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

4. Inicia la aplicación:
   ```bash
   python app.py
   ```

5. Abre en el navegador:
   ```
   http://localhost:5000
   ```

## 🛠️ Dependencias principales

- Flask
- Flask-SQLAlchemy
- PyMySQL
- Werkzeug

Puedes listar todas las dependencias con:

```bash
pip freeze > requirements.txt
```

## 🧑‍💻 Autor

**Emanuel Henriquez**  
Estudiante de Ingeniería de Sistemas  
💻 Apasionado por Python, la ciberseguridad y el desarrollo backend

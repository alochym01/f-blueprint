- Using flask run should be export enviroment variables
	+ FLASK_APP
	+ FLASK_ENV
		- production
		- development
	+ flask run
- Using python run.py
	+ using config.py file
	+ python run.py
- Using flask-migrate
	+ export FLASK_APP=db_migrate.py
	+ flask db migrate
	+ flask db upgrade
	+ **_Create an admin user_**
		+ flask initdb
- Flask structure
	```
	f-blueprint/
	├── app
	│   ├── forms
	│   │   └── login.py
	│   ├── __init__.py
	│   ├── models
	│   │   └── user.py
	│   ├── static
	│   │   ├── css
	│   │   │   ├── AdminLTE.min.css
	│   │   │   ├── ...
	│   │   │   └── jquery-jvectormap.css
	│   │   ├── fonts
	│   │   │   ├── FontAwesome.otf
	│   │   │   ├── ....
	│   │   │   └── Source+Sans+Pro_700_normal.woff
	│   │   ├── images
	│   │   │   ├── default-50x50.gif
	│   │   │   ├── user1-128x128.jpg
	│   │   │   ├── ...
	│   │   │   └── user8-128x128.jpg
	│   │   └── js
	│   │       ├── adminlte.min.js
	│   │       ├── bootstrap.min.js
	│   │       ├── ...
	│   │       └── jquery.sparkline.min.js
	│   ├── templates
	│   │   └── auth
	│   │       └── login.html
	│   └── views
	│       ├── authentication.py
	│       └── __init__.py
	├── app.db
	├── config.py
	├── db_migrate.py							# using for flask migrate
	├── migrations
	│   ├── alembic.ini
	│   ├── env.py
	│   ├── README
	│   ├── script.py.mako
	│   └── versions
	│       └── 991d5a741b1c_.py
	└── run.py								# using FLASK_APP

	```
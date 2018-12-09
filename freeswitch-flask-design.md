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
# [Freeswitch Channel-State](https://docs.freeswitch.org/switch__types_8h.html#aade07b0fc79b95c5362b21b2c33cafb7)
States					| Meaning
--- 					| ---
**CS_NEW**				| Channel is newly created.
**CS_INIT**				| Channel has been initialized.
**CS_ROUTING**			| Channel is looking for an extension to execute.
**CS_SOFT_EXECUTE**		| Channel is ready to execute from 3rd party control.
**CS_EXECUTE**			| Channel is executing it's dialplan.
**CS_EXCHANGE_MEDIA**	| Channel is exchanging media with another channel.
**CS_PARK**				| Channel is accepting media awaiting commands.
**CS_CONSUME_MEDIA**	| Channel is consuming all media and dropping it.
**CS_HIBERNATE**		| Channel is in a sleep state.
**CS_RESET**			| Channel is in a reset state.
**CS_HANGUP**			| Channel is flagged for hangup and ready to end.
**CS_REPORTING**		| Channel is ready to collect call detail.
**CS_DESTROY**			| Channel is ready to be destroyed and out of the state machine.
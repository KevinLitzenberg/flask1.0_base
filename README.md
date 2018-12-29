Flask1.0_base

Python 3.7 using venv.  Activate the environment.

Local Implementation per :
http://flask.pocoo.org/docs/1.0/tutorial/layout/

1. Create a directory for Flask to live in:
>mkdir flask-tutorial
>cd flask-tutorial

http://flask.pocoo.org/docs/1.0/installation/
1.2 Create the Python3.7 venv
>python3.7 -m venv flash-tutorial

1.3 BEFORE working on your project activate the environment.
>. flask-tutorial/bin/activate

1.4 Install Flask
>pip install Flask 

    -Flask-1.0.2-py2.py3-none-any.whl
    -Werkzeug-0.14.1-py2.py3-none-any.whl 
    -Click-7.0-py2.py3-none-any.whl
    -Jinja2-2.10-py2.py3-none-any.whl
    -itsdangerous-1.1.0-py2.py3-none-any.whl
    -MarkupSafe-1.1.0-cp37-cp37m-manylinux1_x86_64.whl

    Installing collected packages: Werkzeug, click, MarkupSafe, Jinja2, itsdangerous, Flask
Successfully installed Flask-1.0.2 Jinja2-2.10 MarkupSafe-1.1.0 Werkzeug-0.14.1 click-7.0 itsdangerous-1.1.0


--------Version 0.0.1--------

*Base install from tutroial on flask.  Acts as a framework to build a customized flask1.0 application.  Uses SQLLite for user data.

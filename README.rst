LOCKATME: Customizable and Modulable Screen Locker
==================================================

Features
--------
Modulable
/////////

Those are the currently available modules (more are to come):

  - password
  - facial_recognition

Themable (TODO)
///////////////


Installation
------------

Using pip::

    $ pip install lockatme


Configuration
-------------
You can choose the modules you want to use by changing ``$XDG_CONFIG_HOME/lockatme/config``
or ``~/.config/lockatme/config`` by default.

For example, if you want to use only password authentication::

    [unlockers]
    password

If you want to use both password and facial recognition at the same time::

    [unlockers]
    password
    facial_recogntion

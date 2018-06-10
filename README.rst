lockatme: Modulable Screen Locker
#################################

lockatme is a screen locker that works with modules. It allows the user
to use the same locker for different types of authentication.

**This locker is in development stage, there is nothing secure about it.
Don't use it for real application just yet.**


.. contents::

.. section-numbering::


Main features
=============

* Modulable
* Themable (TODO)


Installation
============

Using ``pip``:

.. code-block:: bash

    $ pip install lockatme


Usage
=====

From the command line:

.. code-block:: bash

    $ lockatme


Configuration
=============

lockatme uses a ini-like config file.

Config file location
--------------------
The default location of the configuration file is ``$XDG_CONFIG_HOME/lockatme/config`` or
``~/.config/lockatme/config`` if ``$XDG_CONFIG_HOME`` is not set.

Module configuration
--------------------

You can choose which modules you want to use so for example, if you want to use only
password authentication:

.. code-block:: ini

    [unlockers]
    password

If you want to use both password and facial recognition at the same time:

.. code-block:: ini

    [unlockers]
    password
    facial_recogntion


.. |warning| image:: https://png2.kisspng.com/sh/e4d188bc0f796f71a746c6d034155baf/L0KzQYi4UsA5N2Q4UZGAYULlQYjsU8A5a2U1SJCEMkW2QYq5WcE2OWM8T6UBMEOzQ4aCTwBvbz==/5a2b17e308c400.9253192915127736030359.png
    :scale: 1%

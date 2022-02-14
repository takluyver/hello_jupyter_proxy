Jupyter Server Proxy Demo
=========================

This is a demo package showing how to run a web app through
`Jupyter Server Proxy <https://jupyter-server-proxy.readthedocs.io/en/latest/>`_.

This mechanism allows a user to run a separate web app through JupyterHub.
To try it, install this package into the same Python environment which is
used to launch your single-user server::

    pip install hello_jupyter_proxy

If your server is already running use the JupyterHub control panel
(``/hub/home``) to stop and start it. You should have a new 'hello' option in
the 'New' menu (classic notebook) or the launcher (Jupyterlab). You can also
go directly to ``https://(your-jhub-server)/user-redirect/hello/`` .

Building applications to proxy
------------------------------

This is meant as a starting point for building useful applications to run in
Jupyter Server Proxy. See `the JSP docs
<https://jupyter-server-proxy.readthedocs.io/en/latest/>`_ and especially the
`examples page <https://jupyter-server-proxy.readthedocs.io/en/latest/examples.html>`_
for more information.

For real web applications in Python, you will want a web framework rather than
the low-level ``http.server`` module. There are many choices, but `Tornado
<https://www.tornadoweb.org/en/stable/>`_ (used by Jupyter) and `Flask
<https://palletsprojects.com/p/flask/>`_ are two well known ones.

**Security**: Once user A launches your application through Jupyter, it is
listening on a TCP port, and user B can also connect to it and send requests.
You might want to consider:

- Limiting what the application can do and what information it can retrieve, so
  accessing another user's server is not too dangerous.
- Listening only on localhost (as in this example), to limit access to only
  users who can log into the same machine.
- Find some way to verify that the user sending the request matches the user
  which the application is running as.

Which measures make sense will depend on your application and the environment
in which you expect to use it.

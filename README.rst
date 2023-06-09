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

**Security**: This example uses a Unix socket between Jupyter and the proxied
application, which is a new option in Jupyter Server Proxy 4.0. This is set up
so that only the user running the application can connect to it. If you choose
to use a TCP socket instead, pay attention to whether other users can connect to
it and what it might allow them to do.

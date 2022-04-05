Dialogflow: Python Client
=========================


.. warning::
    The package `dialogflow`_ has been renamed to `google-cloud-dialogflow`_.
    `dialogflow`_ will no longer be updated.

    For help upgrading to ``google-cloud-dialogflow>=2.0.0``, see the `Migration Guide`_.

    After **October 28, 2021**, importing code from the latest release of `dialogflow`_ will result in a ``RuntimeError``. If you need to continue to use `dialogflow`_ after this date, please pin to a specific version of `dialogflow`_ (e.g., ``dialogflow==1.1.1``). If you have questions, please `file an issue`_.

.. _dialogflow: https://pypi.org/project/dialogflow
.. _google-cloud-dialogflow: https://pypi.org/project/google-cloud-dialogflow
.. _Migration Guide: https://github.com/googleapis/python-dialogflow/blob/master/UPGRADING.md
.. _file an issue: https://github.com/googleapis/python-dialogflow/issues



    Python idiomatic client for `Google Cloud Dialogflow <https://dialogflow.com/>`__

`Google Cloud Dialogflow <https://dialogflow.com/>`__ is an enterprise-grade NLU platform that makes it easy for
developers to design and integrate conversational user interfaces into
mobile apps, web applications, devices, and bots.

* `Dialogflow Python Client API Reference <https://googleapis.dev/python/dialogflow/latest/index.html>`_
* `Dialogflow Standard Edition Documentation <https://www.dialogflow.com>`_
* `Dialogflow Enterprise Edition Documentation <https://cloud.google.com/dialogflow-enterprise/docs>`_

Read more about the client libraries for Cloud APIs, including the older
Google APIs Client Libraries, in
`Client Libraries Explained <https://cloud.google.com/apis/docs/client-libraries-explained>`_.


Before you begin
----------------

#. Select or create a Cloud Platform `project`_.
#. `Enable billing`_ for your project.
#.  `Enable the Google Cloud Dialogflow API`_.
#.  `Set up authentication`_ with a service account so you can access the
    API from your local workstation.

.. _project: https://console.cloud.google.com/project
.. _Enable billing: https://support.google.com/cloud/answer/6293499#enable-billing
.. _Enable the Google Cloud Dialogflow API: https://console.cloud.google.com/flows/enableapi?apiid=dialogflow.googleapis.com
.. _Set up authentication: https://cloud.google.com/docs/authentication/getting-started


Installation
------------

.. code-block:: shell

    pip install dialogflow

.. note::

    We highly recommend that you install this library in a
    `virtualenv <https://virtualenv.pypa.io/en/latest/>`_.


Supported Python Versions
^^^^^^^^^^^^^^^^^^^^^^^^^
Python >= 3.5

Deprecated Python Versions
^^^^^^^^^^^^^^^^^^^^^^^^^^
Python == 2.7. Python 2.7 support will be removed on January 1, 2020.


Usage
-----

View `usage documentation <https://googleapis.dev/python/dialogflow/latest/index.html>`_.


Versioning
----------

This library follows `Semantic Versioning <http://semver.org/>`_.

This library is considered to be stable. This means and that the code surface will not change in backwards-incompatible
ways unless either absolutely necessary (e.g. because of critical security issues) or with an extensive deprecation
period. Issues and requests against GA libraries are addressed with the highest priority.

More Information: `Google Cloud Python Library Support <https://github.com/googleapis/google-cloud-python/blob/master/README.rst#general-availability>`_

Contributing
------------

Contributions welcome! See the `Contributing Guide <https://github.com/googleapis/python-dialogflow/blob/master/.github/CONTRIBUTING.md>`_.

License
-------

Apache Version 2.0

See `the LICENSE file <https://github.com/googleapis/python-dialogflow/blob/master/LICENSE>`_ for more information.


.. |release level| image:: https://img.shields.io/badge/support-GA-gold.svg
   :target: https://github.com/googleapis/google-cloud-python/blob/master/README.rst#general-availability

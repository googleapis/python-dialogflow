.. image:: https://avatars2.githubusercontent.com/u/2810941?v=3&s=96
    :align: right
    :alt: Google Cloud Platform logo
    :height: 96px
    :width: 96px

Google Cloud Dialogflow Enterprise: Python Client
=================================================

|release level| |circleci| |appveyor| |codecov|

    Python idiomatic client for Google Cloud Dialogflow Enterprise

`Google Cloud Dialogflow Enterprise <https://cloud.google.com/dialogflow-enterprise>`_
is an enterprise-grade NLU platform that makes it easy for developers to
design and integrate conversational user interfaces into mobile apps, web
applications, devices, and bots.

* `Dialogflow Enterprise Python Client API Reference <https://cloud.google.com/dialogflow-enterprise>`_
* `Dialogflow Enterprise Documentation <https://cloud.google.com/dialogflow-enterprise>`_

Read more about the client libraries for Cloud APIs, including the older
Google APIs Client Libraries, in
`Client Libraries Explained <https://cloud.google.com/apis/docs/client-libraries-explained>`_.

Quickstart
----------

Before you begin
~~~~~~~~~~~~~~~~

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
~~~~~~~~~~~~

.. code-block:: shell

    pip install google-cloud-dialogflow

.. note::

    We highly recommend that you install this library in a
    `virtualenv <https://virtualenv.pypa.io/en/latest/>`_.


Versioning
~~~~~~~~~~

This library follows `Semantic Versioning <http://semver.org/>`_.

This library is considered to be in **beta**. This means it is expected to be
mostly stable while we work toward a general availability release; however,
complete stability is not guaranteed. We will address issues and requests
against beta libraries with a high priority.

More Information: `Google Cloud Platform Launch Stages <https://cloud.google.com/terms/launch-stages>`_

Contributing
~~~~~~~~~~~~

Contributions welcome! See the `Contributing Guide <https://github.com/googleapis/python-dialogflow/blob/master/.github/CONTRIBUTING.rst>`_.

License
~~~~~~~

Apache Version 2.0

See `LICENSE <https://github.com/googleapis/python-dialogflow/blob/master/LICENSE>`_


.. |release level| image:: https://img.shields.io/badge/release%20level-beta-yellow.svg?style&#x3D;flat
    :target: https://cloud.google.com/terms/launch-stages
.. |circleci| image:: https://img.shields.io/circleci/project/github/googleapis/python-dialogflow.svg?style=flat)
    :target: https://circleci.com/gh/googleapis/python-dialogflow
.. |appveyor| image:: https://ci.appveyor.com/api/projects/status/github/googleapis/python-dialogflow?branch=master&svg=true)
    :target: https://ci.appveyor.com/project/googleapis/python-dialogflow
.. |codecov| image:: https://img.shields.io/codecov/c/github/googleapis/python-dialogflow/master.svg?style=flat)
    :target: https://codecov.io/gh/googleapis/python-dialogflow

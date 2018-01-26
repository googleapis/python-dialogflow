.. image:: https://avatars2.githubusercontent.com/u/2810941?v=3&s=96
   :height: 96px
   :width: 96px
   :alt: Google Cloud Platform logo
   :align: right

`Dialogflow: Python Client <https://github.com/dialogflow/dialogflow-python-client-v2>`__
=========================================================================

|release level| |CircleCI| |AppVeyor| |codecov|

    Python idiomatic client for
    `Dialogflow <https://dialogflow.com/docs/>`__.

[Dialogflow](https://dialogflow.com/docs/) is a natural language understanding platform that makes it easy for you to design and integrate a conversational user interface into your mobile app, web application, device, bot, and so on.


-  `Dialogflow Python Client API Reference <https://googlecloudplatform.github.io/google-cloud-python/latest/dialogflow/index.html>`__
-  `github.com/dialogflow/dialogflow-python-client-v2 <https://github.com/dialogflow/dialogflow-python-client-v2>`__
-  `Dialogflow Documentation <https://dialogflow.com/docs/>`__

Read more about the client libraries for Cloud APIs, including the older
Google APIs Client Libraries, in `Client Libraries
Explained <https://cloud.google.com/apis/docs/client-libraries-explained>`__.

**Table of contents:**

-  `Quickstart <#quickstart>`__

   -  `Before you begin <#before-you-begin>`__
   -  `Installing the client library <#installing-the-client-library>`__
   -  `Using the client library <#using-the-client-library>`__

-  `Samples <#samples>`__
-  `Versioning <#versioning>`__
-  `Contributing <#contributing>`__
-  `License <#license>`__

Quickstart
----------

Before you begin
~~~~~~~~~~~~~~~~

1. Select or create a Cloud Platform project.

  `Go to the projects page`_

1. Enable billing for your project.

  `Enable billing`_

1. Enable the Dialogflow API.

  `Enable the API`_

1. `Set up authentication with a service account`_ so you
can access the API from your local workstation.

.. _Go to the projects page: https://console.cloud.google.com/project
.. _Enable billing: https://support.google.com/cloud/answer/6293499#enable-billing
.. _Enable the API: https://console.cloud.google.com/flows/enableapi?apiid=dialogflow.googleapis.com
.. _Set up authentication with a service account: https://cloud.google.com/docs/authentication/getting-started


Installing the client library
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    pip install dialogflow

.. note::

    We highly recommend that you install this library in a
    `virtualenv <https://virtualenv.pypa.io/en/latest/>`_.


Using the client library
~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

    import dialogflow
    import uuid

    text = 'Hi, what can I do with your app?'

    session_client = dialogflow.SessionsClient()

    session = session_client.session_path('YOUR_PROJECT_ID', uuid.uuid4())
    print('Session path: {}\n'.format(session))

    text_input = dialogflow.types.TextInput(
        text=text, language_code='en-US')

    query_input = dialogflow.types.QueryInput(text=text_input)

    response = session_client.detect_intent(
        session=session, query_input=query_input)

    print('=' * 20)
    print('Query text: {}'.format(response.query_result.query_text))
    print('Detected intent: {} (confidence: {})\n'.format(
        response.query_result.intent.display_name,
        response.query_result.intent_detection_confidence))
    print('Fulfillment text: {}\n'.format(
        response.query_result.fulfillment_text))


Samples
~~~~~~~

Samples are in the `samples\ <https://github.com/dialogflow/dialogflow-python-client-v2/tree/master/samples>`__
directory. The samples’ ``README.md`` has instructions for running the
samples.

+--------+-------------+--------+
| Sample | Source Code | Try it |
+========+=============+========+
+--------+-------------+--------+

\| Context Management \| `source code <https://github.com/dialogflow/dialogflow-python-client-v2/blob/master/samples/context_management.py>`__ \| |Open in Cloud Shell Context Management| \|

.. |Open in Cloud Shell Context Management| image:: http://gstatic.com/cloudssh/images/open-btn.png
   :target: https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/dialogflow/dialogflow-python-client-v2&page=editor&open_in_editor=samples/context_management.py,samples/README.md

\| Detect Intent Audio \| `source code <https://github.com/dialogflow/dialogflow-python-client-v2/blob/master/samples/detect_intent_audio.py>`__ \| |Open in Cloud Shell Detect Intent Audio| \|

.. |Open in Cloud Shell Detect Intent Audio| image:: http://gstatic.com/cloudssh/images/open-btn.png
   :target: https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/dialogflow/dialogflow-python-client-v2&page=editor&open_in_editor=samples/detect_intent_audio.py,samples/README.md

\| Detect Intent Stream \| `source code <https://github.com/dialogflow/dialogflow-python-client-v2/blob/master/samples/detect_intent_stream.py>`__ \| |Open in Cloud Shell Detect Intent Stream| \|

.. |Open in Cloud Shell Detect Intent Stream| image:: http://gstatic.com/cloudssh/images/open-btn.png
   :target: https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/dialogflow/dialogflow-python-client-v2&page=editor&open_in_editor=samples/detect_intent_stream.py,samples/README.md

\| Context Management \| `source code <https://github.com/dialogflow/dialogflow-python-client-v2/blob/master/samples/context_management.py>`__ \| |Open in Cloud Shell Context Management| \|

.. |Open in Cloud Shell Context Management| image:: http://gstatic.com/cloudssh/images/open-btn.png
   :target: https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/dialogflow/dialogflow-python-client-v2&page=editor&open_in_editor=samples/context_management.py,samples/README.md

\| Context Management \| `source code <https://github.com/dialogflow/dialogflow-python-client-v2/blob/master/samples/context_management.py>`__ \| |Open in Cloud Shell Context Management| \|

.. |Open in Cloud Shell Context Management| image:: http://gstatic.com/cloudssh/images/open-btn.png
   :target: https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/dialogflow/dialogflow-python-client-v2&page=editor&open_in_editor=samples/context_management.py,samples/README.md

\| Context Management \| `source code <https://github.com/dialogflow/dialogflow-python-client-v2/blob/master/samples/context_management.py>`__ \| |Open in Cloud Shell Context Management| \|

.. |Open in Cloud Shell Context Management| image:: http://gstatic.com/cloudssh/images/open-btn.png
   :target: https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/dialogflow/dialogflow-python-client-v2&page=editor&open_in_editor=samples/context_management.py,samples/README.md

\| Context Management \| `source code <https://github.com/dialogflow/dialogflow-python-client-v2/blob/master/samples/context_management.py>`__ \| |Open in Cloud Shell Context Management| \|

.. |Open in Cloud Shell Context Management| image:: http://gstatic.com/cloudssh/images/open-btn.png
   :target: https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/dialogflow/dialogflow-python-client-v2&page=editor&open_in_editor=samples/context_management.py,samples/README.md

\| Context Management \| `source code <https://github.com/dialogflow/dialogflow-python-client-v2/blob/master/samples/context_management.py>`__ \| |Open in Cloud Shell Context Management| \|

.. |Open in Cloud Shell Context Management| image:: http://gstatic.com/cloudssh/images/open-btn.png
   :target: https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/dialogflow/dialogflow-python-client-v2&page=editor&open_in_editor=samples/context_management.py,samples/README.md

\| Context Management \| `source code <https://github.com/dialogflow/dialogflow-python-client-v2/blob/master/samples/context_management.py>`__ \| |Open in Cloud Shell Context Management| \|

.. |Open in Cloud Shell Context Management| image:: http://gstatic.com/cloudssh/images/open-btn.png
   :target: https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/dialogflow/dialogflow-python-client-v2&page=editor&open_in_editor=samples/context_management.py,samples/README.md


The `Dialogflow Python Client API
Reference <https://googlecloudplatform.github.io/google-cloud-python/latest/dialogflow/index.html>`__ documentation also
contains samples.

Versioning
----------

This library follows `Semantic Versioning <http://semver.org/>`__.


More Information: `Google Cloud Platform Launch
Stages <https://cloud.google.com/terms/launch-stages>`__

Contributing
------------

Contributions welcome! See the `Contributing
Guide <https://github.com/dialogflow/dialogflow-python-client-v2/blob/master/.github/CONTRIBUTING.md>`__.

License
-------

Apache Version 2.0

See
`LICENSE <https://github.com/dialogflow/dialogflow-python-client-v2/blob/master/LICENSE>`__


.. |release level| image:: https://img.shields.io/badge/release%20level-general%20availability%20%28GA%29-brightgreen.svg?style=flat
   :target: https://cloud.google.com/terms/launch-stages
.. |CircleCI| image:: https://img.shields.io/circleci/project/github/dialogflow/dialogflow-python-client-v2.svg?style=flat
   :target: https://circleci.com/gh/dialogflow/dialogflow-python-client-v2
.. |AppVeyor| image:: https://ci.appveyor.com/api/projects/status/github/dialogflow/dialogflow-python-client-v2?branch=master&svg=true
   :target: https://ci.appveyor.com/project/dialogflow/dialogflow-python-client-v2
.. |codecov| image:: https://img.shields.io/codecov/c/github/dialogflow/dialogflow-python-client-v2/master.svg?style=flat
   :target: https://codecov.io/gh/dialogflow/dialogflow-python-client-v2
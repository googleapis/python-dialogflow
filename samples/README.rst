.. image:: https://avatars2.githubusercontent.com/u/2810941?v=3&s=96
   :height: 96px
   :width: 96px
   :alt: Google Cloud Platform logo
   :align: right

Dialogflow: Python Samples
=============================

|Open in Cloud Shell|

[Dialogflow](https://dialogflow.com/docs/) is a natural language understanding platform that makes it easy for you to design and integrate a conversational user interface into your mobile app, web application, device, bot, and so on.

Table of Contents
-----------------

-  `Before you begin <#before-you-begin>`__
-  `Samples <#samples>`__
   -  `Context Management <#context-management>`__
   -  `Detect Intent Audio <#detect-intent-audio>`__
   -  `Detect Intent Stream <#detect-intent-stream>`__
   -  `Context Management <#context-management>`__
   -  `Context Management <#context-management>`__
   -  `Context Management <#context-management>`__
   -  `Context Management <#context-management>`__
   -  `Context Management <#context-management>`__
   -  `Context Management <#context-management>`__

Before you begin
----------------

Before running the samples, make sure you’ve followed the steps in the
`Before you begin section <../README.md#before-you-begin>`__ of the
client library’s README.

Samples
-------


Context Management
~~~~~~~~

View the `source code <context_management.py>`__.

|Open in Cloud Shell Context Management|

.. |Open in Cloud Shell Context Management| image:: http://gstatic.com/cloudssh/images/open-btn.png
   :target: https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/dialogflow/dialogflow-python-client-v2&page=editor&open_in_editor=samples/context_management.py,samples/README.md




**Usage:** ``python context_management.py --help``

::

    usage: context_management.py [-h] --project-id PROJECT_ID
                             {list,create,delete} ...

DialogFlow API Context Python sample showing how to manage session
contexts.

Examples:
  python context_management.py -h
  python context_management.py --project-id PROJECT_ID   list --session-id SESSION_ID
  python context_management.py --project-id PROJECT_ID   create --session-id SESSION_ID --context-id CONTEXT_ID
  python context_management.py --project-id PROJECT_ID   delete --session-id SESSION_ID --context-id CONTEXT_ID

positional arguments:
  {list,create,delete}
    list
    create
    delete

optional arguments:
  -h, --help            show this help message and exit
  --project-id PROJECT_ID
                        Project/agent id. Required.


Detect Intent Audio
~~~~~~~~

View the `source code <detect_intent_audio.py>`__.

|Open in Cloud Shell Detect Intent Audio|

.. |Open in Cloud Shell Detect Intent Audio| image:: http://gstatic.com/cloudssh/images/open-btn.png
   :target: https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/dialogflow/dialogflow-python-client-v2&page=editor&open_in_editor=samples/detect_intent_audio.py,samples/README.md




**Usage:** ``python detect_intent_audio.py --help``

::

    usage: detect_intent_audio.py [-h] --project-id PROJECT_ID
                              [--session-id SESSION_ID]
                              [--language-code LANGUAGE_CODE]
                              --audio-file-path AUDIO_FILE_PATH

DialogFlow API Detect Intent Python sample with audio file.

Examples:
  python detect_intent_audio.py -h
  python detect_intent_audio.py --project-id PROJECT_ID   --session-id SESSION_ID --audio-file-path resources/book_a_room.wav
  python detect_intent_audio.py --project-id PROJECT_ID   --session-id SESSION_ID --audio-file-path resources/mountain_view.wav
  python detect_intent_audio.py --project-id PROJECT_ID   --session-id SESSION_ID --audio-file-path resources/today.wav

optional arguments:
  -h, --help            show this help message and exit
  --project-id PROJECT_ID
                        Project/agent id. Required.
  --session-id SESSION_ID
                        Identifier of the DetectIntent session. Defaults to a
                        random UUID.
  --language-code LANGUAGE_CODE
                        Language code of the query. Defaults to "en-US".
  --audio-file-path AUDIO_FILE_PATH
                        Path to the audio file.


Detect Intent Stream
~~~~~~~~

View the `source code <detect_intent_stream.py>`__.

|Open in Cloud Shell Detect Intent Stream|

.. |Open in Cloud Shell Detect Intent Stream| image:: http://gstatic.com/cloudssh/images/open-btn.png
   :target: https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/dialogflow/dialogflow-python-client-v2&page=editor&open_in_editor=samples/detect_intent_stream.py,samples/README.md




**Usage:** ``python detect_intent_stream.py --help``

::

    usage: detect_intent_stream.py [-h] --project-id PROJECT_ID
                               [--session-id SESSION_ID]
                               [--language-code LANGUAGE_CODE]
                               --audio-file-path AUDIO_FILE_PATH

DialogFlow API Detect Intent Python sample with audio files processed
as an audio stream.

Examples:
  python detect_intent_stream.py -h
  python detect_intent_stream.py --project-id PROJECT_ID   --session-id SESSION_ID --audio-file-path resources/book_a_room.wav
  python detect_intent_stream.py --project-id PROJECT_ID   --session-id SESSION_ID --audio-file-path resources/mountain_view.wav

optional arguments:
  -h, --help            show this help message and exit
  --project-id PROJECT_ID
                        Project/agent id. Required.
  --session-id SESSION_ID
                        Identifier of the DetectIntent session. Defaults to a
                        random UUID.
  --language-code LANGUAGE_CODE
                        Language code of the query. Defaults to "en-US".
  --audio-file-path AUDIO_FILE_PATH
                        Path to the audio file.


Context Management
~~~~~~~~

View the `source code <context_management.py>`__.

|Open in Cloud Shell Context Management|

.. |Open in Cloud Shell Context Management| image:: http://gstatic.com/cloudssh/images/open-btn.png
   :target: https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/dialogflow/dialogflow-python-client-v2&page=editor&open_in_editor=samples/context_management.py,samples/README.md




**Usage:** ``python context_management.py --help``

::

    usage: context_management.py [-h] --project-id PROJECT_ID
                             {list,create,delete} ...

DialogFlow API Context Python sample showing how to manage session
contexts.

Examples:
  python context_management.py -h
  python context_management.py --project-id PROJECT_ID   list --session-id SESSION_ID
  python context_management.py --project-id PROJECT_ID   create --session-id SESSION_ID --context-id CONTEXT_ID
  python context_management.py --project-id PROJECT_ID   delete --session-id SESSION_ID --context-id CONTEXT_ID

positional arguments:
  {list,create,delete}
    list
    create
    delete

optional arguments:
  -h, --help            show this help message and exit
  --project-id PROJECT_ID
                        Project/agent id. Required.


Context Management
~~~~~~~~

View the `source code <context_management.py>`__.

|Open in Cloud Shell Context Management|

.. |Open in Cloud Shell Context Management| image:: http://gstatic.com/cloudssh/images/open-btn.png
   :target: https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/dialogflow/dialogflow-python-client-v2&page=editor&open_in_editor=samples/context_management.py,samples/README.md




**Usage:** ``python context_management.py --help``

::

    usage: context_management.py [-h] --project-id PROJECT_ID
                             {list,create,delete} ...

DialogFlow API Context Python sample showing how to manage session
contexts.

Examples:
  python context_management.py -h
  python context_management.py --project-id PROJECT_ID   list --session-id SESSION_ID
  python context_management.py --project-id PROJECT_ID   create --session-id SESSION_ID --context-id CONTEXT_ID
  python context_management.py --project-id PROJECT_ID   delete --session-id SESSION_ID --context-id CONTEXT_ID

positional arguments:
  {list,create,delete}
    list
    create
    delete

optional arguments:
  -h, --help            show this help message and exit
  --project-id PROJECT_ID
                        Project/agent id. Required.


Context Management
~~~~~~~~

View the `source code <context_management.py>`__.

|Open in Cloud Shell Context Management|

.. |Open in Cloud Shell Context Management| image:: http://gstatic.com/cloudssh/images/open-btn.png
   :target: https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/dialogflow/dialogflow-python-client-v2&page=editor&open_in_editor=samples/context_management.py,samples/README.md




**Usage:** ``python context_management.py --help``

::

    usage: context_management.py [-h] --project-id PROJECT_ID
                             {list,create,delete} ...

DialogFlow API Context Python sample showing how to manage session
contexts.

Examples:
  python context_management.py -h
  python context_management.py --project-id PROJECT_ID   list --session-id SESSION_ID
  python context_management.py --project-id PROJECT_ID   create --session-id SESSION_ID --context-id CONTEXT_ID
  python context_management.py --project-id PROJECT_ID   delete --session-id SESSION_ID --context-id CONTEXT_ID

positional arguments:
  {list,create,delete}
    list
    create
    delete

optional arguments:
  -h, --help            show this help message and exit
  --project-id PROJECT_ID
                        Project/agent id. Required.


Context Management
~~~~~~~~

View the `source code <context_management.py>`__.

|Open in Cloud Shell Context Management|

.. |Open in Cloud Shell Context Management| image:: http://gstatic.com/cloudssh/images/open-btn.png
   :target: https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/dialogflow/dialogflow-python-client-v2&page=editor&open_in_editor=samples/context_management.py,samples/README.md




**Usage:** ``python context_management.py --help``

::

    usage: context_management.py [-h] --project-id PROJECT_ID
                             {list,create,delete} ...

DialogFlow API Context Python sample showing how to manage session
contexts.

Examples:
  python context_management.py -h
  python context_management.py --project-id PROJECT_ID   list --session-id SESSION_ID
  python context_management.py --project-id PROJECT_ID   create --session-id SESSION_ID --context-id CONTEXT_ID
  python context_management.py --project-id PROJECT_ID   delete --session-id SESSION_ID --context-id CONTEXT_ID

positional arguments:
  {list,create,delete}
    list
    create
    delete

optional arguments:
  -h, --help            show this help message and exit
  --project-id PROJECT_ID
                        Project/agent id. Required.


Context Management
~~~~~~~~

View the `source code <context_management.py>`__.

|Open in Cloud Shell Context Management|

.. |Open in Cloud Shell Context Management| image:: http://gstatic.com/cloudssh/images/open-btn.png
   :target: https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/dialogflow/dialogflow-python-client-v2&page=editor&open_in_editor=samples/context_management.py,samples/README.md




**Usage:** ``python context_management.py --help``

::

    usage: context_management.py [-h] --project-id PROJECT_ID
                             {list,create,delete} ...

DialogFlow API Context Python sample showing how to manage session
contexts.

Examples:
  python context_management.py -h
  python context_management.py --project-id PROJECT_ID   list --session-id SESSION_ID
  python context_management.py --project-id PROJECT_ID   create --session-id SESSION_ID --context-id CONTEXT_ID
  python context_management.py --project-id PROJECT_ID   delete --session-id SESSION_ID --context-id CONTEXT_ID

positional arguments:
  {list,create,delete}
    list
    create
    delete

optional arguments:
  -h, --help            show this help message and exit
  --project-id PROJECT_ID
                        Project/agent id. Required.


Context Management
~~~~~~~~

View the `source code <context_management.py>`__.

|Open in Cloud Shell Context Management|

.. |Open in Cloud Shell Context Management| image:: http://gstatic.com/cloudssh/images/open-btn.png
   :target: https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/dialogflow/dialogflow-python-client-v2&page=editor&open_in_editor=samples/context_management.py,samples/README.md




**Usage:** ``python context_management.py --help``

::

    usage: context_management.py [-h] --project-id PROJECT_ID
                             {list,create,delete} ...

DialogFlow API Context Python sample showing how to manage session
contexts.

Examples:
  python context_management.py -h
  python context_management.py --project-id PROJECT_ID   list --session-id SESSION_ID
  python context_management.py --project-id PROJECT_ID   create --session-id SESSION_ID --context-id CONTEXT_ID
  python context_management.py --project-id PROJECT_ID   delete --session-id SESSION_ID --context-id CONTEXT_ID

positional arguments:
  {list,create,delete}
    list
    create
    delete

optional arguments:
  -h, --help            show this help message and exit
  --project-id PROJECT_ID
                        Project/agent id. Required.


.. |Open in Cloud Shell| image:: http://gstatic.com/cloudssh/images/open-btn.png
   :target: https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/dialogflow/dialogflow-python-client-v2&page=editor&open_in_editor=samples/README.md
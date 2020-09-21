# 2.0.0 Migration Guide

The 2.0 release of the `google-cloud-dialogflow` client is a significant upgrade based on a [next-gen code generator](https://github.com/googleapis/gapic-generator-python), and includes substantial interface changes. Existing code written for earlier versions of this library will likely require updates to use this version. This document describes the changes that have been made, and what you need to do to update your usage.

If you experience issues or have questions, please file an [issue](https://github.com/googleapis/dialogflow-python-client-v2/issues).

## Supported Python Versions
> **WARNING**: Breaking change

The 2.0.0 release requires Python 3.6+.

## Method Calls
> **WARNING**: Breaking change

Methods expect request objects. We provide a script that will convert most common use cases.

* Install the library
```sh
$ python3 -m pip install google-cloud-dialogflow
```
* The script fixup_keywords.py is shipped with the library. It expects an input directory (with the code to convert) and an empty destination directory.

```sh
$ fixup_dialogflow_v2_keywords.py --input-directory .samples/ --output-directory samples/
```
**Before:**

```py
import dialogflow
client = dialogflow.ContextsClient()

response = client.list_contexts(parent="projects/1337/agent/sessions/1024")
```

**After:**
```py
from google.cloud import dialogflow

client = dialogflow.ContextsClient()

response = client.list_contexts(request={"parent": "projects/1337/agent/sessions/1024", page_size=10})
```

## Package import and naming
> **WARNING**: Breaking change

The 2.0.0 release changes the name and import path of the library to fall under the google-cloud namespace.

**Before:**

```sh
python3 -m pip install dialogflow
```

```py
import dialogflow
```

**After:**

```sh
python3 -m pip install google-cloud-dialogflow
```

```py
from google.cloud import dialogflow
```


### More Details
In google-cloud-dialogflow<2.0.0, parameters required by the API were positional parameters and optional parameters were keyword parameters.

**Before:**
```py
    def detect_intent(
        self,
        session,
        query_input,
        query_params=None,
        output_audio_config=None,
        output_audio_config_mask=None,
        input_audio=None,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
```

In the 2.0.0 release, all methods have a single positional parameter request. Method docstrings indicate whether a parameter is required or optional.

Some methods have additional keyword only parameters. The available parameters depend on the [`google.api.method_signature` annotation](https://github.com/googleapis/googleapis/blob/master/google/cloud/translate/v3/translation_service.proto#L55) specified by the API producer.

**After:**:
```py
    def detect_intent(self,
        request=None,
        *,
        session: str=None,
        query_input=None,
        retry=gapic_v1.method.DEFAULT,
        timeout=None,
        metadata=(),
    ):
```

> **NOTE:** The `request` parameter and flattened keyword parameters for the API are mutually exclusive. Passing both will result in an error.

Both of these calls are valid:
```py
response = client.create_context(
    request={
        "parent": "parent_value",
        "context": dialogflow.Context(name="name_value"),
    }
)
response = client.create_context(
    parent="parent_value",
    context=dialogflow.Context(name="name_value"),
)
```

This call is invalid because it mixes `request` with a keyword argument `audio_config`. Executing this code will result in an error.

```py
response = client.create_context(
    request={
        "parent": "parent_value",
    },
    context=dialogflow.Context(name="name_value"),
)
```

## Enums and Types

> **WARNING:** Breaking change

The submodules `enums` and `types` have been removed in the versionless module.

**Before:**

```py
import dialogflow

encoding = dialogflow.enums.AudioEncoding.AUDIO_ENCODING_FLAC
query_params = dialogflow.types.QueryParameters(time_zone="Europe/Paris")
```

**After:**

```py
from google.cloud import dialogflow

encoding = dialogflow.AudioEncoding.AUDIO_ENCODING_FLAC
query_params = dialogflow.QueryParameters(time_zone="Europe/Paris")
```

The `types` submodule is still present in the versioned module.

E.g.

```py
from google.cloud import dialogvlow_v2

query_params = dialogvlow_v2.types.QueryParameters(time_zone="Europe/Paris")
```

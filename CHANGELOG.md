# Changelog

[PyPI History][1]

[1]: https://pypi.org/project/dialogflow/#history

### [0.7.2](https://www.github.com/googleapis/dialogflow-python-client-v2/compare/v0.7.1...v0.7.2) (2019-10-18)


### Bug Fixes

* define version once in setup.py ([#158](https://www.github.com/googleapis/dialogflow-python-client-v2/issues/158)) ([bf42fc4](https://www.github.com/googleapis/dialogflow-python-client-v2/commit/bf42fc45607b97bc040cbdacbde8ff5a4b6ad29b))

### [0.7.1](https://www.github.com/googleapis/dialogflow-python-client-v2/compare/v0.7.0...v0.7.1) (2019-10-17)


### Bug Fixes

* pin google-api-core>=1.14.0, update format ([#156](https://www.github.com/googleapis/dialogflow-python-client-v2/issues/156)) ([69951d0](https://www.github.com/googleapis/dialogflow-python-client-v2/commit/69951d013b7c99966848565e30d5ab1bad7229fb))

## [0.7.0](https://www.github.com/googleapis/dialogflow-python-client-v2/compare/v0.6.0...v0.7.0) (2019-10-16)


### Features

* regenerate ([#151](https://www.github.com/googleapis/dialogflow-python-client-v2/issues/151)) ([6222277](https://www.github.com/googleapis/dialogflow-python-client-v2/commit/6222277a5332011e9cc2e80bb5b26692a12fad36))
  #### v2 and v2beta1
  * Add `set_agent` and `delete_agent` methods to  `AgentsClient`
  * Add `api_version` and `tier` to `Agents`
  * Add `session_entity_types` to `WebhookResponse`
  * Add `model_variant` and `single_utterance` to `InputAudioConfig`
  * Add `SpeechModelVariant` enum
  * Add `enable_fuzzy_extraction` to `EntityType`
  * Add `KIND_REGEXP` to `EntityType.Kind` enum
  * Add `client_options` to clients
  * Allow kwargs to be passed to transport `create_channel` methods
  * Deprecate `single_utterance` attribute in `StreamingDetectIntentRequest`. Please use `InputAudioConfig.single_utterance`

  #### v2
  * Add Google Hangouts to `Message.Platform` enum

  #### v2beta1 
  * Add `get_validation_result` method to `AgentsClient`
  * Add `gcs_source` and `source` to `reload_document` method in `DocumentsClient`
  * Add Rich Business Messaging (RBM) support, `table_card`, and `media_content` to intent messages
  * Add `enable_word_info`, `speech_contexts` to `InputAudioConfig`
  * `update_document` returns `_OperationFuture` rather than `Operation`
  * Deprecate `projects.agent.knowledgeBases`. Please use `projects.knowledgeBases`.
  * Add `stability`, `speech_word_info` and `speech_end_offset` to `StreamingRecognitionResult`

## 0.6.0

05-06-2019 1:34 PST

### Implementation Changes

- Add routing header to method metadata.([#123](https://github.com/googleapis/dialogflow-python-client-v2/pull/112))
- Warn when deprecated client_config argument is used. ([#123](https://github.com/googleapis/dialogflow-python-client-v2/pull/112))
- Add https://www.googleapis.com/auth/dialogflow OAuth scope. ([#123](https://github.com/googleapis/dialogflow-python-client-v2/pull/112))
- Add channel to gRPC transport classes. ([#123](https://github.com/googleapis/dialogflow-python-client-v2/pull/112))

### Features

- Add argument output_audio_config to detect_intent. ([#123](https://github.com/googleapis/dialogflow-python-client-v2/pull/112))
- Add update_knowledge_base method. ([#123](https://github.com/googleapis/dialogflow-python-client-v2/pull/112))
- Add update_document and reload_document methods. ([#123](https://github.com/googleapis/dialogflow-python-client-v2/pull/112))

### Documentation:
- Change copyright year to 2019. ([#123](https://github.com/googleapis/dialogflow-python-client-v2/pull/112))

### Internal / Testing Changes
- Use mock to patch create_channel in unit tests. ([#123](https://github.com/googleapis/dialogflow-python-client-v2/pull/112))

## 0.5.2

12-18-2018 10:50 PST

### Documentation
- Add notice of Python 2.7 deprecation ([#112](https://github.com/googleapis/dialogflow-python-client-v2/pull/112))
- Fix typo in samples ([#52](https://github.com/googleapis/dialogflow-python-client-v2/pull/52))
- Update README.rst ([#27](https://github.com/googleapis/dialogflow-python-client-v2/pull/27))
- Updating README per ask from Product ([#81](https://github.com/googleapis/dialogflow-python-client-v2/pull/81))
- Add v2beta1 samples for dialogflow and update v2 sample formatting. ([#72](https://github.com/googleapis/dialogflow-python-client-v2/pull/72))

### Internal / Testing Changes
- Update github issue templates ([#103](https://github.com/googleapis/dialogflow-python-client-v2/pull/103))
- Strip dynamic badges from README ([#99](https://github.com/googleapis/dialogflow-python-client-v2/pull/99))
- Correct the repository name in samples README. ([#83](https://github.com/googleapis/dialogflow-python-client-v2/pull/83))
- Fix [#76](https://github.com/googleapis/dialogflow-python-client-v2/pull/76) by adding replacement patterns to dialogflow ([#79](https://github.com/googleapis/dialogflow-python-client-v2/pull/79))

## 0.4.0
- Regenerate v2beta1 endpoint

## 0.3.0
- Regenerate v2 endpoint
- Update documentation comments

## 0.2.0

### New Features
- Add v2 Endpoint (#38)

### Documentation
- Add sample readme, and sample agent (#15)

### Internal / Testing Changes
- Fix typo (#16)

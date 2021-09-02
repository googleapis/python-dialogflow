TEST_CONFIG_OVERRIDE = {
    # An envvar key for determining the project id to use. Change it
    # to 'BUILD_SPECIFIC_GCLOUD_PROJECT' if you want to opt in using a
    # build specific Cloud project. You can also use your own string
    # to use your own Cloud project.
    "gcloud_project_env": "BUILD_SPECIFIC_GCLOUD_PROJECT",
    # A dictionary you want to inject into your test. Don't put any
    # secrets here. These values will override predefined values.
    'envs': {},
}
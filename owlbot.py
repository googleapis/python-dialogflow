# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""This script is used to synthesize generated parts of this library."""

import synthtool as s
from synthtool import gcp
from synthtool.languages import python

common = gcp.CommonTemplates()

default_version = "v2"

for library in s.get_staging_dirs(default_version):
    # Work around gapic generator bug
    s.replace(
        library / f"google/cloud/dialogflow_{library.name}/services/**/client.py",
        "warnings.DeprecationWarning",
        "DeprecationWarning"
    )

    s.move(library, excludes=["docs/index.rst", "setup.py", "README.rst"])

s.remove_staging_dirs()

# # ----------------------------------------------------------------------------
# # Add templated files
# # ----------------------------------------------------------------------------
templated_files = common.py_library(
python.py_samples(skip_readmes=True)
    samples=False,  # set to True only if there are samples
    microgenerator=True,
    cov_level=98,

)
s.move(templated_files, excludes=[".coveragerc"])  # microgenerator has a good .coveragerc file

# Don't treat warnings as errors
# Docstrings have unexpected idnentation and block quote formatting issues
s.replace(
    "noxfile.py",
    '''["']-W["'],  # warnings as errors''',
    "",
)

s.shell.run(["nox", "-s", "blacken"], hide_output=False)

# ----------------------------------------------------------------------------
# Main Branch migration
# ----------------------------------------------------------------------------

s.replace(
  "*.rst",
  "master",
  "main"
)

s.replace(
  "CONTRIBUTING.rst",
  "kubernetes/community/blob/main",
  "kubernetes/community/blob/master"
)

s.replace(
  "docs/conf.py",
  "master",
  "main"
)

s.replace(
  "docs/conf.py",
  "main_doc",
  "root_doc"
)

s.replace(
  ".kokoro/*",
  "master",
  "main"
)

s.replace(
  "samples/*",
  "master",
  "main"
)

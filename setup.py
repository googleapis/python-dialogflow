# Copyright 2019 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import io
import os

import setuptools

name = "dialogflow"
description = "Client library for the Dialogflow API"
version = "0.7.2"
release_status = "Development Status :: 4 - Beta"
dependencies = ["google-api-core[grpc] >= 1.14.0, < 2.0.0dev"]

package_root = os.path.abspath(os.path.dirname(__file__))

readme_filename = os.path.join(package_root, "README.rst")
with io.open(readme_filename, encoding="utf-8") as readme_file:
    readme = readme_file.read()

packages = setuptools.find_packages()

setuptools.setup(
    name="dialogflow",
    version=version,
    author="Google LLC",
    author_email="googleapis-packages@google.com",
    license="Apache 2.0",
    url="https://github.com/dialogflow/dialogflow-python-client-v2",
    classifiers=[
        release_status,
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: Implementation :: CPython",
    ],
    platforms="Posix; MacOS X; Windows",
    packages=packages,
    install_requires=dependencies,
    python_requires=">=2.7,!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*",
    include_package_data=True,
    zip_safe=False,
)

# Copyright 2022, Google LLC
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Test validate webhook session logging snippet."""

import flask
import pytest

from webhook_log_session_info import log_session_id_for_troubleshooting


@pytest.fixture(name="app", scope="module")
def fixture_app():
    """Flask fixture to pass a flask.Request to the test function"""
    return flask.Flask(__name__)


@pytest.fixture
def agent():
    return "test-agent"


@pytest.fixture
def session_id():
    return "d0bdaa0c-0d00-0000-b0eb-b00b0db000b0"


@pytest.fixture
def environment():
    return "0d0000f0-0aac-0d0c-0a00-b00b0000a000"


@pytest.fixture
def session(agent, session_id):
    """Session string

    format: projects/*/<agent>/sessions/<session id>
    """
    return f"projects/test_project/{agent}/sessions/{session_id}"


@pytest.fixture
def session_loc_path(agent, session_id):
    """Session string

    format: projects/*/locations/*/<agent>/sessions/<session id>
    """
    return f"projects/test_project/locations/us-central1/{agent}/sessions/{session_id}"


@pytest.fixture
def session_env_user_path(environment, agent, session_id):
    """Session string

    format: projects/*/<agent>/environments/*/users/*/sessions/<session id>
    """
    return f"projects/test_project/{agent}/environments/{environment}/users/-/sessions/{session_id}"


@pytest.fixture
def session_loc_env_user_path(environment, agent, session_id):
    """Session string

    format: projects/*/locations/*/<agent>/environments/*/users/*/sessions/<session id>
    """
    return f"projects/test_project/locations/us-central1/{agent}/environments/{environment}/users/-/sessions/{session_id}"


def test_logging_session(app, session, session_id):
    """Parameterized test for `projects/<Project ID>/agent/sessions/<Session ID>` type session string."""
    request = {"session": session}
    with app.test_request_context(json=request):
        res = log_session_id_for_troubleshooting(flask.request)
        assert session_id in str(res)


def test_logging_session_with_loc_path(app, session_loc_path, session_id):
    """Parameterized test for `projects//locations//agent/sessions/` type session string."""
    request = {"session": session_loc_path}
    with app.test_request_context(json=request):
        res = log_session_id_for_troubleshooting(flask.request)
        assert session_id in str(res)


def test_logging_session_with_env_user_path(app, session_env_user_path,
                                            session_id):
    """Parameterized test for `projects//agent/environments//users//sessions/` type session string."""
    request = {"session": session_env_user_path}
    with app.test_request_context(json=request):
        res = log_session_id_for_troubleshooting(flask.request)
        assert session_id in str(res)


def test_logging_session_with_loc_env_user_path(app, session_loc_env_user_path,
                                                session_id):
    """Parameterized test for `projects//locations//agent/environments//users//sessions/` type session string."""
    request = {"session": session_loc_env_user_path}
    with app.test_request_context(json=request):
        res = log_session_id_for_troubleshooting(flask.request)
        assert session_id in str(res)

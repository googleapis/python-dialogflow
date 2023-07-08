# -*- coding: utf-8 -*-
# Copyright 2023 Google LLC
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
#
from typing import Any, AsyncIterator, Awaitable, Callable, Sequence, Tuple, Optional, Iterator

from google.cloud.dialogflow_v2.types import conversation_model


class ListConversationModelsPager:
    """A pager for iterating through ``list_conversation_models`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.dialogflow_v2.types.ListConversationModelsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``conversation_models`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListConversationModels`` requests and continue to iterate
    through the ``conversation_models`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.dialogflow_v2.types.ListConversationModelsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """
    def __init__(self,
            method: Callable[..., conversation_model.ListConversationModelsResponse],
            request: conversation_model.ListConversationModelsRequest,
            response: conversation_model.ListConversationModelsResponse,
            *,
            metadata: Sequence[Tuple[str, str]] = ()):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.dialogflow_v2.types.ListConversationModelsRequest):
                The initial request object.
            response (google.cloud.dialogflow_v2.types.ListConversationModelsResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = conversation_model.ListConversationModelsRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[conversation_model.ListConversationModelsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(self._request, metadata=self._metadata)
            yield self._response

    def __iter__(self) -> Iterator[conversation_model.ConversationModel]:
        for page in self.pages:
            yield from page.conversation_models

    def __repr__(self) -> str:
        return '{0}<{1!r}>'.format(self.__class__.__name__, self._response)


class ListConversationModelsAsyncPager:
    """A pager for iterating through ``list_conversation_models`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.dialogflow_v2.types.ListConversationModelsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``conversation_models`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListConversationModels`` requests and continue to iterate
    through the ``conversation_models`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.dialogflow_v2.types.ListConversationModelsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """
    def __init__(self,
            method: Callable[..., Awaitable[conversation_model.ListConversationModelsResponse]],
            request: conversation_model.ListConversationModelsRequest,
            response: conversation_model.ListConversationModelsResponse,
            *,
            metadata: Sequence[Tuple[str, str]] = ()):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.dialogflow_v2.types.ListConversationModelsRequest):
                The initial request object.
            response (google.cloud.dialogflow_v2.types.ListConversationModelsResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = conversation_model.ListConversationModelsRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[conversation_model.ListConversationModelsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = await self._method(self._request, metadata=self._metadata)
            yield self._response
    def __aiter__(self) -> AsyncIterator[conversation_model.ConversationModel]:
        async def async_generator():
            async for page in self.pages:
                for response in page.conversation_models:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return '{0}<{1!r}>'.format(self.__class__.__name__, self._response)


class ListConversationModelEvaluationsPager:
    """A pager for iterating through ``list_conversation_model_evaluations`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.dialogflow_v2.types.ListConversationModelEvaluationsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``conversation_model_evaluations`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListConversationModelEvaluations`` requests and continue to iterate
    through the ``conversation_model_evaluations`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.dialogflow_v2.types.ListConversationModelEvaluationsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """
    def __init__(self,
            method: Callable[..., conversation_model.ListConversationModelEvaluationsResponse],
            request: conversation_model.ListConversationModelEvaluationsRequest,
            response: conversation_model.ListConversationModelEvaluationsResponse,
            *,
            metadata: Sequence[Tuple[str, str]] = ()):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.dialogflow_v2.types.ListConversationModelEvaluationsRequest):
                The initial request object.
            response (google.cloud.dialogflow_v2.types.ListConversationModelEvaluationsResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = conversation_model.ListConversationModelEvaluationsRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[conversation_model.ListConversationModelEvaluationsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(self._request, metadata=self._metadata)
            yield self._response

    def __iter__(self) -> Iterator[conversation_model.ConversationModelEvaluation]:
        for page in self.pages:
            yield from page.conversation_model_evaluations

    def __repr__(self) -> str:
        return '{0}<{1!r}>'.format(self.__class__.__name__, self._response)


class ListConversationModelEvaluationsAsyncPager:
    """A pager for iterating through ``list_conversation_model_evaluations`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.dialogflow_v2.types.ListConversationModelEvaluationsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``conversation_model_evaluations`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListConversationModelEvaluations`` requests and continue to iterate
    through the ``conversation_model_evaluations`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.dialogflow_v2.types.ListConversationModelEvaluationsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """
    def __init__(self,
            method: Callable[..., Awaitable[conversation_model.ListConversationModelEvaluationsResponse]],
            request: conversation_model.ListConversationModelEvaluationsRequest,
            response: conversation_model.ListConversationModelEvaluationsResponse,
            *,
            metadata: Sequence[Tuple[str, str]] = ()):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.dialogflow_v2.types.ListConversationModelEvaluationsRequest):
                The initial request object.
            response (google.cloud.dialogflow_v2.types.ListConversationModelEvaluationsResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = conversation_model.ListConversationModelEvaluationsRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[conversation_model.ListConversationModelEvaluationsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = await self._method(self._request, metadata=self._metadata)
            yield self._response
    def __aiter__(self) -> AsyncIterator[conversation_model.ConversationModelEvaluation]:
        async def async_generator():
            async for page in self.pages:
                for response in page.conversation_model_evaluations:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return '{0}<{1!r}>'.format(self.__class__.__name__, self._response)

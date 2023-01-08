# coding: utf-8
"""
<copyright company="Aspose" file="CellsDevApi.cs">
  Copyright (c) 2023 Aspose.Cells Dev
</copyright>
<summary>
 Permission is hereby granted, free of charge, to any person obtaining a copy
 of this software and associated documentation files (the "Software"), to deal
 in the Software without restriction, including without limitation the rights
 to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 copies of the Software, and to permit persons to whom the Software is
 furnished to do so, subject to the following conditions:

 The above copyright notice and this permission notice shall be included in all
 copies or substantial portions of the Software.

 THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
 SOFTWARE.
</summary>
"""

from __future__ import absolute_import

import sys
import os
import re
import time

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class CellsDevApi(object):

    def __init__(self, base_uri= 'https://api.aspose.dev',version='v1.0'):

        self.version = version 
        if base_uri[-1] == '/' :
            self.base_uri = base_uri[0:len(base_uri)-1]
        else:
            self.base_uri = base_uri

        self.api_client =  ApiClient(self.base_uri +'/' + self.version)

        config = Configuration()
        config.host = self.base_uri +'/' + self.version


    # <summary>
    # </summary>
    # <param name="request">Request. <see cref="GetHealthStatusRequest" /></param>
    def get_health_status(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_health_status_with_http_info(request,**kwargs)
        else:
            (data) = self.get_health_status_with_http_info(request,**kwargs)
            return data    

    # <summary>
    # </summary>
    # <param name="request">Request. <see cref="PostSearchRequest" /></param>
    def post_search(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.post_search_with_http_info(request,**kwargs)
        else:
            (data) = self.post_search_with_http_info(request,**kwargs)
            return data    

    # <summary>
    # </summary>
    # <param name="request">Request. <see cref="PostReplaceRequest" /></param>
    def post_replace(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.post_replace_with_http_info(request,**kwargs)
        else:
            (data) = self.post_replace_with_http_info(request,**kwargs)
            return data    

    # <summary>
    # </summary>
    # <param name="request">Request. <see cref="PostConvertWorkbookRequest" /></param>
    def post_convert_workbook(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.post_convert_workbook_with_http_info(request,**kwargs)
        else:
            (data) = self.post_convert_workbook_with_http_info(request,**kwargs)
            return data    

    # <summary>
    # </summary>
    # <param name="request">Request. <see cref="PostMergeRequest" /></param>
    def post_merge(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.post_merge_with_http_info(request,**kwargs)
        else:
            (data) = self.post_merge_with_http_info(request,**kwargs)
            return data    

    # <summary>
    # </summary>
    # <param name="request">Request. <see cref="PostEncryptWithPasswordRequest" /></param>
    def post_encrypt_with_password(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.post_encrypt_with_password_with_http_info(request,**kwargs)
        else:
            (data) = self.post_encrypt_with_password_with_http_info(request,**kwargs)
            return data    

    # <summary>
    # </summary>
    # <param name="request">Request. <see cref="PostDecryptWithPasswordRequest" /></param>
    def post_decrypt_with_password(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.post_decrypt_with_password_with_http_info(request,**kwargs)
        else:
            (data) = self.post_decrypt_with_password_with_http_info(request,**kwargs)
            return data    

    # <summary>
    # </summary>
    # <param name="request">Request. <see cref="PostDigitalSignatureRequest" /></param>
    def post_digital_signature(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.post_digital_signature_with_http_info(request,**kwargs)
        else:
            (data) = self.post_digital_signature_with_http_info(request,**kwargs)
            return data    

    # <summary>
    # </summary>
    # <param name="request">Request. <see cref="PostSplitRequest" /></param>
    def post_split(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.post_split_with_http_info(request,**kwargs)
        else:
            (data) = self.post_split_with_http_info(request,**kwargs)
            return data    
    def get_health_status_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_health_status" % key
                )
            params[key] = val
        del params['kwargs'] 


        collection_formats = {}

        path_params = {}
        query_params = []
        header_params = {}

        form_params = []
        local_var_files = {}

        body_params =  params['request']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/cells', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='str',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def post_search_with_http_info(self, request, **kwargs):
        all_params = ['request' ]
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_search" % key
                )
            params[key] = val
        del params['kwargs'] 

        # verify the required parameter 'request' is set
        if ('request' not in params) or (params['request'] is None):
            raise ValueError("Missing the required parameter `request` when calling `post_search`")


        collection_formats = {}

        path_params = {}
        query_params = []
        header_params = {}

        form_params = []
        local_var_files = {}

        body_params =  params['request']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/cells/content/search', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='TextItems',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def post_replace_with_http_info(self, request, **kwargs):
        all_params = ['request' ]
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_replace" % key
                )
            params[key] = val
        del params['kwargs'] 

        # verify the required parameter 'request' is set
        if ('request' not in params) or (params['request'] is None):
            raise ValueError("Missing the required parameter `request` when calling `post_replace`")


        collection_formats = {}

        path_params = {}
        query_params = []
        header_params = {}

        form_params = []
        local_var_files = {}

        body_params =  params['request']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/cells/content/replace', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='ResponseFiles',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def post_convert_workbook_with_http_info(self, request, **kwargs):
        all_params = ['request' ]
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_convert_workbook" % key
                )
            params[key] = val
        del params['kwargs'] 

        # verify the required parameter 'request' is set
        if ('request' not in params) or (params['request'] is None):
            raise ValueError("Missing the required parameter `request` when calling `post_convert_workbook`")


        collection_formats = {}

        path_params = {}
        query_params = []
        header_params = {}

        form_params = []
        local_var_files = {}

        body_params =  params['request']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/cells/convert', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='ResponseFiles',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def post_merge_with_http_info(self, request, **kwargs):
        all_params = ['request' ]
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_merge" % key
                )
            params[key] = val
        del params['kwargs'] 

        # verify the required parameter 'request' is set
        if ('request' not in params) or (params['request'] is None):
            raise ValueError("Missing the required parameter `request` when calling `post_merge`")


        collection_formats = {}

        path_params = {}
        query_params = []
        header_params = {}

        form_params = []
        local_var_files = {}

        body_params =  params['request']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/cells/merge', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='ResponseFile',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def post_encrypt_with_password_with_http_info(self, request, **kwargs):
        all_params = ['request' ]
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_encrypt_with_password" % key
                )
            params[key] = val
        del params['kwargs'] 

        # verify the required parameter 'request' is set
        if ('request' not in params) or (params['request'] is None):
            raise ValueError("Missing the required parameter `request` when calling `post_encrypt_with_password`")


        collection_formats = {}

        path_params = {}
        query_params = []
        header_params = {}

        form_params = []
        local_var_files = {}

        body_params =  params['request']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/cells/protect/encrypt-with-password', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='ResponseFiles',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def post_decrypt_with_password_with_http_info(self, request, **kwargs):
        all_params = ['request' ]
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_decrypt_with_password" % key
                )
            params[key] = val
        del params['kwargs'] 

        # verify the required parameter 'request' is set
        if ('request' not in params) or (params['request'] is None):
            raise ValueError("Missing the required parameter `request` when calling `post_decrypt_with_password`")


        collection_formats = {}

        path_params = {}
        query_params = []
        header_params = {}

        form_params = []
        local_var_files = {}

        body_params =  params['request']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/cells/protect/decrypt-with-password', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='ResponseFiles',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def post_digital_signature_with_http_info(self, request, **kwargs):
        all_params = ['request' ]
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_digital_signature" % key
                )
            params[key] = val
        del params['kwargs'] 

        # verify the required parameter 'request' is set
        if ('request' not in params) or (params['request'] is None):
            raise ValueError("Missing the required parameter `request` when calling `post_digital_signature`")


        collection_formats = {}

        path_params = {}
        query_params = []
        header_params = {}

        form_params = []
        local_var_files = {}

        body_params =  params['request']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/cells/protect/digital-signature', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='ResponseFiles',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def post_split_with_http_info(self, request, **kwargs):
        all_params = ['request' ]
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_split" % key
                )
            params[key] = val
        del params['kwargs'] 

        # verify the required parameter 'request' is set
        if ('request' not in params) or (params['request'] is None):
            raise ValueError("Missing the required parameter `request` when calling `post_split`")


        collection_formats = {}

        path_params = {}
        query_params = []
        header_params = {}

        form_params = []
        local_var_files = {}

        body_params =  params['request']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/cells/split', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='ResponseFiles',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
        
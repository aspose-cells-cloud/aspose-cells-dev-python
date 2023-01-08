# coding: utf-8
"""
<copyright company="Aspose" file="AuthUtilpy.cs">
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
import os
import sys
import base64

ABSPATH = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/..")
sys.path.append(ABSPATH)

import asposecellsdev
from asposecellsdev.models.request_file import RequestFile
from asposecellsdev.models.digital_signatur_file import DigitalSignaturFile

grantType = "client_credentials"
clientId = os.getenv('CellsCloudTestClientId')
clientSecret = os.getenv('CellsCloudTestClientSecret')
def GetBaseUrl():
    return os.getenv('CellsCloudTestApiBaseUrl')


api_client = None




def get_request_file( filename): 
    requestFile = RequestFile()
    requestFile.name = filename
    filepath = ABSPATH +"\\TestData\\" + filename
    with open(filepath, 'rb') as f1:
        base64_str = base64.b64encode(f1.read())  # base64类型
        #  b'JVBERi0xLjUNCiXi48
        requestFile.data = base64_str.decode('utf-8')          
    return requestFile

def get_digital_signatur_file( filename, password): 
    digitalSignaturFile = DigitalSignaturFile()
    digitalSignaturFile.name = filename
    digitalSignaturFile.password = password
    filepath = ABSPATH +"\\TestData\\" + filename
    with open(filepath, 'rb') as f1:
        base64_str = base64.b64encode(f1.read())  # base64类型
        #  b'JVBERi0xLjUNCiXi48
        digitalSignaturFile.data = base64_str.decode('utf-8')         
    return digitalSignaturFile

def get_request_files( *args): 
    requestFiles = []
    requestFile = RequestFile()
    for filename in args:
        requestFile.name = filename
        filepath = ABSPATH +"\\TestData\\" + filename
        with open(filepath, 'rb') as f1:
            base64_str = base64.b64encode(f1.read())  
            requestFile.data = base64_str.decode('utf-8')    
        requestFiles.append(requestFile)      
    return requestFiles


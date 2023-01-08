# coding: utf-8

from __future__ import absolute_import

import os
import sys
import unittest
import warnings

ABSPATH = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/..")
sys.path.append(ABSPATH)

import asposecellsdev
from asposecellsdev.rest import ApiException
from asposecellsdev.apis.cells_dev_api import CellsDevApi

from asposecellsdev.models.convert_request import ConvertRequest
from asposecellsdev.models.digital_signatur_file import DigitalSignaturFile
from asposecellsdev.models.digital_signatur_request import DigitalSignaturRequest
from asposecellsdev.models.merge_request import MergeRequest
from asposecellsdev.models.protection_request import ProtectionRequest
from asposecellsdev.models.replace_request import ReplaceRequest
from asposecellsdev.models.request_file import RequestFile
from asposecellsdev.models.request_parameter import RequestParameter
from asposecellsdev.models.response_file import ResponseFile
from asposecellsdev.models.response_files import ResponseFiles
from asposecellsdev.models.search_request import SearchRequest
from asposecellsdev.models.split_request import SplitRequest
from asposecellsdev.models.text_item import TextItem
from asposecellsdev.models.text_items import TextItems

from AuthUtil import *

global_api = None

class TestControllersApi(unittest.TestCase):
    def setUp(self):
        warnings.simplefilter('ignore', ResourceWarning)
        global global_api
        if global_api is None:
           global_api = CellsDevApi("http://192.168.3.38:15000/","v1.0")
        self.api = global_api

    def tearDown(self):
        pass

    def test_post_convert_workbook_pdf(self):
        remoteFolder = 'TestData/In'

        localBook1 = 'Book1.xlsx'
        localMyDoc = 'myDocument.xlsx'

        format = "pdf"

     
        request = ConvertRequest()
        request.format = format 
         
        request.files =[]        
        request.files.append(get_request_file(localBook1))

        request.files.append(get_request_file(localMyDoc))

         

        actual =  self.api.post_convert_workbook(request)
        self.assertIsNotNone(actual,"")


    def test_post_convert_workbook_docx(self):
        remoteFolder = 'TestData/In'

        localBook1 = 'Book1.xlsx'
        localMyDoc = 'myDocument.xlsx'

        format = "docx"

     
        request = ConvertRequest()
        request.format = format 
         
        request.files =[]        
        request.files.append(get_request_file(localBook1))

        request.files.append(get_request_file(localMyDoc))

         

        actual =  self.api.post_convert_workbook(request)
        self.assertIsNotNone(actual,"")


    def test_post_convert_workbook_pptx(self):
        remoteFolder = 'TestData/In'

        localBook1 = 'Book1.xlsx'
        localMyDoc = 'myDocument.xlsx'

        format = "pptx"

     
        request = ConvertRequest()
        request.format = format 
         
        request.files =[]        
        request.files.append(get_request_file(localBook1))

        request.files.append(get_request_file(localMyDoc))

         

        actual =  self.api.post_convert_workbook(request)
        self.assertIsNotNone(actual,"")


    def test_post_convert_workbook_json(self):
        remoteFolder = 'TestData/In'

        localBook1 = 'Book1.xlsx'
        localMyDoc = 'myDocument.xlsx'

        format = "json"

     
        request = ConvertRequest()
        request.format = format 
         
        request.files =[]        
        request.files.append(get_request_file(localBook1))

        request.files.append(get_request_file(localMyDoc))

         

        actual =  self.api.post_convert_workbook(request)
        self.assertIsNotNone(actual,"")


    def test_post_convert_workbook_markdown(self):
        remoteFolder = 'TestData/In'

        localBook1 = 'Book1.xlsx'
        localMyDoc = 'myDocument.xlsx'

        format = "markdown"

     
        request = ConvertRequest()
        request.format = format 
         
        request.files =[]        
        request.files.append(get_request_file(localBook1))

        request.files.append(get_request_file(localMyDoc))

         

        actual =  self.api.post_convert_workbook(request)
        self.assertIsNotNone(actual,"")


    def test_post_convert_workbook_png(self):
        remoteFolder = 'TestData/In'

        localBook1 = 'Book1.xlsx'
        localMyDoc = 'myDocument.xlsx'

        format = "png"

     
        request = ConvertRequest()
        request.format = format 
         
        request.files =[]        
        request.files.append(get_request_file(localBook1))

        request.files.append(get_request_file(localMyDoc))

         

        actual =  self.api.post_convert_workbook(request)
        self.assertIsNotNone(actual,"")


    def test_post_convert_workbook_ods(self):
        remoteFolder = 'TestData/In'

        localBook1 = 'Book1.xlsx'
        localMyDoc = 'myDocument.xlsx'

        format = "ods"

     
        request = ConvertRequest()
        request.format = format 
         
        request.files =[]        
        request.files.append(get_request_file(localBook1))

        request.files.append(get_request_file(localMyDoc))

         

        actual =  self.api.post_convert_workbook(request)
        self.assertIsNotNone(actual,"")


    def test_post_convert_workbook_numbers(self):
        remoteFolder = 'TestData/In'

        localBook1 = 'Book1.xlsx'
        localMyDoc = 'myDocument.xlsx'

        format = "numbers"

     
        request = ConvertRequest()
        request.format = format 
         
        request.files =[]        
        request.files.append(get_request_file(localBook1))

        request.files.append(get_request_file(localMyDoc))

         

        actual =  self.api.post_convert_workbook(request)
        self.assertIsNotNone(actual,"")


    def test_post_convert_workbook_html(self):
        remoteFolder = 'TestData/In'

        localBook1 = 'Book1.xlsx'
        localMyDoc = 'myDocument.xlsx'

        format = "html"

     
        request = ConvertRequest()
        request.format = format 
         
        request.files =[]        
        request.files.append(get_request_file(localBook1))

        request.files.append(get_request_file(localMyDoc))

         

        actual =  self.api.post_convert_workbook(request)
        self.assertIsNotNone(actual,"")


    def test_post_merge_pdf(self):
        remoteFolder = 'TestData/In'

        localBook1 = 'Book1.xlsx'
        localMyDoc = 'myDocument.xlsx'

        format = "pdf"

     
        request = MergeRequest()
        request.format = format 
        request.in_one_sheet = True 
         
        request.files =[]        
        request.files.append(get_request_file(localBook1))

        request.files.append(get_request_file(localMyDoc))

         

        actual =  self.api.post_merge(request)
        self.assertIsNotNone(actual,"")


    def test_post_merge_docx(self):
        remoteFolder = 'TestData/In'

        localBook1 = 'Book1.xlsx'
        localMyDoc = 'myDocument.xlsx'

        format = "docx"

     
        request = MergeRequest()
        request.format = format 
        request.in_one_sheet = True 
         
        request.files =[]        
        request.files.append(get_request_file(localBook1))

        request.files.append(get_request_file(localMyDoc))

         

        actual =  self.api.post_merge(request)
        self.assertIsNotNone(actual,"")


    def test_post_merge_pptx(self):
        remoteFolder = 'TestData/In'

        localBook1 = 'Book1.xlsx'
        localMyDoc = 'myDocument.xlsx'

        format = "pptx"

     
        request = MergeRequest()
        request.format = format 
        request.in_one_sheet = True 
         
        request.files =[]        
        request.files.append(get_request_file(localBook1))

        request.files.append(get_request_file(localMyDoc))

         

        actual =  self.api.post_merge(request)
        self.assertIsNotNone(actual,"")


    def test_post_merge_json(self):
        remoteFolder = 'TestData/In'

        localBook1 = 'Book1.xlsx'
        localMyDoc = 'myDocument.xlsx'

        format = "json"

     
        request = MergeRequest()
        request.format = format 
        request.in_one_sheet = True 
         
        request.files =[]        
        request.files.append(get_request_file(localBook1))

        request.files.append(get_request_file(localMyDoc))

         

        actual =  self.api.post_merge(request)
        self.assertIsNotNone(actual,"")


    def test_post_merge_markdown(self):
        remoteFolder = 'TestData/In'

        localBook1 = 'Book1.xlsx'
        localMyDoc = 'myDocument.xlsx'

        format = "markdown"

     
        request = MergeRequest()
        request.format = format 
        request.in_one_sheet = True 
         
        request.files =[]        
        request.files.append(get_request_file(localBook1))

        request.files.append(get_request_file(localMyDoc))

         

        actual =  self.api.post_merge(request)
        self.assertIsNotNone(actual,"")


    def test_post_merge_png(self):
        remoteFolder = 'TestData/In'

        localBook1 = 'Book1.xlsx'
        localMyDoc = 'myDocument.xlsx'

        format = "png"

     
        request = MergeRequest()
        request.format = format 
        request.in_one_sheet = True 
         
        request.files =[]        
        request.files.append(get_request_file(localBook1))

        request.files.append(get_request_file(localMyDoc))

         

        actual =  self.api.post_merge(request)
        self.assertIsNotNone(actual,"")


    def test_post_merge_ods(self):
        remoteFolder = 'TestData/In'

        localBook1 = 'Book1.xlsx'
        localMyDoc = 'myDocument.xlsx'

        format = "ods"

     
        request = MergeRequest()
        request.format = format 
        request.in_one_sheet = True 
         
        request.files =[]        
        request.files.append(get_request_file(localBook1))

        request.files.append(get_request_file(localMyDoc))

         

        actual =  self.api.post_merge(request)
        self.assertIsNotNone(actual,"")


    def test_post_merge_numbers(self):
        remoteFolder = 'TestData/In'

        localBook1 = 'Book1.xlsx'
        localMyDoc = 'myDocument.xlsx'

        format = "numbers"

     
        request = MergeRequest()
        request.format = format 
        request.in_one_sheet = True 
         
        request.files =[]        
        request.files.append(get_request_file(localBook1))

        request.files.append(get_request_file(localMyDoc))

         

        actual =  self.api.post_merge(request)
        self.assertIsNotNone(actual,"")


    def test_post_merge_html(self):
        remoteFolder = 'TestData/In'

        localBook1 = 'Book1.xlsx'
        localMyDoc = 'myDocument.xlsx'

        format = "html"

     
        request = MergeRequest()
        request.format = format 
        request.in_one_sheet = True 
         
        request.files =[]        
        request.files.append(get_request_file(localBook1))

        request.files.append(get_request_file(localMyDoc))

         

        actual =  self.api.post_merge(request)
        self.assertIsNotNone(actual,"")


    def test_post_split_pdf(self):
        remoteFolder = 'TestData/In'

        localBook1 = 'Book1.xlsx'
        localMyDoc = 'myDocument.xlsx'

        format = "pdf"

     
        request = SplitRequest()
        request.format = format 
         
        request.files =[]        
        request.files.append(get_request_file(localBook1))

        request.files.append(get_request_file(localMyDoc))

         

        actual =  self.api.post_split(request)
        self.assertIsNotNone(actual,"")


    def test_post_split_docx(self):
        remoteFolder = 'TestData/In'

        localBook1 = 'Book1.xlsx'
        localMyDoc = 'myDocument.xlsx'

        format = "docx"

     
        request = SplitRequest()
        request.format = format 
         
        request.files =[]        
        request.files.append(get_request_file(localBook1))

        request.files.append(get_request_file(localMyDoc))

         

        actual =  self.api.post_split(request)
        self.assertIsNotNone(actual,"")


    def test_post_split_pptx(self):
        remoteFolder = 'TestData/In'

        localBook1 = 'Book1.xlsx'
        localMyDoc = 'myDocument.xlsx'

        format = "pptx"

     
        request = SplitRequest()
        request.format = format 
         
        request.files =[]        
        request.files.append(get_request_file(localBook1))

        request.files.append(get_request_file(localMyDoc))

         

        actual =  self.api.post_split(request)
        self.assertIsNotNone(actual,"")


    def test_post_split_json(self):
        remoteFolder = 'TestData/In'

        localBook1 = 'Book1.xlsx'
        localMyDoc = 'myDocument.xlsx'

        format = "json"

     
        request = SplitRequest()
        request.format = format 
         
        request.files =[]        
        request.files.append(get_request_file(localBook1))

        request.files.append(get_request_file(localMyDoc))

         

        actual =  self.api.post_split(request)
        self.assertIsNotNone(actual,"")


    def test_post_split_markdown(self):
        remoteFolder = 'TestData/In'

        localBook1 = 'Book1.xlsx'
        localMyDoc = 'myDocument.xlsx'

        format = "markdown"

     
        request = SplitRequest()
        request.format = format 
         
        request.files =[]        
        request.files.append(get_request_file(localBook1))

        request.files.append(get_request_file(localMyDoc))

         

        actual =  self.api.post_split(request)
        self.assertIsNotNone(actual,"")


    def test_post_split_png(self):
        remoteFolder = 'TestData/In'

        localBook1 = 'Book1.xlsx'
        localMyDoc = 'myDocument.xlsx'

        format = "png"

     
        request = SplitRequest()
        request.format = format 
         
        request.files =[]        
        request.files.append(get_request_file(localBook1))

        request.files.append(get_request_file(localMyDoc))

         

        actual =  self.api.post_split(request)
        self.assertIsNotNone(actual,"")


    def test_post_split_ods(self):
        remoteFolder = 'TestData/In'

        localBook1 = 'Book1.xlsx'
        localMyDoc = 'myDocument.xlsx'

        format = "ods"

     
        request = SplitRequest()
        request.format = format 
         
        request.files =[]        
        request.files.append(get_request_file(localBook1))

        request.files.append(get_request_file(localMyDoc))

         

        actual =  self.api.post_split(request)
        self.assertIsNotNone(actual,"")


    def test_post_split_numbers(self):
        remoteFolder = 'TestData/In'

        localBook1 = 'Book1.xlsx'
        localMyDoc = 'myDocument.xlsx'

        format = "numbers"

     
        request = SplitRequest()
        request.format = format 
         
        request.files =[]        
        request.files.append(get_request_file(localBook1))

        request.files.append(get_request_file(localMyDoc))

         

        actual =  self.api.post_split(request)
        self.assertIsNotNone(actual,"")


    def test_post_split_html(self):
        remoteFolder = 'TestData/In'

        localBook1 = 'Book1.xlsx'
        localMyDoc = 'myDocument.xlsx'

        format = "html"

     
        request = SplitRequest()
        request.format = format 
         
        request.files =[]        
        request.files.append(get_request_file(localBook1))

        request.files.append(get_request_file(localMyDoc))

         

        actual =  self.api.post_split(request)
        self.assertIsNotNone(actual,"")


    def test_post_search_123(self):
        remoteFolder = 'TestData/In'

        localBook1 = 'Book1.xlsx'
        localMyDoc = 'myDocument.xlsx'

        text = "123"

     
        request = SearchRequest()
        request.text = text 
         
        request.files =[]        
        request.files.append(get_request_file(localBook1))

        request.files.append(get_request_file(localMyDoc))

         

        actual =  self.api.post_search(request)
        self.assertIsNotNone(actual,"")


    def test_post_search_test(self):
        remoteFolder = 'TestData/In'

        localBook1 = 'Book1.xlsx'
        localMyDoc = 'myDocument.xlsx'

        text = "test"

     
        request = SearchRequest()
        request.text = text 
         
        request.files =[]        
        request.files.append(get_request_file(localBook1))

        request.files.append(get_request_file(localMyDoc))

         

        actual =  self.api.post_search(request)
        self.assertIsNotNone(actual,"")


    def test_post_replace_123_456(self):
        remoteFolder = 'TestData/In'

        localBook1 = 'Book1.xlsx'
        localMyDoc = 'myDocument.xlsx'

        new_value = "123"
        old_value = "456"

     
        request = ReplaceRequest()
        request.new_value = new_value 
        request.old_value = old_value 
         
        request.files =[]        
        request.files.append(get_request_file(localBook1))

        request.files.append(get_request_file(localMyDoc))

         

        actual =  self.api.post_replace(request)
        self.assertIsNotNone(actual,"")


    def test_post_replace_testnew_testold(self):
        remoteFolder = 'TestData/In'

        localBook1 = 'Book1.xlsx'
        localMyDoc = 'myDocument.xlsx'

        new_value = "testnew"
        old_value = "testold"

     
        request = ReplaceRequest()
        request.new_value = new_value 
        request.old_value = old_value 
         
        request.files =[]        
        request.files.append(get_request_file(localBook1))

        request.files.append(get_request_file(localMyDoc))

         

        actual =  self.api.post_replace(request)
        self.assertIsNotNone(actual,"")


    def test_post_encrypt_with_password(self):
        remoteFolder = 'TestData/In'

        localBook1 = 'Book1.xlsx'
        localMyDoc = 'myDocument.xlsx'

     
        request = ProtectionRequest()
        request.password = '123456' 
         
        request.files =[]        
        request.files.append(get_request_file(localBook1))

        request.files.append(get_request_file(localMyDoc))

         

        actual =  self.api.post_encrypt_with_password(request)
        self.assertIsNotNone(actual,"")


    def test_post_decrypt_with_password(self):
        remoteFolder = 'TestData/In'

        localBook1 = 'Book1.xlsx'
        localMyDoc = 'myDocument.xlsx'

     
        request = ProtectionRequest()
        request.password = '123456' 
         
        request.files =[]        
        request.files.append(get_request_file(localBook1))

        request.files.append(get_request_file(localMyDoc))

         

        actual =  self.api.post_decrypt_with_password(request)
        self.assertIsNotNone(actual,"")


    def test_post_digital_signature(self):
        remoteFolder = 'TestData/In'

        localBook1 = 'Book1.xlsx'
        localMyDoc = 'myDocument.xlsx'
        localPfx = 'roywang.pfx'

     
        request = DigitalSignaturRequest()
         
        request.digital_signatur_files =[]        
        request.digital_signatur_files.append(get_digital_signatur_file(localPfx, "12345"))


         
        request.files =[]        
        request.files.append(get_request_file(localBook1))

        request.files.append(get_request_file(localMyDoc))

        print(request)

        actual =  self.api.post_digital_signature(request)
        self.assertIsNotNone(actual,"")


if __name__ == '__main__':
    unittest.main()
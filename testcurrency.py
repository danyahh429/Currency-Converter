"""
Unit tests for module currency

When run as a script, this module invokes several procedures that test
the various functions in the module currency.

Author: Danyah Harris
Date:  November 3, 2020
"""

import introcs
import currency

def test_before_space():
    print("Testing before_space")
    
    # call the function on sample input 
    # store the returned result as a variable
    # compare the result with the expected output
    
    
    # Test case 1
    result = currency.before_space('yuhgj uyvjhm')
    introcs.assert_equals('yuhgj', result)
    
    #Test case 2
    result = currency.before_space(' adf')
    introcs.assert_equals('',result)
    
    #Test case 3
    result = currency.before_space('asf ase asd')
    introcs.assert_equals('asf', result)
    
    #Test case 4
    result = currency.before_space('dread   the dead or ')
    introcs.assert_equals('dread', result)
    
    
def test_after_space():
    print ("Testing after_space")
    
    #Test case 1
    result = currency.after_space('yuhgj uyvjhm')
    introcs.assert_equals('uyvjhm', result)
    
    #Test case 2
    result = currency.after_space('yhgj ')
    introcs.assert_equals('',result)
    
    #Test case 3
    result = currency.after_space('asf ase asd')
    introcs.assert_equals('ase asd', result)
    
    #Test case 4
    result = currency.after_space('dread   the dead or ')
    introcs.assert_equals('  the dead or ', result)
    
    
def test_first_inside_quotes():
    print("Testing first_inside_quotes")
    
    #Test case 1
    result = currency.first_inside_quotes("\"Hello\"")
    introcs.assert_equals("Hello", result)
    
    #Test case 2
    result = currency.first_inside_quotes("abc\"a\"")
    introcs.assert_equals("a", result)
    
    #Test case 3
    result = currency.first_inside_quotes("\"\"")
    introcs.assert_equals("", result)
    
    #Test case 4 
    result = currency.first_inside_quotes(" reap what yo\"u sow\" \"sd\" ")
    introcs.assert_equals("u sow", result)
    

def test_get_src():
    print("Testing get_src")
    
    #Test case 1
    result = currency.get_src('{"success": true, "src": "2 United States Dollars",'+
                              ' "dst": "1.772814 Euros", "error": ""}')
    introcs.assert_equals("2 United States Dollars", result)
    
    #Test case 2
    result = currency.get_src('{"success":false,"src":"","dst":"",'+
                              '"error":"Source currency code is invalid."}')
    introcs.assert_equals("", result)
    
    #Test case 3
    result = currency.get_src( '{"success":true, "src":"2 United States Dollars",'+
                              ' "dst":"1.772814 Euros", "error":""}')
    introcs.assert_equals("2 United States Dollars", result)
    
    #Test case 4
    result = currency.get_src('{"success": false, "src": "" ,"dst" : "", '+
                              '"error" : "Source currency code is invalid."}')
    introcs.assert_equals("", result)
    
    
def test_get_dst():
    print("Testing get_dst")
    #Test case 1
    result = currency.get_dst('{"success": true, "src": "2 United States Dollars", '+
                              '"dst": "1.772814 Euros", "error": ""}')
    introcs.assert_equals("1.772814 Euros", result)
    
    #Test case 2
    result = currency.get_dst('{"success":false,"src":"","dst":"",'+
                              '"error":"Source currency code is invalid."}')
    introcs.assert_equals("", result)
    
    #Test case 3
    result = currency.get_dst( '{"success":true, "src":"2 United States Dollars",'+
                              ' "dst":"1.772814 Euros", "error":""}')
    introcs.assert_equals("1.772814 Euros", result)
    
    #Test case 4
    result = currency.get_dst('{"success": false , "src": "", "dst": "" ,'+
                              ' "error": "invalid access key."}')
    introcs.assert_equals("", result)
    
    
def test_has_error():
    print("Testing has_error")
    #Test case 1
    result = currency.has_error('{"success": true, "src": "2 United States Dollars",'+
                                ' "dst": "1.772814 Euros", "error": ""}')
    introcs.assert_false(False, result)
    
    #Test case 2
    result = currency.has_error('{"success":false,"src":"","dst":"",'+
                                '"error":"Source currency code is invalid."}')
    introcs.assert_true(True, result)
    
    #Test case 3
    result = currency.has_error( '{"success":true, "src":"2 United States Dollars",'+
                                ' "dst":"1.772814 Euros", "error":""}')
    introcs.assert_false(False, result)
    
    #Test case 4
    result = currency.has_error('{"success": false , "src": "", "dst": "" ,'+
                                ' "error": "invalid access key."}')
    introcs.assert_true(True, result)
    
    
def test_service_response():
    print("Testing service_response")
    #Test case 1
    result = currency.service_response('USD','EUR',2.5)
    introcs.assert_equals('{"success": true, "src": "2.5 United States Dollars",'+
                          ' "dst": "2.2160175 Euros", "error": ""}', result)
    
    #Test case 2
    result = currency.service_response('abc','bbc',2.5)
    introcs.assert_equals('{"success": false, "src": "", "dst": "",'+
                          ' "error": "The rate for currency ABC is not present."}',result)
    
    #Test case 3
    result = currency.service_response('USD','bbc',2.5)
    introcs.assert_equals('{"success": false, "src": "", "dst": "",'+
                          ' "error": "The rate for currency BBC is not present."}',result)
    
    #Test case 4
    result = currency.service_response('USD','EUR',-2.5)
    introcs.assert_equals('{"success": true, "src": "-2.5 United States Dollars",'+
                          ' "dst": "-2.2160175 Euros", "error": ""}',result)
    
    
def test_iscurrency():
    print("Testing iscurrency")
    
    #Test case 1 
    result = currency.iscurrency('jhb')
    introcs.assert_equals(False, result)
   
    #Test case 2
    result = currency.iscurrency('USD')
    introcs.assert_equals(True, result)
    
    
def test_exchange():
    print("Testing exchange")
    
    #Test case 1
    result = currency.exchange('USD','EUR',2.5)
    introcs.assert_floats_equal(2.2160175, result)
    
    #Test case 2
    result = currency.exchange('USD', "EUR", -2.5)
    introcs.assert_floats_equal(-2.2160175, result)
    
    
test_before_space()
test_after_space()
test_first_inside_quotes()
test_get_src()
test_get_dst()
test_has_error()
test_service_response()
test_iscurrency()
test_exchange()
print("All tests completed successfully.")
"""
Module for currency exchange

This module provides several string parsing functions to implement a simple
currency exchange routine using an online currency service. The primary function
in this module is exchange().

Author:Danyah Harris
Date:   11/3/20
"""
import introcs
APIKEY = 'xWN1vBTdfMslXdXUBs4r2F6mnMWo8zIMmvAcgsMPMbEe'



def is_string(s):
    """
    Returns true if s is a string
    """
    
    return type(s) == str


def has_space(s):
    assert is_string(s), 'Not a string'
    """
    Returns true if s has a space
    """
    result = introcs.find_str(s,' ')
    result2 = introcs.startswith_str(s, ' ')
    myVar = (result != -1) or result2
    return myVar


def is_num(amt):
    """
    returns true if amt is an int or float
    """
    return type(amt) == (float or int)
    

def matching_quotes(s):
    """
    Returns True if the string s has a matching pair of quotes.

    Example: matching_parens(' "B" C') returns True
    Example: matching_parens('A " C') returns False

    Parameter s: The string to check
    Precondition: s is a string (possibly empty)
    """
    assert is_string(s)
    # Search for the first quote 
    first = introcs.find_str(s, '"')
    # print(first)
    remain = s[first+1:]
    # print(remain)
        
    # Search for the last quote AFTER the first quote
    last = introcs.find_str(remain,'"')
    # print (last)
    
    # Compare both searches to -1 and return True if BOTH are not -1 
    return first != -1 and last != -1
    

def before_space(s):
    """
    Returns the substring of s up to, but not including, the first space.

    Example: before_space('Hello World') returns 'Hello'

    Parameter s: the string to slice
    Precondition: s is a string with at least one space in it
    """
    #s is a string
    assert is_string(s), 'Not a string'
    assert has_space(s), 'There is no space'
    
    space = introcs.find_str(s,' ')
    pre_space = s[:space]
    return pre_space
     
    
def after_space(s):
    """
    Returns the substring of s after the first space

    Example: after_space('Hello World') returns 'World'

    Parameter s: the string to slice
    Precondition: s is a string with at least one space in it
    """
    assert is_string(s), 'Not a string' 
    assert has_space(s), 'There is no space'
    
    space = introcs.find_str(s,' ')
    post_space = s[space+1:]
    return post_space


def first_inside_quotes(s):
    """
    Returns the first substring of s between two (double) quote characters

    Note that the double quotes must be part of the string.  So "Hello World" is a 
    precondition violation, since there are no double quotes inside the string.

    Example: first_inside_quotes('A "B C" D') returns 'B C'
    Example: first_inside_quotes('A "B C" D "E F" G') returns 'B C', because it only 
    picks the first such substring.

    Parameter s: a string to search
    Precondition: s is a string with at least two (double) quote characters inside
    """
    assert is_string(s), 'Not a string'
    assert matching_quotes(s), 'No matching quotes'
    
    # Search for the first quote 
    first = introcs.find_str(s, '"')
    # print(first)
    remain = s[first+1:]
    # print(remain)
        
    # Search for the last quote AFTER the first quote
    last = introcs.find_str(remain,'"')
   # print (last)
    
    in_quote = remain[:last]
    return in_quote


def get_src(json):
    """
    Returns the src value in the response to a currency query.

    Given a JSON string provided by the web service, this function returns the string
    inside string quotes (") immediately following the substring '"src"'. For example,
    if the json is
    
    '{"success": true, "src": "2 United States Dollars", "dst": "1.772814 Euros", "error": ""}'

    then this function returns '2 United States Dollars' (not '"2 United States Dollars"'). 
    On the other hand if the json is 
    
    '{"success":false,"src":"","dst":"","error":"Source currency code is invalid."}'

    then this function returns the empty string.

    The web server does NOT specify the number of spaces after the colons. The JSON
    
    '{"success":true, "src":"2 United States Dollars", "dst":"1.772814 Euros", "error":""}'
    
    is also valid (in addition to the examples above).

    Parameter json: a json string to parse
    Precondition: json a string provided by the web service (ONLY enforce the type)
    """
    
   # assert type is json
    data =json
    assert is_string(data)
    #print(type(data))
    # return src value
    first_colon = introcs.find_str(data, ':')
    #print (first_colon)
    after_success = data[first_colon+1:]
    #print(after_success)
    src_colon = introcs.find_str(after_success, ':')
    #print(src_colon)
    remain = after_success[src_colon+1:]
    #print(remain)
    src_value = first_inside_quotes(remain)
    return(src_value)


def get_dst(json):
    """
    Returns the dst value in the response to a currency query.

    Given a JSON string provided by the web service, this function returns the string
    inside string quotes (") immediately following the substring '"dst"'. For example,
    if the json is
    
    '{"success": true, "src": "2 United States Dollars", "dst": "1.772814 Euros", "error": ""}'
    
    then this function returns '1.772814 Euros' (not '"1.772814 Euros"'). On the other
    hand if the json is 
    
    '{"success":false,"src":"","dst":"","error":"Source currency code is invalid."}'

    then this function returns the empty string.

    The web server does NOT specify the number of spaces after the colons. The JSON
    
    '{"success":true, "src":"2 United States Dollars", "dst":"1.772814 Euros", "error":""}'
    
    is also valid (in addition to the examples above).

    Parameter json: a json string to parse
    Precondition: json a string provided by the web service (ONLY enforce the type)
    """
    # assert type is json
    data =json
    assert is_string(data)
    #print(type(data))
    # return src value
    first_colon = introcs.find_str(data, ':')
    #print (first_colon)
    after_success = data[first_colon+1:]
    #print(after_success)
    src_colon = introcs.find_str(after_success, ':')
    #print(src_colon)
    remain = after_success[src_colon+1:]
    #print(remain)
    second_colon = introcs.find_str(remain,':')
    #print(second_colon)
    final_string = remain[second_colon+1:]
    dst_value = first_inside_quotes(final_string)
    return(dst_value)


def has_error(json):
    """
    Returns True if the response to a currency query encountered an error.

    Given a JSON string provided by the web service, this function returns True if the
    query failed and there is an error message. For example, if the json is
    
    '{"success":false,"src":"","dst":"","error":"Source currency code is invalid."}'

    then this function returns True (It does NOT return the error message 
    'Source currency code is invalid'). On the other hand if the json is 
    
    '{"success": true, "src": "2 United States Dollars", "dst": "1.772814 Euros", "error": ""}'

    then this function returns False.

    The web server does NOT specify the number of spaces after the colons. The JSON
    
    '{"success":true, "src":"2 United States Dollars", "dst":"1.772814 Euros", "error":""}'
    
    is also valid (in addition to the examples above).

    Parameter json: a json string to parse
    Precondition: json a string provided by the web service (ONLY enforce the type)
    """
    # assert type is json
    data =json
    assert is_string(data)
    #print(type(data))
    # return src value
    first_colon = introcs.find_str(data, ':')
    #print (first_colon)
    after_success = data[first_colon+1:]
    #print(after_success)
    src_colon = introcs.find_str(after_success, ':')
    #print(src_colon)
    remain = after_success[src_colon+1:]
    #print(remain)
    second_colon = introcs.find_str(remain,':')
    #print(second_colon)
    next_string = remain[second_colon+1:]
    #print(next_string)
    error_colon = introcs.find_str(next_string, ':')
   # print(error_colon)
    final = next_string[error_colon+1:]
    error_code = first_inside_quotes(final)
    #print(error_code)
    empty = ""
    error_bool = error_code != empty
    return(error_bool)


def service_response(src, dst, amt):
    """
    Returns a JSON string that is a response to a currency query.

    A currency query converts amt money in currency src to the currency dst. The response 
    should be a string of the form

    '{"success": true, "src": "<src-amount>", dst: "<dst-amount>", error: ""}'

    where the values src-amount and dst-amount contain the value and name for the src 
    and dst currencies, respectively. If the query is invalid, both src-amount and 
    dst-amount will be empty, and the error message will not be empty.

    There may or may not be spaces after the colon.  To test this function, you should
    chose specific examples from your web browser.

    Parameter src: the currency on hand
    Precondition src is a nonempty string with only letters

    Parameter dst: the currency to convert to
    Precondition dst is a nonempty string with only letters

    Parameter amt: amount of currency to convert
    Precondition amt is a float or int
    """
    
    assert introcs.isalpha(src), 'empty src or numbers'
    assert introcs.isalpha(dst) , 'empty dst or numbers'
    assert is_num(amt) , 'not a number'
    
    
    #open website
    url = 'https://ecpyfac.ecornell.com/python/currency/fixed?src=' + src +'&dst=' + dst +'&amt='+ str(amt) +'&key=' + APIKEY
    #print(url)
    #request a response
    response = introcs.urlread(url)
    #return resposne
    return(response)
   
    
def iscurrency(currency):
    """
    Returns True if currency is a valid (3 letter code for a) currency.

    It returns False otherwise.

    Parameter currency: the currency code to verify
    Precondition: currency is a nonempty string with only letters
    """
    assert is_string(currency) , 'Not a string'
 
  
    intial_response = service_response(currency,'EUR',2.5)
    #print(intial_response)
    #returns true if there is an error
    x = has_error(intial_response)
    return x != True 
 

def exchange(src,dst,amt):
    """
    Returns the amount of currency received in the given exchange.

    In this exchange, the user is changing amt money in currency src to the currency 
    dst. The value returned represents the amount in currency currency_to.

    The value returned has type float.

    Parameter src: the currency on hand
    Precondition src is a string for a valid currency code

    Parameter dst: the currency to convert to
    Precondition dst is a string for a valid currency code

    Parameter amt: amount of currency to convert
    Precondition amt is a float or int
    """
    assert iscurrency(src)
    assert iscurrency(dst)
    assert is_num(amt) 
    
    web_response = service_response(src, dst, amt)
    
    web_response = get_dst(web_response)
    space = introcs.find_str(web_response,' ')
    dst_value = web_response[:space]
    return float(dst_value)
# Explore Python Classes

### Part 1: Review Functions, Methods, and Classes
In this part, you review the difference between functions and methods. You also review the basic structure of a class.
#### Step 1: What is a function?
As a quick review, recall that a function is an independently defined block of code that is called by name. In the following example, the function called functionName is defined and then called. Notice that it is an independent block of code. It is not encapsulated in any other code.
```
# Define the function
def functionName:
    ...blocks of code...

# Call the function
functionName()
```

#### Step 2: What is a method?
A method, however, cannot be called by itself. It is dependent on the object in which it is defined. In the following example, the class className is declared and three methods are defined. The class is instantiated and then each method of the class is called.
Note: This pseudo-code does not explicitly show the class constructor __init__ method with the self variable. This special method is reviewed below.
```
# Define the class
class className

    # Define a method
    def method1Name
        ...blocks of code

    # Define another method
    def method2Name
        ...blocks of code

    # Define yet another method
    def method3Name
        ...blocks of code

# Instantiate the class
myClass = className()

# Call the instantiation and associated methods
myClass.method1Name()
myClass.method2Name()
myClass.method3Name()
```


### Part 2: Define a Function
In this part, you will define a function with arguments and then call the function.
1.	Open a new text file and save it as myCity.py in your src/solution directory.
2.	Define the function myCity with the argument city for city name. When the function is called with a specified city name, it prints a statement that includes the city name.
```
def myCity(city):
    print("I live in " + city + ".")
```
3.	Call the function myCity passing it different values for city, as shown in the following examples.
```
myCity("Austin")
myCity("Tokyo")
myCity("Salzburg")
```
4.	Save and run the myCity.py file. You should get the following output.
```
I live in Austin.
I live in Tokyo.
I live in Salzburg.
```

### Part 3: Define a Class with Methods
In this part, you will define a class, use the __init__() function to define a method for the class, and then create instances of the class.

#### Step 1: Define and then instantiate a class with the __init__() method.
A Python class is used to create objects that have properties and methods. All Python classes typically include an explicitly defined __init__() function, although you can create a class without defining one. The __init__() function is always initiated when a class is instantiated. Instantiating a class creates a copy of the class which inherits all the class variables and methods.
Note: Although it is sometimes called the __init__() function, it is dependent on the class. Therefore, it is technically a method. 
1. Open a new text file and save it as myLocation.py. 
2. Define a class with the name Location and press Enter. If you are working is VS Code, then the text editor should automatically indent four spaces.
```
class Location:
|<-- cursor should now be here
```
3.	Next, define the __init__() function. By convention, the first parameter is called self. The self parameter is a reference to the current instance of the class itself and is used to access variables that belong to the entire class. The __init__() function is then assigned any variables the entire class needs. In the following example, define a name and country variable. Press Enter twice and then backspace twice to the left margin.
```
def __init__(self, name, country):
    self.name = name
    self.country = country

|<-- cursor should now be here
```
4.	You can test that this class is now ready to use. Instantiate the class by assigning it a name of your choice. Then specify the values for the required class variables name and country. The following example uses the Location class to instantiate a class called loc with a name and country specified by you. Use your name and country.
```
loc = Location("Your_Name", "Your_Country")
```
5.	To verify that the instantiated loc class now has your assigned name and country, add print statements to your script.  
```
print(loc.name)
print(loc.country)
```
6.	To verify the loc is indeed a class, add the following print statement that will print the data type for loc.
```
print(type(loc))
```
7.	Save and run your script. You should get the following output except with your supplied name and country.
```
Your_Name
Your_Country
<class '__main__.Location'>
```

#### Step 2: Add a method to the Location class.
Now add a method to the Location class that can be called by a programmer when the class is instantiated. In this simple example, create a method to print the statement, “My name is [name] and I live in [country].”
1. Delete the code the begins with the instantiation of the loc class. Your myLocation.py script should now only include the following code.
```
class Location:
    def __init__(self, name, country):
        self.name = name
        self.country = country
```
2. With your cursor at the end of the line self.country = country, press the Enter key twice and backspace once.
```
        self.country = country

    |<--Your cursor should be here
```
3. Define a new method call myLocation and assigned it the self parameter so that the new method can access the variables defined in the __init__() function. Then, define a print statement to print out the string specified above.
Note: The print statement should be on one line.
```
    def myLocation(self):
        print("Hi, my name is " + self.name + " and I live in " + self.country + ".")
```
4. Press the Enter key twice and backspace twice.
5. Save and run your script to make sure there are no errors. You will not get any output yet.

#### Step 3: Instantiate the Location class multiple times and call the myLocation method.
Now that you have a class, you can instantiate it as many times as you like providing different values for the class variables each time.
1. Add the following code to your myLocation.py script to instantiate Location class and call the method. You do not need to add the comments.
```
# First instantiation of the class Location 
loc1 = Location("Tomas", "Portugal")
# Call a method from the instantiated class
loc1.myLocation()
```
2. Save and run your script. You should get the following output.
```
Hi, my name is Tomas and I live in Portugal.
```
3. Add two more instantiations and then a fourth one where you specify the name and values for your_loc.
```
loc2 = Location("Ying", "China")
loc3 = Location("Amare", "Kenya")
loc2.myLocation()
loc3.myLocation()
your_loc = Location("Your_Name", "Your_Country")
your_loc.myLocation()
```
4. Save and run your script. You should get the following output.
```
Hi, my name is Tomas and I live in Portugal.
Hi, my name is Ying and I live in China.
Hi, my name is Amare and I live in Kenya.
Hi, my name is Your_Name and I live in Your_Country.
```

### 5: Review the circleClass.py Script
The example in the course shows how to create a class that calculates the circumference of a circle and then print out the calculated value. There are a few things to note in this script. 
* The class includes three methods including the __init__() function. The __init__() function provides a method for entering the radius value.
* The circumference method calculates the circumference and returns the value storing it in the circumferenceValue variable. 
* The printCircumference method prints a string. Notice that the variables are casted as strings with the str() function. Otherwise, the print statement would throw an error because self.radius and myCircumference are not strings.
* The Circle class instantiated three times.


# Create a Python Unit Test
### Background / Scenario
Unit tests examine independent units of code, like functions, classes, modules, and libraries. There are many reasons for writing a script using Python’s unittest library. One obvious reason is that if you find an issue in isolated code by deliberate testing, you know that the problem is in the function or other unit under test. The problem is not in the larger application that may call this function. You will also know exactly what triggered the error because you wrote the unit test that exposed the issue. Bugs found this way are usually quick and easy to fix, and fixes made at this detailed level are less likely to cause unanticipated side effects later on in other code that relies on the tested code.
You can run unit tests manually if the code is small, but typically unit tests should be automated. When writing a unit test, think about the following:
* The unit test should be simple and easy to implement.
* The unit test should be well documented, so it's easy to figure out how to run the test, even after several years.
* Consider the test methods and inputs from every angle.
* Test results should be consistent. This is important for test automation.
* Test code should work independently of code being tested. If you write tests that need to change program state, capture state before changing it, and change it back after the test runs.
* When a test fails, results should be easy to read and clearly point out what is expected and where the issues are.
In this lab, you will explore the unittest framework and use unittest to test a function.

#### Part 1: Explore Options in the unittest Framework
Python provides a Unit Testing Framework (called unittest) as part of the Python standard library. If you are not familiar with this framework, study the “Python unittest Framework” to familiarize yourself. Search for it on the internet to find the documentation at python.org. You will need that knowledge or documentation to answer questions in this part.
Questions:
1. What unittest class do you use to create an individual unit of testing?
2. How does the test runner know which methods are a test?
Place answers in unittest directory in ans.txt file.
What command will list all of the command line options for unittest shown in the following output?
```
devasc@labvm:~/labs/devnet-src$ python3 -m unittest -h
<output omitted>
optional arguments:
  -h, --help           show this help message and exit
  -v, --verbose        Verbose output
  -q, --quiet          Quiet output
  --locals             Show local variables in tracebacks
  -f, --failfast       Stop on first fail or error
  -c, --catch          Catch Ctrl-C and display results so far
  -b, --buffer         Buffer stdout and stderr during tests
  -k TESTNAMEPATTERNS  Only run tests which match the given substring

Examples:
  python3 -m unittest test_module               - run tests from test_module
  python3 -m unittest module.TestClass          - run tests from module.TestClass
  python3 -m unittest module.Class.test_method  - run specified test method
  python3 -m unittest path/to/test_file.py      - run tests from test_file.py
<output omitted>
For test discovery all test modules must be importable from the top level
directory of the project.
devasc@labvm:~/labs/devnet-src$
```

### Part 2: Test a Python Function with unittest
In this part, you will use unittest to test a function that performs a recursive search of a JSON object. The function returns values tagged with a given key. Programmers often need to perform this kind of operation on JSON objects returned by API calls.
This test will use three files as summarized in the following table:
|File                       |	Description                                                                                                     |
|---------------------------|-------------------------------------------------------------------------------------------------------------------|
|recursive_json_search.py   |	This script will include the json_search() function we want to test.                                            |
|test_data.py               |	This is the data the json_search() function is searching.                                                       |
|test_json_search.py        |	This is the file you will create to test the json_search() function in the recursive_json_search.py script.     |

#### Step 1: Review the test_data.py file.
Open the ~/labs/devnet-src/unittest/test_data.py file and examine its contents. This JSON data is typical of data returned by a call to Cisco’s DNA Center API. The sample data is sufficiently complex to be a good test. For example, it has dict and list types interleaved.
```
devasc@labvm:~/labs/devnet-src$ more unittest/test_data.py 
key1 = "issueSummary"
key2 = "XY&^$#*@!1234%^&"

data = {
  "id": "AWcvsjx864kVeDHDi2gB",
  "instanceId": "E-NETWORK-EVENT-AWcvsjx864kVeDHDi2gB-1542693469197",
  "category": "Warn",
  "status": "NEW",
  "timestamp": 1542693469197,
  "severity": "P1",
  "domain": "Availability",
  "source": "DNAC",
  "priority": "P1",
  "type": "Network",
  "title": "Device unreachable",
  "description": "This network device leaf2.abc.inc is unreachable from controll
er. The device role is ACCESS.",
  "actualServiceId": "10.10.20.82",
  "assignedTo": "",
  "enrichmentInfo": {
    "issueDetails": {
      "issue": [
        {
--More--(12%)
```

#### Step 2: Create the json_search() function that you will be testing.
Our function should expect a key and a JSON object as input parameters, and return a list of matched key/value pairs. Here is the current version of the function that needs to be tested to see if it is working as intended. The purpose of this function is to import the test data first. Then it searches for data that matches the key variables in the test_data.py file. If it finds a match, it will append the matched data to a list. The print() function at the end prints the contents for the list for the first variable key1 = "issueSummary".
```
from test_data import *
def json_search(key,input_object):
    ret_val=[]
    if isinstance(input_object, dict): # Iterate dictionary
        for k, v in input_object.items(): # searching key in the dict
            if k == key:
                temp={k:v}
                ret_val.append(temp)
            if isinstance(v, dict): # the value is another dict so repeat
                json_search(key,v)
            elif isinstance(v, list): # it's a list
                for item in v:
                    if not isinstance(item, (str,int)): # if dict or list repeat
                        json_search(key,item)
    else: # Iterate a list because some APIs return JSON object in a list
        for val in input_object:
            if not isinstance(val, (str,int)):
                json_search(key,val)
    return ret_val
print(json_search("issueSummary",data))
```
1. Open the ~/labs/devnet-src/unittest/recursive_json_search.py file. 
2. Copy the code above into the file and save it. 
3.	Run the code. You should get no errors and output of [ ] indicating an empty list. If the json_search() function was coded correctly (which it is not), this would tell you that there is no data with the "issueSummary" key reported by JSON data returned by the Cisco DNA Center API. In other words, there are no issues to report.
```
devasc@labvm:~/labs/devnet-src/unittest$ python3 recursive_json_search.py 
[]
devasc@labvm:~/labs/devnet-src/unittest$
```
4. But how do you know that the json_search() function is working as intended? You could open the test_data.py file and search for the key “issueSummary”, as shown below. If you did, you would indeed find that there is an issue. This is a small data set and a relatively simple recursive search. However, production data and code is rarely this simple. Therefore, testing code is vital to quickly finding and fixing errors in your code.
```
<output omitted>
      "issue": [
        {
          "issueId": "AWcvsjx864kVeDHDi2gB",
          "issueSource": "Cisco DNA",
          "issueCategory": "Availability",
          "issueName": "snmp_device_down",
          "issueDescription": "This network device leaf2.abc.inc is unreachable from controller. The device role is ACCESS.",
          "issueEntity": "network_device",
          "issueEntityValue": "10.10.20.82",
          "issueSeverity": "HIGH",
          "issuePriority": "",
          "issueSummary": "Network Device 10.10.20.82 Is Unreachable From Controller",
          "issueTimestamp": 1542693469197,
          "suggestedActions": [
            {
<output omitted>
```

#### Step 3: Create some unit tests that will test if the function is working as intended.
1. Open the unittest/test_json_search.py file.
2. In the first line of the script after the comment, import the unittest library.
import unittest
3. Add lines to import the function you are testing as well as the JSON test data the function uses.
```
from recursive_json_search import *
from test_data import *
```
4. Now add the following json_search_test class code to the test_json_search.py file. The code creates the subclass TestCase of the unittest framework. The class defines some test methods to be used on the json_search() function in the recursive_json_search.py script. Notice that each test method begins with test_, enabling the unittest framework to discover them automatically. Add the following lines to the bottom of your ~labs/devnet-src/unittest/test_json_search.py file:
```
class json_search_test(unittest.TestCase):
    '''test module to test search function in `recursive_json_search.py`'''
    def test_search_found(self):
        '''key should be found, return list should not be empty'''
        self.assertTrue([]!=json_search(key1,data))
    def test_search_not_found(self):
        '''key should not be found, should return an empty list'''
        self.assertTrue([]==json_search(key2,data))
    def test_is_a_list(self):
        '''Should return a list'''
        self.assertIsInstance(json_search(key1,data),list)
```
In the unittest code, you are using three methods to test the search function:
    * Given an existing key in the JSON object, see if the testing code can find such a key.
    * Given a non-existent key in the JSON object, see if the testing code confirms that no key can be found.
    * Check if our function returns a list, as it should always do.
To create these tests, the script uses some of the built-in assert methods in the unittest TestCase class to check for conditions. The assertTrue(x) method checks if a condition is true and assertIsInstance(a, b) checks if a is an instance of the b type. The type used here is list.
Also, notice that the comments for each method are specified with the triple single quote ('''). This is required if you want the test to output a description of the test method when it runs. Using the single hash symbol (#) for the comment would not print out the description of a failed test.
5. For the last part of the script, add the unittest.main() method. This enables running unittest from the command line. The purpose of if __name__ == ‘__main__’ is to make sure that the unittest.main() method runs only if the script is run directly. If the script is imported into another program, unittest.main() will not run. For example, you might use a different test runner than unittest to run this test.
```
if __name__ == '__main__':
```

#### Step 4: Run the test to see the initial results.
1. Run the test script in its current state to see what results it currently returns. First, you see the empty list. Second, you see the .F. highlighted in the output. A period (.) means a test passed and an F means a test failed. Therefore, the first test passed, the second test failed, and the third test passed.
```
devasc@labvm:~/labs/devnet-src/unittest$ python3 test_json_search.py 
 []
.F.
======================================================================
FAIL: test_search_found (__main__.json_search_test)
key should be found, return list should not be empty
----------------------------------------------------------------------
Traceback (most recent call last):
  File "test_json_search.py", line 11, in test_search_found
    self.assertTrue([]!=json_search(key1,data))
AssertionError: False is not true

----------------------------------------------------------------------
Ran 3 tests in 0.001s

FAILED (failures=1)
devasc@labvm:~/labs/devnet-src/unittest$
```
2. To list each test and its results, run the script again under unittest with the verbose (-v) option. Notice that you do not need the .py extension for the test_json_search.py script. You can see that your test method test_search_found is failing. 
Note: Python does not necessarily run your tests in order. Tests are run in alphabetical order based on the test method names.
```
devasc@labvm:~/labs/devnet-src/unittest$ python3 -m unittest -v test_json_search
[]
test_is_a_list (test_json_search.json_search_test)
Should return a list ... ok
test_search_found (test_json_search.json_search_test)
key should be found, return list should not be empty ... FAIL
test_search_not_found (test_json_search.json_search_test)
key should not be found, should return an empty list ... ok

======================================================================
FAIL: test_search_found (test_json_search.json_search_test)
key should be found, return list should not be empty
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/devasc/labs/devent-src/unittest/test_json_search.py", line 11, in test_search_found
    self.assertTrue([]!=json_search(key1,data))
AssertionError: False is not true

----------------------------------------------------------------------
Ran 3 tests in 0.001s

FAILED (failures=1)
devasc@labvm:~/labs/devnet-src/unittest$
```

#### Step 5: Investigate and correct the first error in the recursive_json_search.py script.
The assertion, key should be found, return list should not be empty ... FAIL, indicates the key was not found. Why? If we look at the text of our recursive function, we see that the statement ret_val=[ ] is being repeatedly executed, each time the function is called. This causes the function to empty the list and lose accumulated results from the ret_val.append(temp) statement, which is adding to the list created by ret_val=[ ].
```
def json_search(key,input_object):
    ret_val=[]
    if isinstance(input_object, dict):
        for k, v in input_object.items():
            if k == key:
                temp={k:v}
                ret_val.append(temp)
```
1.	Move the ret_val=[ ] out of our function in recursive_json_search.py so that the iteration does not overwrite the accumulated list each time. 
```
ret_val=[]
def json_search(key,input_object):
```
2.	Save and run the script. You should get the following output which verifies that you resolved the issue. The list is no longer empty after the script runs. 
```
devasc@labvm:~/labs/devnet-src/unittest$ python3 recursive_json_search.py 
[{'issueSummary': 'Network Device 10.10.20.82 Is Unreachable From Controller'}]
devasc@labvm:~/labs/devnet-src/unittest$
```

#### Step 6: Run the test again to see if all errors in the script are now fixed.
1. You got some output last time you ran recursive_json_search.py, you cannot yet be sure you resolved all the errors in the script? Run unittest again without the -v option to see if test_json_search returns any errors. Typically, you do not want to use -v option to minimize console output and make tests run faster. At the start of the log you can see ..F, meaning that the third test failed. Also notice that the list is still printing out. You can stop this behavior by removing the print() function in the resursive_json_search.py script. But that is not necessary for your purposes in this lab. 
```
devasc@labvm:~/labs/devnet-src/unittest$ python3 -m unittest test_json_search
[{'issueSummary': 'Network Device 10.10.20.82 Is Unreachable From Controller'}]
..F
======================================================================
FAIL: test_search_not_found (test_json_search.json_search_test)
key should not be found, should return an empty list
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/devasc/labs/devnet-src/unittest/test_json_search.py", line 14, in test_search_not_found
    self.assertTrue([]==json_search(key2,data))
AssertionError: False is not true

----------------------------------------------------------------------
Ran 3 tests in 0.001s

FAILED (failures=1)
devasc@labvm:~/labs/devnet-src/unittest$
```
2.	Open the test_data.py file and search for issueSummary, which is the value for key1. You should find it twice, but only once in the JSON data object. But if you search for the value of key2, which is XY&^$#*@!1234%^&, you will only find it at the top where it is defined because it is not in the data JSON object. The third test is checking to make sure it is not there. The third test comment states key should not be found, should return an empty list. However, the function returned a non-empty list.

#### Step 7: Investigate and correct the second error in the recursive_json_search.py script.
1. Review the recursive_json_search.py code again. Notice that the ret_val is now a global variable after you fixed it in the previous step. This means that its value is preserved across multiple invocations of the json_search() function. This is a good example of why it's bad practice to use global variables within functions.
2. To resolve this issue, wrap the json_search() function with an outer function. Delete your existing json_search() function and replace with the refactored one below: (It won't hurt to call the function twice but it's not best practice to repeat a function.)
```
from test_data import *
def json_search(key,input_object):
    """
    Search a key from JSON object, get nothing back if key is not found
    key : "keyword" to be searched, case sensitive
    input_object : JSON object to be parsed, test_data.py in this case
    inner_function() is actually doing the recursive search
    return a list of key:value pair
    """
    ret_val=[]
    def inner_function(key,input_object):
        if isinstance(input_object, dict): # Iterate dictionary
            for k, v in input_object.items(): # searching key in the dict
                if k == key:
                    temp={k:v}
                    ret_val.append(temp)
                if isinstance(v, dict): # the value is another dict so repeat
                    inner_function(key,v)
                elif isinstance(v, list):
                    for item in v:
                        if not isinstance(item, (str,int)): # if dict or list repeat
                            inner_function(key,item)
        else: # Iterate a list because some APIs return JSON object in a list
            for val in input_object:
                if not isinstance(val, (str,int)):
                    inner_function(key,val)
    inner_function(key,input_object)
    return ret_val
print(json_search("issueSummary",data))
```
3.	Save the file and run unittest on the directory. You do not need the name of the file. This is because the unittest Test Discovery feature will run any local file it finds whose name begins with test. You should get the following output. Notice that all tests now pass and the list for the "issueSummary" key is populated. You can safely delete the print() function as it would not normally be used when this test is aggregated with other tests for a larger test run.
```
devasc@labvm:~/labs/devnet-src/unittest$ python3 -m unittest
[{'issueSummary': 'Network Device 10.10.20.82 Is Unreachable From Controller'}]
...
----------------------------------------------------------------------
Ran 3 tests in 0.001s

OK
devasc@labvm:~/labs/devnet-src/unittest$
```

# Parse Different Data Types with Python
### Background / Scenario
Parsing means analyzing a message, breaking it into its component parts, and understanding the purpose of each part in context. When messages are transmitted between computers, they travel as a stream of characters. Those characters are effectively a string. That message needs to be parsed into a semantically-equivalent data-structure containing data of recognized types (e.g., integers, floats, strings, and Booleans) before the data can be interpreted and acted upon.
In this lab, you will use Python to parse each data format in turn: XML, JSON, and YAML. We'll walk through code examples and talk about how each parser works.

### Part 1: Parse XML in Python
Because of the flexibility provided by Extensible Markup Language (XML), it can be tricky to parse. XML’s all-text tagged data fields do not map unambiguously to default data types in Python or other popular languages. In addition, it is not always obvious how attribute values should be represented in data.
These issues can be sidestepped by Cisco developers working in some contexts, because Cisco has provided tools such as YANG-CLI, which validates and consumes XML relevant to data modeling and related tasks. Below is content of the myfile.xml file found in ~/labs/devnet-src/parsing. This is an example of the sort of file that YANG-CLI manages. You will parse this file in Python to get access to the information it contains.
```
<?xml version="1.0" encoding="UTF-8"?>
<rpc message-id="1"
 xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
 <edit-config>
  <target>
   <candidate/>
  </target>
  <default-operation>merge</default-operation>
  <test-option>set</test-option>
  <config>
   <int8.1
    xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0"
    nc:operation="create"
    xmlns="http://netconfcentral.org/ns/test">9</int8.1>
  </config>
 </edit-config>
</rpc>
```

#### Step 1: Build a script to parse the XML data.
1. Open the parsexml.py file found in the ~/labs/devnet-src/parsing directory.
2. Import the ElementTree module of the xml library and the regular expression engine. The ElementTree module will be used to do the parsing. The regular expression engine will be used to search for specific data.
Note: If you do not have any experience with using regular expressions in Linux, Python, or other object-oriented programming languages, search the internet for tutorials.
```
import xml.etree.ElementTree as ET
import re
```
3. Next, use the parse function from ET (ElementTree) to parse the myfile.xml file and assign it to a variable (xml). Then, get the root element with the getroot function and assign it to a variable (root).
```
xml = ET.parse("myfile.xml")
root = xml.getroot()
```
4.	Now the top level of the tree can be searched for the containing tag `<edit-config>`, and when found, that tagged block can be searched for two named values it contains: `<default-operation>` and `<test-option>`. Create a regular expression to get the contents of the XML root content in the `<rpc>` tag and then add additional regular expressions to drill down into the content in order to find the value of the `<edit-config>`, `<default-operation>`, and `<test-option>` elements.
```
ns = re.match('{.*}', root.tag).group(0)
editconf = root.find("{}edit-config".format(ns))
defop = editconf.find("{}default-operation".format(ns))
testop = editconf.find("{}test-option".format(ns))
```
e.	Add print statements to print the value of the `<default-operation>` and `<test-option>` elements.
```
print("The default-operation contains: {}".format(defop.text))
print("The test-option contains: {}".format(testop.text))
```

#### Step 2: Run the script.
Save and run the parsexml.py. You should get the following output.
```
devasc@labvm:~/labs/devnet-src/parsing$ python3 parsexml.py 
The default-operation contains: merge
The test-option contains: set
devasc@labvm:~/labs/devnet-src/parsing$
```

### Part 3: Parse JSON in Python
Parsing JavaScript Object Notation (JSON) is a frequent requirement of interacting with REST APIs. The steps are usually as follows:
1. Authenticate using a user/password combination to retrieve a token that will expire after a set amount of time. This token is used for authenticating subsequent requests.
2. Execute a GET request to the REST API, authenticating as required, to retrieve the state of a resource, requesting JSON as the output format.
3. Modify the returned JSON, as needed.
4. Execute a POST (or PUT) to the same REST API (again, authenticating as required) to change the state of the resource, again requesting JSON as the output format and interpreting it as needed to determine whether the operation was successful.
The JSON example to parse is this response from a token request:
```
{
 "access_token":"ZDI3MGEyYzQtNmFlNS00NDNhLWFlNzAtZGVjNjE0MGU1OGZmZWNmZDEwN2ItYTU3",
 "expires_in":1209600,
 "refresh_token":"MDEyMzQ1Njc4OTAxMjM0NTY3ODkwMTIzNDU2Nzg5MDEyMzQ1Njc4OTEyMzQ1Njc4",
 "refreshtokenexpires_in":7776000
}
```
In Python scripts, the Python json library can be used to parse JSON into Python native data structures, and serialize data structures back out as JSON. The Python yaml library can be used to convert the data to YAML. 
The following program uses both modules to parse the above JSON data, extract and print data values, and output a YAML version of the file. It uses the json library loads() method to parse a string into which the file has been read. It then uses normal Python data references to extract values from the resulting Python data structure. Finally, it uses the yaml library dump() function to serialize the Python data back out as YAML, to the terminal.

#### Step 1: Build a script to parse the JSON data.
1. Open the parsejson.py file found in the parsing directory.
2. Import the json and yaml libraries.
```
import json
import yaml
```
3. Use the Python with statement to open myfile.json and set it to the variable name json_file. Then use the json.load method to load the JSON file into a string set to the variable name ourjson.
Note: There is no need to explicitly close the file as the with statement ensures proper opening and closing of the file.
```
with open('myfile.json','r') as json_file:
    ourjson = json.load(json_file)
```
4.	Add a print statement for ourjson to see that it is now a Python dictionary.
```
print(ourjson)
```

#### Step 2: Run the script to print the JSON data and then modify it to print data of interest.
1. Save and run your script. You should see the following output.
```
devasc@labvm:~/labs/devnet-src/parsing$ python3 parsejson.py 
{'access_token': 'ZDI3MGEyYzQtNmFlNS00NDNhLWFlNzAtZGVjNjE0MGU1OGZmZWNmZDEwN2ItYTU3', 'expires_in': 1209600, 'refresh_token': 'MDEyMzQ1Njc4OTAxMjM0NTY3ODkwMTIzNDU2Nzg5MDEyMzQ1Njc4OTEyMzQ1Njc4', 'refreshtokenexpires_in': 7776000}
devasc@labvm:~/labs/devnet-src/parsing$
```
2. Add print statements that display the token value and how many seconds until the token expires.
```
print("The access token is: {}".format(ourjson['access_token']))
print("The token expires in {} seconds.".format(ourjson['expires_in']))
```
3. Save and run your script. You should see the following output.
```
devasc@labvm:~/labs/devnet-src/parsing$ python3 parsejson.py 
{'access_token': 'ZDI3MGEyYzQtNmFlNS00NDNhLWFlNzAtZGVjNjE0MGU1OGZmZWNmZDEwN2ItYTU3', 'expires_in': 1209600, 'refresh_token': 'MDEyMzQ1Njc4OTAxMjM0NTY3ODkwMTIzNDU2Nzg5MDEyMzQ1Njc4OTEyMzQ1Njc4', 'refreshtokenexpires_in': 7776000}
1209600
The access token is ZDI3MGEyYzQtNmFlNS00NDNhLWFlNzAtZGVjNjE0MGU1OGZmZWNmZDEwN2ItYTU3
The token expires in 1209600 seconds
devasc@labvm:~/labs/devnet-src/parsing$
```

#### Step 3: Output the parsed JSON data in a YAML data format.
1. Add a print statement that will display the three dashes required for a YAML file. The two \n will add two lines after the previous output. Then add a statement to print ourjson as YAML data by using the dump() method of the yaml library. 
```
print("\n\n---")
print(yaml.dump(ourjson))
```
2. Save and run your script. You should see the following output.
```
devasc@labvm:~/labs/devnet-src/parsing$ python3 parsejson.py 
<output from previous steps omitted>
---
access_token: ZDI3MGEyYzQtNmFlNS00NDNhLWFlNzAtZGVjNjE0MGU1OGZmZWNmZDEwN2ItYTU3
expires_in: 1209600
refresh_token: MDEyMzQ1Njc4OTAxMjM0NTY3ODkwMTIzNDU2Nzg5MDEyMzQ1Njc4OTEyMzQ1Njc4
refreshtokenexpires_in: 7776000

devasc@labvm:~/labs/devnet-src/parsing$
```

### Part 4: Parse YAML in Python
The following program imports the json and yaml libraries, uses PyYAML to parse a YAML file, extract and print data values, and output a JSON version of the file. It uses the yaml library safe_load() method to parse the file stream and normal Python data references to extract values from the resulting Python data structure. It then uses the json library dumps() function to serialize the Python data back out as JSON.
The YAML example to parse is the same YAML file you outputted in Part 3:
```
---
access_token: ZDI3MGEyYzQtNmFlNS00NDNhLWFlNzAtZGVjNjE0MGU1OGZmZWNmZDEwN2ItYTU3
expires_in: 1209600
refresh_token: MDEyMzQ1Njc4OTAxMjM0NTY3ODkwMTIzNDU2Nzg5MDEyMzQ1Njc4OTEyMzQ1Njc4
refreshtokenexpires_in: 7776000
```

#### Step 1: Build a script to parse the YAML data.
1. Open the parseyaml.py file found in the ~/labs/devnet-src/parsing directory.
2. Import the json and yaml libraries.
```
import json
import yaml
```
3. Use the Python with statement to open myfile.yaml and set it to the variable name yaml_file. Then use the yaml.safe_load method to load the YAML file into a string set to the variable name ouryaml.
```
with open('myfile.yaml','r') as yaml_file:
    ouryaml = yaml.safe_load(yaml_file)
```
4.	Add a print statement for ouryaml to see that it is now a Python dictionary.
```
print(ouryaml)
```

#### Step 2: Run the script to print the YAML data and then modify it to print data of interest.
1. Save and run your script. You should see the following output.
```
devasc@labvm:~/labs/devnet-src/parsing$ python3 parseyaml.py 
{'access_token': 'ZDI3MGEyYzQtNmFlNS00NDNhLWFlNzAtZGVjNjE0MGU1OGZmZWNmZDEwN2ItYTU3', 'expires_in': 1209600, 'refresh_token': 'MDEyMzQ1Njc4OTAxMjM0NTY3ODkwMTIzNDU2Nzg5MDEyMzQ1Njc4OTEyMzQ1Njc4', 'refreshtokenexpires_in': 7776000}
devasc@labvm:~/labs/devnet-src/parsing$
```
2. Add print statements that display the token value and how many seconds until the token expires.
```
print("The access token is {}".format(ouryaml['access_token']))
print("The token expires in {} seconds.".format(ouryaml['expires_in']))
```
3. Save and run your script. You should see the following output.
```
devasc@labvm:~/labs/devnet-src/parsing$ python3 parseyaml.py 
{'access_token': 'ZDI3MGEyYzQtNmFlNS00NDNhLWFlNzAtZGVjNjE0MGU1OGZmZWNmZDEwN2ItYTU3', 'expires_in': 1209600, 'refresh_token': 'MDEyMzQ1Njc4OTAxMjM0NTY3ODkwMTIzNDU2Nzg5MDEyMzQ1Njc4OTEyMzQ1Njc4', 'refreshtokenexpires_in': 7776000}
The access token is ZDI3MGEyYzQtNmFlNS00NDNhLWFlNzAtZGVjNjE0MGU1OGZmZWNmZDEwN2ItYTU3
The token expires in 1209600 seconds.
devasc@labvm:~/labs/devnet-src/parsing$
```

#### Step 3: Output the parsed YAML data in a JSON data format.
1. Add a print statement to add two blank lines after the previous output. Then add a statement to print ouryaml as JSON data by using the dumps() method of the json library. Add the indent  parameter to prettify the JSON data.
```
print("\n\n")
print(json.dumps(ouryaml, indent=4))
```
2. Save and run your script. You should see the following output. Notice that the output looks just like the myfile.json.
```
devasc@labvm:~/labs/devnet-src/parsing$ python3 parseyaml.py 
<output from previous steps omitted>
{
  "access_token": "ZDI3MGEyYzQtNmFlNS00NDNhLWFlNzAtZGVjNjE0MGU1OGZmZWNmZDEwN2ItYTU3",
  "expires_in": 1209600,
  "refresh_token": "MDEyMzQ1Njc4OTAxMjM0NTY3ODkwMTIzNDU2Nzg5MDEyMzQ1Njc4OTEyMzQ1Njc4",
  "refreshtokenexpires_in": 7776000
}
devasc@labvm:~/labs/devnet-src/parsing$
```
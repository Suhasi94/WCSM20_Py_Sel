# rules to use pytest
#1.the module name should either start with test_* or *_test
#   ex:test_module1.py or module1_test.py

#2 All the classes inside the module should start from TestClassname or ClassnameTest
#3.functions/methods : test_methodname



import pytest

"""
@pytest.fixture()
def greet():
    print("****hi****")  #setup

def test_spam(greet):
    print("in test spam")

def test_display(greet):
    print("displaying a message")
"""

#########using autouse
"""
@pytest.fixture(autouse=True)
def greet():
    print("****hi****")  #setup
    yield
    print("***bye***") #teardown

def test_spam():
    print("in test spam")

def test_display():
    print("displaying a message")
"""

######## scope - function,class,session,module ### autouse=True,False


@pytest.fixture(scope="class")
def greet():
    print("****hi****")  #setup
    yield
    print("***bye***") #teardown

@pytest.mark.usefixtures("greet")
class TestSpam:
    def test_spam(self):
        print("in test spam")

    def test_display(self):
        print("displaying a message")
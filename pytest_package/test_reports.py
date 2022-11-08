# to gernerate reports
# pip install pytest-html
# in terminal -  pytest modulename -vs --html="report/path.html"



import pytest

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


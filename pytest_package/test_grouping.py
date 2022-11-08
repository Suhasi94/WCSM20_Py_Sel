#grouping test cases
#1. import pytest use @pytest.mark
#2types of markers - custom markers(grouping the test cases),inbuilt markers




from pytest import mark

"""
@mark.smoke
def test_validate_login(): #smoke
    print("executing login test")

@mark.regression
def test_shopping(): #regression
    print("executing shopping test")

@mark.regression
def test_payment(): #regression
    print("executing payment test")

@mark.smoke
def test_registration(): #smoke
    print("executing registration test")
"""

#inbuilt marker to parametrize the test cases
# @pytest.mark.parameterize(argument_names,argument_values)
# arguments_names - (string/list/tuples) where each name is sep by comma
#argument values - list of lists/list of tuple

@mark.parametrize("a,b",[(1,2),(3,4),(5,6)])
def test_add(a,b):
    print(a+b)

@mark.parametrize("l",[[2,3],[4,5]])
def test_square(l):
    for i in l:
        print(i*i)





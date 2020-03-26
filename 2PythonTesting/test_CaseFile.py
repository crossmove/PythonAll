
#Mandatory test file and test methods should start with 'test_' prefix 
# else tests doesnot identify by pytest

#Open command prompt in this directory 
# run following command 
# py.test


def test_add():
    print('add')
    assert 10 == 10

def test_sub():
    print('Subtract')
    assert 20 == 20
def one():
    print('one')
 
def two():
    print('two')

def three(a):
    print(a)
 
def switchFunction(abc):
    switcher = {
        1: one,
        2: two,
        3: three(2)    
    }
    # Get the function from switcher dictionary
    func = switcher.get(abc, lambda: "Invalid month")
    # Execute the function
    func()

if __name__ == "__main__":
    switchFunction(1)
    
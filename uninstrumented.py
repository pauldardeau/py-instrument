
def print_message(s):
    print(s)

def add_numbers(x,y):
    return x + y

def main():
    print_message('hello world')
    sum = add_numbers(3,4)
    print_message('sum of numbers = %s' % str(sum))

if __name__=='__main__':
    main()

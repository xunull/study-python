
testvar = 123

def test():
    global testvar
    testvar = 111
    print(testvar)

def main():
    print(testvar)
    test()
    print(testvar)

if __name__ == '__main__':
    main()
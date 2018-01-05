import os

def runTest(cmd, language):
    result = os.popen(cmd).read()
    print(language)
    print(result)
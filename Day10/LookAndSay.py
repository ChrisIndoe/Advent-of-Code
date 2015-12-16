import time
def looksay(string):
    curchar = ''
    curCount = 0
    outputString = ''
    for c in string:
        if c == curchar:
            curCount = curCount+ 1
        else:
            if curCount > 0:
                outputString = outputString + curCount.__str__() + curchar
            curchar = c
            curCount = 1
    return outputString + curCount.__str__() + curchar


result = '3113322113'
for n in range(50):
    start = time.time()
    result = looksay(result)
    end = time.time()
    print (n, ":",len(result), ":", end - start)

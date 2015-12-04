import hashlib

key = "bgvyzdsv"
value = 1

while True:
    hashValue = key+value.__str__()
    md5 = hashlib.md5(hashValue.encode('utf-8'))
    hashval = md5.hexdigest()
    if(hashval[:6] == '000000'):
        print("value Found", value)
        break
    # if(value > 99000000):
    #     print("Too many attempts: abandoning")
    #     break
    value = value + 1

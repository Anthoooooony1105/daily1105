import itertools
import zipfile

filename = '/Users/anthoooooony/Desktop/aaaa.zip'

def uncompress(file,password):
    try:
        with zipfile.ZipFile(filename) as zfile:
            zfile.extractall('./',pwd=password.encode("utf-8"))
            return True
    except:
        return False


chars = 'abcdefghijklmnopqrstuvwxyz0123456789'

for c in itertools.permutations(chars,4):
    password = "".join(c)
    print(password)
    result = uncompress(filename,password)
    if not result:
        print('fail',str(password))
    else:
        print('success'+str(password))
        break



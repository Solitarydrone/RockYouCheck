# Script i use to match with Rockyou
# Put RockYou in same folder or change path match

test_pass = input('Enter Password to test: \n')
path = 'rockyou.txt'

rslt = False
print("\nTesting.. {}".format(test_pass))

with open(path, errors="ignore") as fp:
    line = fp.readline()
    c = 1
    while line:
        line = fp.readline()
        if line.strip() == test_pass:
            print('{}: at index {}'.format(line.strip(), c))
            rslt = True
            break
        else:
            try:
                c += 1
            except:
                print("ERROR")
                
    if rslt is False:
        print("--------------------------------")
        print("No matches found!!!")
        print("Your password is STRONG")
        print("  So tuff - ᕙ(⇀‸↼‶)ᕗ\n")
    else:
        print("--------------------------------")
        print("Seemed it was leaked all along!")
        print("  Ah well, gotta run! - ᕕ( ᐛ )ᕗ\n")
        
input('Press Anykey to exit')

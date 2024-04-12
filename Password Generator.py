import string
import random
import sys

if __name__ == "__main__":
    
    s1 = string.ascii_lowercase
    s2 = string.ascii_uppercase
    s3 = string.digits
    s4 = string.punctuation
    

print("Welcome To Password Generator by Harshit Nashine")

try:
    plen = int(input("Enter Your Desired Password Length\n"))
except:
   sys.exit("Invalid Length\nYour Password Length should be in Integers only!") 


s = []
s.extend(list(s1))
s.extend(list(s2))
s.extend(list(s3))
s.extend(list(s4))
    
random.shuffle(s)

print("Your Password is:")
print("".join(s[0:plen]))
    
    
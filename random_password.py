import random
passlen = int(input("Enter the length of password: "))
n="abcdefghijklmnopqrstuvwxyz01234567890" \
  "ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
a =  "".join(random.sample(n,passlen ))
print (a)

secret_word = "python"
guess =""
while guess != secret_word:
   guess = input ("enter your password: ") 
if guess != secret_word:
      print("access denied! try again.")
else:
     print("access granted! The vault is open.")
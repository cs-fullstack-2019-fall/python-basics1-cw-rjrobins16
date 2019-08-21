
# ### Problem 1:
# Create two variables. One should equal “My name is: “ and the other should equal your actual name.
# Print the two variables in one print message.
# 

temp1= ("My name is: ")
myName = ("Rachel")

print(temp1 + myName)

# ### Problem 2:
# Ask the user to enter the extra credit they earned. If they entered less than 5 print 
# “That’s not enough extra credit.” If they entered more than 20 print “That’s too much extra credit”.

exCredit = int(input("Enter the extra credit earned"))

if exCredit <5:
    print("That's not enough extra credit")
    
if exCredit > 20:
    print("Too much dip on your chip")

# 
# ### Problem 3:
# Ask a user to enter a password. Enter a password. Ask user to reenter password. 
# Check to see if they are correct.
# 

userPassword = input("Enter a password")
userPassword2 = input("Re-Enter your password")

while userPassword != userPassword2:
    print("Passwords do not match. Re-enter your password.")
    userPassword2 = input("")

# ### Problem 4:
# Ask for two card numbers. If it equals 21 print BLACKJACK!, if it’s greater than 21 print BUST!, if it’s less than 21 print 
# “The total is [THE TOTAL]”

card1= int(input("Enter a card."))
card2= int(input("Enter another card."))
cardTotal = card1+card2
print(cardTotal)

if cardTotal == 21:
    print("BLACKJACK!")
    
elif cardTotal >21:
    print("BUST!")
    
elif cardTotal <21:
    print("The total is",+ cardTotal)
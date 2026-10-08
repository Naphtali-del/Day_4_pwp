Score = int(input("Enter your score: "))
print()

print("====================================================================")
print("==========================SS2 Promotion Checker=====================")
print("====================================================================")
print()



print("Your score is: ", Score)

if Score >= 70:
    print("Your grade is A")

elif Score >= 60:
    print("Your grade is B")

elif Score >= 50:
    print("Your grade is C")

elif Score >= 45:
    print("Your grade is D")

else:
    print("Your grade is F")

if Score >= 45:
    print("Congratulations on your promotion to SS2, see you next session.")
else:
    print("Unfortunately, you have not been promoted to SS2, please try again next semester.")
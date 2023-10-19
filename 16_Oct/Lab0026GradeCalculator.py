# Write a program that calculates and displays the letter grade for a given numerical score (e.g., A, B, C, D, or F) based on the following grading scale:

# input- score - 89
# output- B

Score = float(input("Enter your Percenatge\n"))

if Score >=90 and Score <=100:
    print(f"Your Grade is A")
elif Score >=80 and Score <=89:
    print(f"Your Grade is B")
elif Score >=70 and Score <=79:
    print(f"Your Grade is C")
elif Score >=60 and Score <=69:
    print(f"Your Grade is D")
elif Score>=0 and Score<=59:
    print(f"Your grade is F")
else:
    print(f"Invalid input")

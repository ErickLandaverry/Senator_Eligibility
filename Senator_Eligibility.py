#A person is eligible to be a US senator if they are at least 30 years old and have been a US citizen for at least 9 years. To be a US Representative, these numbers are 25 and 7. Write a program that accepts an age and years of citizenship and prints their eligibility for Senate and for House. Submit your source code as your answer.

def house():
  age_house = int(input("What is your age?: "))
  years_cit = int(input("How long have you been a US citizen? (years): "))

  if age_house >= 25 and years_cit >= 7:
    print("You qualify!")
  else:
    print("You do not qualify for a US Representative!")

def main():
  print("Let's see if you are eligible to be a US Senator!")
  
  age_senator = int(input("What is your age?: "))
  years_citizen = int(input("How long have you been a US citizen? (years): "))

  if age_senator >= 30 and years_citizen >= 9:
    print("You qualify!")
  else:
    print("You do not qualify as a US Senator!")

  print("Now let's see if you qualify to be a US Representative!")

  house()


main()

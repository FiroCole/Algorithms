# exercise-01 Vowel or Consonant

# Write the code that:
# 1. Prompts the user to enter a letter in the alphabet:
#      Please enter a letter from the alphabet (a-z or A-Z): 
# 2. Write the code that determines whether the letter entered is a vowel
# 3. Print one of following messages (substituting the letter for x):
#      - The letter x is a vowel
#      - The letter x is a consonant


letter = input("Please enter a letter from the alphabet (a-z or A-Z): ").lower()
vowels = "aeiou"
if letter in vowels:
  print(f"the letter {letter} is a vowel")
else:
  print(f"The letter {letter} is a consonant")


# exercise-02 Length of Phrase

# Write the code that:
# 1. Prompts the user to enter a phrase:
#      Please enter a word or phrase: 
# 2. Print the following message:
#      - What you entered is xx characters long
# 3. Return to step 1, unless the word 'quit' was entered.

word = ""
while True:
  word = input("Please enter a word or phrase: ")
  print(f" What you entered is {len(word)} characters long")
  
  if word =="quit":
    break


# exercise-03 Calculate Dog Years

# Write the code that:
# 1. Prompts the user to enter a dog's age like this:
#      Input a dog's age: 
# 2. Calculates the equivalent dog years, where:
#      - The first two years count as 10 years each
#      - Any remaining years count as 7 years each
# 3. Prints the answer in the following format:
#      The dog's age in dog years is xx


dog_years =""
while True:
  dog_years = input("Input a dog's age: ")
  dog_years = int(dog_years)
  
  age_calc = 0
  if dog_years <=2:
    age_calc = 10*dog_years
    print(f"The dog's age in dog years is {age_calc}")
  else:
    age_calc = (dog_years-2)*7 + 20
    print(f"The dog's age in dog years is {age_calc}")
  break

# exercise-04 What kind of Triangle?

# Write the code that:
# 1. Prompts the user to enter the three lengths of a triangle (one at a time):
#      Enter the lengths of three side of a triangle:
#      a: 
#      b:
#      c:
# 2. Write the code that determines if the triangle is:
#      equilateral - all three sides are equal in length
#      scalene - all three sides are unequal in length
#      isosceles - exactly two sides are the same length
# 3. Print a message such as:
#      - A triangle with sides of <a>, <b> & <c> is a <type of triangle> triangle


a =""
b = ""
c = ""
type = ""
while True:
  a =int(input(" Enter the lengths of three sides of a triangle: "))
  b =int(input(" Enter the lengths of three sides of a triangle: "))
  c =int(input(" Enter the lengths of three sides of a triangle: "))
  if a == b and a ==c:
    type = "equilateral"
  elif a !=b and a !=c:
    type = "scalene"
  else:
    type = "isosceles"
  print(f" A triangle with side lengths of {a}, {b} & {c} is a {type} triangle")
  break

# exercise-05 Fibonacci sequence for first 50 terms

# Write the code that:
# 1. Calculates and prints the first 50 terms of the fibonacci sequence.
# 2. Print each term and number as follows:
#      term: 0 / number: 0
#      term: 1 / number: 1
#      term: 2 / number: 1
#      term: 3 / number: 2
#      term: 4 / number: 3
#      term: 5 / number: 5
#      etc.


a, b = 0, 1
for term in range(50):
  print(a) 
  a, b = b, a + b 



# exercise-06 What's the Season?

# Write the code that:
# 1. Prompts the user to enter the month (as three characters):
#      Enter the month of the year (Jan - Dec):
# 2. Then prompts the user to enter the day of the month: 
#      Enter the day of the month:
# 3. Calculate what season it is based upon this chart:
#      Dec 21 - Mar 19: Winter
#      Mar 20 - Jun 20: Spring
#      Jun 21 - Sep 21: Summer
#      Sep 22 - Dec 20: Fall
# 4. Print the result as follows:
#      <Mmm> <dd> is in <season> 


month =""
day = ""
while True:
  month = input("Enter the month of the year (Jan - Dec): ").capitalize()
  day = int(input("Enter the day of the month: "))

  month = month[:3]  # Take the first three letters of the month
  season = ""

  if month in ("Jan", "Feb") or (month == "Dec" and day >= 21):
      season = "Winter"
  elif month in ("Apr", "May") or (month == "Mar" and day >= 20):
      season = "Spring"
  elif month in ("Jul", "Aug") or (month == "Jun" and day >= 21):
      season = "Summer"
  elif month in ("Oct", "Nov") or (month == "Sep" and day >= 22):
      season = "Autumn"
  elif month == "Dec" and day < 21:
      season = "Autumn"
  elif month == "Mar" and day < 20:
      season = "Winter"
  elif month == "Jun" and day < 21:
      season = "Spring"
  elif month == "Sep" and day < 22:
      season = "Summer"

  if season:
      print(f"{month} {day} is in {season}")
 


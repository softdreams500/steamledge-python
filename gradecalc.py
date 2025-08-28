# Step 1: Ask the user for a score
score = int(input("Enter your Score (0-100): "))
if score < 0 or score > 100:
  print ("wrong input")
else:
 if score >= 90:
  print ("Your Grade is A")
 elif score >= 80 and score < 90:
  print("Your Grade is B")
 elif score >= 70 and score < 80:
  print("Your Grade is C")
 elif score >= 40 and score < 70:
  print ("Your Grade is D")
 else:
  print("You  Failed")
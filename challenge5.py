score = input("Enter your score(0-100): ")
score = int(score)
if score >= 75 and score <= 100:
    print("A")
elif score >= 60 and score < 75:
    print("B")
elif score >= 50 and score < 60:
    print("C")
elif score >= 40 and score < 50:
    print("D")
elif score >= 0 and score < 40:
    print("F")
else:
    print("invalid")
score = input("Enter Score: ")
score = float(raw_input("Enter Score: "))
if(score>1.0):
    print ("out of range")
elif score >= 0.9:
    print ("A")
elif score >= 0.8:
    print ("B")
elif score >= 0.7:
    print ("C")
elif score >= 0.6:
    print ("D")
elif score < 0.6:
    print ("F")

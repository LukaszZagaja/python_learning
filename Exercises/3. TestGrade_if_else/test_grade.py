print('\nGive a score between 0 and 100')
score = int(input("Give a score to grade: "))

if(score >= 0 and score <= 100):
    print('Score good to grade')
    
    if(score >= 0 and score <=50):
        print(score, " equals 2.0 grade")
    elif(score > 50 and score <= 60):
        print(score, ' equals 3.0 grade')
    elif(score > 60 and score <= 70):
        print(score, ' equals 3.5 grade')
    elif(score > 70 and score <= 80):
        print(score, "equals 4.0 grade")
    elif(score > 80 and score <= 90):
        print(score, "equals 4.5 grade")
    elif(score > 90 and score <= 100):
        print(score, "equals 5.0 grade")
else:
    print('Not a score on test')
import random
random_num = random.randint(60,100)

def scores_grades():
    count = 0
    print "Scores and Grades"
    while (count < 10):
        random_num = random.randint(60,100)
        count = count + 1
        if (random_num >= 60) and (random_num <= 69):
            print "Score: {}; Your grade is a D.".format(random_num)
        elif (random_num >= 70) and (random_num <= 79):
            print "Score: {}; Your grade is a C.".format(random_num)
        elif (random_num >= 80) and (random_num <= 89):
            print "Score: {}; Your grade is a B.".format(random_num)
        elif (random_num >= 90) and (random_num <= 100):
            print "Score: {}; Your grade is a A.".format(random_num)
    print "End of program. Bye!"        
scores_grades()

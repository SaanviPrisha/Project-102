totalDayLeft = input("Days left to study: ")
totalDaysLeft = int(totalDayLeft)
chapters = input("Number of chapters total: ")
averageTimePerChapter = input("The average time you take per chapter in hours: ")

totalTimeToBeSpent = float(chapters)*float(averageTimePerChapter)

timePerDay = float(totalTimeToBeSpent)/float(totalDaysLeft)
print("You need to spend ",timePerDay," hours studying everyday")

if(timePerDay >= 10):
    print("You needed to start studying earlier! Remeber that for the future... but for now start cramming. ")
elif(totalDaysLeft >= 15 and timePerDay <= 6):
    print("You have a whole bunch of time, but there isn't anytime to study then like the future.")
else:
    print("The ideal time to start studying. Start making your planner!")


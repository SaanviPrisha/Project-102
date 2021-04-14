print("  DAILY STUDY TIME")
totalDaysLeft = input("Days left to study (num): ")
chapters = input("Number of chapters total: ")
averageTimePerChapter = input("The average time you take per chapter in hours: ")

totalTimeToBeSpent = float(chapters)*float(averageTimePerChapter)
print("You need to study for ",totalTimeToBeSpent,"hours in all. ")
print("Which means,")

timePerDay = float(totalTimeToBeSpent)/float(totalDaysLeft)
print("You need to spend ",timePerDay," hours studying everyday")
print("or you can spend",timePerDay*2,"hours studying alternate days")
print("In minutes: ")
print("You need to spend ",timePerDay*60," minutes studying everyday")
print("or you can spend",timePerDay*120,"minutes studying alternate days, to keep the flow")
58

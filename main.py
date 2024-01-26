# Morning time zone starts at 04:00:00 to 11:59:59
# Afternoon time zone starts at 12:00:00 to 15:59:59
# Evening time zone starts at 16:00:00 to 19:59:59
# Night time zone starts at 20:00:00 to 24:59:59

import time
RealTime = time.strftime('%H:%M:%S')
Hours = int(time.strftime('%H'))
Name = input("Enter Your Name Please: ").capitalize()


if Hours >= 4 and Hours <= 12:
    print(Name, ", Good Morning Sir!")

elif Hours >= 12 and Hours <= 16:
    print(Name, ", Good Afternoon Sir!")       

elif Hours >= 16  and Hours <= 20:
    print(Name, ", Good Evening Sir!")  

elif Hours >= 20 and Hours <= 24:
    print(Name,", Good Night Sir!")     
#  be found at https://github.com/github/gitignore/blob/main/Global/JetBrains.gitignore
#  and can be added to the global gitignore or merged into this file.  For a more nuclear
#  option (not recommended) you can uncomment the following to ignore the entire idea folder.
#.idea/

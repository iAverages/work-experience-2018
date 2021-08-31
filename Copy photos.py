import os
import datetime
import time
import shutil

#File Dirs
backupDir = "C:\\Backups\\"
photoDir = "C:\\Photos\\"

#Current Date
now = str(datetime.datetime.now())
#Creates String for date
year = now[:4]
month = now[5:7]
day = now[8:10]
tdate = year + month + day
print ("Current date")


#Current day of week
tdate1 = datetime.datetime.today()
tday = tdate1.weekday()
#Reset tday. Fixs calc bug
tday = tday + 1
oday = tday

print("Date - " + str(tdate))
print("Weekday - " + str(tday))
 

#Loop
for root, dirs, files in os.walk(photoDir, topdown=False):
    for name in dirs:
        tday = oday #Resets day. Fixed calc bug
        ntday = oday #^^

        #Creates dir path of file
        fullname = os.path.join(root, name)
        print("\n\nFile Info\nFile Dir - " + fullname)

        #Get file stats
        modtime = os.stat(fullname)
        #converts seconds since epoch to utc
        fday= time.gmtime(modtime[8])
        
        #Creates sting for date modified
        fday1 = "0" + str(fday[1])
        fday2 = "0" + str(fday[2])
        fdate = str(fday[0]) + fday1[-2:] + fday2[-2:]
        fday = fday[6]
        fday = fday + 1

        #Prints values
        print("TodayDate (tdate) - " + str(tdate))
        print("FileDate (fdate) - " +str(fdate))
        print("TodayDay (tday) - " + str(tday))
        print("FileDay (fday) - " + str(fday))

        #Correcting date numbers to calc correctly
        if tday < fday:
            ntday = tday + 7
        calc = ntday - fday
        print("NewTodayDay (ntday) - "+ str(ntday))
        datediff = int(tdate) - int(fdate)
        
        #Difference between today day and file modified day
        diff = int(ntday) - int(fday)
        print("Day differnece - " + str(diff))

        #date diff
        print("Date Difference - " + str(datediff))
        if datediff > 6:
            shutil.move(fullname, backupDir)
            print("Moved Old files to" + backupDir)
            continue

        maxdays = 2
        # vv  Remove # for debugging  vv
        #print("MaxDaysBeforeCalc - " + str(maxdays))
        if tday == 0 or tday == 1 or tday == 5 or tday == 6:
            maxdays = maxdays + 2
            
        # vv  Remove # for debugging  vv
        #print("MaxDaysAfterCalc - " + str(maxdays))
            
        #Move Files if older than maxdays old 
        if calc > maxdays:
            shutil.move(fullname, backupDir)
            print("Copied and Removed to - " + backupDir)

        #Ignore file if less than 2 days old 
        if calc < 2:
            print("Ignoring file. Less than 2 days old")

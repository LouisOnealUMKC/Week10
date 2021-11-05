import csv

def month_from_number(MonthNumber):
    MonthNames = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    return MonthNames[int(MonthNumber)-1]

def read_in_file(filename):
    Reports = []
    file = open(filename, encoding = "utf-8")
    file_csv = csv.reader(file)
    for line in file_csv:
        Reports.append(line)
    file.close
    return Reports

def create_reported_date_dict(fileList):
    keyCount = {}
    for line in fileList:
        if line[1] in keyCount:
            keyCount[line[1]] = keyCount[line[1]] + 1
        else:
            keyCount[line[1]] = 1
    return keyCount

def create_reported_month_dict(fileList):
    keyCount = {}
    for line in fileList:
        if line[1].split('/')[0] in keyCount:
            keyCount[line[1].split('/')[0]] = keyCount[line[1].split('/')[0]] + 1
        else:
            keyCount[line[1].split('/')[0]] = 1
    return keyCount

def create_offense_dict(fileList):
    keyCount = {}
    for line in fileList:
        if line[7] in keyCount:
            keyCount[line[7]] = keyCount[line[7]] + 1
        else:
            keyCount[line[7]] = 1
    return keyCount


def create_offense_by_zip(fileList):
    OffenseDict = {}
    for line in fileList:
        if line[7] not in OffenseDict:
            OffenseDict[line[7]] = {}
        else:
            if line[13] in OffenseDict[line[7]]:
                OffenseDict[line[7]][line[13]] = OffenseDict[line[7]][line[13]] + 1
            else:
                OffenseDict[line[7]][line[13]] = 1
    return OffenseDict

'KCPD_Crime_Data_2019.csv'


def MainProgram():
    try:
        fileName = input("Enter the name of the crime data file ==> ")
        MyReports = read_in_file(fileName)
    except:
        print("Could not find the file specified")
        MainProgram()
    
    MonthDict = create_reported_month_dict(MyReports)
    max_key = max(MonthDict, key = MonthDict.get)
    print("The month with the highest # of crimes is " + month_from_number(max_key) + " with " + str(MonthDict[max_key]) + " offenses.")

    MostOffenses = create_offense_dict(MyReports)
    Offenses_max_key = max(MostOffenses, key = MostOffenses.get)
    print("The offense with the highest # of crimes is {} with {} offenses".format(Offenses_max_key,MostOffenses[Offenses_max_key]))
    zipOffenses = create_offense_by_zip(MyReports)
    target = input("Enter an offense: ")
    while(target not in zipOffenses):
        print('No valid offense found. Try again. ')
        target = input("Enter an offense: ")
    print("{} offenses by Zip Code".format(target))
    print( "{0:20} {1}".format("Zip Code", "# Offenses"))  
    print("====================================")  
    for k, v in zipOffenses[target].items():  
        print( "{0:20} {1}".format(k,v))

if __name__ == "__main__":
    MainProgram()

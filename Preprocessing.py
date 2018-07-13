# This program takes Stock Data of a company as input and returns another file containing trends about variations

import pandas

# This function finds whether stock values increased/decreased in comparison to previous day and also calculates the percent change
def Preprocess_File(file):
    newsheet = pandas.read_csv(file)
    date = newsheet['Date']
    Close = newsheet['Close']
    Percent_Change = [0]* len(date)
    Shift = [0]* len(date)

    dates = [i.split(' ', 1)[0] for i in date]

    for i in range (1,len(date)):
        if Close[i] > Close[i-1] :
            Shift[i] = "+"
            Percent_Change[i] = (Close[i]-Close[i-1])/Close[i-1]
        else :
            Shift[i] = "-"
            Percent_Change[i] = (Close[i-1] - Close[i]) / Close[i - 1]

    newsheet = pandas.DataFrame({'Date':date, 'Close':Close, 'Percent Change':Percent_Change, 'Shift':Shift})   # Creates new empty table with the mentioned columns

PF0 = Preprocess_File("NASDAQ.csv")
PF1 = Preprocess_File("Amazon.csv")
PF2 = Preprocess_File("Facebook.csv")
PF3 = Preprocess_File("Google.csv")
PF4 = Preprocess_File("Microsoft.csv")
PF5 = Preprocess_File("Netflix.csv")
PF6 = Preprocess_File("Samsung.csv")
PF7 = Preprocess_File("Sony.csv")
PF8 = Preprocess_File("Tesla.csv")

# New File of each company created containing required data
PF0.newsheet.to_csv("NASDAQ_Processed.csv",index=False,header=True)
PF1.newsheet.to_csv("Amazon_Processed.csv",index=False,header=True)
PF2.newsheet.to_csv("Facebook_Processed.csv",index=False,header=True)
PF3.newsheet.to_csv("Google_Processed.csv",index=False,header=True)
PF4.newsheet.to_csv("Microsoft_Processed.csv",index=False,header=True)
PF5.newsheet.to_csv("Netflix_Processed.csv",index=False,header=True)
PF6.newsheet.to_csv("Samsung_Processed.csv",index=False,header=True)
PF7.newsheet.to_csv("Sony_Processed.csv",index=False,header=True)
PF8.newsheet.to_csv("Tesla_Processed.csv",index=False,header=True)
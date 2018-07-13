# This program uses data from preprocessed files and calculates other trends and returns one large training dataset

import pandas

file0 = "NASDAQ_Processed.csv"
file1 = "Amazon_Processed.csv"
file2 = "Facebook_Processed.csv"
file3 = "Google_Processed.csv"
file4 = "Microsoft_Processed.csv"
file5 = "Netflix_Processed.csv"
file6 = "Samsung_Processed.csv"
file7 = "Sony_Processed.csv"
file8 = "Tesla_Processed.csv"

# Function which returns parameters of each stock file as a list
def Extract_Processed_Data(file):
    new = pandas.read_csv(file)
    Date = new['Date']
    Close = new['Close']
    Percent_Change = new['Percent Change']
    Shift = new['Shift']
    parameter_list = [Date, Close, Percent_Change, Shift]      # List containing lists of column info
    return parameter_list

EL0 = Extract_Processed_Data(file0)
EL1 = Extract_Processed_Data(file1)
EL2 = Extract_Processed_Data(file2)
EL3 = Extract_Processed_Data(file3)
EL4 = Extract_Processed_Data(file4)
EL5 = Extract_Processed_Data(file5)
EL6 = Extract_Processed_Data(file6)
EL7 = Extract_Processed_Data(file7)
EL8 = Extract_Processed_Data(file8)

SVM_List = [EL0, EL1, EL2, EL3, EL4, EL5, EL6, EL7, EL8]

end = 1513    # This is the number of rows of data in each stock file plus 1

# This function returns a list of Average Percent change over 5 days
def Calculate_Average_Percent_Change(Extracted_List):
    list = []
    for i in range(5, end):
        Average_Percent_Change = (Extracted_List[2][i] + Extracted_List[2][i-1] + Extracted_List[2][i-2] + Extracted_List[2][i-3] + Extracted_List[2][i-4])/5
        # Extracted_List[2] contains list of percent changes for each file
        list.append(Average_Percent_Change)
    return list

# This function returns a list of Average Shift over 5 days
def Calculate_Average_Shift(Extracted_List):
    list = []
    Shift_List = []
    # Converting + to 1 and - to 0 for calculating shift change and storing it in a list
    for i in range(1,end):
        if Extracted_List[3][i] == '+':
            Shift_List.append(1)
        else:
            Shift_List.append(0)
    for j in range(5,end):
        Average_Shift = (Shift_List[j] + Shift_List[j-1] + Shift_List[j-2] + Shift_List[j-3] + Shift_List[j-4])/5
        list.append(Average_Shift)
    return list

Stock_Value, Stock_Value_Fluctuation, Stock_Shift, Market_Fluctuation, Market_Shift = [],[],[],[],[]

for x in range(1,9):
    for y in range(1,end):
        Stock_Value.append(SVM_List[x][1][y])

    l1 = Calculate_Average_Percent_Change(SVM_List[x])
    for value in l1:
        Stock_Value_Fluctuation.append(value)

    l2 = Calculate_Average_Shift(SVM_List[x])
    for value in l2:
        Stock_Shift.append(value)

for x in range (1,end):
    for y in range (1,9):
        Market_Fluctuation.append(EL0[2][x])
        Market_Shift.append(EL0[3][x])

# Creating new file which contains the final training dataset
dataset = pandas.DataFrame({'Stock Value': Stock_Value, 'Stock Value Fluctuation': Stock_Value_Fluctuation, 'Stock Shift': Stock_Shift, 'Market Fluctuation': Market_Fluctuation, 'Market Shift': Market_Shift})
dataset.to_csv("SVM_Training_Data.csv",index=False,header=False)


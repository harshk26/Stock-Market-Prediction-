import time
import numpy
from sklearn import svm
from csv import reader

# Function for reading training dataset file
def Read_file(file_name):
    dataset = list()
    with open(file_name, 'r', newline='',encoding='utf-8') as file:
        csv_reader = reader(file)
        for row in csv_reader:
            if not row:
                continue
            dataset.append(row)
    return dataset

training_dataset = Read_file('SVM_Input_File.csv')
test_target= Read_file('SVM_Target.csv')

start_time = time.time()

n_epoch = 30
w = 0
r = 1
runs = [0]*30

for j in range(len(runs)):
    # learning_rate = learning_rate + 0.05
    # n_epoch = n_epoch + 4
    r =  r + 1000
    if (r + 10000) > 12100:
        r = w
        w += 300
    traindataset = [testdataset[i] for i in range(r, r + 10000)]
    train_target = [test_target[i] for i in range(r, r + 10000)]
    clf = svm.SVC(kernel="rbf", decision_function_shape='ovo')
    clf.fit(traindataset, train_target)

    # test network
    count = 0
    total = 0
    for i in range(0, len(testdataset)):
        total += 1
        temp = clf.predict([testdataset[i]])
        if temp == test_target[i]:
            count += 1
    accuracy = count * 100 / total
    print('Accuracy: %s' % accuracy)
    runs[j] = accuracy

mean = sum(runs)/len(runs)
print("n_epoch: {}".format(n_epoch))
print("Mean_Accuracy: {}".format(mean))
print("Standard_Deviation: {}".format(np.std(runs, 0)))
time_taken = time.time() - start_time
print("total_time : {}".format(time_taken))

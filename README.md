# Stock-Market-Prediction-
Stock Market Prediction using Machine Learning

This is a basic stock market predictor
Uses SVM(Support Vector Machine)

Methodology:
Raw Data containing information about stocks was collected online. I collected 6 years of data from July 9,2012 to July 8,2018. Data was collected from the following 8 companies: Amazon, Facebook, Google, Microsoft, Netflix, Samsung, Sony, Tesla. The selection of the companies was completely random. In addition to this data was collected from the NASDAQ Stock Exchange Market. 
The data obtained contained the following features: Date, Open, High, Close, Adj Close and Volume. I considered the daily closing values of each stock as their stock value.
From this data I first determined whether the change(shift) in stock price was positive or negative for each day. I also calculated the percentage change in the stock values.
For building my training dataset I calculated the following 5 features from the preprocessed data:
1. Stock Value : This is the price of the stock at close of market each day
2. Stock Value Fluctuation : This was calculated as an average of the percentage change over the previous 5 days
3. Stock Shift : This was calculated as an average of the Shift in Stock over the previous 5 days. This was done by assigning 1 to an increase and 0 to a decrease.
4. Market Fluctuation : This was calculated as an average of the percentage change of the NASDAQ Index over the previous 5 days.
5. Market Shift : This was calculated as an average of the Shift in stocks in NASDAQ Index over the previous 5 days. This was done by assigning 1 to an increase and 0 to a decrease.
The final training dataset contained 12088 rows as each processed file had 1511 rows of data. 1511 * 8 = 12088.

Prediction:
The aim of the project was to simply predict a positive or negative change in the stock prices for the next day. Hence this problem was treated as a classification problem. In Machine Learing, SVM's are supervised learning models used for classification and regression analysis. Given a set of training examples each marked as belonging to one or the other of the two categories, an SVM training algorithm builds a model that assigns new examples to each category. In this case the model was first trained using the training dataset and was then used for prediction.



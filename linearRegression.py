#Load python library to read the CSV created
import pandas 
import csv

#Read the data from csv into a pandas data frame
df = pandas.read_csv('new2_training_dataset.csv')
df_test = pandas.read_csv('test_dataset.csv')

#Import the linear regression function from sklearn
from sklearn.linear_model import LinearRegression
estimator = LinearRegression()

train = df[['followers','listed','followings','verified','Total_favourite_count']]

labels = df[['tweet_favorite_count']]

test_data = df_test[['followers','listed','followings','verified','Total_favourite_count']]

print train

print labels

print test_data

#fit the data into the model
estimator.fit(train, labels)

#get predictions
ans = estimator.predict(test_data[:3000])

print 'ans: ', ans
print len(ans)

for item in ans:
	print item





import pandas
db = pandas.read_csv('marks.csv')
db
y = db['marks']
x = db['hours']
from sklearn.linear_model import LinearRegression
mind = LinearRegression()
x = x.values
y = y.values
type(x)
x=x.reshape(3,1)
x
mind.fit( x, y)
p = int(input("the prediction of digit?? "))

q=(mind.predict([[p]]))
print(q)

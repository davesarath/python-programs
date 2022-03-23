import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

data =\
[
[0, 1],
[1, 2],
[2, 4],
[3, 6],
[4, 8],
[5,10],
[6,12],
[7,14],
[8,16],
[9,18],
[10,20]
]

X = np.array(data)[:,0].reshape(-1,1)
y = np.array(data)[:,1].reshape(-1,1)
print("X=")
print(X)
print("y=")
print(y)

to_predict_x= [11,12,13]
to_predict_x= np.array(to_predict_x).reshape(-1,1)

regsr=LinearRegression()
regsr.fit(X,y)

predicted_y= regsr.predict(to_predict_x)
m= regsr.coef_
c= regsr.intercept_
print("Predicted y:\n",predicted_y)
print("slope (m): ",m)
print("y-intercept (c): ",c)



# https://www.codespeedy.com/predict-next-number-in-a-sequence-with-scikit-learn/


### for graph
# import matplotlib.pyplot as plt
# %matplotlib inline
# plt.title('Predict the next numbers in a given sequence')  
# plt.xlabel('X')  
# plt.ylabel('Numbers') 
# plt.scatter(X,y,color="blue")
# new_y=[ m*i+c for i in np.append(X,to_predict_x)]
# new_y=np.array(new_y).reshape(-1,1)
# plt.plot(np.append(X,to_predict_x),new_y,color="red")
# plt.show()

## Hey Here!!! ###
    we are seeing about model_prediction using linear regression.

    
## 1. Data collection
    import pandas as pd
    student_marks=pd.read_csv("student marks.csv",sep='\t')
    student_marks.head()

## 2. Initial analysis
     student_marks.isnull().sum() 

## 3. Data preparation
      here, already have clean the dataset.

## 4. Data understanding
# about the dataset:""Number of rows is 0 to 100
# mean(average of courses,study_time,marks)=5,4,24
# and max=55,
# min=5 then ,median=20,important thing about the dataset is looks it that percentage"" 
      student_marks.describe()

## 5. Find the relationship by using correlation
      student_marks.corr()

## 6. To build the model
      from sklearn.model_selection import train_test_split

      x = student_marks[['number_courses','time_study']]
      y = student_marks[['Marks']]
      x_train,x_test,y_train,y_test= train_test_split(x,y,test_size=0.2,random_state=42)

## 7. To train the model
      from sklearn.linear_model import LinearRegression
      
      model = LinearRegression()
      model.fit(x_train,y_train)
      model.score(x_test,y_test)

## 8. Model testing (PREDICTION)
      model.predict([[5,4]])

##  9. Save my trained model
      import joblib
      joblib.dump(model,"linear_model.pkl") 

**** you got the saved your trained ml model ****


    
    

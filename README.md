##### Hey Here!!! #####
  ##### we are seeing about model_prediction using linear regression.

    
##### 1. Data collection
    import pandas as pd
    student_marks=pd.read_csv("student marks.csv",sep='\t') ## tab_space file 
    print(student_marks)

##### 2. Initial analysis
     student_marks.isnull().sum() 

##### 4. Data understanding
#### about the dataset:""Number of rows is 0 to 100 mean(average of courses,study_time,marks)=5,4,24 and max=55, min=5 then ,median=20,important thing about the dataset is looks it that percentage"" 
      student_marks.describe()
      
##### 4. Data preparation
      here, already have clean the dataset.


##### 5. Find the relationship by using correlation
      student_marks.corr()

##### 6. To split the training dataset
      from sklearn.model_selection import train_test_split

      x = student_marks[['number_courses','time_study']]
      y = student_marks[['Marks']]
      x_train,x_test,y_train,y_test= train_test_split(x,y,test_size=0.2,random_state=42)

##### 7. To build the model
      from sklearn.linear_model import LinearRegression
      
      model = LinearRegression()

##### 8. To train the model     
      model.fit(x_train,y_train)

##### 9. To test/evaluate the model 
      model.score(x_test,y_test)

##### 10. To Model the PREDICT
      model.predict([[5,4]])

##### 11.To Save trained model
      import joblib
      joblib.dump(model,"linear_model.pkl") 

**** you got the saved your trained ml model ****


    
    

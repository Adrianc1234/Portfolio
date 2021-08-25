# DATA BASE ABOUT CANCER USING EDA-CANCER
# STEPS:
## STEP 1:
We imported the libreries that we used to make that the functions or tools works
these are the libreries that you need to import and you need to have installed on your computer like mathplotlib that is a librery that python does not have installed.
````Python
from sklearn import datasets
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
````
## STEP 2:
We made a function to get the target names of the file that we will read and after that we return the value of the names inside of the target names, in this case the names are "malignant" and "benign".
````Python
def cancer(value):
    cancer = breast_cancer.target_names[value]
    return cancer
#python lamda function
cancer_function = lambda x: breast_cancer.target_names[x]
````
## STEP 3:
For this step we read the json and we print it to see the keys and other things that we will need for the next things.
````Python
breast_cancer = datasets.load_breast_cancer()
breast_cancer
````
If you want to see the picture for this step, you can see the output:
https://github.com/Adrianc1234/Cancer/blob/master/Cancer%20homework/imagen_1.png

## STEP 4:
In this step we make a DataFrame and we call the json and use the key data to make the table with feature_names which has all the titles for the columns on the table. Then, we make a column with the name Types and we call from the json the values that are in the key target and put them inside it; after we say how the Data Frame will read the title and we delete the space on them and for the end we apply the function to change 0 or 1 by the names on target_names.
````Python
data= pd.DataFrame(breast_cancer.data, columns= breast_cancer.feature_names)
data['Types']= breast_cancer.target
data.columns = data.columns.str.replace(" ","")
data.Types= data.Types.apply(cancer)
data.head()
````
You can see the output:
https://github.com/Adrianc1234/Cancer/blob/master/Cancer%20homework/imagen_2.jpg

And to see some statistical calculations we make this code:
````Python
data.describe()
````
Output:
https://github.com/Adrianc1234/Cancer/blob/master/Cancer%20homework/imagen_3.jpg

We can see the target_names using:
````Python
breast_cancer.target_names
````
If we want to see  all the information about the Data Frame we can run this code:
````Python
data.info()
````
Output:
https://github.com/Adrianc1234/Cancer/blob/master/Cancer%20homework/imagen_4.png

We can check if some column has an empty values with this function, where .isnull() function checks the empty values and the .sum() function makes a sum to count how many values are empty:
````Python
data.isnull().sum()
````
Output:
https://github.com/Adrianc1234/Cancer/blob/master/Cancer%20homework/imagen_5.png

If we check how many types of values are in Types column, we use this function where the .Type says the column that we will check and the other function that is .value_counts() make the count of the values and print it.
````Python
data.Types.value_counts()
````
Output:
https://github.com/Adrianc1234/Cancer/blob/master/Cancer%20homework/imagen_6.png

## STEP 5:
### we classify the different values in one specific Data Frame.
We need to separate by titles the data set beacuse if we don't, it will look one over another because we have many data.
````Python
#making the frist table for mean
means=pd.DataFrame(data.iloc[:,0:10])
means['type']=breast_cancer.target
means.type= means.type.apply(cancer)

#making dataframe for error
error=pd.DataFrame(data.iloc[:,10:20])
error['type']=breast_cancer.target
error.type= error.type.apply(cancer)

#making dataframe for worst
worst=pd.DataFrame(data.iloc[:,20:30])
worst['type']=breast_cancer.target
worst.type= worst.type.apply(cancer)
````
Output:
https://github.com/Adrianc1234/Cancer/blob/master/Cancer%20homework/imagen_7.png

## STEP 6
Now we use these different functions to show the histogram about data and get the standar deviation and others Statitical values.(We are using mathplotlib.plt) if we want to use one function of pandas then you need to write "nameofyourdataset.function".
### Univariate analysis
````Python
#Histograma
plt.rcParams["figure.figsize"] = (20,20)
mean_variables.hist()
plt.suptitle("Histograms Mean Parameters")
plt.show()

#Boxplot
mean_variables.boxplot()
plt.title("Boxplot")
plt.show()

#Displot
for column in mean_variables.columns[:9]:
    g = sns.FacetGrid(cancer_data, hue = "TypeCancer", height = 4)
    g = g.map(sns.distplot, column)
    g = g.add_legend()
    plt.show()
    
#Mean features
plt.rcParams["figure.figsize"] = (10,10)
mean_variables.groupby(by = 'Type').mean().plot(kind = "bar")
plt.title("Dataset Mean Variables")
plt.ylabel("Features Mean")
plt.grid(True)
plt.legend(loc = 'upper left', bbox_to_anchor = (1,1))
plt.show()

plt.rcParams["figure.figsize"] = (10,10)
mean_variables.iloc[:, 4:].groupby(by = 'Type').mean().plot(kind = "bar")
plt.title("Dataset Mean Variables")
plt.ylabel("Features Mean")
plt.grid(True)
plt.legend(loc = 'upper left', bbox_to_anchor = (1,1))
plt.show()
````
### Multivariate analysis
````Python
# Correlation matrix Mean variables
correlation_matrix_mean = mean_variables.corr()

# Heatmap
sns.heatmap(correlation_matrix_mean, annot = True, cmap ='RdBu')
plt.show()

#Pairplot
g = sns.pairplot(mean_variables, hue = 'Type')
plt.show()
````
## STEP 7
### showing the graphics.
In this part we make all the respective graphs for every DataFrame that we divided by "Mean", "Error" and "worst".
#### Univariate graphs:
You can see in this folder the Univariate graphs:
https://github.com/Adrianc1234/Prepocessing-Data/tree/master/Cancer%20homework/Univariate
#### Conclusions:

##### Boxplot:
###### Mean: The box of the meanarea shows an important difference taking into account that the rest of the parameters are smaller quantities 

###### Error: The same happens in errorarea as a relevant parameter to perform the classification since it is the same area and it represents an larger quantity

###### Worst: The worstarea is the most visible parameter 


##### Features:
###### Mean:  Mean area shows an important difference between the malignant and benign types of cancer, but it is clear that is the parameter with the largest quantities so we decided to plot the rest parameters excluding the mean area, and we realized that an important parameter that shows an important difference is the meanconcavitiy and meancompacteness, the rest of parameters are irrelevant since this do not show an important difference in quantity between the type of cancer.

###### Error: Error area is the parameter that shows an important difference followed by the concavity error and compactness error as these parameters are correlated to the mean parameters.

###### Worst: The same happens to the worst parameters, worst concavity, worst compactness and worst area.

##### Histogram:

- Mean:   Mean smoothness mean texture and mean texture histograms show that our data has a tendency to be normally distributed, contrary to the rest of the parameter which are positively skewed.
- Error: The histograms for the error parameters show that are positively skewed, this means that most of the observations are close to cero and there a few parameters with a large error.
- Worst: Worst smoothness and worst texture are normally distributed, contrary to the rest of the parameters which are positively skewed.


#### Multivariate graphs:
You can see in this folder the Multivariate graphs:
https://github.com/Adrianc1234/Prepocessing-Data/tree/master/Cancer%20homework/Multivariate
#### Conclusions:

##### Correlation matrix:

- Mean: In the correlation matrix the variables with the most obvious correlation are mean area and mean radius, the other important correlation was the mean area and the mean perimeter with a correlation of .99; other relevant correlations were mean concave points with mean concavity with a correlation of .92; mean compactness with mean concavity with .88. Mean concave points share a correlation above .80 with mean radius, mean area, mean perimeter. In the other hand mean fractal dimension shared a negative correlation between mean radius, mean texture, mean perimeter and mean area.

- Error: In the correlation matrix the parameters that shows an important correlation are perimeter error and the radius error with a correlation of .97 which can be obvious, the error area shows important correlation with the radius error and the perimeter error with .94 and .95 respectively, compactness error shares a relevant correlation between fractal dimension error, concave points error and concavity error with a correlation close to .80; concavity error shows a correlation with fractal dimension and concave points error. The rest of the parameters share a low correlation.
 
- Worst: In the correlation matrix of the parameters with the worst prefix, it shares a similar relation between the error parameters with just a  small difference.

##### Pairplot:

- Mean: The pairplot for the mean shows an important separation of types of cancer, except for the meanfractaldimension parameter which its data overlaps and there is no clear difference between the types, so I wouldn’t be relevant for a later classification.

- Error: For the error parameters just radius error, perimeter error and area error are the variables that shows a difference between the types, when these parameters are plotted with the rest of the variables.


- Worst: In the pairplot for worst, happens a similar case to the mean parameters, the worst fractal dimension and the worst texture with worst smoothness are not clear for a classification 

#### Conclusions:

__Given the multivariate and univariate analysis we can conclude that the most relevant parameters to perform a classification of a benign or a malignant type of cancer are area, perimeter and radius, the rest are relevant to perform a classification but it is important to point out the fractal dimension would help in a classification process since it has a low correlation between the rest of the parameters, and the pair plot does not share a clear path to perform a classification between the variables.__

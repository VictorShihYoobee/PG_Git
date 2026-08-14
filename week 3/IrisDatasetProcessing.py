from ucimlrepo import fetch_ucirepo 
  
# fetch dataset 
iris = fetch_ucirepo(id=53) 
  
# data (as pandas dataframes) 
features = iris.data.features 
targets = iris.data.targets 
  
# metadata 
print("Total number of record: ",len(features)) 
unique_names = targets.iloc[:, 0].nunique()
print("Number of unique flower types: ",unique_names)
for name in targets.iloc[:, 0].unique():
    print(name)


# variable information 
#print(iris.variables) 

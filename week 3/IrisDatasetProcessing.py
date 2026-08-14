from ucimlrepo import fetch_ucirepo 
  
# fetch dataset 
iris = fetch_ucirepo(id=53) 
  
# data (as pandas dataframes) 
features = iris.data.features 
targets = iris.data.targets 
  
""" 
summary of the dataset
"""
print("Total number of record: ",len(features)) 
unique_names = set(targets.iloc[:, 0])
print("Number of unique flower types: ",len(unique_names) )
for name in unique_names:
    print(name)


# variable information 
#print(iris.variables) 

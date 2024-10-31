

def create_feature_type_dict(df):
   
    feature_types = {
        'numerical': {
            'continuous': ['Age', 'Fare'],  
            'discrete': ['SibSp', 'Parch']  
        },
        'categorical': {
            'nominal': ['Sex', 'Embarked'], 
            'ordinal': ['Pclass']  
        }
    }
    
    return feature_types
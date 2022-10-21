def stats(df):
    print("\t\t\tDatatypes")
    print("---------------------------------------------------------------------------------------------------------")
    print(df.dtypes, "\n\n")
    
    
    print("\t\t\tRows and Columns")
    print("---------------------------------------------------------------------------------------------------------")
    print("There are {} rows and {} columns in the dataset\n\n".format(df.shape[0], df.shape[1]))
    
    
    print("\t\t\tMissing Values")
    print("---------------------------------------------------------------------------------------------------------")
    print(df.isna().sum(), "\n\n")
    
    
    print("\t\t\tPercentage of Missing Values")
    print("---------------------------------------------------------------------------------------------------------")
    print(df.isna().sum()*100/df.shape[0], "\n\n")
    
    
    print("\t\t\tDuplicated rows")
    print("---------------------------------------------------------------------------------------------------------")
    print("This dataset has {} duplicated row \n\n".format(len(df[df.duplicated()])))
    
    
    print("\t\t\tNumber of Unique Values")
    print("---------------------------------------------------------------------------------------------------------")
    print(df.nunique(),'\n\n')
    
    
    
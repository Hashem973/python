import pandas as pd
students_data = pd.DataFrame({"Name" :["Alice","Bob","Charlie","David","Eva"],
                              "Age" :[20 , 22 , 19 , 21 , 20],
                              "Grade" :["A","B","A","C","B"],
                              "Marks" :[85 , 78 , 92 , 65 , 74]})
print(students_data.head(3))
print(students_data[["Name" , "Marks"]])
print(students_data[students_data["Grade"]=="A"])
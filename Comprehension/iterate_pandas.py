import pandas

student_dict = {
    "student" : ["Angela","James","Lily"],
    "score" : [56,76,98]
}

data = pandas.DataFrame(student_dict)
for(index, row) in data.iterrows():
    print(row.student)
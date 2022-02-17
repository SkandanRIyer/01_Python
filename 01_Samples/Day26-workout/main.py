student_dict = {
    "student": ["ramu", "ganga", "geetha"],
    "score": [56, 76, 98]
}
import pandas

student_data_frame = pandas.DataFrame(student_dict)
for (index, row) in student_data_frame.iterrows():
    print(row.student, row.score)
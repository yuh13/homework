
import pandas as pd
import numpy as np

csv_schools = "schools_complete.csv"
csv_students = "students_complete.csv"

schools_pd = pd.read_csv(csv_schools)
students_pd = pd.read_csv(csv_students)

#Totals
total_schools = schools_pd["School ID"].count()
total_students = students_pd["Student ID"].count()
total_budget = '${0:,.2f}'.format(schools_pd['budget'].sum())

#Average scores
avg_math = round(students_pd.math_score.mean(),3)
avg_reading = round(students_pd.reading_score.mean(),3)


#Passing score set to >= 70. Count of passing students
total_passing_math = students_pd[students_pd.math_score >= 70]['math_score'].count()
total_passing_reading = students_pd[students_pd.reading_score >= 70]['reading_score'].count()

#Convert to percent by total passing/total students
perc_math = round(total_passing_math/total_students*100,3)
perc_reading = round(total_passing_reading/total_students*100,3)
perc_passing = (perc_math + perc_reading)/2

#Generate first table with summary variables
District_Summary = pd.DataFrame({
                            "Total Schools": [total_schools],
                            "Total Students": [total_students],
                            "Total Budget": [total_budget],
                            "Avg Math Score": [avg_math],
                            "Avg Reading Score": [avg_reading],
                            "% Passing Math": [perc_math],
                            "% Passing Reading": [perc_reading],
                            "% Overall Passing": [perc_passing],

})

#Rearrange columns
District_Summary = District_Summary[["Total Schools", "Total Students", "Total Budget", 
                                     "Avg Math Score", "Avg Reading Score", 
                                     "% Passing Math", "% Passing Reading", "% Overall Passing"]]
District_Summary

#sort schools_pd and reset index to school name
schools_pd = schools_pd.rename(columns={'name': 'school'})
schools_sort = schools_pd.sort_values(['school']).set_index('school')
# .reset_index(inplace=False)

#Calculate budget per student by budget divided by size
per_budget = schools_sort['budget']/schools_sort['size']

#Group students by 'school' to find means
#ensure to merge in sorted alphabetical order by school
grouped_scores = students_pd.groupby(['school']).mean()
school_math = grouped_scores['math_score']
school_reading = grouped_scores['reading_score']

#Filter students_pd by scores that are passing. Passing defined as >= 70
students_passing_math = students_pd[students_pd.math_score >= 70]
students_passing_reading = students_pd[students_pd.reading_score >= 70]

#Count of students who pass math or reading by school
passing_math = students_passing_math.groupby(['school']).count()
passing_reading = students_passing_reading.groupby(['school']).count()

#Percent of students who passed divided by number of size of each school
perc_passing_math = round(passing_math['math_score']/schools_sort['size']*100,3)
perc_passing_reading = round(passing_reading['reading_score']/schools_sort['size']*100,3)
perc_passing_school = (perc_passing_math + perc_passing_reading)/2 

#Create school summary data frame and rename/reorganize columns
School_summary = pd.DataFrame({
                            "% Passing Math": perc_passing_math,
                            "% Passing Reading": perc_passing_reading,
                            "School Type": schools_sort['type'],
                            "Total Students": schools_sort['size'],
                            "Total School Budget": schools_sort['budget'],
                            "Per Student Budget": per_budget,
                            "Average Math Score": school_math,
                            "Average Reading Score": school_reading,
                            "% Passing Math": perc_passing_math,
                            "% Passing Reading": perc_passing_reading,
                            "Overall Passing Rate": perc_passing_school,
})
School_summary.reset_index(inplace=True)
School_summary = School_summary.rename(columns={'school': 'School Name'})
School_summary['Total School Budget'] = School_summary['Total School Budget'].map('${:,.2f}'.format)
School_summary['Per Student Budget'] = School_summary["Per Student Budget"].map('${:,.2f}'.format)

School_summary = School_summary[["School Name", "School Type", "Total Students", "Total School Budget", 
                                     "Per Student Budget", "Average Math Score", "Average Reading Score", 
                                     "% Passing Math", "% Passing Reading", "Overall Passing Rate"]]
School_summary.head()



#Sort by ascending Overall Passing Rate and only return top 5
Bottom_sort = School_summary.sort_values("Overall Passing Rate").reset_index().drop('index', axis=1)
Bottom_schools = Bottom_sort.iloc[:5]
Bottom_schools

#Sort by descending Overall Passing Rate and only return top 5
Top_sort = School_summary.sort_values("Overall Passing Rate", ascending=False).reset_index().drop('index', axis=1)
Top_schools = Top_sort.iloc[:5]
Top_schools

#get sum of scores per grade per school
by_grade = students_pd.groupby(['school','grade'])
total_by_grade = by_grade.sum()
#get count of students per grade per school
count_by_grade = by_grade["Student ID"].count()

#divide sum of scores by students per grade per school
reading_by_grade = pd.DataFrame(total_by_grade['reading_score']/count_by_grade)
math_by_grade = pd.DataFrame(total_by_grade['math_score']/count_by_grade)

#reset key IDs to create pivot of tables

Math_summary = math_by_grade.reset_index(inplace=False)
Math_summary = Math_summary.rename(columns={0:'Avg Math'})
Math_summary = Math_summary.pivot(index='school', columns ='grade', values='Avg Math')
Math_summary.head()


#reset key IDs to create pivot of tables
Reading_summary = reading_by_grade.reset_index(inplace=False).rename(columns={0:'Avg Reading'})
Reading_summary = Reading_summary.pivot(index='school', columns ='grade', values='Avg Reading')
Reading_summary.head()

#bins of 4 groups...find max and min of budget per student
max_budget = per_budget.max()
min_budget = per_budget.min()

#create bins encompassing 587 to 655 with error
bin_budget = [0, 604, 621, 638, 1000]
bin_names = ['< $603', '$604-620', '$621-637', '> $638']

#add budget bins to summary table
bin_budget_df = pd.DataFrame(per_budget)
budget_range = pd.cut(bin_budget_df[0], bin_budget, labels=bin_names).reset_index(drop=True)
School_summary['Spending Range (Per Student)'] = budget_range

#Group by bins
Spending_group = School_summary.groupby('Spending Range (Per Student)')

#Sum and divide by count to get average
Spending_group_totals = Spending_group.sum()
Spending_group_number = Spending_group.count()
Spending_summary = Spending_group_totals/Spending_group_number

#Generate final spending table
Spending_summary = Spending_summary[['Average Math Score', "Average Reading Score", 
                                     '% Passing Math', '% Passing Reading', 'Overall Passing Rate']]
Spending_summary.head()

#bin of 3 groups... find min and max for buckets for small, medium, large
max_size = School_summary['Total Students'].max()
min_size = School_summary['Total Students'].min()

#create bins from sizes [0-1899, 1900-3399, 3400 - 5000]
bin_size = [0, 1900, 3400, 5000]
bin_names = ['Small', 'Medium', 'Large']

#add size to summary table
bin_size_df = School_summary['Total Students']
size_range = pd.cut(bin_size_df, bin_size, labels=bin_names)
School_summary['School Size'] = size_range

#group by size
Size_group = School_summary.groupby('School Size')

#Sum and divide by count to get average
Size_group_totals = Size_group.sum()
Size_group_number = Size_group.count()
Size_summary = Size_group_totals/Size_group_number

#Generate final spending table
Size_summary = Size_summary[['Average Math Score', "Average Reading Score", 
                                     '% Passing Math', '% Passing Reading', 'Overall Passing Rate']]
Size_summary.head()

#Group by School Type
Type_group = School_summary.groupby('School Type')

#Sum and divide by count to get average
Type_group_totals = Type_group.sum()
Type_group_number = Type_group.count()
Type_summary = Type_group_totals/Type_group_number

#Generate final spending table
Type_summary = Type_summary[['Average Math Score', "Average Reading Score", 
                           '% Passing Math', '% Passing Reading', 'Overall Passing Rate']]
Type_summary.head()

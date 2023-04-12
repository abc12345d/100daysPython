import pandas

data = pandas.read_csv("weather_data.csv")

# two ways to get the average of temp
temp_list = data["temp"].to_list()
avg_temp1 = sum(temp_list) / len(temp_list)
avg_temp2 = data["temp"].mean()

# to get max of temp
max_temp = data['temp'].max()

# two ways to get data in columns
column1 = data.condition
column2 = data['condition']

# way to get data in rows with certain filter
row1 = data[data['day'] == 'Monday']
row_max_temp = data[data.temp == max_temp]

# create a dataframe from scratch
data_dict = {
    'students' : ['a','b','c'],
    'scores' : [1,2,3]
}
data_student_score = pandas.DataFrame(data_dict)
data_student_score.to_csv('data_student_score.csv',index=False)


# practice
squirrel_data = pandas.read_csv('2018_Squirrel_Data.csv')
squirrel_colour = squirrel_data['Primary Fur Color'].dropna()
squirrel_colour = squirrel_colour.groupby(squirrel_colour).count()[::-1]

labels = ['Fur Color','Count']
colors = ['grey','red','black']
squirrel_data_dict = {
    labels[0]: colors, 
    labels[1]: squirrel_colour.to_list()
}
df_color_count = pandas.DataFrame(squirrel_data_dict)
df_color_count.to_csv("squirrel_count.csv")











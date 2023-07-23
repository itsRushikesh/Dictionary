#list vs dictionary
# program

# daily_temp = [20,30,40,50,60,70,80]
# day = input("enter week day in short form")

# if day == 'sun':
#     dayname = 'sunday'
#     temp = daily_temp[0]
# elif day =='mon':
#     dayname = 'monday'
#     temp = daily_temp[1]
    
# elif day == 'tue':
#     dayname ='tuesday'
#     temp = daily_temp[2]
# elif day == 'wed':
#     dayname = 'wednesday'
#     temp = daily_temp[3]
# else:
#     print("wrong input")
    
    
# print("ther day is", dayname, "and temperature is", temp)


#---------------------------------------------------------------------------------------------------------
#same program using dictionary
# days = {'sun':20, 'mon':30, 'tue':40, 'wed': 40, 'thurs':50, "fri":60, 'sat':90}
# day_in = input("enter the day name")

# print("the day is", day_in, "temp is",days[day_in])


#--------------------------------------------------------------------------------
#creating dictionary using list
a = [1,2,3]
b = ["apple","dog",'cat']
my_dict = {}
for i in range(len(a)):
    my_dict[a[i]]= b[i]
    
print(my_dict) 
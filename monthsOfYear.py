#this program uses a func that takes 2 integers and returns 
startMonth = int(input("Start Month: "))
endMonth = int(input("End Month: "))

def months_of_year(startMonth,endMonth): 
    months = ["Jan", "Feb", "March", "April", "May", "June"]
    return months[startMonth], months[endMonth]

startMonth, endMonth = months_of_year(startMonth,endMonth)

print(f'Start Month: {startMonth}')
print(f'End Month: {endMonth}')

#this program uses a func and if else logic to print month from the listif found or not
month = input("Enter the Month: ")

def search(month):
    months = ['Jan', 'Feb', 'March', 'April', 'May', 'June', 'July', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

    if month in months:
        print(f'We found {month} in the months list. Search successful!')
    else:
        print(f'We could not find {month} in the months list.')

search(month)

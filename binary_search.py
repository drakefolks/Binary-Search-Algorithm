def binary_search(number_list, search_value):
    found = False
    low = 0
    middle = len(number_list) // 2 # '//' is the floor divison operator in python
    high = len(number_list) - 1

    while (high >= low):
        middle = (high + low) // 2 #finding middle based on current high and low

        if(number_list[middle] < search_value): 
            print('Middle value is smaller than search value, updating low to higher range')
            low = middle + 1

        elif(number_list[middle] > search_value):
            print('Middle value is larger than search value, updating high to lower range')
            high = middle - 1

        else: #successfully found value; returning found as True
            found = True
            return found
    
    return found

numbers = [1,2,3,4,5,6,7,8,9,10] #initializing list of numbers, assuming they are ordered in this case
search_input = ' '

while search_input == ' ': #run input validation loop as long as search_input does not get assigned a new value
    try:
        search_input = int(input('Please enter a number you would like to search for\n'))

    except:
        print('Enter a valid integer')


is_found = binary_search(numbers,search_input) #pass user input to linear_search function

if is_found == False:
    print('{num} not found'.format(num=search_input))

if is_found == True:
    print('{num} found'.format(num=search_input))



'''
NAME > Braden Shrum

FILE NAME > Dean's List & Honor Roll Calculator

DESCRIPTION > This app will allow the user to input the student's first and last names and the respective GPA and the program will calculate whether the student belongs
              on the Dean's List, the Honor Roll, both, or none.
'''

def getFirstName():
    '''Uses a while loop to grab the first name of the student and perform input validation'''
    firstName = input("Enter the student's first name or ZZZ to quit > ") #primer input

    while True: #Loop until a valid name is entered
        #perform input validation
        if firstName == "ZZZ":
            return "ZZZ"
        elif firstName.isalpha():
            break
        elif firstName.isdigit():
            print("The name should not contain digits\n")
        
        firstName = input("Enter the student's name or ZZZ to quit > ") # get input if a valid name is not entered
    
    return firstName

def getLastName(name):
    '''Uses a while loop to grab the last name of the student and perform input validation'''
    #if the user decides to quit, skip over the function
    if name == "ZZZ":
        return "ZZZ"

    lastName = input("Enter the student's last name or ZZZ to quit > ") #primer input

    while True: #Loop until a valid name is entered
        #perform input validation
        if lastName.isalpha():
            break
        elif lastName.isdigit():
            print("The name should not contain digits\n")
        
        lastName = input("Enter the student's name or ZZZ to quit > ") # get input if a valid name is not entered
    
    return lastName

def getGPA(firstName, lastName):
    '''Uses a while loop to grab the gpa of the student and perform input validation'''
    #if the user decides to quit, skip over the function
    if firstName == "ZZZ":
        return -1

    gpa = input(f"Enter {firstName} {lastName}'s GPA > ") #primer input

    while True: #loop until a valid gpa is entered
        #perform input validation using try/except blocks. This will check whether the input is a float, 
        #and will make sure that no invalid characters are involved
        try:
            gpa = float(gpa)
        except ValueError:
            print(f"You cannot have letters in {firstName} {lastName}'s GPA\n")
            gpa = input(f"Enter {firstName} {lastName}'s GPA > ")
            continue

        if gpa > 4.0: #check if the GPA entered is over 4.0
            print(f"{firstName} {lastName}'s GPA cannot be greater than 4.0")
            gpa = input(f"Enter {firstName} {lastName}'s GPA > ")
            continue
        break #if every check has passed, break and return GPA
    return gpa

def main():
    while True: #Loop until the user decides they want to stop inputting values
        #setup the variables
        finalReport = ""
        firstName = getFirstName()
        lastName = getLastName(firstName)
        gpa = getGPA(firstName, lastName)

        #If the user entered "ZZZ", then quit the program
        if firstName == "ZZZ":
            break

        if gpa > 3.25: #if the gpa is greater than 3.25, display the honor roll message
            finalReport += f"{firstName} {lastName} has a GPA of {gpa} and has made the honor roll"
        
            if gpa > 3.5: #If the gpa is greater than 3.5, concatenate the Dean's List message onto the honor roll message.
                finalReport += " and the Dean's List!\n"
            else: # otherwise, concatenate the exclamation mark onto the honor roll message to complete it
                finalReport += "!\n"
        else: # otherwise, set the finalReport variable to a message that tells the user that the student didn't make either of the titles
            finalReport = f"{firstName} {lastName} has not made the honor roll or the Dean's List"

        print(finalReport) #print whether or not the student has made the honor roll or Dean's List

if __name__ == '__main__':
    main()
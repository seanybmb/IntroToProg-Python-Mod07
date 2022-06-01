# ------------------------------------------------- #
# Title: Lab7-1 Exception Handling
# Description: A simple way of handling an error
# ChangeLog: SMBB, May 31, 2022, Created Script
# ------------------------------------------------- #

# IO Error - file does not exist
try:
    File=open('ZeroDatabase.txt', 'r')
except IOError:
    print ("Could not find the file, create it?")
else:
    data=File.read()
    print(data)
    File.close()

# ZeroDivisionError, ValueError
while True:
    user_input=input('Please enter a number other than zero, 1000 will be divided by this number:')
    try:
        y=float(user_input)
        s=1000/y
    except (ValueError):
        print ('....Really? Input needs to be a number!')
    except (ZeroDivisionError):
        print ('Try again, you cant divide by zero, you know better!')
    else:
        print ('The the answer is', s)
        break
    finally:
        print ('Done')
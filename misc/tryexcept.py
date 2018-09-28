# Exception handling in Python

'''
A modern way of handling potential errors in a program at runtime: TRY to execute some statement, and if an error occurs
within the TRY block, then RAISE an exception by jumping to the corresponding EXCEPT block, whose statements may provide a
remedy for the error. The EXCEPT block is skipped if no error occurs in the corresponding TRY block.
In order for the EXCEPT block to be accessed, the exception raised in the TRY block must match the exception named after
the EXCEPT keyword. After execution of the EXCEPT clause, execution continues after the TRY statement
'''

while True:
    try:
        x = int(raw_input("Please enter a number (0 to terminate): "))
        if x == 0:
            break
    except ValueError:
        print "Oops... that wasn't a number! Try again"

'''
In the above ValueError is an optional argument of EXCEPT which specifies that the 'anticipated' error in the TRY block
that we are covering our backs for is a ValueError type error (i.e. x is not of the expected type - e.g. a string cannot be
an argument of int()). To catch all errors in the TRY block, we could have simply used 'except:'. Other common types of error:
'''

#List indices out of range
data = [1.0/i for i in range(1,10)]
try:
    data[9]
except IndexError:
    print "index does not exist in this list!"

#Trying to use a variable that is not initialised:
try:
    nonexistent[3]
except NameError:
    print "does not exist!"

#Division by zero:
try:
    3.0/0
except ZeroDivisionError:
    print "Cannot divide by zero!"

#Applying operations invalid for the type
try:
    "a string"*3.14
except TypeError:
    print "You can't multiply a string by a float silly!"

#Trying to open a file that doesn't exist
#(Also note you can have multiple exceptions as a parenthesized tuple: 'except (RunTimeError, SyntaxError):'
try:
    f = open('nonexistent.txt')
except IOError as e: # More general: 'except Exception as e:'
    print "you tried to open a nonexistent file!"
    print(e.args[0])
else:
    print "haha the file really does exist!"
    f.close()
finally:
    print "Goodbye, world!"
'''In this last example, note additional features:
-a TRY-EXCEPT block can have an optional ELSE block that is executed if no exception is raised in the TRY block
-the exception info can be used with an AS target...
-...this allows info to be gathered on the exception (e.g. e.args[0])
-a TRY-EXCEPT block can have an optional FINALLY block that is always executed before leaving the TRY statement,
whether an exception has occurred or not. When an exception has occurred in the TRY clause and has not been handled in the
EXCEPT clause (or it has occured in an EXCEPT or ELSE clause). The FINALLY clause is also executed 'on the way out' when any
other clause of the TRY statement is left via a break, continue or return statement.

The RAISE statement allows the programmer to force a specified exception to occur. For example, signal a user-generated
interruption by raising the KeyboardInterrupt exception:
'''

try:
    print "I am going to raise a keyboard interruption..."
    raise KeyboardInterrupt
except:
    print "I told you"

'''
If an exception occurs which does not match the exception named in the except clause, then it is passed on to outer TRY
statements; if no handler is found, it is an 'unhandled exception' and execution stops.
A TRY statement can have more than one except clause, to specify handlers for different exceptions. If you want an error
to be ignored, use the PASS statement ('null operation', used when a statement is required syntactically but you do not
want any commands to execute
'''

try:
    raise KeyboardInterrupt
    raise RuntimeError
except KeyboardInterrupt:
    print "Ignoring keyboardinterrupt..."
    pass
except RuntimeError:
    print "Not ignoring runtimeerror..." # This statement never gets executed because the PASS statement exits the TRY-EXCEPT block

'''
When an exception occurs, it may have an associated value, known as the exception's argument (we have seen this passed with
the AS target). Instead of specifying a variable after the EXCEPT keyword, one may instantiate an exception first before
raising it and then we can add any attributes as desired. The exception variable is bound to an exception instance with the
arguments stored in instance.args
'''

try:
    raise Exception('spam', 'eggs')
except Exception as inst:
    print type(inst) # the exception instance
    print inst.args # arguments stored in .args

'''
We have seen that the RAISE statement is used to force a specified exception to occur. The sole argument to RAISE indicates the
exception to be raised. This must either be an exception instance or an exception class.
Using the RAISE statement within an EXCEPT block re-raises the exception. This can be used if you need to determine whether an
exception was raised in the TRY block, but you do not wish to handle the exception
'''

try:
    raise NameError('Hi there')
except NameError:
    print "This will terminate the program :("
    raise

#Basic Functions:
# def my_function():
#   Do This
#   Do that
#   And now this too

# Functions with Inputs:

# def my_function(something):
#   Do this with something
#   Then this
#   And then this

# Functions with Outputs:

# def my_function():
#   result = 3 * 2
#   return result

# The result of this will mean that if you say:
# output = my_function()
# The result of the calculation happening in the function becomes the value of result.

#Functions with Outputs Tries:

# def format_name(f_name, l_name):
#   formated_f_name = f_name.title()
#   formated_l_name = l_name.title()
#   return f"{formated_f_name} {formated_l_name}"
#   ####THE part after the 'return' is what gets stored in the variable.

# formated_string = format_name("valerie", "yAManaka")
# print(formated_string)


##MULTIPLE RETURNS

def format_name(f_name, l_name):
  if f_name == "" or l_name == "":
    return "You didn't provide valid inputs." ##This basicaly escapes the function, stops it

  formated_f_name = f_name.title()
  formated_l_name = l_name.title()
  return f"{formated_f_name} {formated_l_name}"
  
print(format_name(input("What is your first name? "), input("What is your last name? ")))
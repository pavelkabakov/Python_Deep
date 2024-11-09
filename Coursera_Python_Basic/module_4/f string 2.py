s = "I saw the movie, Mary Poppins Returns, and I thought it was great."

# all the expressions
r_count = s.count("r")
print(r_count)
all_case_r_count = s.lower().count("r")
r_precentage = all_case_r_count/len(s) * 100

# use mostly variables inside f-strings or format()
first_str = f"The number of r characters: {r_count}."
second_str = "The percentage of r characters (upper or lower case): {:.2f}%.".format(r_precentage)

# display
print( first_str + " " + second_str)
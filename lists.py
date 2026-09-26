#Exercise 15. Find the Longest String in a List

words = ["PHP", "Exercises", "Backend", "Python"]

# The elegant way: find the max based on length
longest = max(words, key=len)
#Exercise 16. Turn Every Item of a List into its Square (List Comprehension)

print(f"Longest word: {longest}")

numbers = [1, 2, 3, 4, 5]

# The shorthand way to create a new list
squared_numbers = [x * x for x in numbers]

print(f"Squared List: {squared_numbers}")
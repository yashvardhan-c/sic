# Example usage:
#strings = ["banana", "Apple", "cherry", "date", "apricot"]
#sorted_strings = insertion_sort(strings)
#print("Sorted strings (case insensitive):", sorted_strings)
import insertion_sort_strings
import string
array = input("Enter the elements to be separated by spaces(case insensitive): ").split()
sorted_array=insertion_sort_strings.insertion_sort(array)
print("Sorted strings ", sorted_array)

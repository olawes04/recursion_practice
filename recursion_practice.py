import time

#Converts a positive number to a binary represented as a list of 0s and 1s.
#using the algorithm of divide by 2 and put the remainder in the small column then start again with the quotient as input
def pos_dec_to_binary(decimal,bit_list):
    if decimal<=1:
        bit_list.append(decimal%2)
        return list(reversed(bit_list))
    else:
        bit_list.append(decimal%2)
        return pos_dec_to_binary(decimal//2,bit_list)
    
#why does this not work? Fix it!
def countdown(number):
    print(number)
    time.sleep(1)
    countdown(number-1)


#try to complete this
def fibonacci(n):
    #base case
    if n == 0:
        return 0
    elif n == 1:
        return 1
    #recursive case: the fibonacci number is the sum of the previous 2

#triangular numbers
def triangular(n):
    #base case
    #recursive case
    pass

#try to complete this
def factorial(input_number):
    #base case
    
    #recursive case
    pass

def is_palendromic(string):
    pass

#try to complete a recursive linear search, returning the index of the item, or -1
def linear_search_recursive(items, start_index, end_index, search_item):
    #base cases
    #recursive case:

    pass


def binary_search_recursive(items, start_index, end_index, search_item):
  """ a recursive binary search, returning the index of the item, or -1 if not in list. 
  The start index should be 0 and the end index should be 1 less than the length of the list."""
  # base case 1: item not in list
  # TODO use start_index and end_index to find out if the sublist is of size 0 or less and return appropriate int
  #if ______:
  #  return _____
  # TODO work out middle index of the sublist
  # middle_index = 
  # TODO from that, set current item
  #current_item = 
  # TODO base case 2: find out if current item is the search item and return the appropriate index
  # recursive cases: do a BS on a subset of the list by tweaking appropriate start or end index
  #if current_item < search_item:
  #  return binary_search_recursive(items, ????????????, ????????????, search_item)
  #else:
  #  return binary_search_recursive(items, ????????????, ????????????, search_item)
  pass

"""EXTENSION: Euclid's algorithm. The greatest common divisor (gcd) of two positive integers is the largest integer
that divides evenly into both of them. For example, the gcd(102, 68) = 34.
We can efficiently compute the gcd using the following property, which holds for positive integers p and q:

If p > q, the gcd of p and q is the same as the gcd of q and p % q."""

#tests
#print(pos_dec_to_binary(1234,[]))
##or, neater (using a generator expression (outside scope of A-level CS))
#print("".join(str(i) for i in pos_dec_to_binary(1234,[])))
#
#print (factorial(4))
#countdown(10)
#print(binary_search_recursive([1,2,3,4,54,56,58],0,6,1))

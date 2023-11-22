import time
items=[1,2,3,4,54,56,58]
start_index=0
end_index=6
search_item=1
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
    if number<0:
        pass
    else:
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
    else:
        return(fibonacci(n-1)+fibonacci(n-2))
    #recursive case: the fibonacci number is the sum of the previous 2

#triangular numbers
def triangular(n):
    if n==1:
        return 1
    else:
        return(n+triangular(n-1))
    print (triangular(10))

#try to complete this
def factorial(num, count_num):
    for i in range (num-1):
        count_num=count_num*(num-1)
        num=num-1
        print(count_num)
    pass


def is_palendromic(string):
  def reverse_recursion(string):
    length=len(string)
    if length == 0:
      if string==normal_string:
        return("Yes",string,"is palendromic")
      else:
        return("No",string,"is not palendromic")
    else:
      normal_string=string
      length=length-1
      return reverse_recursion(string[1:]) + string[0]
      

#try to complete a recursive linear search, returning the index of the item, or -1
def linear_search_recursive(items, start_index, end_index, search_item):
    # Base cases
    if start_index > end_index:
        # Item not found
        return -1

    if items[start_index] == search_item:
        # Item found at the current index
        return start_index

    # Recursive case
    return linear_search_recursive(items, start_index + 1, end_index, search_item)

# Example usage


result = linear_search_recursive(items, start_index, end_index, search_item)



def binary_search_recursive(items, start_index, end_index, search_item):
    if start_index > end_index:
        return -1
  # TODO use start_index and end_index to find out if the sublist is of size 0 or less and return appropriate int
    if start_index>=end_index :
        return ("Index is too small")

  # TODO work out middle index of the sublist
    middle_index = (start_index + end_index)
  # TODO from that, set current item
    current_item = items[middle_index]
  # TODO base case 2: find out if current item is the search item and return the appropriate index
    if current_item==search_item:
        return middle_index
  # recursive cases: do a BS on a subset of the list by tweaking appropriate start or end index
    if current_item < search_item:
        return binary_search_recursive(items, middle_index+1, end_index, search_item)
    else:
        return binary_search_recursive(items, middle_index-1, end_index, search_item)


"""EXTENSION: Euclid's algorithm. The greatest common divisor (gcd) of two positive integers is the largest integer
that divides evenly into both of them. For example, the gcd(102, 68) = 34.
We can efficiently compute the gcd using the following property, which holds for positive integers p and q:

If p > q, the gcd of p and q is the same as the gcd of q and p % q."""

#tests
#print(pos_dec_to_binary(1234,[]))
##or, neater (using a generator expression (outside scope of A-level CS))
#print("".join(str(i) for i in pos_dec_to_binary(1234,[])))
#print(fibonacci(10))
#print (factorial(4, 4))
#countdown(10)
print(binary_search_recursive([1,2,3,4,54,56,58],0,6,1))
#Linear Search:
"""items = [9, 4, 7, 2, 1, 8, 5, 6, 3]
start_index = 0
end_index = len(items) - 1
search_item = 5
result = linear_search_recursive(items, start_index, end_index, search_item)
if result != -1:
    print(f"Item {search_item} found at index {result}")
else:
    print(f"Item {search_item} not found in the list.")"""


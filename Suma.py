def print_subset_sum(i, sol, psum, elements, x):
    # Base case
    if psum == x:
        print_subset_binary(sol, elements)
    elif i < len(elements):
        # Generate candidates
        for k in range(0, 2):

            # Check if recursion tree can be pruned
            if psum + k * elements[i] <= x:

                # Expand partial solution
                sol[i] = k

                # Update sum related to partial solution
                psum = psum + k * elements[i]

                # Try to expand partial solution
                print_subset_sum(i + 1, sol, psum, elements, x)

                # not necessary:
                #psum = psum - k*elements[i]

        # Make sure a 0 indicates the absence of an element
        sol[i] = 0


def print_subset_sum_wrapper(elements, x):
    sol = [0] * (len(elements))
    print_subset_sum(0, sol, 0, elements, x)


# Test
def print_subset_binary(sol, elements):
    no_elements = True
    print('{', end='')
    for i in range(0, len(sol)):
        if sol[i] == 1:
            if no_elements:
                print(elements[i], sep='', end='')
                no_elements = False
            else:
                print(', ', elements[i], sep='', end='')
    print('}')


print_subset_sum_wrapper([2, 6, 3, 5], 8)
print()
print_subset_sum_wrapper([1, 2, 3, 5, 6, 7, 9], 13)

-------

# Returns true if the
# there is a subarray
# of arr[] with sum
# equal to 'sum' 
# otherwise returns
# false. Also, prints
# the result 
def subArraySum(arr, n, sum_):
      
    # Pick a starting 
    # point
    for i in range(n):
        curr_sum = arr[i]
      
        # try all subarrays
        # starting with 'i'
        j = i + 1
        while j <= n:
          
            if curr_sum == sum_:
                print ("Sum found between")
                print("indexes % d and % d"%( i, j-1))
                  
                return 1
                  
            if curr_sum > sum_ or j == n:
                break
              
            curr_sum = curr_sum + arr[j]
            j += 1
  
    print ("No subarray found")
    return 0
  
# Driver program 
arr = [15, 2, 4, 8, 9, 5, 10, 23]
n = len(arr)
sum_ = 23
  
subArraySum(arr, n, sum_)

------

# An efficient program 
# to print subarray
# with sum as given sum 
  
# Returns true if the 
# there is a subarray 
# of arr[] with sum
# equal to 'sum' 
# otherwise returns 
# false. Also, prints 
# the result.
def subArraySum(arr, n, sum_):
      
    # Initialize curr_sum as
    # value of first element
    # and starting point as 0 
    curr_sum = arr[0]
    start = 0
  
    # Add elements one by 
    # one to curr_sum and 
    # if the curr_sum exceeds 
    # the sum, then remove 
    # starting element 
    i = 1
    while i <= n:
          
        # If curr_sum exceeds
        # the sum, then remove
        # the starting elements
        while curr_sum > sum_ and start < i-1:
          
            curr_sum = curr_sum - arr[start]
            start += 1
              
        # If curr_sum becomes
        # equal to sum, then
        # return true
        if curr_sum == sum_:
            print ("Sum found between indexes")
            print ("% d and % d"%(start, i-1))
            return 1
  
        # Add this element 
        # to curr_sum
        if i < n:
            curr_sum = curr_sum + arr[i]
        i += 1
  
    # If we reach here, 
    # then no subarray
    print ("No subarray found")
    return 0
  
# Driver program
arr = [15, 2, 4, 8, 9, 5, 10, 23]
n = len(arr)
sum_ = 23
  
subArraySum(arr, n, sum_)
# 2.1 Reading numbers
'''
“Suppose you’re building an app to keep track of your finances.Every 
day, you write down everything you spent money on. At the end of the 
month, you review your expenses and sum up how much you spent. So you 
have lots of inserts and a few reads. Should you use an array or a list?”

Answer: I would use a Linked list because the insertion for a linked list is constant time O(1) and reading is O(n)
'''

# 2.2 Order Queue
'''
Would you use an array or a linked list to implement this queue? 
(Hint: Linked lists are good for inserts/deletes, and arrays are 
good for random access. Which one are you going to be doing here?)

Answer: Linked list is best for inserting and deleteing nodes because 
the insert/delete being constant time
'''

# 2.3 Facebook App
'''
Let’s run a thought experiment. Suppose Facebook keeps a list of 
usernames. When someone tries to log in to Facebook, a search is done 
for their username. If their name is in the list of usernames, they can 
log in. People log in to Facebook pretty often, so there are a lot of 
searches through this list of usernames. Suppose Facebook uses binary 
search to search the list. Binary search needs random access—you need 
to be able to get to the middle of the list of usernames instantly. 
Knowing this, would you implement the list as an array or a linked list?

Answer: Arrays are the best data structure for this use case becasue 
we have a bunch of random searches and the list has to be sorted. Their
are needed to be randomly accessed based on the username being included 
in a list.
'''

# 2.4 Facebook Signup
'''
People sign up for Facebook pretty often, too. Suppose you decided 
to use an array to store the list of users. What are the downsides of 
an array for inserts? In particular, suppose you’re using binary search 
to search for logins. What happens when you add new users to an array?

Answer: When inserting new users into an array that keeps track of users
that are logged in. Each user in the loggin array has to shift over one 
element to keep the sort state of the array.

insertion works on a O(n) which is really slow given that it has to 
read over all the elements and run a condtion for each element to 
determine where to place the newly inserted element.
'''

# 2.5 Hybrid Facebook Data Structure
'''
In reality, Facebook uses neither an array nor a linked list to store 
user information. Let’s consider a hybrid data structure: an array of 
linked lists. You have an array with 26 slots. Each slot points to a 
linked list. For example, the first slot in the array points to a linked 
list containing all the usernames starting with A. The second slot 
points to a linked list containing all the usernames starting with B, 
and so on.

Suppose Adit B signs up for Facebook, and you want to add them to the 
list. You go to slot 1 in the array, go to the linked list for slot 1, 
and add Adit B at the end. Now, suppose you want to search for Zakhir 
H. You go to slot 26, which points to a linked list of all the Z names. 
Then you search through that list to find Zakhir H.

Answer: for insertions and for searching the data structure used is slower 
because it uses a combination of constant time and linear time for search
and insertion.
'''

# Selection Sort Smallest Number
array = [20, 2, 748, 46, 1, 326, 78, 4, 57, 84]

def find_smallest(arr):
    smallest_value = arr[0]
    smallest_index = 0

    for i in range(1, len(arr)):
        if smallest_value > arr[i]:
            smallest_value = arr[i]
            smallest_index = i

    return smallest_index

def selection_sort(arr):
    new_arr = []
    copied_arr = list(arr)

    for i in range(len(copied_arr)):
        smallest = find_smallest(copied_arr)
        new_arr.append(copied_arr.pop(smallest))

    return new_arr

result = selection_sort(array)
print(result)
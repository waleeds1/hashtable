## Hash Table
Hash Table is a data structure that stores data against a key in an
associative manner. It uses a Hash function to generate an index based on the key where data can be inserted or searched and deleted from. It offers θ(1) average case complexity for insertion, deletion and searching.

##  Functions
Hash table has the following functions

 - ### Private Functions
	Operations that the table's functionality is based upon.
	 - #### Hash Function:
		 Hash function gets key, value, and function as arguments and returns an index using the key. The function argument can be either search or insert and performs operation based on the required function. The hash function is implemented using division method and uses double hashing for collision handling.
	- #### LF:
		It calculates the load factor which is the ratio of the total elements stored in the list to the size of the list.
	- #### Rehash:
		It increases the size of the array when the load factor is greater than 0.75, to maintain efficiency. When the load factor reaches 0.1 or lower, it reduces the size of the array to optimize space usage. After resizing, the elements from the older array are inserted into the resized array by re applying the hash function.
 - ### User accessible functions:
	Functions the helps the user use the hash table
	- #### Insert:
		It takes a key and data to be stored against it, as arguments and inserts them in the table at an index generated by the hash function.
	- #### Search:
		It takes a key as an argument and returns the data stored against it.
	- #### Delete:
		It takes a key as an argument and removes the key and data against it from the table. The function returns they key and data deleted in the form of a tuple.
	- #### PrintTable:
		This function prints all the keys and data in the table
	- #### PrintArray:
		It prints the array where used by the hash table which contains all the elements. This helps to inspect the indexes the data is stored and also to check for rehashing by inspecting the size of the array.
	
##  How To Use:
 - Create a file in the folder where the HashTable.py is or place the HashTable.py in the folder in which the file that will use the hash table is.
 - Import hash table in that file. 
 `import HashTable`
 - Create object of the hashtable by using the code
	  `ob1=HashTable.HashTable(m)`
	  where m is the initial size of the table. The initial size **should not be less than 8**

 - To insert data into the table call the **Insert** function through the object giving a key as the first argument and data as the second argument.
 `ob1.Insert(key,data)`
 - To search for data stored against a key, call the **Search** function through the object, giving the key as the argument. If the key is not found it returns *False*.
 `ob1.Search(key)`
 - To delete an element , call the **Delete** function through the object, giving the key as the argument. If the key is not found it returns *False*.
 `ob1.Delete(key)`
 - Call the **PrintTable** function to print all the elements stored in the table.
 `ob1.PrintTable`
 - Call the **PrintArray** function to print the array used by the hash table where all the elements are stored. There is *None* at indexes where no element is stored.
 `ob1.PrintArray`
## Examples:

 - marks.py uses the hashtable to store quiz marks against roll numbers
 - openaddressing.py shows open addressing implemented.
 - rehashing.py demonstrates the rehashing being.

	

##  Features:

 - The keys can be numeric and even non numeric such as strings and symbols.
 - When the keys are numeric and smaller than the size of the table, **open addressing** is implemented automatically where the data is stored at the index of the same value as the key.
 - The table is resized and rehashed automatically when needed, it maintains efficiency when more data is being stored and also maintains space when more data has been deleted.

## Team Members:
 

 - Waleed Muhammad Sohail (18B-123-SE-A) (Team Lead)
 - Ahmad Zaman Qureshi (18B-045-SE-A)
 - Shazaib Awaan (18B-134-SE-A)

from LinkedList import LinkedList

class HashTable:

  def __init__(self, size):
    self.size = size
    self.arr = self.create_arr(size)


  # The create_arr method.
  # Each element of the hash table (arr) is a linked list.
  # This method creates an array (list) of a given size and populates each of its elements with a LinkedList object.
  def create_arr(self, size):
    
    lst = []

    for i in range(size):
      ll = LinkedList()
      lst.append(ll)
    
    return lst


  # Creates hash function.
  def hash_func(self, key):
    return len(key) % self.size


  # Insert method.
  # Inserts a key value pair into the hash table, where the key is the word and the value is a counter for the number of times the word appeared.
  def insert(self, key, value):

    new_data = (key, value)
    arr_index = self.hash_func(key)
    ll = self.arr[arr_index]

    # If not found, append
    # print("-------find(key)---------",ll.find(key))
    
    # for ll in self.arr:
    #   ll.print_nodes()

    has_key = False    
    p = ll.head

    while p is not None:
      print(p.data[0])
      if p.data[0] == key:
        has_key = True
      p = p.next
    
    if has_key:
      ll.update(key, value)
    else:
      print(f"{key} was not found")
      ll.append(new_data)



  # Prints key values 
  # For example: 
  # Node 1: ('be', 1)
  # Node 2: ('by', 1)
  # Node 3: ('on', 2)
  # Node 4: ('to', 2)
  # Node 5: ('nationwide', 1)
  # Node 6: ('we', 2)
  # Node 7: ('of', 3)
  # Node 8: ('in', 2)
  def print_key_values(self):
    
    for ll in self.arr:
      ll.print_nodes()



from Deque import Deque

class Array_Deque(Deque):

	def __init__(self):
		# capacity starts at 1; we will grow on demand.
		# TODO replace pass with any additional initializations you need.
		self.__capacity = 1
		self.__contents = [None] * self.__capacity	
		self.__size = 0
		self.__front_idx = 0
		self.__back_idx = 0
	def __str__(self):
		# TODO replace pass with an implementation that returns a string of
		# exactly the same format as the __str__ method in the Linked_List_Deque.
		if self.__size == 0:
			return ('[ ]')
		
		result = '['
		result = result + ' ' + str(self.__contents[self.__front_idx])
		for i in range(self.__size - 1):
			result = result + ', ' +  str(self.__contents[(self.__front_idx + i + 1) % self.__capacity])
		result += " ]"
		
		return result
	def __len__(self):
		# TODO replace pass with an implementation that returns the number of
		# items in the deque. This method must run in constant time.
		return(self.__size)	
	def __grow(self):
		# TODO replace pass with an implementation that doubles the capacity
		# and positions existing items in the deque starting in cell 0 (why is
		# necessary?)
		temp_arr = [None] * 2 * self.__capacity
		for i in range(self.__capacity):
			temp_arr[i] = self.__contents[(self.__front_idx + i) % self.__capacity]
		self.__contents = temp_arr
		self.__front_idx = 0
		self.__back_idx = self.__capacity - 1
		self.__capacity = self.__capacity * 2
	def push_front(self, val):
		# TODO replace pass with your implementation, growing the array before
		# pushing if necessary.
		if self.__capacity == self.__size:
			self.__grow()
		self.__front_idx = (self.__front_idx - 1)% self.__capacity
		self.__contents[self.__front_idx] = val
		self.__size += 1
	def pop_front(self):
		# TODO replace pass with your implementation. Do not reduce the capacity.
		to_return = self.__contents[self.__front_idx]
		self.__contents[self.__front_idx] = None
		self.__front_idx = (self.__front_idx + 1) % self.__capacity
		self.__size -= 1
		return to_return
	def peek_front(self):
		# TODO replace pass with your implementation.
		return(self.__contents[self.__front_idx])
	def push_back(self, val):
		# TODO replace pass with your implementation, growing the array before
		# pushing if necessary.
		if self.__capacity == self.__size:
			self.__grow()
		self.__back_idx = (self.__back_idx + 1)% self.__capacity
		self.__contents[self.__back_idx] = val
		self.__size += 1
	def pop_back(self):
		# TODO replace pass with your implementation. Do not reduce the capacity.
		to_return = self.__contents[self.__back_idx]
		self.__contents[self.__back_idx] = None
		self.__back_idx = (self.__back_idx - 1) % self.__capacity
		self.__size -= 1
		return to_return
	def peek_back(self):
	# TODO replace pass with your implementation.
		return(self.__contents[self.__back_idx])
# No main section is necessary. Unit tests take its place.
#if __name__ == '__main__':
	#pass
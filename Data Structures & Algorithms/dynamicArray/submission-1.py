class DynamicArray:
    
    def __init__(self, capacity: int):
        # Store capacity just incase it changes
        self.capacity = capacity
        # Set initial size of the array length to 0
        self.length = 0
        # Initilize Array
        self.array = [0] * self.capacity

    def get(self, i: int) -> int:
        # Assuming every index would be valid
        return self.array[i]


    def set(self, i: int, n: int) -> None:
        # Assuming all values are valid
        self.array[i] = n


    def pushback(self, n: int) -> None:
        # Handle over flow errors
        if self.length == self.capacity:
            # Double the array
            self.resize()
        
        # Our array should grow as numbers are inserted
        self.array[self.length] = n
        self.length += 1


    def popback(self) -> int:
        # Arrays always start at 0
        self.length -= 1
        return self.array[self.length]
 
    # Double the size of the array
    def resize(self) -> None:
        # Declare and double the capacity
        self.capacity = 2 * self.capacity
        # Declare a new array for simplicty 
        new_Array = [0] * self.capacity

        # Copy all values to new array
        for i in range (self.length):
            new_Array[i] = self.array[i]
        self.array = new_Array


    def getSize(self) -> int:
        # Just recall variables declared
        return self.length
    
    def getCapacity(self) -> int:
        # Just recall variables declared
        return self.capacity

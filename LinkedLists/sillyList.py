
'''
OK, so here's silly thing I made for no reason other than sheer curiosity. Could a 
python dict be used as a very rudimentary linked list like creature. Answer: yes it can.
Course it's completely useless tbh. Since a dict is a collection of key/value pairs,
I decided to make the value of each entry be the key of the next entry. Basically 
forming a totally pointless (pun intended lol) singly linked list. Since we aren't
storing anything but simple values, this script serves no purpose other than 
maybe introducing a new programmer to the basic idea of a linked list. Instead 
of a pointer to the memory address of the next entry (usually a struct in C at least),
we use the value of the key/value pair. This may be a simple way to teach someone the
general structure of a linked list. Theoretically, we could use class objects in our
dict and actually make a real linked list with this that could store useful data,
I may revisit that idea in the future. 

The script gives simple options for navigating the list to maybe help 
a new programmer to visualize what's happening.

We can add and remove entries. We can also view either the whole list, or a 
single entry with the option to move to the next entry until the end of the list.

'''



class LinkedList:
    def __init__(self, dictionary):
        self.dictionary = dictionary
        
        
    ## Add entry to end of list
    ## Removes end of list "None" value from current last entry and 
    ##      replaces with value entered. Then adds a key/value pair with new
    ##      "None" value to designate the new end of the list
    ## In case of repeats, appends counter to value. Kind of like when
    ##      files in a directory have the same name
    def add_entry(self, value):
        
        # Call repeats method to append number to end of entry if a duplicate
        if value in self.dictionary:
            value = self.repeats(value,value)
        
        ## Find last entry (Designated by 'None' value)
        for k, v in self.dictionary.items():
            if v == None:
                self.dictionary[k] = value
        self.dictionary[value] = None
        
        
    ## If value is a repeat, recursively run until we find a counter that is
    ##  not a repeat to append to the value
    def repeats(self,value,altered_value,counter=1):
        altered_value = f'{value}({counter})'
        if altered_value in self.dictionary:
            altered_value = self.repeats(value,altered_value,counter+1)
        return altered_value
        
    
    
    ## Delete an entry. This is a bit different than an actual linked list
    ##      because since we arent using pointers, we cant just change pointer 
    ##      values. We also have to delete the entry itself. But pretty close.
    ## We first find the entry before the target and redefine its value to be
    ##      the key for the entry after the target.
    ## Then we just delete the target entry.
    def delete_entry(self, value):
        if value in self.dictionary:
            if len(self.dictionary) <= 1:
                self.dictionary = {}
            else:
                next_entry = self.dictionary[value]
                
                for k, v in self.dictionary.items():
                    if v == value:
                        last_entry = k
                        
                self.dictionary[last_entry] = next_entry                    
                del self.dictionary[value]
        else:
            print(f'{value} not in list.')
        
        
        
        
        
def main():
    print('\nWelcome to a silly "linked list" script that has no utilitarian purpose, but is undoubtedly fun.')        
     
    ## Create empty list       
    Llist = LinkedList({})       
         
    ## Ask for user input and act accordingly
    while 1:
        user_input = input('What would you like to do? (A)dd, (R)emove, (V)iew (Q)uit:  ')    
        
        if user_input == 'A' or user_input == 'a':
            input_value = input('Enter a value to input:  ')
            Llist.add_entry(input_value)
            
        elif user_input == 'R' or user_input == 'r':
            input_value = input('Enter a value to remove:  ') 
            Llist.delete_entry(input_value)
            
        elif user_input == 'V' or user_input == 'v':
            view_choice = input('(W)hole list or (S)ingle entry: ')
            if view_choice == 'W' or view_choice == 'w':
                for k in Llist.dictionary.keys():
                    print('\n' + k)
            
            elif view_choice == 'S' or view_choice == 's':
                view_entry = input('Enter entry to view:  ')
                while 1:
                    if view_entry in Llist.dictionary:
                        print(f'\n{view_entry} points to {Llist.dictionary[view_entry]}')
                    else:
                        print(f'\n{view_entry} not in list. ')
                        break
                
                    view_next = input('(N)ext entry or (B)ack to main menu:  ')
                    if view_next == 'N' or view_next == 'n':
                        view_entry = Llist.dictionary[view_entry]
                        if view_entry == None:
                            print('\nEnd of List. ')
                            break
                    elif view_next == 'B' or view_next == 'b':
                        break
                    
                    else:
                        print('\nCommand not recognized.')
                        break
            
            
            else:
                print('Command not recognized')
            
            
            
            
            
        elif user_input == 'Q' or user_input == 'q':
            break
        
        else:
            print('Command not recognized. ')
        
        
        



if __name__ == '__main__':
    main()

























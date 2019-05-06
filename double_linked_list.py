def transformString(input_string):
    output_string = input_string.lower()
    return str(output_string)


class Node:

    def __init__(self, name, number,id=None):
        self.id = transformString(id)
        self.name = name
        self.number = number
        self.link_to_next_node = None
        self.link_to_previous_node = None

    def update(self,name,number):
        self.name = name
        self.number = number
    
    def compare(self, other):
        value = False
        if(self.name.lower() == other.name.lower()  and self.number == other.number ):
            value = True
        return value

class DoubleLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0
        self.new_node_id = 0

    def add_contact(self,name,number,id):
        new_node = Node(name,number,id)
        if(self.head == None):
            self.head = new_node
            return True
        list_iterator_pointer = self.head
        if(list_iterator_pointer.link_to_previous_node == None and new_node.name < list_iterator_pointer.name):
            new_node.link_to_next_node = list_iterator_pointer
            list_iterator_pointer.link_to_previous_node = new_node
            self.head = new_node
            return True
        if(list_iterator_pointer.link_to_previous_node == None and list_iterator_pointer.link_to_next_node == None and new_node.name > list_iterator_pointer.name):
            list_iterator_pointer.link_to_next_node = new_node
            new_node.link_to_previous_node = list_iterator_pointer
            return True
        while(list_iterator_pointer.link_to_next_node  != None):
            if(list_iterator_pointer.link_to_previous_node == None and new_node.name < list_iterator_pointer.link_to_next_node.name):
                new_node.link_to_next_node = list_iterator_pointer.link_to_next_node
                list_iterator_pointer.link_to_next_node.link_to_previous_node = new_node
                new_node.link_to_previous_node = list_iterator_pointer
                list_iterator_pointer.link_to_next_node = new_node
                return True
            if(new_node.name < list_iterator_pointer.name and new_node.name > list_iterator_pointer.link_to_previous_node.name):
                new_node.link_to_next_node = list_iterator_pointer
                list_iterator_pointer.link_to_previous_node.link_to_next_node = new_node
                new_node.link_to_previous_node = list_iterator_pointer.link_to_previous_node
                list_iterator_pointer.link_to_previous_node = new_node
                return True
            list_iterator_pointer = list_iterator_pointer.link_to_next_node
        if(list_iterator_pointer.link_to_next_node == None and list_iterator_pointer.compare(new_node)):
            print("Contact already in phonebook")
            return False
        list_iterator_pointer.link_to_next_node = new_node
        new_node.link_to_previous_node = list_iterator_pointer
        return True

    def delete_by_name(self,string):
        list_iterator_pointer = self.head       
        string = transformString(string)
        while(list_iterator_pointer.name != string and list_iterator_pointer.link_to_next_node != None):
            list_iterator_pointer = list_iterator_pointer.link_to_next_node
        if(list_iterator_pointer == None):
            return False
        if(list_iterator_pointer.link_to_previous_node == None and list_iterator_pointer.link_to_next_node !=None):
            self.head = list_iterator_pointer.link_to_next_node
            list_iterator_pointer = None
            return True
        if(list_iterator_pointer.link_to_previous_node == None and list_iterator_pointer.link_to_next_node == None):
            self.head = None
            list_iterator_pointer = None
            return True
        list_iterator_pointer.link_to_previous_node.link_to_next_node = list_iterator_pointer.link_to_next_node
        list_iterator_pointer = None
        self.size = self.size - 1
        return True

    def delete_by_id(self,id):
        deleted = False
        id = transformString(id)
        list_iterator_pointer = self.head
        while(list_iterator_pointer != None):
            if(list_iterator_pointer.id == id):
                if(list_iterator_pointer.link_to_previous_node == None):
                    self.head = list_iterator_pointer.link_to_next_node
                    list_iterator_pointer.link_to_next_node.link_to_previous_node = None
                    list_iterator_pointer = None
                    deleted = True
                    break
                if(list_iterator_pointer.link_to_previous_node != None and list_iterator_pointer.link_to_next_node != None):
                    list_iterator_pointer.link_to_previous_node.link_to_next_node = list_iterator_pointer.link_to_next_node
                    list_iterator_pointer.link_to_next_node.link_to_previous_node = list_iterator_pointer.link_to_previous_node
                    list_iterator_pointer = None
                    deleted = True
                    break
            list_iterator_pointer = list_iterator_pointer.link_to_next_node
        return deleted

    def update_contact_by_id(self,id,name,number):
        selected_node = self.search_by_id(id)
        if(selected_node != False):
            selected_node.name = transformString(name)
            selected_node.number = number
            return True
        return False

    
    def search_by_number(self,number):
        number  = str(number)
        print(number)
        search_results = []
        list_iterator_pointer = self.head
        while(list_iterator_pointer != None):
            print(f' searched number {number}')
            print(f' current node number {list_iterator_pointer.number}')
            if(list_iterator_pointer.number.find(number) != -1):          
                search_results.append(list_iterator_pointer)
            list_iterator_pointer = list_iterator_pointer.link_to_next_node
        return search_results if len(search_results) > 0 else False

    def search_by_name(self, name):
        search_results = []
        name = transformString(name)
        list_iterator_pointer = self.head
        while(list_iterator_pointer != None):
            if(list_iterator_pointer.name.find(name) != -1):
                search_results.append(list_iterator_pointer)
            list_iterator_pointer = list_iterator_pointer.link_to_next_node
        return search_results if len(search_results) > 0 else False


    def search_by_id(self, id):
        id = transformString(id)
        list_iterator_pointer = self.head
        while(list_iterator_pointer != None):
            if(list_iterator_pointer.id == id):
                return list_iterator_pointer
            list_iterator_pointer = list_iterator_pointer.link_to_next_node
        return False if list_iterator_pointer == None else  list_iterator_pointer

    def printPhoneBook(self):
        new_header_pointer = self.head
        index = 1
        print("************* Phone book *********************************************")
        while(True): 
            print("Contact " + str(index) + " ID: " + str(new_header_pointer.id))
            print("Contact " + str(index) + " name : " + str(new_header_pointer.name.capitalize()))
            print("Contact " + str(index) + " Number: " + str(new_header_pointer.number))
            print("*****************************************************************")
            if(new_header_pointer.link_to_next_node == None):
                return False
            else:
                new_header_pointer = new_header_pointer.link_to_next_node
                index = index + 1

    def add_node_alfa(self,name,number,id):
        new_node = Node(name,number,id)
        
        #Case 1:  List is empty set head equal to new_node
        if(self.head == None):
            self.head = new_node
        
        #create pointer through loop to list
        list_iterator_pointer = self.head

        # Check to see if the pointer points to first elelemt in the list
        if(list_iterator_pointer.link_to_previous_node == None):

            #case: new_node name comes before first_node name
            if(new_node.name <  list_iterator_pointer.name):
                new_node.link_to_next_node = list_iterator_pointer
                list_iterator_pointer.link_to_previous_node = new_node
                self.head = new_node
                return True
            #case: there is only one element in the list and new_node name comes after node1 name
            if(new_node.name > list_iterator_pointer.name and list_iterator_pointer.link_to_next_node == None):
                list_iterator_pointer.link_to_next_node = new_node
                new_node.link_to_previous_node = list_iterator_pointer
                return True
            #case: there is Only one element in the list and node is equal to new_node
            if(list_iterator_pointer.link_to_next_node == None and list_iterator_pointer.compare(new_node)):
                print("element allready in the list")
                return False
        # Looping through the contents of the list        
        while(list_iterator_pointer.link_to_next_node != None):
            if(list_iterator_pointer.compare(new_node)):
                print("element allready in the list")
                return False
            #case: pointer points to first node and next node is not None and new_name name comes after node1 name and before node 2 name
            if(list_iterator_pointer.link_to_previous_node == None and new_node.name > list_iterator_pointer.name and new_node.name < list_iterator_pointer.link_to_next_node.name):
                new_node.link_to_next_node = list_iterator_pointer.link_to_next_node
                new_node.link_to_previous_node = list_iterator_pointer
                list_iterator_pointer.link_to_next_node.link_to_previous_node = new_node
                list_iterator_pointer.link_to_next_node = new_node
                return True
            #case: pointer points to an element1 ,element1 that is not first one and element2 that is not the last one. The new_node name comes after element1 name and before element2 name 
            if(list_iterator_pointer.link_to_previous_node != None  and new_node.name > list_iterator_pointer.name and new_node.name < list_iterator_pointer.link_to_next_node.name):
                new_node.link_to_next_node = list_iterator_pointer.link_to_next_node
                new_node.link_to_previous_node = list_iterator_pointer
                list_iterator_pointer.link_to_next_node = new_node
                return True
            #case: pointer points to element 1 and that element is not the first or the last, and new_node name comes before that elements name but after the previous elements 1(-1) name
            if(list_iterator_pointer.link_to_previous_node  != None and new_node.name > list_iterator_pointer.link_to_previous_node.name and new_node.name < list_iterator_pointer.name):
                list_iterator_pointer.link_to_previous_node.link_to_next_node = new_node
                new_node.link_to_next_node = list_iterator_pointer
                new_node.link_to_previous_node = list_iterator_pointer.link_to_previous_node
                list_iterator_pointer.link_to_previous_node = new_node
                return False
            list_iterator_pointer = list_iterator_pointer.link_to_next_node
        
        #case: last element in the list and new_node name comes before that element
        if(list_iterator_pointer.link_to_next_node == None and new_node.name < list_iterator_pointer.name):
            new_node.link_to_next_node = list_iterator_pointer
            new_node.link_to_previous_node = list_iterator_pointer.link_to_previous_node
            list_iterator_pointer.link_to_previous_node.link_to_next_node = new_node
            list_iterator_pointer.link_to_previous_node = new_node
            return False
        if(list_iterator_pointer.link_to_next_node == None and list_iterator_pointer.compare(new_node)):
                print("element allready in the list")
                return False    
        #case: when the pointer is the last element in the list and new_name comes after this element
        list_iterator_pointer.link_to_next_node = new_node
        new_node.link_to_previous_node = list_iterator_pointer
        return True



    
def main():
    list = DoubleLinkedList()
    list.add_node_alfa("Dad","3433554231","DA1")
    list.add_node_alfa("Mom","022483433","MO1")
    list.add_node_alfa("Home","453432","HO1")
    list.add_node_alfa("Dad","3433554231","DA1")
    list.add_node_alfa("Me","43432423","ME1")
    list.add_node_alfa("Myself","0423353","ME2")
    list.add_node_alfa("Brother","4234522","BR1")
    
    list.printPhoneBook()

    user_id = input("Enter contact id: \n")

    result = list.delete_by_id(user_id)
    if(result):
        print("Contact deleted")
    else:
        print("contact not deleted")
    list.printPhoneBook()
main()

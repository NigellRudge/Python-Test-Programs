def transformString(input_string):
    output_string = input_string.lower()
    return output_string

class Node:
    def __init__(self,name,number, link_to_next_node):
        self.name = name
        self.number = number
        self.link_to_next_node = link_to_next_node

class linkList:

    def __init__(self):
        self.header = None

    def checkIfContactExist(self,name,number=None):
        pass

    def addContact(self):
        print("Add new contact!!")
        name = input("add contact Name: ")
        number = input("add contact number: ")
        if(findContactByName(name)!=False): 
            return False
        if(findContactByNumber(number)!=False):
            return False
        addNode(name,number)

    def addNode(self,name,number):   
        name = transformString(name)
        newNode = Node(name,number,None)
        if(self.header == None):
            self.header = newNode
            return
        newHeadPointer = self.header
        while(newHeadPointer.link_to_next_node != None):
            newHeadPointer = newHeadPointer.link_to_next_node
        newHeadPointer.link_to_next_node = newNode

    def findContactByName(self,name):
        name = transformString(name)
        new_header_pointer = self.header
        while(new_header_pointer.name != name):
            if(new_header_pointer.link_to_next_node == None):
                return False
            new_header_pointer = new_header_pointer.link_to_next_node
        return new_header_pointer

    def printPhoneBook(self):
        new_header_pointer = self.header
        index = 1
        print("************* Phone book *********************************************")
        while(True):
            
            print("Contact " + str(index) + " name : " + str(new_header_pointer.name.capitalize()))
            print("Contact " + str(index) + " Number: " + str(new_header_pointer.number))
            print("*****************************************************************")
            if(new_header_pointer.link_to_next_node == None):
                return False
            else:
                new_header_pointer = new_header_pointer.link_to_next_node
                index = index + 1

    def findContactByNumber(self,number):
        new_header_pointer = self.header
        while(new_header_pointer.number != number):
            if(new_header_pointer.link_to_next_node == None):
                return False
            new_header_pointer = new_header_pointer.link_to_next_node
        return new_header_pointer

    def findContactByNumber2(self,number):
        contacts = []

    

def main():
    list = linkList()
    list.addNode("deyon","08748503")
    list.addNode("Eric","08771705")
    list.addNode("Papa","08835621")

    user_input = input("Enter contact name: \n")
    result = list.findContactByName(user_input)
    if(result != False):
        print("Contact  name : " + str(result.name.capitalize()))
        print("Contact  Number: " + str(result.number))

    user_input = input("Enter contact Number: \n")
    result = list.findContactByNumber(user_input)
    if(result != False):
        print("Contact  name : " + str(result.name.capitalize()))
        print("Contact  Number: " + str(result.number))
    #list.printPhoneBook()

main()

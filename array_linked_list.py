def transform_string(input_string):
    input_string = input_string.toLower()
    return input_string

class ArrayElement

    def __init__(self,element_object,index=None,link_to_next=None, link_to_previous=None):
        self.array_element_object = element_object
        self.item_index = index
        link_to_previous_element = link_to_previous
        link_to_next_element = link_to_next

    def update(self,updated_element):
        self.arraY_element_object = updated_element

class ArrayLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
    
    def add_element(self,new_element):
            new_element = ArrayElement(new_element)
        if(self.head == None):
            self.head = new_element
            return True
        list_iterator_pointer = self.head
        if(list_iterator_pointer.link_to_previous_element == None and new_element.name < list_iterator_pointer.name):
            new_element.link_to_next_element = list_iterator_pointer
            list_iterator_pointer.link_to_previous_element = new_element
            self.head = new_element
            return True
        if(list_iterator_pointer.link_to_previous_element == None and list_iterator_pointer.link_to_next_element == None and new_element.name > list_iterator_pointer.name):
            list_iterator_pointer.link_to_next_element = new_element
            new_element.link_to_previous_element = list_iterator_pointer
            return True
        while(list_iterator_pointer.link_to_next_element  != None):
            if(list_iterator_pointer.link_to_previous_element == None and new_element.name < list_iterator_pointer.link_to_next_element.name):
                new_element.link_to_next_element = list_iterator_pointer.link_to_next_element
                list_iterator_pointer.link_to_next_element.link_to_previous_element = new_element
                new_element.link_to_previous_element = list_iterator_pointer
                list_iterator_pointer.link_to_next_element = new_element
                return True
            if(new_element.name < list_iterator_pointer.name and new_element.name > list_iterator_pointer.link_to_previous_element.name):
                new_element.link_to_next_element = list_iterator_pointer
                list_iterator_pointer.link_to_previous_element.link_to_next_element = new_element
                new_element.link_to_previous_element = list_iterator_pointer.link_to_previous_element
                list_iterator_pointer.link_to_previous_element = new_element
                return True
            list_iterator_pointer = list_iterator_pointer.link_to_next_element
        if(list_iterator_pointer.link_to_next_element == None and list_iterator_pointer.compare(new_element)):
            print("Contact already in phonebook")
            return False
        list_iterator_pointer.link_to_next_element = new_element
        new_element.link_to_previous_element = list_iterator_pointer
        return True



class ArrayList:
    item_index_list = None
    item_list = ArrayLinkedList()

    def __init__(self,***args):
        pass

    
    def add(new_element):
        pass

    def get(element_index):
        pass

    def remove(element_id):
        pass

    def pop_end():
        pass

    def pop():
        pass

    def size():
        pass

    def insert_at(insert_position_index,new_element):
        pass

    def clear():
        pass

    def contains(element):
        pass

    def get_index_list():
        pass
 
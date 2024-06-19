import json
from controls.tda.linked.linkedList import Linked_List
from controls.exception.linkedEmpty import LinkedEmpty
from controls.tda.linked.order.quickSort import QuickSort
from controls.tda.linked.search.binary import Binary

class StackOperation(Linked_List):
    def __init__(self, tope=20):  # Establecer el límite predeterminado a 20
        super().__init__()
        self.__tope = tope

    @property
    def _tope(self):
        return self.__tope

    @_tope.setter
    def _tope(self, value):
        self.__tope = value

    @property
    def verifyTop(self):
        return self._length <= self.__tope

    def push(self, data):
        if self._length < self.__tope:
            self.add(data)
        else:
            self.delete(0)  # Eliminar el primer elemento
            self.add(data)

    @property    
    def pop(self):
        if self.isEmpty:
            raise LinkedEmpty("Stack empty")
        else:
            return self.delete()
        
    def search(self, parametro):
        current = self._head
        while current is not None:
            if current._data.lower() == parametro.lower():
                return current._data
            current = current._next
        return None
    
    def linear_search(self, item):
        results = Linked_List()
        for i in range(self._length):
            if item.lower() in self.get(i).lower():
                results.add(self.get(i))
        return results

    def binary_search(self, item):
        array = self.toArray
        order = QuickSort()
        array = order.sort_primitive_ascendent(array)
        search = Binary()
        results = Linked_List()
        for elem in array:
            if item.lower() in elem.lower():
                results.add(elem)
        return results

    def __iter__(self):
        current = self._head
        while current is not None:
            yield current._data
            current = current._next   
        
    def to_json(self, file_path=None):
        stack_list = [self.get(i) for i in range(self._length)]
        
        json_data = json.dumps(stack_list)
        
        if file_path is None:
            file_path = r"C:\Users\A S U S\Downloads\Practica1\data\stack_data.json"
        
        with open(file_path, "w") as file:
            file.write(json_data)

        print("JSON guardado en", file_path)
        return stack_list
    
    @staticmethod
    def from_json(file_path):
        try:
            with open(file_path, "r") as file:
                json_data = file.read()
            stack_list = json.loads(json_data)
            stack_operation = StackOperation()
            for data in stack_list:
                stack_operation.push(data)
            return stack_operation
        except FileNotFoundError:
            return StackOperation()
        except Exception as e:
            raise e

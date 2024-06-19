class Binary:
    def binary_primitive(self, array, data, low, high):
        if low > high:
            print("Valor no encontrado en la lista")
            return -1
        mid = (low + high) // 2
        if array[mid] == data:
            print(f"Valor encontrado en la posicion: {mid}")
            return mid
        elif array[mid-1] == data:
            print(f"Valor encontrado en la posicion: {mid-1}")
            return mid-1    
        elif array[mid+1] == data:
            print(f"Valor encontrado en la posicion: {mid+1}")
            return mid+1   
        elif array[mid] < data:
            return self.binary_primitive(array, data, mid + 1, high)
        else:
            return self.binary_primitive(array, data, low, mid - 1)
        
   
        
    def binary_string(self, array, data, low, high):
        if low > high:
            print("Valor no encontrado en la lista")
            return -1
        mid = (low + high) // 2
        if array[mid].lower().endswith(data.lower()):
            print(f"Valor encontrado en la posicion: {mid}")
            return mid
        elif array[mid+1].lower().endswith(data.lower()):
            print(f"Valor encontrado en la posicion: {mid+1}")
            return mid+1    
        elif array[mid-1].lower().endswith(data.lower()):
            print(f"Valor encontrado en la posicion: {mid-1}")
            return mid-1
        elif array[mid] > data:
            return self.binary_string(array, data, mid + 1, high)
        else:
            return self.binary_string(array, data, low, mid - 1)
        
    
    def search_binary_models(self, array, element, attribute, low, high):
        if low > high:
            print("Valor no encontrado en la lista")
            return None
        mid = (low + high) // 2
        if float(getattr(array[mid], attribute)) == (element):
            print(f"Valor encontrado en la posicion: {mid}")
            print(array[mid])
        elif mid > 0 and float(getattr(array[mid-1], attribute)) == (element):
            print(f"Valor encontrado en la posicion +1: {mid-1}")
            print(array[mid-1])
        elif mid < len(array) - 1 and float(getattr(array[mid+1], attribute)) == (element):
            print(f"Valor encontrado en la posicion -1: {mid+1}")
            print(array[mid+1])
        elif float(getattr(array[mid], attribute)) < float(element):
            return self.search_binary_models(array, float(element), attribute, mid + 1, high)
        else:
            return self.search_binary_models(array, float(element), attribute, low, mid - 1)
        

    def search_binary_models_string(self, array, element, attribute, low, high):
        if low > high:
            print("Valor no encontrado en la lista")
            return None
        mid = (low + high) // 2
        if (getattr(array[mid], attribute)) == (element):
            print(f"Valor encontrado en la posicion: {mid}")
            print(array[mid])
            return array[mid]
        elif mid > 0 and (getattr(array[mid-1], attribute)) == (element):
            print(f"Valor encontrado en la posicion +1: {mid-1}")
            print(array[mid-1])
            return array[mid-1]
        elif mid < len(array) - 1 and (getattr(array[mid+1], attribute)) == (element):
            print(f"Valor encontrado en la posicion -1: {mid+1}")
            print(array[mid+1])
            return array[mid+1]
        elif (getattr(array[mid], attribute)) < (element):
            return self.search_binary_models_string(array, (element), attribute, mid + 1, high)
        else:
            return self.search_binary_models_string(array, (element), attribute, low, mid - 1)
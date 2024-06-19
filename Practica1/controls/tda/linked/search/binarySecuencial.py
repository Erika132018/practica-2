class BinarySecuencial:
    def binary_primitive_secuencial(self, array, data, low, high):
        if low > high:
            return []

        mid = (low + high) // 2
        result = []

        if array[mid] == data:
            result.append(array[mid])

        # Buscar en la mitad derecha
        if array[mid] <= data:
            result += self.binary_primitive_secuencial(array, data, mid + 1, high)
        # Buscar en la mitad izquierda
        if array[mid] >= data:
            result += self.binary_primitive_secuencial(array, data, low, mid - 1)

        return result

    def binary_models_secuencial(self, array, data, low, high, attribute):
        if low > high:
            return []

        mid = (low + high) // 2
        result = []

        if getattr(array[mid], attribute) == data:
            result.append(array[mid])

        # Buscar en la mitad derecha
        if getattr(array[mid], attribute) <= data:
            result += self.binary_models_secuencial(array, data, mid + 1, high, attribute)
        # Buscar en la mitad izquierda
        if getattr(array[mid], attribute) >= data:
            result += self.binary_models_secuencial(array, data, low, mid - 1, attribute)

        return result

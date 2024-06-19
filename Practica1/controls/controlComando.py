import json
from controls.tda.stack.stackOperation import StackOperation

@staticmethod
def to_json(stack_operation, file_path):
        stack_operation = StackOperation()
        stack_list = stack_operation.to_list()
        json_data = json.dumps(stack_list)
        with open(file_path, "w") as file:
            file.write(json_data)

        print("JSON saved to", file_path)
        return stack_list

@staticmethod
def from_json(file_path):
        with open(file_path, "r") as file:
            json_data = file.read()
        stack_list = json.loads(json_data)
        stack_operation = StackOperation()
        stack_operation.from_list(stack_list)
        return stack_operation
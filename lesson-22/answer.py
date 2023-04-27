from dataclasses import dataclass
@dataclass
class item:
    name: str
    weight: int
    value: int
def make_as_class(data):
    transformed = []
    for i in range(2, (int(data[0])),3):
        transformed.append(item(data[i],data[i+1],data[i+2]))
    return transformed
def devouring(data):
    items = make_as_class(data)
    capacity = data[1]
    total_items = data[1]
    grid = [[0 for x in range(capacity + 1)] for x in range(total_items + 1)]
    for item in range(total_items + 1):
        for weight in range(capacity + 1):
            if item == 0 or weight == 0:
                grid[item][weight] = 0
            elif items







if __name__=="__main__":
    filename = input()

    with open(filename) as data_file:
        lines:list[str] = data_file.readlines()
        
    devouring(lines)

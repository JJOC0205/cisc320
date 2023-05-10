from dataclasses import dataclass
@dataclass
class Food:
    value: int
    items: list[str]

def devouring(total,cap,names,weights,values):
    grid = [[Food(0,[]) for x in range(cap + 1)] for x in range(total + 1)]
    for item in range(total + 1):
        for weight in range(cap + 1):
            if item == 0 or weight == 0:
                grid[item][weight].value = 0
                grid[item][weight].items.append("")
            elif weights[item - 1] <= weight:
                grid[item][weight].value =max(values[item-1] + grid[item-1][weight-weights[item-1]].value, grid[item-1][weight].value)
                if grid[item][weight].value == grid[item-1][weight].value:
                    grid[item][weight].items = grid[item-1][weight].items.copy()
                else:
                    grid[item][weight].items = grid[item-1][weight-weights[item-1]].items.copy()
                    grid[item][weight].items.append(names[item-1])
            else:
                grid[item][weight].value = grid[item-1][weight].value
                grid[item][weight].items = grid[item-1][weight].items.copy()
    return grid[total][cap]


if __name__=="__main__":
    filename = input()

    with open(filename) as data_file:
        lines:list[str] = data_file.readlines()
        
    total = int(lines[0])
    cap = int(lines[1])
    values = []
    names = []
    weights = []
    for i in range(2,len(lines)):
        item = lines[i].split()
        values.append(int(item[2]))
        weights.append(int(item[1]))
        names.append(item[0])
    total_value = devouring(total,cap,names,weights,values)

    for name in total_value.items:
        if name != "":
            print(name)
    print(total_value.value)

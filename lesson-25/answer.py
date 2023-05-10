def find_closest(lines: list[list[int]], current: int, visited: set[int]):
    closest = -1
    closest_dist = 1000
    for i in range(len(lines)):
        if i in visited:
            continue
        if lines[current][i] < closest_dist:
            closest = i
            closest_dist = lines[current][i]
    return closest
def greedy(lines: list[list[int]]):
    path = []
    visited = set()
    visited.add(0)
    for i in range(len(lines)):
        path.append(find_closest(lines, i, visited))
        visited.add()
    return sum(path)
def TSP(lines: list[list[int]]):
    visited = set()
    path = []
    visited.add(0)
    current = 0
    while len(visited) < len(lines):
        path.append(current)
        visited.add(current)
    return 0


if __name__=="__main__":
    filename = input()

    with open("input.txt") as data_file:
        lines:list[str] = data_file.readlines()
    lines = [line.strip() for line in lines]
    lines = [line.split() for line in lines]
    lines = [[eval(num) for num in line] for line in lines]
    print(greedy(lines))
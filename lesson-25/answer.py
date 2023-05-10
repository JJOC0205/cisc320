def tsp(lines, start):
    n = len(lines)
    path = []
    visited = [False] * n
    visited[start] = True
    path.append(start)
    current = start
    dist = 0
    
    for i in range(n-1):
        next = -1
        shortest = float("inf")
        for j in range(n):
            if not visited[j] and lines[current][j] < shortest:
                next = j
                shortest = lines[current][j]
        visited[next] = True
        path.append(next)
        dist += shortest
        current = next
    
    dist += lines[path[-1]][start]
    path.append(start)
    return path, dist

if __name__=="__main__":
    filename = input()

    with open("input.txt") as data_file:
        lines:list[str] = data_file.readlines()
    lines = [line.strip().split() for line in lines]
    lines = [[eval(num) for num in line] for line in lines]
    path, dist = tsp(lines, 0)
    print(*path[:-1], sep="\n")
    print(dist)
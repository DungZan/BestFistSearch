import heapq

# Định nghĩa đồ thị dưới dạng danh sách kề (adjacency list)
graph = {
    'A': ['C', 'D', 'E'],
    'C': ['F'],
    'D': ['F', 'I'],
    'E': ['K','G'],
    'F': ['B'],
    'I': ['B', 'G'],
    'K': [],
    'G': ['H'],
    'H': ['B'],
    'B': []
}

# Giá trị heuristic của từng đỉnh
heuristic = {
    'A': 20,
    'C': 15,
    'D': 6,
    'E': 7,
    'F': 10,
    'G': 5,
    'H': 3,
    'I': 8,
    'K': 12,
    'B': 0
}

def best_first_search(start, goal):
    # Danh sách ưu tiên (priority queue) để lưu các đỉnh cần mở rộng, sắp xếp theo heuristic
    open_list = [(heuristic[start], start)]
    # Danh sách các đỉnh đã được thăm
    closed_list = set()
    # Lưu đường đi (parent của mỗi đỉnh)
    parent = {start: None}

    while open_list:
        # Lấy đỉnh có giá trị heuristic nhỏ nhất
        _, current = heapq.heappop(open_list)

        # Nếu đã đến đích, dừng lại
        if current == goal:
            break

        # Thêm đỉnh hiện tại vào closed list
        closed_list.add(current)

        # Mở rộng các đỉnh con của đỉnh hiện tại
        for neighbor in graph[current]:
            if neighbor not in closed_list:
                # Nếu đỉnh con chưa được thăm, thêm vào open list
                if neighbor not in [node[1] for node in open_list]:
                    heapq.heappush(open_list, (heuristic[neighbor], neighbor))
                    parent[neighbor] = current
                # Nếu đỉnh con đã có trong open list, cập nhật nếu cần (trong trường hợp này không cần vì heuristic cố định)

    # Nếu không tìm thấy đường đi
    if goal not in parent:
        return None, None

    # Khôi phục đường đi từ đích về đầu
    path = []
    current = goal
    while current is not None:
        path.append(current)
        current = parent[current]
    path.reverse()

    # Lưu các bước mở rộng (các đỉnh đã được thăm)
    steps = list(closed_list)
    steps.sort(key=lambda x: list(parent.keys()).index(x) if x in parent else float('inf'))

    return path, steps

def main():
    start = 'A'
    goal = 'B'

    # Chạy thuật toán Best First Search
    path, steps = best_first_search(start, goal)

    # Ghi kết quả ra file
    with open("BestFirstSearch_output.txt", "w", encoding="utf-8") as f:
        if path:
            f.write("Đường đi từ trạng thái đầu đến trạng thái kết thúc:\n")
            f.write(" -> ".join(path) + "\n\n")
            
            f.write("Các bước thực hiện thuật toán:\n")
            for step, node in enumerate(steps, 1):
                f.write(f"Bước {step}: Mở rộng đỉnh {node} (heuristic = {heuristic[node]})\n")
        else:
            f.write("Không tìm thấy đường đi từ A đến B.\n")

    print("Kết quả đã được ghi vào file 'BestFirstSearch_output.txt'.")

if __name__ == "__main__":
    main()
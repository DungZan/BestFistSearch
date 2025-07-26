from tabulate import tabulate


def readfile(filename:str):
        trongso = {}
        ke = {}

        with open(filename, 'r') as file:
            n = int(file.readline().strip())

            for _ in range(n):
                line = file.readline().strip().split()
                key = line[0]
                value = int(line[1])
                trongso[key] = value
                
            for _ in range(n):
                line = file.readline().strip().split()
                key1 = line[0]
                value1 = line[1:]
                ke[key1] = value1

            start, end = file.readline().strip().split()
        return trongso, ke, start, end

def Search(trongso, ke, start, end):
        row =[]
        L = [(start, [start])]

        while L:
            u, path = L.pop(0)
 
            if u == end:
                print("Tìm kiếm thành công")
                row.append([u + str(trongso[u]), "TTKT-Dừng", None])
                return tabulate(row, headers=["Phát triển TT", "Trạng thái kề", "Danh sách L"]) + "\nĐường đi là: " + " => ".join(i + str(trongso[i]) for i in path)
            
            for v in ke.get(u, []):
                new_path = path + [v]
                L.append((v, new_path))
                L.sort(key=lambda x: trongso.get(x[0]))
            row.append([u+str(trongso[u]), ", ".join([i + str(trongso[i]) for i in ke[u]]),", ".join(i1 + str(trongso[i1]) for i1,i2 in L)])
        
        return "Không tìm thấy đường đi"

def printFile(filename, content):
        file = open(filename, "w", encoding="utf-8")
        file.write(content)
        file.close()

if __name__ == '__main__':
    trongso, ke, start, end = readfile("BestFistSearch/inputbfs1.txt")
    #print(Search(trongso, ke, start, end))
    printFile("BestFistSearch/output1.txt",Search(trongso, ke, start, end))


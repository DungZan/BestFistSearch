        print('so dinh: '+str(n))
        for key, value in data_dict.items():
             print(key + " " + str(value))
        for vertex, neighbors in graph.items():
            print(f"Đinh {vertex}: Kề {neighbors}")
        print("Bắt đầu từ "+start+ " đến "+ end)
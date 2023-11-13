population_database = {}

#输入区块
def add_person():
    name = input("请输入姓名: ")
    age = int(input("请输入年龄: "))
    city = input("请输入城市: ")
    state = input("请输入目前状态：")
    population_database[name] = {'姓名':name,'年龄': age, '城市': city, '状态': state}
    print(f"{name} 的信息已添加到羊口数据库。")
    save_population_data()
#查询区块
def query_person():
    name = input("请输入要查询的姓名: ")
    if name in population_database:
        person_info = population_database[name]
        print(f"姓名: {name}, 年龄: {person_info['年龄']}, 城市: {person_info['城市']}, 状态: {person_info['状态']}")
    else:
        print(f"{name} 不在羊口数据库中。")
#写入文件区块
def save_population_data():
    file_path = r'F:\qqcyrkpc\cos.txt'
    with open(file_path, 'w') as file:
        for name, info in population_database.items():
            file.write(f"姓名: {name}, 年龄: {info['年龄']}, 城市: {info['城市']}, 状态: {info['状态']}\n")
#读取文件区块
def load_population_data():
    file_path = r'F:\qqcyrkpc\cos.txt'
    data = {}
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            for line in lines:
                parts = line.strip().split(', ')
                if len(parts) >= 4:  # 确保至少有四个部分
                    name = parts[0].split(': ')[1]
                    age = int(parts[1].split(': ')[1])
                    city = parts[2].split(': ')[1]
                    state = parts[3].split(': ')[1]
                    data[name] = {'年龄': age, '城市': city, '状态': state}
        return data
    except FileNotFoundError:
        return {}
#操作区块
population_database = load_population_data()
while True:
    print("\n青青草原羊口普查")
    print("1. 添加新的羊口记录")
    print("2. 查询羊口信息")
    print("3. 退出")
    choice = input("请选择操作 (1/2/3): ")

    if choice == '1':
        add_person()
    elif choice == '2':
        query_person()
    elif choice == '3':
        break
    else:
        print("无效的选择，请重新选择。")

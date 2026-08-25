print("shahid=====================================>")
def run():
    list = [1,2,4,5,6]
    dic = {
        "age": 20,
        "name": "shahid",
        "class": "BCA"
    }
    list.sort()
    print(list)

    list.append(4)
    print(list)
    list.clear()
    print(list)

    list1 = [1,2,34,5,6]
    a= list1.pop(2)
    print(a)

    list1.reverse()
    print(list1)

    for dic in dic.items():
        print(dic)

    print("========>")

    dict = {
        "age": 20,
        "name": "shahid",
        "class": "BCA"
    }
    
    print(dict.keys())
    print('------------------------')
    print([key for key in dict.keys()])
    print('------------------------')
    

    for val in dict.values():
        print(val)

    dict.pop("class")
    print(dict)

    dict.clear()
    print(dict)


run()
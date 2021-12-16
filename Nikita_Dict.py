sonastik={} #Создал словарь с помощью литерала
riigid=linnad=[]
file=open("File.txt", "r")
file=open("Pop.txt", "r")
for line in file:
    k, v=line.strip().split(" - ")
    sonastik[k.strip()] = v.strip()
    riigid.append(k.strip())
    linnad.append(v)
file.close()
#print(sonastik)
#print(riigid)
#print(linnad)
while True:
    print()
    print("Привет! Пройдёмся по странам и их столицам!")
    print("1 - Узнать столицу страны или наоборот\n2 - Добавить новую страну и столицу\n3 - Проверь свои знания\n3 - Исправить информацию")
    v=int(input())
    if v==1:
        b=int(input("Если Столицу страны - 1\nЕсли вы хотите узнать страну по столице - 2\n==>"))
        if b==1:
            riik=input("Введите название страны: ")
            print("Столица этой страны ==>",sonastik[riik])
        elif b==2:
            linn=input("Введите название столицы: ")
            print("Страна этой столицы ==>" , riik)
        else:
            print("Введи 1 или 2")
    elif v==2:
        a=input("Введите страну и столицу которую вы хотите добавить.(Через тире -)\n==> ")
        file=open("File.txt" , "a")
        print("Вы ввели страну и столицу" , a)

    elif v==3:
        a=input("Что будем исправлять?\nСтраны - 1\nСтолицы - 2?\n")
        if a=="1":
            name=input("Введите название страны для исправления: ")
            a1=state_cleanup(sonastik, a, name)
            a2=state_update(sonastik, name)
        if a=="2":
            name=input("Введите название столицы для исправления: ")
            a=city_cleanup(sonastik, a, name)
            update=add_new(sonastik, new_state, city)
    elif v==4:
        kusimus=="Pop.txt"
        riik=="File.txt"
        a=input(kusimus)
        if v=="Tallinn": 
            print("Правильно ")
        else:
           print("Не правильно иди учи карту!!")
           break
    else:
        print("Введи правильные цифры!")
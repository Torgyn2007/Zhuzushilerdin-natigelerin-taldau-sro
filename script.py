akparat = ("ЖҮЗУ ЖАРЫСЫ", "100 МЕТРГЕ ЕРКІН ЖҮЗУ")
print("Жарыс туралы мәлімет:", akparat)
sportshy1 = input("Бірінші спортшының аты: ")
uakyty1 = float(input("жүзу уақыты (секунд): "))
zhasy1 = int(input("Жасы: "))
sportshy2 = input("Екінші спортшының аты: ")
uakyty2 = float(input("жүзу уақыты (секунд): "))
zhasy2 = int(input("Жасы: "))
sportshy3 = input("Үшінші спортшының аты: ")
uakyty3 = float(input("жүзу уақыты (секунд): "))
zhasy3 = int(input("Жасы: "))

natizheler = {
    sportshy1: {"uakyt": uakyty1, "zhas": zhasy1},
    sportshy2: {"uakyt": uakyty2, "zhas": zhasy2},
    sportshy3: {"uakyt": uakyty3, "zhas": zhasy3}
}

ortasha_uakyt = (uakyty1 + uakyty2 + uakyty3) / 3
print("Орташа уақыт:", int(ortasha_uakyt * 10) / 10, "секунд")

if uakyty1 == uakyty2 == uakyty3:
    print("Барлық спортшылардың уақыты бірдей!")
elif uakyty1 < uakyty2 and uakyty1 < uakyty3:
    print(f"Ең жылдам спортшы:", sportshy1)
elif uakyty2 < uakyty1 and uakyty2 < uakyty3:
    print(f"Ең жылдам спортшы:", sportshy2)
elif uakyty3 < uakyty1 and uakyty3 < uakyty2:
    print(f"Ең жылдам спортшы:", sportshy3)
else:
    print("Бірнеше спортшының уақыты бірдей және ең жылдам нәтиже көрсетті!")
sportshylar = list(natizheler.keys())
izdeu = input("Қай спортшыны іздегіңіз келеді? ")

if izdeu.lower() in [a.lower() for a in sportshylar]:
    print(izdeu, "жарысқа қатысады!")
else:
    print(izdeu, "тізімде жоқ.")
while True:
    print("Мәзір ")
    print("1. Спортшы қосу")
    print("2. Барлық нәтижелерді көру + орташа уақыт + топ-3, ")
    print("3. Шығу")
    tandau = input("Таңдаңыз: ")

    if tandau == "1":
        at = input("Жаңа спортшы аты: ")
        uakyt = float(input("Жүзу уақыты: "))
        zhas = int(input("жасы: "))
        natizheler[at] = {"uakyt": uakyt, "zhas": zhas}
        print(at, "қосылды.")

    elif tandau == "2":
        print(" Барлық спортшылар")
        for name, info in natizheler.items():
            print(name + " - Жасы: " + str(info['zhas']) + ", Уақыты: " + str(info['uakyt']) + " сек")

        ortasha_uakyt = sum(i["uakyt"] for i in natizheler.values()) / len(natizheler)
        print("Орташа уақыт:", int(ortasha_uakyt * 10) / 10, "секунд")
        results = []
        for name, info in natizheler.items():
            results.append((name, info["uakyt"], info["zhas"]))

        for i in range(len(results)):
            for j in range(i + 1, len(results)):
                if results[i][1] > results[j][1]:
                    results[i], results[j] = results[j], results[i]

        print("Топ-3 үздік спортшы:")
        for i in range(min(3, len(results))):
            name, uakyt, zhas = results[i]
            print(i+1, ".", name, "-", uakyt, "сек,", "Жасы:", zhas)

        print("График түрінде нәтижелер:")
        max_time = max(i["uakyt"] for i in natizheler.values())
        for at, info in natizheler.items():
            uzun = int((info["uakyt"] / max_time) * 40)
            print(at.ljust(10) + ": " + "█" * uzun + " " + str(info['uakyt']) + " сек")

    elif tandau == "3":
        print("Бағдарлама аяқталды.")
        break

    else:
        print("Қате таңдау! Қайта көріңіз.")

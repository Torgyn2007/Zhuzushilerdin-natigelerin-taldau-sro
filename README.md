# Zhuzushilerdin-natigelerin-taldau-sro
Ибадулла Ақторғын СИБ 21 
 ТАҚЫРЫП : ЖҮЗУШІЛЕРДІҢ НӘТИЖЕЛЕРІН ТАЛДАУ 
 МАҚСАТЫ: Бұл бағдарлама спортшылардың нәтижелерін енгізіп,орташа уақытты есептейді, ең жылдам спортшыны табады, спортшы іздейді, және мәзір арқылы жаңа қатысушыларды қосады.
 akparat = ("ЖҮЗУ ЖАРЫСЫ", "100 МЕТРГЕ ЕРКІН ЖҮЗУ") мұнда мен кортеж қолдандым 
print("Жарыс туралы мәлімет:", akparat) оны шыгардым 

sportshy1 = input("Бірінші спортшының аты: ")
uakyty1 = float(input("жүзу уақыты (секунд): "))
zhasy1 = int(input("Жасы: "))
sportshy2 = input("Екінші спортшының аты: ")
uakyty2 = float(input("жүзу уақыты (секунд): "))
zhasy2 = int(input("Жасы: "))
sportshy3 = input("Үшінші спортшының аты: ")
uakyty3 = float(input("жүзу уақыты (секунд): "))
zhasy3 = int(input("Жасы: "))  Мұнда пайдаланушыдан үш спортшының аттары мен жүзу уақыты , жасын сұрайды сосын пайдалануш оны енгізеді
float() — уақыт ондық сан болуы үшін жаздым 
natizheler = {
    sportshy1: {"uakyt": uakyty1, "zhas": zhasy1},
    sportshy2: {"uakyt": uakyty2, "zhas": zhasy2},
    sportshy3: {"uakyt": uakyty3, "zhas": zhasy3}
}
Мен мұнда natizheler  нәтижелер  деген сөздік ашып мәліметтерді сақтадым 
ortasha_uakyt = (uakyty1 + uakyty2 + uakyty3) / 3
print("Орташа уақыт:", int(ortasha_uakyt * 10) / 10, "секунд") арифметика ортасын таптым яғни орташа уакытын 

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
Бұл код бөлігінде  кім ең аз уақытта жүзгенін анықтайды. Яғни шарт аркылы және and арқылы бір бірімен салыстырып кішісін табамыз.
Егер бәрінің уақыты тең болса  — «Барлық спортшылардың уақыты бірдей!» дейді.
Егер екі спортшы тең болса — соңғы else арқылы екеуі де ең жылдам екенін хабарлайды.
sportshylar = list(natizheler.keys()) 
izdeu = input("Қай спортшыны іздегіңіз келеді? ")

if izdeu.lower() in [a.lower() for a in sportshylar]:
    print(izdeu, "жарысқа қатысады!")
else:
    print(izdeu, "тізімде жоқ.")  
lower() — әріптердің регистрін елемеу үшін яғни енгізілген мәлімет улкен не кіші әріппен болса
while True:  цикл  тоқтамай жұмыс істейді.    .
    print("Мәзір ")
    print("1. Спортшы қосу")
    print("2. Барлық нәтижелерді көру + орташа уақыт + топ-3, ")
    print("3. Шығу")
    tandau = input("Таңдаңыз: ") мұнда мен мәзір жасадым яғни пайдаланушыға таңдаңыз сөзі шығады сол кезде 1 санын енгізгенде жаңа жүзуші қоса алады , 2 санын енгізсе жүзушілердің  нәтижелерді көре алады, 3 санын енгізсе бағдарламадан шығады.
    if tandau == "1":
        at = input("Жаңа спортшы аты: ")
        uakyt = float(input("Жүзу уақыты: "))
        zhas = int(input("жасы: "))
        natizheler[at] = {"uakyt": uakyt, "zhas": zhas}
        print(at, "қосылды.")  пайдаланушы 1 санын енгізгенде жаңа жүзушіні қоса алады
    elif tandau == "2":
        print(" Барлық спортшылар")
        for name, info in natizheler.items():
            print(name + " - Жасы: " + str(info['zhas']) + ", Уақыты: " + str(info['uakyt']) + " сек")
        ortasha_uakyt = sum(i["uakyt"] for i in natizheler.values()) / len(natizheler)
        print("Орташа уақыт:", int(ortasha_uakyt * 10) / 10, "секунд") мұнда тағы орташа уакытын табамыз
Мұнда natizheler.values() — сөздіктегі барлық мәндерді  қайтарады 
sum() — осы мәндердің қосындысын есептейді
len() — спортшылардың санын есептейді. ягни узындык аркылы
ortasha_uakyt = sum(natizheler.values()) / len(natizheler) орташа уакыт табылады
        results = []
        for name, info in natizheler.items():
            results.append((name, info["uakyt"], info["zhas"])) 
        for i in range(len(results)):
            for j in range(i + 1, len(results)):
                if results[i][1] > results[j][1]:
                    results[i], results[j] = results[j], results[i]
Мұнда карапайым сұрыптау жүргіздім 
        print("Топ-3 үздік спортшы:")
        for i in range(min(3, len(results))):
            name, uakyt, zhas = results[i]
            print(i+1, ".", name, "-", uakyt, "сек,", "Жасы:", zhas)
min(3, len(results)) — егер спортшылар саны 3-тен аз болса, қате шықпасын деп, аз санын алады,for циклі әр үздік спортшыны бір-бірлеп шығарады, print() нәтижені нөмірмен және мәнімен көрсетеді.
            print("График түрінде нәтижелер:")
        max_time = max(i["uakyt"] for i in natizheler.values())
        for at, info in natizheler.items():
            uzun = int((info["uakyt"] / max_time) * 40)
            print(at.ljust(10) + ": " + "█" * uzun + " " + str(info['uakyt']) + " сек")
 Әр спортшының уақыты графикалық жолақ (█) түрінде бейнеленеді. Ұзындығы — олардың уақытына байланысты. info["uakyt"] / max_time — әр спортшының уақыты ең үлкен уақытқа қатынасы (үлесі) есептеледі. * 40 — осы үлесті 40 таңбалық ұзындыққа көбейтеді, яғни жолақтың ұзындығын анықтайды. int() — нәтижені бүтін санға айналдырады.
    elif tandau == "3":
        print("Бағдарлама аяқталды.")
        break
  Пайдаланушы 3  санын енгізгенде бағдарлама токтайды өйткені break опеарторы оны токтатады 
    else:
        print("Қате таңдау! Қайта көріңіз.")
ал пайдаланушы баска сан енгізсе else орындалады

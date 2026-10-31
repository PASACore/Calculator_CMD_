print("""
██╗  ██╗███████╗███████╗ █████╗ ██████╗     ███╗   ███╗ █████╗ ██╗  ██╗██╗███╗   ██╗███████╗███████╗██╗
██║  ██║██╔════╝██╔════╝██╔══██╗██╔══██╗    ████╗ ████║██╔══██╗██║ ██╔╝██║████╗  ██║██╔════╝██╔════╝██║
███████║█████╗  ███████╗███████║██████╔╝    ██╔████╔██║███████║█████╔╝ ██║██╔██╗ ██║█████╗  ███████╗██║
██╔══██║██╔══╝  ╚════██║██╔══██║██╔═══╝     ██║╚██╔╝██║██╔══██║██╔═██╗ ██║██║╚██╗██║██╔══╝  ╚════██║██║
██║  ██║███████╗███████║██║  ██║██║         ██║ ╚═╝ ██║██║  ██║██║  ██╗██║██║ ╚████║███████╗███████║██║
╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝         ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝╚══════╝╚══════╝╚═╝                                                                                                   
               ------------->>>>>>>| ▄︻デ══━一 ᴍᴀᴅᴇ ɪɴ ᴛᴜʀᴋᴇʏ :D |<<<<<<<-------------
""")
islem = {"+": lambda a, b: a + b,
         "-": lambda a, b: a - b,
         "*": lambda a, b: a * b,
         "/": lambda a, b: a / b,
      "kare": lambda a, b: a * a}
yeni = True
while True:
     if yeni:
        try:
            a = float(input("SAYI1 GİR:"))
            yeni = False
        except ValueError:
            print("SAYI GİR MAL")
            continue
          
     while True:
        op = input("(+, -, *, /, kare, ac, q):").lower()
        if op in islem or op in ("ac","q"):
            break
        print("Geçersiz Operatör")

     if op == "q":
        print("Çıkış Yapılıyor")
        quit()
     if op == "ac":
        print(">>> YENİ İŞLEM <<<")
        yeni = True
        continue
       
     while True:
        try:
            if op == "kare":
                 b = 0

            else:
                 b = float(input("SAYI2 GİR:"))
            a = islem[op](a, b)
            print("->>SONUÇ:{:,}<<-".format(a))
            break

       
        except ValueError:
            print("SAYI GİR MAL")
        except ZeroDivisionError:
            print("SAYI SIFARA BÖLÜNMEZ!")

    
    

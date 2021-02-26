def menu ():
    print ("Selamat Datang!")
    print ("MENU:")
    print ("1. Daftar Kontak")
    print ("2. Tambah Kontak")
    print ("3. Keluar")


    #menu()
    pilihanmenu= int(input("Pilih menu: "))

    while pilihanmenu != 0:
        if pilihanmenu == 1:
            daftarkontak ()
            
        elif pilihanmenu == 2:
            tambahkontak()


        elif pilihanmenu == 3:
            print ("program selesai, sampai jumpa!")
            break

        else:
            print ("menu tidak tersedia")
            break
    
    menu ()
    pilihanmenu= int(input("Pilih menu: "))

    def daftarkontak ():
        nama = []
        no_telepon = []

        n = int (input("jumlah kontak:"))
        for x in range (n):
            print (x+1, ". nama: ")
            nama.append (input())
            print("no_telepon: ")
            no_telepon.append(input())
        
        for x in range (n):
                print (x+1,".", nama [x])
                print (" ", no_telepon [x])

    menu ()         


    def tambahkontak ():
        x = {}
        name = input ("masukan nama:")
        phone = int (input ("masukan no telpon: "))
        x[name] = phone

        print ("kontak berhasil ditambahkan")
    

menu ()

 
print(r'''
    ___
 .-'   `'.
/         \
|  ;  |  ; |
|0) ~ (0)  |
| _.---'`__.-(
 (_.   __.--'`_..
  '.__.\   '--.
   \_.-' ,.--'`
     `""` ( ,.--'`
   ',__    /./;
     ;, '.__.'`
    __ _`)  ) .---.__.'
   / | |\   \__..--""
   """--.,_ `---'
     .'.''-._.-'`_./
      /\ '. \ _.-~~~````~~~-._`-.__.'
      | | .' _.-'          | |  \ \
      '. `~---`            \ \/ .' \ \
        '.  '-._)           \/ /    \ \
          `=.__`~-.                 / /\
               `)  )               / /
                `"".`\           , _.-'.'
                      \ \       / / ( (
                       / /      `--~`  ) )
                       .-'.'         '.'.
                      | (           (/`
                       ( (`           ) )
                        '-;            `
''')
print("==========================================")
print("   P R O J E   A B İ S ' E   H O Ş G E L D İ N İ Z")
print("==========================================")
print("\nYıl 2084. İnsanlık, Pasifik Okyanusu'nun en derin noktası olan Mariana Çukuru'nun dibinde, "
      "bilinmeyen bir enerji sinyali tespit etti. Sen, 'Leviathan' adlı son teknoloji denizaltının kaptanısın. "
      "Görevin, basınca dayanıp bu sinyalin kaynağını bulmak. Ancak okyanusun karanlık dipleri affedici değildir...\n")

tercih = "a"
print("Denizaltı 8.000 metre derinliğe ulaştığında radar iki farklı yol gösteriyor. Biri devasa hidrotermal bacaların (kaynar su fışkıran çatlaklar) olduğu aktif bir bölge, diğeri ise tamamen zifiri karanlık, dar bir yarık.\n")
tercih = input("Rotayı nereye çevireceksin? 'Sicak' (Hidrotermal bacalar) mı yoksa 'Karanlik' (Karanlık yarık) mı? ")
if tercih == "Sicak":
    print("Kaynar sular denizaltının dış zırhını eritir, gövde parçalanır. (Game Over)")
    exit()
elif tercih == "Karanlik":
    print("Dar yarıktan usta bir manevrayla geçersin ve devasa bir yeraltı mağarasına ulaşırsın.\n")
    print("Mağaranın içinde ilerlerken, denizaltının etrafında devasa, parlayan (biyolüminesans) gözleri olan tarih öncesi bir deniz yaratığı belirmeye başlar. Yaratık sese ve ışığa duyarlıdır.")
    tercih = input("Yaratık yaklaşıyor! 'Flas' (Farları yakıp onu korkut) mı yoksa 'Sessiz' (Tüm sistemleri kapatıp saklan) mi? ")
    if tercih == "Flas":
        print("Güçlü ışık yaratığı kör etmek yerine öfkelendirir. Denizaltıyı dev bir ısırıkla ezer. (Game Over)")
    elif tercih == "Sessiz":
        print("Motorlar durur, ışıklar söner. Yaratık bir süre etrafında döner ve ilgisini kaybedip uzaklaşır. (Oyun devam eder...)\n")
        print("Tehlikeyi atlattıktan sonra sinyalin kaynağına ulaşıyorsun. Karşında sular altında kalmış antik bir uzaylı şehri var! İçeri girmek için denizaltıyı kenetlemen (docking) gerekiyor ama iki farklı giriş var. Kuzey kapısında garip semboller parlıyor, Güney kapısı ise yarı yarıya çökmüş durumda.")
        tercih = input("Hangi kapıya kenetleneceksin? 'Kuzey' mi, 'Guney' mi? ")
        if tercih == "Guney":
            print("Zaten zayıf olan yapı, denizaltının ağırlığına dayanamaz ve tamamen çöker. Molozların altında kalırsın. (Game Over)")
        elif tercih == "Kuzey":
            print("Kenetlenme başarılı! Dalgıç kıyafetini giyip içeri girersin. (Oyun devam eder...)\n")
            print("Şehrin merkezine vardığında, o gizemli enerji kaynağını (devasa parlayan bir kristal) buluyorsun. Ancak kristal bir güvenlik mekanizmasıyla korunuyor. Önünde 4 farklı renkte tuş var. Yanlış tuşa basarsan tüm şehir kendini imha edecek.")
            tercih = input("Hangi tuşa basacaksın? 'Kirmizi', 'Mavi', 'Sari' veya 'Siyah'? ")
            if tercih == "Kirmizi":
                print("Oda aniden alev alır, oksijenin tükenir. (Game Over)")
            elif tercih == "Mavi":
                print("Mavi: Odaya saniyeler içinde dondurucu sıvı nitrojen dolar. (Game Over)")
            elif tercih == "Sari":
                print("Güçlü bir elektrik akımına kapılırsın. (Game Over)")
            elif tercih == "Siyah":
                print("Hiçliği ve uzayı temsil eden tuş doğru olanıdır! Kristal yuvasından çıkar, insanlığın enerji krizini çözecek gücü elde ettin. Kaptan, tarih yazdın! (You Win!)")




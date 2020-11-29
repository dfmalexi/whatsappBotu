def speech(s):
    s=str(s).lower()
    if("kimsin" in s):
        text= "Ben araçların piyasa değerini en doğru şekilde hesaplayan bir bilgisayar programıyım.\nNasıl çalıştığımı öğrenmek için nasıl çalışır yazabilirsin."
        return text
    elif("nasıl" in s or  "nasil" in s) and ("çalışır" in s or "calisir" in s or "çalisir" in s or "çalişir" in s or "calişir"in s or "calısır" in s):
        text= "Türkiye içerisinde yayınlanan neredeyse tüm araba ilanlarının fiyatlarını araştırarak sizin için bir arabanın piyasası hakkında en doğru bilgiyi verir. "
        return text
    elif ("nasıl" in s or "nasil" in s)and ("kullanırım"in s or "kullanirim"in s or "kullanabilirim" in s or "kullanılır" in s or"kullanilir"in s):
        text="Arama türünü seçtikten sonra (detaylı veya hızlı) arabanızın modelini yazarak kullanabilirsiniz.Örneğin: hızlı opel corsa y2015 km30.000-180.000 m1.6CDTI vManuel"
        return text
    elif("yardim" in s and "talebi" in s):
        text="Yardım talebiniz oluşturuldu, size en kısa zamanda geri dönüş yapılacaktır. Anlayışınız için teşekkür ederiz."
        return text 
    elif("yardim" in s or "yardım" in s or "help" in s):
        text="Kullanım talimatları için: 'nasıl kullanılır'\nNasıl çalıştığını öğrenmek için: 'nasıl çalışır'\nYardım talebi için:'yardım talebi' yazabilirsiniz..."
        return text 
    elif("detaylı" in s or "hızlı" in s):
        text="Sayın ?\nSize hitap etmek için isminizi öğrenebilirmiyim?"
        return text
    else:
        text= "Beni mağzur görün ancak anlayamadım...\nYardım yazarak kullanım rehberini görüntüleyebilirsiniz."
        return text
# text=speech("nasl")
# print(text)
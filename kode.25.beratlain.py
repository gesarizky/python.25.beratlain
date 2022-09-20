# Author  : Gesa Rizky Nugraha
# Email   : gesarizkynugraha@gmail.com
# Website : karenabelajar.blogspot.com

# Menginput Satuan Jarak
Kilogram = float(input("Tuliskan Berapa Kilogram: "))

# Mengkonversi
ons  = Kilogram * 10
pon  = Kilogram * 2
kwintal = Kilogram * 0.01
ton = Kilogram * 0.001
 
# Menampilkan Hasil 
print('%0.2f  Kilogram sama dengan %0.2f Ons' %(Kilogram,ons))
print('%0.2f  Kilogram sama dengan %0.2f Pon' %(Kilogram,pon))
print('%0.2f  Kilogram sama dengan %0.2f Kwintal' %(Kilogram,kwintal))
print('%0.2f  Kilogram sama dengan %0.2f Ton' %(Kilogram,ton))

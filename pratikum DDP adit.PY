
#Buat program untuk minta input jumlah baris
# dan buatrangkaian berikut ini
#*
#**
#***
#****
#Dan seterusnya sejumlah baris yang diinputkan
#Gunakan for loop dengan range


#no.1

number=[951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544,  615, 83, 165, 141, 501,
        263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941,  386, 462, 47, 418, 907, 344, 236, 375, 
        823, 566, 597, 978, 328, 615, 953, 345,  399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950,
        626, 949, 687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
        958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470, 743, 527
]
j=0
k=553
while j < len(number):
    if number[j] % 2 !=0 and number[j] <= k:
        print(number[j], end=' ')
    j+=1
    
print('')
    
#no.2 

jumlah = 0
for a in range(1, 20, 2):
    jumlah += a
    print(a,end=' + ')
print('=', jumlah)
    
#no.3

nilai = int(input('masukan baris: '))
for b in range(nilai):
    for c in range(b+1):
        print(' * ', end=(' '))
print('')
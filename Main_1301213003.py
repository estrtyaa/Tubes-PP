#inisialisasi list kosong petak_sawah
petak_sawah = []

#membaca file text, dan menambah elemen berupa dictionary ke dalam list petak_sawah
with open('padi.txt') as teks:
    while True:
        read = teks.readline()
        if read:
            read = read.replace('\n','').split(' ')
            if int(read[1]) < 365:
                tahun = int(365/int(read[1]))
            else:
                tahun = int(int(read[1])/365)
            petak_sawah.append({'Lokasi':read[0],
                                'Total Gabah':tahun * float(read[2]),
                                'Total Penjualan':(tahun * float(read[2]) * 1000) * int(read[3])})
        else:
            break


#membuat fungsi report untuk menampilkan total gabah dan total penjualan selama setahun
def report(petak_sawah):
    total_gabah = 0.0
    total_penjualan = 0
    for petak in petak_sawah:
        total_gabah += petak["Total Gabah"] #menambahkan nilai total_gabah dengan value dari "Total Gabah" dari setiap petak
        total_penjualan += petak["Total Penjualan"] #menambahkan nilai total_penjualan dengan value dari "Total Penjualan" dari setiap petak
    print('Total Penjualan Sebesar Rp. {} dengan menjual {:.2f} ton gabah'.format(total_penjualan, total_gabah))

#membuat fungsi rerata untuk mencari rata-rata hasil panen berdasarkan jumlah petak sawah
def rerata(petak_sawah, lokasi):
    total_gabah = 0
    for petak in petak_sawah:
        if petak["Lokasi"] == lokasi:
            total_gabah += petak["Total Gabah"]

    if total_gabah != 0:
        return total_gabah/365, (total_gabah * 1000)/365
    return 0, 0

#membuat fungsi produktif untuk menunjukkan petak sawah yang menghasilkan gabah terbanyak
def produktif(petak_sawah):
    lokasi = []
    for petak in petak_sawah:
        #cianjur udah ga ya?
        if petak["Lokasi"] in lokasi:
            continue #kalau sudah ada, diskip
        else:
            lokasi.append(petak['Lokasi']) # jika lokasi belum ada maka akan ditambahkan ke dalam list lokasi

    maks_ton = 0
    maks_kg = 0
    hasil_lokasi = None
    #mendeteksi setiap elemen dalam list lokasi
    for l in lokasi:
        ton, kg = rerata(petak_sawah, l)
        if ton > maks_ton:
            maks_ton = ton
            maks_kg = kg
            hasil_lokasi = l
        elif ton == maks_ton:
            hasil_lokasi += ", " + l

    print("Petak Sawah paling produktif adalah {} dengan rata - rata hasil panen per tahun adalah {:.2f} ton atau {:.2f} kg".format(hasil_lokasi, maks_ton, maks_kg))

#main program
print("Struktur Data yang dibuat :")
print(petak_sawah)

print("\nPemanggilan Fungsi Report")
report(petak_sawah)

print("\nPemanggilan Fungsi Rerata")
ton, kg = rerata(petak_sawah, 'Cianjur')
print("Rata - Rata Petak Sawah di Cianjur per tahun adalah {:.2f} ton atau {:.2f} kg".format(ton, kg))
ton, kg = rerata(petak_sawah, 'Garut')
print("Rata - Rata Petak Sawah di Garut per tahun adalah {:.2f} ton atau {:.2f} kg".format(ton, kg))

print('\nPemanggilan Fungsi Produktif')
produktif(petak_sawah)

#nomor 1

class MhsTIF(object) :
    def __init__ (self, nama, no, kota, uangsaku):
        self.nama = nama
        self.no = no
        self.kt = kota
        self.uangsaku = uangsaku

    def __str__ (self) :
        s = self.nama + ",Nomor" +str(self.no) + "tinggal di" + self.kt +\
            "uang saku sebesar"+str(self.uangsaku) +"per bulan."
        return s
    def getno(self) :
        return self.no

c1 = MhsTIF ("Piki", 10, "Ngawi", 900000)
c2 = MhsTIF ("Hasri", 18, "Sukoharjo", 950000)
c3 = MhsTIF ("Pomade", 15, "Pemalang", 1000000)
c4 = MhsTIF ("Gremeng", 17, "Purwodadi", 1100000)
c5 = MhsTIF ("Paijo", 21, "Semarang", 850000)

Daftar = [c1, c2, c3, c4, c5]

def mergesort(A) :
    if len (A) > 1 :
        mid = len(A) // 2
        separuhkiri = A[:mid]
        separuhkanan = A[mid:]

        mergesort(separuhkiri)
        mergesort(separuhkanan)

        i=0;j=0;k=0
        while i < len (separuhkiri)and j < len (separuhkanan) :
            if separuhkiri[i].no < separuhkanan[j].no :
                A[k].no = separuhkiri[i].no
                i = i+1
            else :
                A[k].no = separuhkanan[j].no
                j = j+1
            k = k+1

        while i < len (separuhkiri) :
            A[k].no = separuhkiri[i].no
            i = i+1
            k = k+1
        while j < len (separuhkanan) :
            A[k].no = separuhkanan[j].no
            j = j+1
            k = k+1

        return A
    
def quicksort(A):
    quicksortbantu (A,0, len(A) -1)
    return A

def quicksortbantu(A, awal, akhir):
    if awal < akhir :
        titikbelah = partisi(A, awal, akhir)
        quicksortbantu(A, awal, titikbelah -1)
        quicksortbantu(A, titikbelah +1, akhir)

def partisi(A, awal, akhir):
    nilaipivot = A[awal].getno()

    penandakiri = awal +1
    penandakanan = akhir

    selesai = False
    while not selesai :
        while penandakiri <= penandakanan and \
              A[penandakiri].getno() <= nilaipivot :
            penandakiri +=1
        while A[penandakanan].getno() >= nilaipivot and \
            penandakanan >= penandakiri :
            penandakanan -=1
        if penandakanan < penandakiri :
            selesai = True
        else :
            temp = A[penandakiri]
            A[penandakiri] = A[penandakanan]
            A[penandakanan] = temp

    temp = A[awal]
    A[awal] = A[penandakanan]
    A[penandakanan] = temp

    return penandakanan

      
mergesort(Daftar)
for i in Daftar:
    print(i)

quicksort(Daftar)
for i in Daftar:
print(i)

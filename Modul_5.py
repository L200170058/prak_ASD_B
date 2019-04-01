

##1
class MhsTIF(object):
    def __init__(self, nama, NIM, alamat,us):
        self.nama = nama
        self.NIM = NIM
        self.alamat = alamat
        self.us = us

    def __str__(self):
        s = self.nama + "NIM" + str(self.NIM)\
            + ". Tinggal di " + self.alamat\
            + ". Uang Saku Rp. " + str(self.us)\
            + " Tiap Bulannya."
        
def swap(A,p,q):
    tmp = A[p]
    A[p] = A[q]
    A[q] = tmp
    
#Nomor1    
Daftar = [MhsTIF('Anom', "L200170071", 'Sukoharjo', 150000),
          MhsTIF('Lutfi', "L200170048", 'Karanganyar', 125000),
          MhsTIF('Gentur', "L200170085", 'Surakarta', 20500),
          MhsTIF('Alvicky', "L200170065", 'Sragen', 350000),
          MhsTIF('Bayu', "L200170052", 'Sragen', 500000),
          MhsTIF('Kori', "L200170053", 'Surakarta', 430000),
          MhsTIF('Susi', "L200170047", 'Bojonegoro', 450000),
          MhsTIF('Rima', "L200170044", 'Klaten', 430000),
          MhsTIF('Sidiq', "L200170058", 'Klaten', 235000),
          MhsTIF('Yoga', "L200170034", 'Karanganyar', 350000)]

def cekNIM(object):
    for i in object:
        print (i.NIM)
         
          
def urutNIM(object):
    n = len(object)
    for i in range(n-1):
        for j in range(n-i-1):
            if object[j].NIM > object[j+1].NIM:
                swap(object,j,j+1)

##2
#Nomer2
list1 = [1,6,7,8,10]
list2 = [2,3,4,5,9]

def gabung(A, B):
    la = len(A)
    lb = len(B)
    c = list()
    i = 0
    j = 0
    while i < la and j < lb:
        if A[i] < B[j]:
            c.append(A[i])
            i += 1
        else:
            c.append(B[j])
            j += 1
    while i < la:
        c.append(A[i])
        i += 1
    while j < lb:
        c.append(B[j])
        j += 1
    return c

## 3

def swap(A,p,q):
    tmp = A[p]
    A[p] = A[q]
    A[q] = tmp

def cariPosisiYangTerkecil(A, dariSini, sampaiSini):
    posisiTerkecil = dariSini
    for i in range(dariSini+1, sampaiSini):
        if A[1] < A[posisiTerkecil]:
            posisiTerkecil = 1
    return posisiTerkecil

def bubbleSort(A):
    n = len(A)
    for i in range(n-1):
        for j in range(n-i-1):
            if A[j] > A[j+1]:
                swap(A,j,j+1)

def selectionSort(A):
    n = len(A)
    for i in range(n-1):
        indexKecil = cariPosisiYangTerkecil(A, i, n)
        if indexKecil != i:
            swap(A, i, indexKecil)

def insertionSort(A):
    n = len(A)
    for i in range(1,n):
        nilai = A[i]
        pos = i
        while pos > 0 and nilai < A[pos-1]:
            A[pos] = A[pos-1]
            pos = pos-1
        A[pos] = nilai
        
#Nomor3
from time import time as detak
from random import shuffle as kocok

k = [i for i in range(1,6001)]
kocok(k)
u_bub = k[:]
u_sel = k[:]
u_ins = k[:]

aw = detak();bubbleSort(u_bub);ak=detak();print("Bubble    : %g detik"%(ak-aw));
aw = detak();selectionSort(u_sel);ak=detak();print("Selection : %g detik"%(ak-aw));
aw = detak();insertionSort(u_ins);ak=detak();print("Insertion : %g detik"%(ak-aw));

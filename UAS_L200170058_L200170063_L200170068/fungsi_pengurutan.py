from data_karyawan import *

def pengurut_nip(A):
        
    if len(A) > 1:
        mid = len(A) // 2
        mid_Kiri = A[:mid]
        mid_Kanan = A[mid:]

        pengurut_nip(mid_Kiri)
        pengurut_nip(mid_Kanan)

        i = 0 ; j = 0 ; k = 0
        while i < len(mid_Kiri) and j < len(mid_Kanan):
            if mid_Kiri[i][0] < mid_Kanan[j][0]:
                A[k] = mid_Kiri[i]
                i += 1
            else:
                A[k] = mid_Kanan[j]
                j += 1
            k += 1

        while i < len(mid_Kiri):
            A[k] = mid_Kiri[i]
            i += 1
            k += 1

        while j < len(mid_Kanan):
            A[k] = mid_Kanan[j]
            j += 1
            k += 1
            
        return A

def pengurut_pegawai(A):
        
    if len(A) > 1:
        mid = len(A) // 2
        mid_Kiri = A[:mid]
        mid_Kanan = A[mid:]

        pengurut_pegawai(mid_Kiri)
        pengurut_pegawai(mid_Kanan)

        i = 0 ; j = 0 ; k = 0
        while i < len(mid_Kiri) and j < len(mid_Kanan):
            if mid_Kiri[i][1] < mid_Kanan[j][1]:
                A[k] = mid_Kiri[i]
                i += 1
            else:
                A[k] = mid_Kanan[j]
                j += 1
            k += 1

        while i < len(mid_Kiri):
            A[k] = mid_Kiri[i]
            i += 1
            k += 1

        while j < len(mid_Kanan):
            A[k] = mid_Kanan[j]
            j += 1
            k += 1
            
        return A

def pengurut_jabatan(A):
        
    if len(A) > 1:
        mid = len(A) // 2
        mid_Kiri = A[:mid]
        mid_Kanan = A[mid:]

        pengurut_jabatan(mid_Kiri)
        pengurut_jabatan(mid_Kanan)

        i = 0 ; j = 0 ; k = 0
        while i < len(mid_Kiri) and j < len(mid_Kanan):
            if mid_Kiri[i][2] < mid_Kanan[j][2]:
                A[k] = mid_Kiri[i]
                i += 1
            else:
                A[k] = mid_Kanan[j]
                j += 1
            k += 1

        while i < len(mid_Kiri):
            A[k] = mid_Kiri[i]
            i += 1
            k += 1

        while j < len(mid_Kanan):
            A[k] = mid_Kanan[j]
            j += 1
            k += 1
            
        return A


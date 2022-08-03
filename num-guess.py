import random
import math

lower = int(input("Angka terkecil : "))
upper = int(input("Angka terbesar : "))
x = random.randint(lower,upper)
print("\nPunya kesempatan sebanyak : ",round(math.log(upper-lower+1,2))," kali")

count = 0
while count < math.log(upper-lower+1,2):
    count+=1

    tebak = int(input("Tebak angka : "))

    if x == tebak:
        print("Congrats kamu berhasil di percobaan ke - ",count)
        break
    elif x < tebak:
        print("Angka terlalu tinggi")
    elif x > tebak:
        print("Angka terkalu kecil")

if count >= math.log(upper-lower+1,2):
    print("Jawabannya adalah : ",x)
    print("Coba Lagi!!")

    
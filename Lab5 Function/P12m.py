''' --------------------------
Do not change anything here 
------------------------------'''
import P12f

''' --------------------------
Put your code for the main part here 
------------------------------'''
if __name__ == "__main__":
    x, y, z = P12f.readInput()
    n1, n2, n3 = P12f.sort(x, y, z)
    # print(n1)
    # print(n2)
    # print(n3)
    print("%.1f <= %.1f <= %.1f" % (n1, n2, n3))
    # จาก P12f ที่เรียงค่าใหม่ n1 => เป็นค่าที่น้อยที่สุด

    
    
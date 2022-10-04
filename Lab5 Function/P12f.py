''' --------------------------
Put your functions here 
------------------------------'''

def readInput():
        number = input("Enter 3 numbers: ").split()
        x, y, z = list(map(float, number))
        return x, y, z

def sort(x, y, z):
        # arrange => จัด, เรียง
        arrange = [x, y, z] # ทำให้เป็น list
        arrange.sort() # .sort => เรียงเลขน้อยไปมาก
        return arrange

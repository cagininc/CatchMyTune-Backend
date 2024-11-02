
num=5
def findNum(num):
    list=[1,2,5,3,5,8,]

    for i in range (len(list)):
        if list[i]==num:
            list[i]=100
    return print (list)

if __name__=="__main__":
    num= int(input("Bir sayı giriniz"))
    result= findNum(num)
    print(result)
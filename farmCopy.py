import tkinter, clipboard

window = tkinter.Tk()
window.title("farm_macro")
window.geometry("580x311")

def letsGo():
    global index
    clipboard.copy(farmList[index])
    index += 1
    print(index)
    print(farmList)
    
def letsDelete():
    global farmList
    if index < 1:
        return
    else:
        farmList.pop(index-1)
        print(farmList)
        f = open('farmlist_신수.txt', 'w', encoding = 'utf-8')
        for farm in farmList:
           f.writelines(farm + '\n')
        f.close()
        
btn_1 = tkinter.Button(window, height=20, width=40, text='Go', command = letsGo).grid(row=0, column=1)
btn_2 = tkinter.Button(window, height=20, width=40, text='Delete', command = letsDelete).grid(row=0, column=2)

f = open('farmlist_신수.txt', 'r', encoding = 'utf-8')
line = f.readline()
index = 0
farmList = []

while line:
    lastWord = line.split()[-1]
    findMult = lastWord.find('*')
    if findMult != -1:
        farmName = lastWord[0:findMult]
    else:
        farmName = lastWord
    farmList.append(farmName)
    line = f.readline()
f.close()
print(farmList)

f = open('farmlist_신수.txt', 'w', encoding = 'utf-8')
for farm in farmList:
    f.writelines(farm + '\n')
f.close()

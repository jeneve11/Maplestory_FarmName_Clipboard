import tkinter, clipboard

window = tkinter.Tk()
window.title("farm_macro")
window.geometry("660x450")

def letsGo():
    global index
    clipboard.copy(farmList[index])
    index += 1

btn = tkinter.Button(window, height=100, width=100, text='', command = letsGo).grid(row=0, column=1)

f = open('farmlist_신수.txt', encoding = 'utf-8')
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
  

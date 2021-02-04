import tkinter, clipboard
# 중복제거 / input 콘솔말고 팝업으로 / 
window = tkinter.Tk()
window.title("farm_macro")
window.geometry("580x333")

entry_1 = tkinter.Entry(window)
entry_1.grid(row=1, column=0, columnspan=2)
entry_2 = tkinter.Entry(window)
entry_2.grid(row=1, column=2, columnspan=2)

def letsGo():
    global index
    clipboard.copy(farmList[index])
    index += 1
    print(farmList[index-1])
    print(farmList)
    entry_1.delete(0, tkinter.END)
    entry_1.insert(0, farmList[index-1])
    entry_2.delete(0, tkinter.END)
    entry_2.insert(0, str(index)+'/'+str(len(farmList)))
    
def letsDelete():
    global farmList, index
    if index < 1:
        return
    else:
        farmList.pop(index-1)
        clipboard.copy(farmList[index-1])
        print(farmList[index-1])
        print(farmList)
        entry_1.delete(0, tkinter.END)
        entry_1.insert(0, farmList[index-1])
        entry_2.delete(0, tkinter.END)
        entry_2.insert(0, str(index)+'/'+str(len(farmList)))
        f = open(file_name, 'w', encoding = 'utf-8')
        for farm in farmList:
           f.writelines(farm + '\n')
        f.close()

btn_1 = tkinter.Button(window, height=20, width=40, text='Next Farm', command = letsGo).grid(row=0, column=1)
btn_2 = tkinter.Button(window, height=20, width=40, text='Next Farm(Delete)', command = letsDelete).grid(row=0, column=2)
        
file_name = input("Input your text file name: ") + '.txt'
f = open(file_name, 'r', encoding = 'utf-8')
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

f = open(file_name, 'w', encoding = 'utf-8')
for farm in farmList:
    f.writelines(farm + '\n')
f.close()

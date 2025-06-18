# Glowfroot Tardigrade

import tkinter as tk
from tkinter import filedialog
import pandas as pd
import pyperclip
import os
from pathlib import Path

root = tk.Tk()
root.title("Tardigrade")
root.iconbitmap(f'{Path(__file__).parent}\Data\Tardigrade.ico')

text = tk.Text(root)
text.grid(row=2, column=0)

label = tk.Text(root, state=tk.NORMAL)
label.grid(row=2, column=1)

def contains_partition(partition, x):
    return x in partition

def append_text(text_1):
    label.config(state=tk.NORMAL)
    label.insert(tk.END, text_1)
    label.config(state=tk.DISABLED)
    
def openfile():
    file_path = filedialog.askopenfilename(
        title="Select a File",
        filetypes=[("CSV files", "*.csv")]
    )
    if file_path:
        pyperclip.copy(f"IMPORT CSV {file_path}")
        append_text(">> Added command to clipboard! \n")

def SubmitCode():
    code = text.get('1.0', "end")
    return code


def add(x, y):
    return x + y

def delete():
    label.delete("1.0", "end")

def ExecCode():
    k = 0
    code = SubmitCode()
    array = {}
    code0 = code.strip().split('\n')
    j = 0
    stack = []
    while j < len(code0):
        code05 = code0[j]
        code1 = code05.split(';')
        i = 0
        while i < len(code1):

            code2 = code1[i]
            code3 = code2.split(' ')
                
            if(code3[0] == "LOOP"):
                if (len(code3) > 5):
                    if(str(code3[4]) == "="):
                        if(int(array[str(code3[3])]) != int(code3[5])):
                            j += 1
                            break
                    if(str(code3[4]) == ">"):
                        if(int(array[str(code3[3])]) < int(code3[5])):
                            j += 1
                            break
                    if(str(code3[4]) == "<"):
                        if(int(array[str(code3[3])]) > int(code3[5])):
                            j += 1
                            break
                    
                if(code3[2] in array):
                    code3[2] = array[code3[2]]

                print("stack is 0")
                
                if not stack or stack[-1]['ID'] != j:
                    print(stack)
                    stack.append({'LINE': code3[1], 'LOOP': code3[2], 'ID': j})
                    
                
                if(int(stack[-1]['LOOP']) > 0):
                    stack[-1]['LOOP'] = int(stack[-1]['LOOP'])
                    stack[-1]['LOOP'] -= 1
                    
                    print(stack[-1]['LOOP'])
                    
                    j = int(stack[-1]['LINE']) - 2
                else:
                    stack.pop()
                    
                    
                
            try:   
                if(code3[0] == "SET"):
                    array[code3[1]] = code3[2]
                elif (code3[0] == "PLUS"):
                    array[str(code3[1])] = float(array.get(str(code3[1]), 0)) + float(code3[2])
                elif (code3[0] == "TIMES"):
                    array[str(code3[1])] = float(array.get(str(code3[1]), 0)) * float(code3[2])
                elif(code3[0] == "PRINT"):
                    append_text(">>")
                    for cd in code3[1:]:
                        if cd in array:
                            append_text(str(array[cd]))
                        else:
                            append_text(str(cd))
                        append_text(" ")
                    append_text(" \n")
                elif(code3[0] == "LIST"):
                    array[code3[1]] = code3[2:]
                elif(code3[0] == "INDEX"):
                    if(code3[3] in array):
                        array[str(code3[1])] = array[code3[2]][int(array[code3[3]])]
                    else:
                        array[str(code3[1])] = array[code3[2]][int(code3[3])]
                elif code3[0] == "IMPORT":
                    if(str(code3[1]) == "CSV"):
                        dict1 = pd.read_csv(str(code3[2]))
                        for _, row in dict1.iterrows():
                            array.update(row.to_dict())
                
                    
                
            except Exception as exc:
                append_text(">>")
                append_text(str(exc))
                append_text("\n")
            
            k += 1;
            i += 1
        j += 1

        

send = tk.Button(root, text="Send over", command=ExecCode)
send.grid(row=0, column=0)

openbutton = tk.Button(root, text="Import CSV", command=openfile)
openbutton.grid(row=3, column=0)

terminalesc = tk.Button(root, text="Clear Terminal", command=delete)
terminalesc.grid(row=3, column=1)

root.mainloop()
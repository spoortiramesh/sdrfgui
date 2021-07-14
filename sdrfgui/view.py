import csv

import pandas as pd
from tkinter import *
from PIL import ImageTk, Image
import tkinter as tk
import glob, os, shutil
from tkinter import filedialog
class View():

    def __init__(self):
        self.secs = ["Default", "Human", "Vertebrates", "Non-vertebrates", "Plants", "Cell lines"]
        self.master = Tk()
        self.master.geometry("800x800")
        self.master.title("Sweet GUI")  # Adding a title
        self.v = StringVar(self.master)
        self.v.set(self.secs[0])
        self.data = []
        self.sourcePath = None


        self.folder_path = StringVar()
        self.lbl1 = Label(self.master,textvariable=self.folder_path)
        self.lbl1.grid(row=0, column=1)

        self.buttonBrowse = Button(text="Browse folder", command=self.browse_button)
        self.buttonBrowse.grid(row=1, column=3)
        Button(self.master, text='Set directory', command=self.set_dir).grid(row=1, column=4, sticky=W, pady=4)

        self.w = OptionMenu(self.master, self.v, *self.secs, command=self.on_option_change)
        self.w.grid(row=1, column=0)

        self.laba = tk.Label(self.master, text='No. of raw files: ')
        self.laba.grid(row=1,column=7,sticky=W)
        self.ent0 = tk.Entry(self.master)
        self.ent0.grid(row=1, column=9)

        self.okbtn = tk.Button(self.master, text='OK',command=self.on_click)
        self.okbtn.grid(row=1, column=10)
        mainloop()


    def next_step(self, entry):
        if entry.get():
            # the user entered data in the mandatory entry: proceed to next step
            instruction_label= Label(self.master, text='Next step')
            instruction_label.grid(row=21, column=0, sticky=E)
            
        else:
            # the mandatory field is empty
            instruction_label = Label(self.master, text="mandatory data missing")
            instruction_label.grid(row=16, column=0, sticky=E)
            entry.focus_set()


    def browse_button(self):
        # Allow user to select a directory and store it in global var
        # called folder_path
        filename = filedialog.askdirectory()
        self.folder_path.set(filename)
        print(filename)

    def set_dir(self):
        self.sourcePath = self.folder_path.get()
        os.chdir(self.sourcePath)  # Provide the path here


    def saveinfo(self):
        valor0=entry0.get()
        valor1 = entry1.get()
        valor2 = entry2.get()
        valor3 = entry3.get()
        valor4 = entry4.get()
        valor5 = entry5.get()
        valor6 = entry6.get()
        valor7 = entry7.get()
        valor8 = entry8.get()
        valor9 = entry9.get()
        valor10 = entry10.get()
        valor11=entry11.get()
        self.data.append([valor0,valor1, valor2, valor3,valor4,valor5,valor6,valor7,valor8,valor9,valor10,valor11])
        print(self.data)    

    def export(self):
        with open('test_sdrf.tsv', 'w', encoding='UTF8') as f:
            list_human=['Source Name','characteristics[organism]','characteristics[organism parts]','characteristics[cell type]','characteristics[developmental stage]','characteristics[disease]','characteristics[sex]','characteristics[individual]','characteristics[cell line]','comment[data file]','comment[fraction identifier]','comment[label]']
            f = pd.DataFrame(self.data,columns=list_human)
            nan_value = float("NaN")
            f.replace("", nan_value, inplace=True)
            f.dropna(how='all', axis=1, inplace=True)
            filename = "sdrf_test.tsv"
            path = os.path.join(self.sourcePath, filename)
            f.to_csv(path,sep="\t")

    def saveinfo_ver(self):
        valor0=entry0.get()
        valor1 = entry1.get()
        valor2 = entry2.get()

        valor3 = entry3.get()
        valor4 = entry4.get()
        valor5 = entry5.get()
        valor6 = entry6.get()
        valor7 = entry7.get()
        valor8 = entry8.get()
        valor9 = entry9.get()
        valor10 = entry10.get()
        valor11=entry11.get()
        valor12=entry12.get()
        valor13=entry13.get()
        valor14=entry14.get()
        valor15=entry15.get()
        valor16=entry16.get()
        valor17=entry17.get()
        valor18 = entry18.get()

        self.data.append([valor0,valor1,valor2,valor3,valor4,valor5,valor6,valor7,valor8,valor9,valor10,valor11,valor12,valor13,valor14,valor15,valor16,valor17,valor18])
        print(self.data)    

    def export_ver(self):
        with open('test_sdrf.tsv', 'w', encoding='UTF8') as f:
            list_v=['Source Name','characteristics[organism]','characteristics[age]','characteristics[developmental stage]','characteristics[sex]','characteristics[disease]','characteristics[organism part]','characteristics[cell type]','technology type','assay name','characteristics[individual]','characteristics[biological replicate]','comment[data file]','comment[technical replicate]','comment[fraction identifier]','comment[label]','comment[cleavage agent details]','comment[instrument]']
            f = pd.DataFrame(self.data,columns=list_v)
            nan_value = float("NaN")
            f.replace("", nan_value, inplace=True)
            f.dropna(how='all', axis=1, inplace=True)
            filename = "sdrf_test.tsv"
            path = os.path.join(self.sourcePath, filename)
            f.to_csv(path,sep="\t")


    def saveinfo_def(self):
        valor0=entry0.get()
        valor1 = entry1.get()
        valor3 = entry3.get()
        valor4 = entry4.get()
        valor5 = entry5.get()
        valor6 = entry6.get()
        valor7 = entry7.get()
        valor8 = entry8.get()
        valor9 = entry9.get()
        valor10 = entry10.get()
        valor11=entry11.get()
        valor12=entry12.get()
        valor13=entry13.get()
        valor14=entry14.get()

        self.data.append([valor0,valor1,  valor3,valor4,valor5,valor6,valor7,valor8,valor9,valor10,valor11,valor12,valor13,valor14])
        print(self.data)    

    def export_def(self):
        with open('test_sdrf.tsv', 'w', encoding='UTF8') as f:
            list_d=['Source Name','characteristics[organism]','characteristics[disease]','characteristics[organism part]','characteristics[cell type]','technology type','assay name','characteristics[biological replicate]','comment[data file]','comment[technical replicate]','comment[fraction identifier]','comment[label]','comment[cleavage agent details]','comment[instrument]']
            f = pd.DataFrame(self.data,columns=list_d)
            nan_value = float("NaN")
            f.replace("", nan_value, inplace=True)
            f.dropna(how='all', axis=1, inplace=True)
            filename = "sdrf_test.tsv"
            path = os.path.join(self.sourcePath, filename)
            f.to_csv(path,sep="\t")

    def saveinfo_plants(self):
        valor0=entry0.get()
        valor1 = entry1.get()
        valor2 = entry2.get()
        valor3 = entry3.get()
        valor4 = entry4.get()
        valor5 = entry5.get()
        valor6 = entry6.get()
        valor7 = entry7.get()
        valor8 = entry8.get()
        valor9 = entry9.get()
        valor10 = entry10.get()
        valor11=entry11.get()
        valor12=entry12.get()
        valor13=entry13.get()
        valor14=entry14.get()
        valor15=entry15.get()
        valor16=entry16.get()
        valor17=entry17.get()
        valor18 = entry18.get()
        valor19 = entry19.get()

        self.data.append([valor0,valor1, valor2, valor3,valor4,valor5,valor6,valor7,valor8,valor9,valor10,valor11,valor12,valor13,valor14,valor15,valor16,valor17,valor18,valor19])
        print(self.data)    

    def export_plants(self):
        with open('test_sdrf.tsv', 'w', encoding='UTF8') as f:
            list_v=['Source Name','characteristics[organism]','characteristics[ecotype/cultivar]','characteristics[age]','characteristics[developmental stage]','characteristics[organism part]','characteristics[cell type]','technology type','assay name','characteristics[individual]','characteristics[biological replicate]','comment[data file]','comment[technical replicate]','comment[fraction identifier]','comment[label]','comment[cleavage agent details]','comment[instrument]']
            f = pd.DataFrame(self.data,columns=list_v)
            nan_value = float("NaN")
            f.replace("", nan_value, inplace=True)
            f.dropna(how='all', axis=1, inplace=True)
            filename = "sdrf_test.tsv"
            path = os.path.join(self.sourcePath, filename)
            f.to_csv(path,sep="\t")

    def on_option_change(self, event):       
        global entry0
        global entry1
        global entry2
        global entry3
        global entry4
        global entry5
        global entry6
        global entry7
        global entry8
        global entry9
        global entry10
        global entry11
        global entry12
        global entry13
        global entry14
        global entry15
        global entry16
        global entry17
        global entry18
        global entry19



        if self.v.get() == 'Human':
                entry0 = tk.Entry(self.master)
                entry0.grid(row=2, column=1)
                lab0 = tk.Label(self.master, text='Source Name')
                
                lab0.grid(row=2, column=0, sticky=E)
                
                entry1 = tk.Entry(self.master)
                entry1.grid(row=3, column=1)
                lab1 = tk.Label(self.master, text='characteristics[organism]')
                lab1.grid(row=3, column=0, sticky=E)
                entry2 = tk.Entry(self.master)
                entry2.grid(row=4, column=1)
                lab2 = tk.Label(self.master, text='characteristics[organism parts]')
                lab2.grid(row=4, column=0, sticky=E)
                entry3 = tk.Entry(self.master)
                entry3.grid(row=5, column=1)
                lab3 = tk.Label(self.master, text='characteristics[cell type]')       
                lab3.grid(row=5,column=0,sticky=E)        
                entry4 = tk.Entry(self.master)
                entry4.grid(row=6, column=1)
                lab4 = tk.Label(self.master, text='characteristics[developmental stage]')
                lab4.grid(row=6, column=0, sticky=E)
                entry5 = tk.Entry(self.master)
                entry5.grid(row=7, column=1)
                lab5 = tk.Label(self.master, text='characteristics[disease]')
                lab5.grid(row=7, column=0, sticky=E)
                entry6 = tk.Entry(self.master)
                entry6.grid(row=8, column=1)
                lab6 = tk.Label(self.master, text='characteristics[sex]')
                lab6.grid(row=8, column=0, sticky=E)
                entry7 = tk.Entry(self.master)
                entry7.grid(row=9, column=1)
                lab7 = tk.Label(self.master, text='characteristics[individual]')
                lab7.grid(row=9, column=0, sticky=E)
                entry8 = tk.Entry(self.master)
                entry8.grid(row=10, column=1)    
                lab8=tk.Label(self.master, text='characteristics[cell line]')
                lab8.grid(row=10, column=0, sticky=E)
                
                entry9 = tk.Entry(self.master)
                entry9.grid(row=11, column=1)
                lab9 = tk.Label(self.master, text='comment[data file]')
                lab9.grid(row=11, column=0, sticky=E)
                entry10 = tk.Entry(self.master)
                entry10.grid(row=12, column=1)
                lab10 = tk.Label(self.master, text='comment[fraction identifier]')
                lab10.grid(row=12, column=0, sticky=E)
                entry11 = tk.Entry(self.master)
                entry11.grid(row=13, column=1)
                lab11 = tk.Label(self.master, text='comment[label]')       
                lab11.grid(row=13,column=0,sticky=E)
            
                button1 = tk.Button(text='Save',command=self.saveinfo)
                button1.grid(row=20, column=1, sticky=W)
                button2 = tk.Button(text='Export as .tsv', command=self.export)
                button2.grid(row=20, column=2, sticky=W)

            
        elif self.v.get() == 'Vertebrates':
            entry0 = tk.Entry(self.master)
            entry0.grid(row=2, column=1)
            lab0 = tk.Label(self.master, text='Source Name (*):')
            nxtbt0 = tk.Button(self.master, text='OK', command=lambda : self.next_step(entry0))
            lab0.grid(row=2, column=0, sticky=E)
            
            entry1 = tk.Entry(self.master)
            entry1.grid(row=3, column=1)
            lab1 = tk.Label(self.master, text='characteristics[organism] (*): ')
            nxtbt1 = tk.Button(self.master, text='OK', command=lambda: self.next_step(entry0))
            lab1.grid(row=3, column=0, sticky=E)
            
            
            entry2 = tk.Entry(self.master)
            entry2.grid(row=4, column=1)
            lab2 = tk.Label(self.master, text='characteristics[age]')
            lab2.grid(row=4, column=0, sticky=E)
            
            entry5 = tk.Entry(self.master)
            entry5.grid(row=5, column=1)
            lab5 = tk.Label(self.master, text='characteristics[developmental stage]')        
            lab5.grid(row=5,column=0,sticky=E)     
            
            entry6 = tk.Entry(self.master)
            entry6.grid(row=6, column=1)
            lab6 = tk.Label(self.master, text='characteristics[sex]')
            lab6.grid(row=6, column=0, sticky=E)
            
            entry7 = tk.Entry(self.master)
            entry7.grid(row=7, column=1)
            lab7 = tk.Label(self.master, text='characteristics[disease] (*):')
            nxtbt7 = tk.Button(self.master, text='OK', command=lambda: self.next_step(entry0))
            lab7.grid(row=7, column=0, sticky=E)
            
            entry8 = tk.Entry(self.master)
            entry8.grid(row=10, column=1)
            lab8 = tk.Label(self.master, text='characteristics[organism part] (*):')
            nxtbt8 = tk.Button(self.master, text='OK', command=lambda: self.next_step(entry0))
            lab8.grid(row=10, column=0, sticky=E)
            
            
        
            entry9 = tk.Entry(self.master)
            entry9.grid(row=11, column=1)
            lab9 = tk.Label(self.master, text='characteristics[cell type]:')
            lab9.grid(row=11, column=0, sticky=E)
            
            entry10 = tk.Entry(self.master)
            entry10.grid(row=12, column=1)
            nxtbt10 = tk.Button(self.master, text='OK', command=lambda: self.next_step(entry0))
            lab10 = tk.Label(self.master, text='technology type] (*):')
            lab10.grid(row=12, column=0, sticky=E)        
            
            entry11 = tk.Entry(self.master)
            entry11.grid(row=13, column=1)
            lab11 = tk.Label(self.master, text='assay name')
            lab11.grid(row=13, column=0, sticky=E)
            
            
            
            entry12 = tk.Entry(self.master)
            entry12.grid(row=14, column=1)
            lab12 = tk.Label(self.master, text='characteristics[individual]')
            lab12.grid(row=14, column=0, sticky=E)
            
        
            
            entry13 = tk.Entry(self.master)
            entry13.grid(row=15, column=1)
            lab13 = tk.Label(self.master, text='characteristics[biological replicate] (*):')    
            nxtbt13= tk.Button(self.master, text='OK', command=lambda: self.next_step(entry0))
            lab13.grid(row=15,column=0,sticky=E)
            
            entry14 = tk.Entry(self.master)
            entry14.grid(row=16, column=1)
            lab14 = tk.Label(self.master, text='comment[data file] (*):')  
            nxtbt14 = tk.Button(self.master, text='OK', command=lambda: self.next_step(entry0))
            lab14.grid(row=16,column=0,sticky=E)  
            
            entry15 = tk.Entry(self.master)
            entry15.grid(row=17, column=1)
            lab15 = tk.Label(self.master, text='comment[technical replicate] (*):')  
            nxtbt15 = tk.Button(self.master, text='OK', command=lambda: self.next_step(entry0))
            lab15.grid(row=17,column=0,sticky=E)   
            
            entry16 = tk.Entry(self.master)
            entry16.grid(row=18, column=1)
            lab16 = tk.Label(self.master, text='comment[fraction identifier] (*):')  
            nxtbt16 = tk.Button(self.master, text='OK', command=lambda: self.next_step(entry0))
            lab16.grid(row=18,column=0,sticky=E)  
            
            entry17 = tk.Entry(self.master)
            entry17.grid(row=19, column=1)
            lab17 = tk.Label(self.master, text='comment[label] (*):')  
            nxtbt17 = tk.Button(self.master, text='OK', command=lambda: self.next_step(entry0))
            lab17.grid(row=19,column=0,sticky=E)   
            
            entry18 = tk.Entry(self.master)
            entry18.grid(row=20, column=1)        
            lab18= tk.Label(self.master, text='comment[cleavage agent details] (*):')    
            nxtbt18 = tk.Button(self.master, text='OK', command=lambda: self.next_step(entry0))
            lab18.grid(row=20,column=0,sticky=E)   
            
            entry19 = tk.Entry(self.master)
            entry19.grid(row=21, column=1)        
            lab19 = tk.Label(self.master, text='comment[instrument] (*):')      
            nxtbt19 = tk.Button(self.master, text='OK', command=lambda: self.next_step(entry0))
            lab19.grid(row=21,column=0,sticky=E)    
        
            button1 = tk.Button(text='Save',command=self.saveinfo_ver)
            button1.grid(row=22, column=1, sticky=W)
            button2 = tk.Button(text='Export as .tsv', command=self.export_ver)
            button2.grid(row=22, column=2, sticky=W)

            
        elif self.v.get() == 'Default':
            entry0 = tk.Entry(self.master)
            entry0.grid(row=2, column=1)
            lab0 = tk.Label(self.master, text='Source Name (*) :')
            nxtbt0 = tk.Button(self.master, text='OK', command=lambda: self.next_step(entry0))
            lab0.grid(row=2, column=0, sticky=E)
            
            entry1 = tk.Entry(self.master)
            entry1.grid(row=3, column=1)
            lab1 = tk.Label(self.master, text='characteristics[organism] (*) :')
            nxtbt1 = tk.Button(self.master, text='OK', command=lambda: self.next_step(entry0))
            nxtbt11=tk.Button(self.master, text='OK', command=lambda: self.next_step(entry0))
            lab1.grid(row=3, column=0, sticky=E)
                    
            entry3 = tk.Entry(self.master)
            entry3.grid(row=5, column=1)
            lab3 = tk.Label(self.master, text='characteristics[disease] (*):')    
            nxtbt3= tk.Button(self.master, text='OK', command=lambda: self.next_step(entry0))
            lab3.grid(row=5,column=0,sticky=E) 
            
            entry4 = tk.Entry(self.master)
            entry4.grid(row=6, column=1)
            lab4 = tk.Label(self.master, text='characteristics[organism part] (*)')
            nxtbt4= tk.Button(self.master, text='OK', command=lambda: self.next_step(entry0))
            lab4.grid(row=6, column=0, sticky=E)
            
            entry5 = tk.Entry(self.master)
            entry5.grid(row=7, column=1)
            lab5 = tk.Label(self.master, text='characteristics[cell type] (*):')
            nxtbt5= tk.Button(self.master, text='OK', command=lambda: self.next_step(entry0))
            lab5.grid(row=7, column=0, sticky=E)
            
            entry6 = tk.Entry(self.master)
            entry6.grid(row=8, column=1)
            lab6 = tk.Label(self.master, text='technology type (*)')
            nxtbt6= tk.Button(self.master, text='OK', command=lambda: self.next_step(entry0))
            lab6.grid(row=8, column=0, sticky=E)
            
            
            entry7 = tk.Entry(self.master)
            entry7.grid(row=9, column=1)
            lab7 = tk.Label(self.master, text='assay name')
            lab7.grid(row=9, column=0, sticky=E)
            
            
            entry8 = tk.Entry(self.master)
            entry8.grid(row=10, column=1)
            lab8= tk.Label(self.master, text='characteristics[biological replicate] (*):')    
            nxtbt8= tk.Button(self.master, text='OK', command=lambda: self.next_step(entry0))
            lab8.grid(row=10,column=0,sticky=E)
            
            entry9 = tk.Entry(self.master)
            entry9.grid(row=11, column=1)
            lab9= tk.Label(self.master, text='comment[data file] (*):')  
            nxtbt9= tk.Button(self.master, text='OK', command=lambda: self.next_step(entry0))
            lab9.grid(row=11,column=0,sticky=E)  
            
            entry10 = tk.Entry(self.master)
            entry10.grid(row=12, column=1)
            lab10 = tk.Label(self.master, text='comment[technical replicate] (*):')  
            nxtbt10 = tk.Button(self.master, text='OK', command=lambda: self.next_step(entry0))
            lab10.grid(row=12,column=0,sticky=E)   
            
            entry11 = tk.Entry(self.master)
            entry11.grid(row=13, column=1)
            lab11 = tk.Label(self.master, text='comment[fraction identifier] (*):')  
            nxtbt11 = tk.Button(self.master, text='OK', command=lambda: self.next_step(entry0))
            lab11.grid(row=13,column=0,sticky=E)  
            
            entry12 = tk.Entry(self.master)
            entry12.grid(row=14, column=1)
            lab12 = tk.Label(self.master, text='comment[label] (*):')  
            nxtbt12 = tk.Button(self.master, text='OK', command=lambda: self.next_step(entry0))
            lab12.grid(row=14,column=0,sticky=E)   
            
            entry13 = tk.Entry(self.master)
            entry13.grid(row=15, column=1)        
            lab13= tk.Label(self.master, text='comment[cleavage agent details] (*):')    
            nxtbt13 = tk.Button(self.master, text='OK', command=lambda: self.next_step(entry0))
            lab13.grid(row=15,column=0,sticky=E)   
            
            entry14 = tk.Entry(self.master)
            entry14.grid(row=16, column=1)        
            lab14 = tk.Label(self.master, text='comment[instrument] (*):')      
            nxtbt14 = tk.Button(self.master, text='OK', command=lambda: self.next_step(entry0))
            lab14.grid(row=16,column=0,sticky=E)    
            
            button1 = tk.Button(text='Save',command=self.saveinfo_def)
            button1.grid(row=17, column=1, sticky=W)
            button2 = tk.Button(text='Export as .tsv', command=self.export_def)
            button2.grid(row=17, column=2, sticky=W)
            
        elif self.v.get() == 'Plants':
            entry0 = tk.Entry(self.master)
            entry0.grid(row=2, column=1)
            lab0 = tk.Label(self.master, text='Source Name(*): ')
            nxtbt0 = tk.Button(self.master, text='OK', command=lambda: self.next_step(entry0))
            lab0.grid(row=2, column=0, sticky=E)

            entry1 = tk.Entry(self.master)
            entry1.grid(row=3, column=1)
            lab1 = tk.Label(self.master, text='characteristics[organism](*): ')
            nxtbt1 = tk.Button(self.master, text='OK', command=lambda: self.next_step(entry0))
            lab1.grid(row=3, column=0, sticky=E)

            
            entry2 = tk.Entry(self.master)
            entry2.grid(row=4, column=1)
            lab2 = tk.Label(self.master, text='characteristics[ecotype/cultivar] :')
            entry2 = tk.Entry(self.master)
            entry2.grid(row=4, column=1)

            entry3 = tk.Entry(self.master)
            entry3.grid(row=5, column=1)
            lab3 = tk.Label(self.master, text='characteristics[age] : ')
            lab3.grid(row=5, column=0, sticky=E)

            entry4 = tk.Entry(self.master)
            entry4.grid(row=6, column=1)
            lab4 = tk.Label(self.master, text='characteristics[developmental stage] : ')
            lab4.grid(row=6, column=0, sticky=E)

            entry5 = tk.Entry(self.master)
            entry5.grid(row=7, column=1)
            lab5 = tk.Label(self.master, text='characteristics[organism part](*): ')
            nxtbt5 = tk.Button(self.master, text='OK', command=lambda: self.next_step(entry0))
            lab5.grid(row=7, column=0, sticky=E)

            entry6 = tk.Entry(self.master)
            entry6.grid(row=8, column=1)
            lab6 = tk.Label(self.master, text='characteristics[cell type] (*): ')
            nxtbt6 = tk.Button(self.master, text='OK', command=lambda: self.next_step(entry0))

            lab6.grid(row=8, column=0, sticky=E)
            
            entry7 = tk.Entry(self.master)
            entry7.grid(row=9, column=1)
            lab7 = tk.Label(self.master, text='technology type (*) : ')
            nxtbt7 = tk.Button(self.master, text='OK', command=lambda: self.next_step(entry0))

            lab7.grid(row=9, column=0, sticky=E)
            
            
            entry8 = tk.Entry(self.master)
            entry8.grid(row=10, column=1)
            lab8 = tk.Label(self.master, text='assay name: ')
            lab8.grid(row=10, column=0, sticky=E)
            
            

            entry9 = tk.Entry(self.master)
            entry9.grid(row=11, column=1)
            lab9 = tk.Label(self.master, text='characteristics[individual]: ')
            lab9.grid(row=11, column=0, sticky=E)

            entry10 = tk.Entry(self.master)
            entry10.grid(row=12, column=1)
            lab10= tk.Label(self.master, text='characteristics[biological replicate](*): ')
            nxtbt10 = tk.Button(self.master, text='OK', command=lambda: self.next_step(entry0))

            lab10.grid(row=12, column=0, sticky=E)

            entry11 = tk.Entry(self.master)
            entry11.grid(row=13, column=1)
            lab11 = tk.Label(self.master, text='comment[data file](*): ')
            nxtbt11 = tk.Button(self.master, text='OK', command=lambda: self.next_step(entry0))

            lab11.grid(row=13, column=0, sticky=E)

            entry12 = tk.Entry(self.master)
            entry12.grid(row=14, column=1)
            lab12 = tk.Label(self.master, text='comment[technical replicate](*): ')
            lab12.grid(row=14, column=0, sticky=E)

            entry13 = tk.Entry(self.master)
            entry13.grid(row=15, column=1)
            lab13 = tk.Label(self.master, text='comment[fraction identifier](*): ')
            lab13.grid(row=15, column=0, sticky=E)

            entry14 = tk.Entry(self.master)
            entry14.grid(row=16, column=1)
            lab14 = tk.Label(self.master, text='comment[label](*): ')
            lab14.grid(row=16, column=0, sticky=E)

            entry15 = tk.Entry(self.master)
            entry15.grid(row=17, column=1)
            lab15 = tk.Label(self.master, text='comment[cleavage agent details](*): ')
            lab15.grid(row=17, column=0, sticky=E)

            entry16 = tk.Entry(self.master)
            entry16.grid(row=18, column=1)
            lab16 = tk.Label(self.master, text='comment[instrument](*): ')
            lab16.grid(row=18, column=0, sticky=E)
            
            button1 = tk.Button(text='Save',command=self.saveinfo_plants)
            button1.grid(row=19, column=1, sticky=W)
            button2 = tk.Button(text='Export as .tsv', command=self.export_plants)
            button2.grid(row=19, column=2, sticky=W)
        


            
        

    
        #lab2 = tk.Label(self.master, text=secs[0])
        #lab2.grid(row=2, column=1, sticky=W)

    def on_click(self):
        num = self.ent0.get()
        if num.isdigit():
            numl= tk.Label(self.master, text=num)
            numl.grid(row=1,column=8)
            self.ent0.destroy()
            self.okbtn.destroy()


        else:
            numno = tk.Label(self.master, text='Enter valid number')
            numno.grid(row=1, column=6)



View()
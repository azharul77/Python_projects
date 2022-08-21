import tkinter
from tkinter.constants import END
import tkinter.messagebox
from typing import Text
import pickle

root = tkinter.Tk()
root.title("Todo list of Azharul")

#function for tex show in listbox
def add_task():
    task = text_entry_task.get()
    if task != "":
        listbox_tasks.insert(tkinter.END, task)
        text_entry_task.delete(0, tkinter.END)
    else:
        tkinter.messagebox.showwarning(title="Warning!", message="You must enter a task..")    

def delete_task():
    try:
        task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(task_index)
    except:
         tkinter.messagebox.showwarning(title="Warning!", message="You must select a task..")  

def load_tasks():
    try:
       tasks = pickle.load(open("task.dat", "rb"))
       listbox_tasks.delete(0, tkinter.END)
       for task in tasks:
          listbox_tasks.insert(tkinter.END, task)

    except:
          tkinter.messagebox.showwarning(title="Warning!", message="Can't find task.dat..")       


def save_tasks():
    tasks = listbox_tasks.get(0, listbox_tasks.size())
    pickle.dump(tasks, open("task.dat", "wb"))

#Create Gui
frame_tasks = tkinter.Frame(root)
frame_tasks.pack()

listbox_tasks = tkinter.Listbox(frame_tasks, height=12, width=50)
listbox_tasks.pack()

scrollbar_tasks = tkinter.Scrollbar(frame_tasks)
scrollbar_tasks.pack(side=tkinter.RIGHT)

text_entry_task = tkinter.Entry(root, width=50)
text_entry_task.pack()


#All Buttons Of Todo List
button_add_task = tkinter.Button(root, text="Add Task", width=48, command=add_task)
button_add_task.pack()

button_delete_task = tkinter.Button(root, text="Delete Task", width=48, command=delete_task)
button_delete_task.pack()

button_load_tasks = tkinter.Button(root, text="Load Tasks", width=48, command=load_tasks)
button_load_tasks.pack()

button_save_tasks = tkinter.Button(root, text="Save Tasks", width=48, command=save_tasks)
button_save_tasks.pack()



root.mainloop()
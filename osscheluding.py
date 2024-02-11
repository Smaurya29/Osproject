import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
def calculate_fcfs():
    processes = int(processes_entry_fcfs.get())
    arrival_times = list(map(int, arrival_entry_fcfs.get().split()))
    burst_times = list(map(int, burst_entry_fcfs.get().split()))

    waiting_time = [0] * processes
    turnaround_time = [0] * processes
    waiting_time[0] = 0
    turnaround_time[0] = burst_times[0]
    for i in range(1, processes):
        waiting_time[i] = waiting_time[i - 1] + burst_times[i - 1]
        turnaround_time[i] = waiting_time[i] + burst_times[i]
        avg_waiting_time_fcfs = sum(waiting_time) / processes
        avg_turnaround_time_fcfs = sum(turnaround_time) / processes
    for i in range(processes):
        fcfs_tree.insert("", "end", values=(i + 1, arrival_times[i], burst_times[i], waiting_time[i], turnaround_time[i]))
        avg_turnaround_label_fcfs.config(text=f"Average Turnaround Time: {avg_turnaround_time_fcfs:.2f}")
        avg_waiting_label_fcfs.config(text=f"Average Waiting Time: {avg_waiting_time_fcfs:.2f}")
        generate_gantt_chart("FCFS", processes, arrival_times, burst_times)

def calculate_sjf():
    processes = int(processes_entry_sjf.get())
    arrival_times = list(map(int, arrival_entry_sjf.get().split()))
    burst_times = list(map(int, burst_entry_sjf.get().split()))

    waiting_time = [0] * processes
    turnaround_time = [0] * processes
    processes_info = list(zip(range(1, processes + 1), arrival_times, burst_times))
    processes_info.sort(key=lambda x: x[1])  # Sort by arrival time

    current_time = 0

    for i in range(processes):
        current_process, arrival_time, burst_time = processes_info[i]
        if arrival_time > current_time:
            current_time = arrival_time
        waiting_time[current_process - 1] = current_time - arrival_time
        turnaround_time[current_process - 1] = waiting_time[current_process - 1] + burst_time
        current_time += burst_time

    
    avg_turnaround_time_sjf = sum(turnaround_time) / processes
    avg_waiting_time_sjf = sum(waiting_time) / processes
    for i in range(processes):
        sjf_tree.insert("", "end", values=(i + 1, arrival_times[i], burst_times[i], waiting_time[i], turnaround_time[i]))

    
    avg_turnaround_label_sjf.config(text=f"Average Turnaround Time: {avg_turnaround_time_sjf:.2f}")
    avg_waiting_label_sjf.config(text=f"Average Waiting Time: {avg_waiting_time_sjf:.2f}")
    generate_gantt_chartt("SJF", processes, arrival_times, burst_times)

def generate_gantt_chart(algorithm, processes, arrival_times, burst_times):
    gantt_chart_window = tk.Toplevel(root)
    gantt_chart_window.title(f"{algorithm} Gantt Chart")

    canvas = tk.Canvas(gantt_chart_window, width=600, height=200)
    canvas.pack()

    x = 10
    for i in range(processes):
        canvas.create_rectangle(x, 50, x + burst_times[i] * 10, 150, fill='yellow')
        canvas.create_text(x + burst_times[i] * 10 // 2, 175, text=f"P{i + 1}", font=("Helvetica", 12))
        x += burst_times[i] * 10
        
def generate_gantt_chartt(algorithm, processes, arrival_times, burst_times):
    gantt_chart_window = tk.Toplevel(root)
    gantt_chart_window.title(f"{algorithm} Gantt Chart")

    canvas = tk.Canvas(gantt_chart_window, width=600, height=200)
    canvas.pack()

    x = 10
    for i in range(processes):
        canvas.create_rectangle(x, 50, x + burst_times[i] * 10, 150, fill='blue')
        canvas.create_text(x + burst_times[i] * 10 // 2, 175, text=f"P{i + 1}", font=("Helvetica", 12))
        x += burst_times[i] * 10
root = tk.Tk()
root.title("Scheduling Algorithm Simulator")


fcfs_label = tk.Label(root, text="FCFS Scheduling Algorithm")
fcfs_label.pack()

processes_label_fcfs = tk.Label(root, text="Number of Processes:")
processes_label_fcfs.pack()

processes_entry_fcfs = tk.Entry(root)
processes_entry_fcfs.pack()

arrival_label_fcfs = tk.Label(root, text="Arrival Time (space-separated):")
arrival_label_fcfs.pack()

arrival_entry_fcfs = tk.Entry(root)
arrival_entry_fcfs.pack()

burst_label_fcfs = tk.Label(root, text="Burst Time (space-separated):")
burst_label_fcfs.pack()

burst_entry_fcfs = tk.Entry(root)
burst_entry_fcfs.pack()

calculate_button_fcfs = tk.Button(root, text="Calculate FCFS", command=calculate_fcfs)
calculate_button_fcfs.pack()
columns_fcfs = ("Process", "Arrival Time", "Burst Time", "Waiting Time", "Turnaround Time")
fcfs_tree = ttk.Treeview(root, columns=columns_fcfs, show="headings")
for col in columns_fcfs:
    fcfs_tree.heading(col, text=col)
    fcfs_tree.column(col, width=165)
fcfs_tree.pack()
avg_waiting_label_fcfs = tk.Label(root, text="")
avg_waiting_label_fcfs.pack()

avg_turnaround_label_fcfs = tk.Label(root, text="")
avg_turnaround_label_fcfs.pack()

separator_fcfs = ttk.Separator(root, orient='horizontal')
separator_fcfs.pack(fill='x', pady=15)
sjf_label = tk.Label(root, text="SJF Scheduling Algorithm")
sjf_label.pack()

processes_label_sjf = tk.Label(root, text="Number of Processes:")
processes_label_sjf.pack()

processes_entry_sjf = tk.Entry(root)
processes_entry_sjf.pack()

arrival_label_sjf = tk.Label(root, text="Arrival Time (space-separated):")
arrival_label_sjf.pack()

arrival_entry_sjf = tk.Entry(root)
arrival_entry_sjf.pack()

burst_label_sjf = tk.Label(root, text="Burst Time (space-separated):")
burst_label_sjf.pack()

burst_entry_sjf = tk.Entry(root)
burst_entry_sjf.pack()

calculate_button_sjf = tk.Button(root, text="Calculate SJF", command=calculate_sjf)
calculate_button_sjf.pack()

avg_waiting_label_sjf = tk.Label(root, text="")
avg_waiting_label_sjf.pack()

avg_turnaround_label_sjf = tk.Label(root, text="")
avg_turnaround_label_sjf.pack()
columns_sjf = ("Process", "Arrival Time", "Burst Time", "Waiting Time", "Turnaround Time")
sjf_tree = ttk.Treeview(root, column=columns_sjf, show="headings")
for col in columns_sjf:
    sjf_tree.heading(col, text=col)
    sjf_tree.column(col, width=165)
sjf_tree.pack()
root.mainloop()

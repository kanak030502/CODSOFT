import tkinter as tk
from tkinter import messagebox, ttk

# Store contacts in memory as a list of dictionaries
contacts = []

def add_contact():
    name = name_entry.get().strip()
    phone = phone_entry.get().strip()
    email = email_entry.get().strip()

    if name and phone:
        contacts.append({"Name": name, "Phone": phone, "Email": email})
        update_contact_list()
        name_entry.delete(0, tk.END)
        phone_entry.delete(0, tk.END)
        email_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Missing Info", "Name and Phone are required.")

def update_contact_list(filtered=None):
    for i in contact_tree.get_children():
        contact_tree.delete(i)
    data = filtered if filtered else contacts
    for contact in data:
        contact_tree.insert("", "end", values=(contact["Name"], contact["Phone"], contact["Email"]))

def search_contact():
    keyword = search_entry.get().strip().lower()
    filtered = [c for c in contacts if keyword in c["Name"].lower()]
    update_contact_list(filtered)

def delete_contact():
    selected = contact_tree.selection()
    if not selected:
        messagebox.showwarning("No Selection", "Please select a contact to delete.")
        return
    values = contact_tree.item(selected[0])["values"]
    for c in contacts:
        if c["Name"] == values[0] and c["Phone"] == values[1]:
            contacts.remove(c)
            break
    update_contact_list()

# GUI Setup
root = tk.Tk()
root.title("Contact Book")
root.geometry("500x500")
root.resizable(False, False)

# Input Frame
frame = tk.Frame(root)
frame.pack(pady=10)

tk.Label(frame, text="Name").grid(row=0, column=0)
name_entry = tk.Entry(frame)
name_entry.grid(row=0, column=1)

tk.Label(frame, text="Phone").grid(row=1, column=0)
phone_entry = tk.Entry(frame)
phone_entry.grid(row=1, column=1)

tk.Label(frame, text="Email").grid(row=2, column=0)
email_entry = tk.Entry(frame)
email_entry.grid(row=2, column=1)

tk.Button(frame, text="Add Contact", command=add_contact).grid(row=3, columnspan=2, pady=5)

# Search Frame
search_frame = tk.Frame(root)
search_frame.pack(pady=5)
tk.Label(search_frame, text="Search by Name").pack(side=tk.LEFT)
search_entry = tk.Entry(search_frame)
search_entry.pack(side=tk.LEFT)
tk.Button(search_frame, text="Search", command=search_contact).pack(side=tk.LEFT)

# Contact List
columns = ("Name", "Phone", "Email")
contact_tree = ttk.Treeview(root, columns=columns, show="headings")
for col in columns:
    contact_tree.heading(col, text=col)
contact_tree.pack(expand=True, fill="both", padx=10, pady=10)

# Delete Button
tk.Button(root, text="Delete Contact", command=delete_contact).pack(pady=5)

root.mainloop()
1
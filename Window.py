import tkinter as tk
from tkinter import messagebox 
from tkinter import filedialog 
from Contact import Contact
import csv

class Window:
    contacts = []

    fields = [
    ("Name", "name"),
    ("Mobile Phone", "mobilePhone"),
    ("Company Name", "companyName"),
    ("Company Occupation", "companyOccupation"),
    ("Company Address", "companyAddress"),
    ("Company Web Page", "companyWebPage"),
    ("Mobile Phone 2", "phone2"),
    ("Mobile Phone 3", "phone3"),
    ("Home Phone", "homePhone"),
    ("Office Phone", "officePhone"),
    ("Private Email 1", "privateEmail1"),
    ("Private Email 2", "privateEmail2"),
    ("Office Email", "officeEmail"),
    ("Address", "address"),
    ("Birthday", "birthDay"),
    ("Notes", "notes"),
    ("Child Name", "childName"),
    ("Child Birthday", "childBirthDay"),
    ("Child Notes", "childNotes")
    ]

    def __init__(self, master):
        self.master = master
        self.setup_ui()
    
    def import_contact_list(self):
        try:
            file_path = filedialog.askopenfilename(
                title="Open Contact List",
                filetypes=[("CSV files", "*.csv"), ("All files", "*.*")]
            )
            if not file_path:
                return  # user cancelled

            with open(file_path, newline='', encoding="utf-8") as csvfile:
                reader = csv.DictReader(csvfile)

                for row in reader:
                    contact = Contact(
                        name=row.get("Name", ""),
                        mobilePhone=row.get("Mobile Phone", ""),
                        companyName=row.get("Company Name", ""),
                        companyOccupation=row.get("Company Occupation", ""),
                        companyAddress=row.get("Company Address", ""),
                        companyWebPage=row.get("Company Web Page", ""),
                        phone2=row.get("Mobile Phone 2", ""),
                        phone3=row.get("Mobile Phone 3", ""),
                        homePhone=row.get("Home Phone", ""),
                        officePhone=row.get("Office Phone", ""),
                        privateEmail1=row.get("Private Email 1", ""),
                        privateEmail2=row.get("Private Email 2", ""),
                        officeEmail=row.get("Office Email", ""),
                        address=row.get("Address", ""),
                        birthDay=row.get("Birthday", ""),
                        notes=row.get("Notes", ""),
                        childName=row.get("Child Name", ""),
                        childBirthDay=row.get("Child Birthday", ""),
                        childNotes=row.get("Child Notes", "")
                    )
                    self.contacts.append(contact)
                    self.contact_list.insert(tk.END, contact.name)

            messagebox.showinfo("Import Successful", "Contacts imported successfully.")

        except Exception as e:
            messagebox.showerror("Import Error", f"An error occurred while importing:\n{str(e)}")
    
    def export_contact_list(self):
        try:
            with open("contactList.csv", "w", newline='', encoding="utf-8") as csvfile:
                writer = csv.writer(csvfile)

                # Write header row
                writer.writerow([
                    "Name", "Mobile Phone", "Company Name", "Company Occupation", "Company Address", "Company Web Page",
                    "Mobile Phone 2", "Mobile Phone 3", "Home Phone", "Office Phone",
                    "Private Email 1", "Private Email 2", "Office Email",
                    "Address", "Birthday", "Notes",
                    "Child Name", "Child Birthday", "Child Notes"
                ])

                # Write each contact's data
                for contact in self.contacts:
                    writer.writerow([
                        contact.name, contact.mobilePhone, contact.companyName, contact.companyOccupation,
                        contact.companyAddress, contact.companyWebPage,
                        contact.phone2, contact.phone3, contact.homePhone, contact.officePhone,
                        contact.privateEmail1, contact.privateEmail2, contact.officeEmail,
                        contact.address, contact.birthDay, contact.notes,
                        contact.childName, contact.childBirthDay, contact.childNotes
                    ])

            messagebox.showinfo("Export Successful", "Contacts were exported to contactList.csv")
        except Exception as e:
            messagebox.showerror("Export Error", f"An error occurred while exporting:\n{str(e)}")

    def exit_program(self):
        self.master.destroy()
    
    def setup_ui(self):
        menu = tk.Menu(self.master)
        self.master.config(menu=menu)

        file_menu = tk.Menu(menu, font=("Arial", 10))

        file_menu.add_command(label="Import contact list", command=self.import_contact_list)
        file_menu.add_command(label="Export contact list", command=self.export_contact_list)

        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.exit_program)
        menu.add_cascade(label="File", menu=file_menu)
        
        self.label = tk.Label(self.master, text="Welcome to Contact Book!", font=("Arial", 16))
        self.label.pack(pady=20)

        self.contact_list = tk.Listbox(self.master)
        self.contact_list.pack(side=tk.LEFT, fill=tk.BOTH, expand=tk.TRUE)

        self.contact_list.bind("<Double-Button-1>", self.show_contact_details)

        scrollbar = tk.Scrollbar(self.master)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.contact_list.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.contact_list.yview)
        
        self.button = tk.Button(self.master, text="Add Contact", command=self.add_contact_popup, width=15)
        self.button.pack(padx=5)
        
        self.button = tk.Button(self.master, text="Edit Contact", command=self.edit_contact_popup, width=15)
        self.button.pack(padx=5)
        
        self.button = tk.Button(self.master, text="Delete Contact", command=self.delete_contact_popup, width=15)
        self.button.pack(padx=5)

    def add_contact_popup(self):
        self.popup = tk.Toplevel(self.master)
        self.popup.title("Add New Contact")
        self.popup.geometry("400x700")

        # Canvas and Scrollbar
        canvas = tk.Canvas(self.popup)
        popup_scrollbar = tk.Scrollbar(self.popup, orient="vertical", command=canvas.yview)
        scroll_frame = tk.Frame(canvas)

        scroll_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=scroll_frame, anchor="nw")
        canvas.configure(yscrollcommand=popup_scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        popup_scrollbar.pack(side="right", fill="y")

        self.entries = {}
        for label_text, field_id in self.fields:
            label = tk.Label(scroll_frame, text=label_text + ":")
            label.pack(pady=1)
            entry = tk.Entry(scroll_frame, width=50)
            entry.pack(pady=2, padx=30)
            self.entries[field_id] = entry  # use field_id as the key

        submit_btn = tk.Button(scroll_frame, text="Save Contact", command=self.save_contact)
        submit_btn.pack(pady=10)

    def edit_contact_popup(self):
        self.popup = tk.Toplevel(self.master)
        self.popup.title("Edit contact")
        self.popup.geometry("400x700")
        
        selection = self.contact_list.curselection()
        if not selection:
            return

        index = selection[0]
        contact = self.contacts[index]

        # Canvas and Scrollbar
        canvas = tk.Canvas(self.popup)
        popup_scrollbar = tk.Scrollbar(self.popup, orient="vertical", command=canvas.yview)
        scroll_frame = tk.Frame(canvas)

        scroll_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=scroll_frame, anchor="nw")
        canvas.configure(yscrollcommand=popup_scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        popup_scrollbar.pack(side="right", fill="y")

        self.entries = {}
        for label_text, field_id in self.fields:
            label = tk.Label(scroll_frame, text=label_text + ":")
            label.pack(pady=1)
            entry = tk.Entry(scroll_frame, width=50)
            entry.pack(pady=2, padx=30)
            entry.insert(0, getattr(contact, field_id, ""))
            self.entries[field_id] = entry  # use field_id as the key


        submit_btn = tk.Button(scroll_frame, text="Save Contact", command=lambda: self.update_contact(contact, index))
        submit_btn.pack(pady=10)
        
    def delete_contact_popup(self):
        if messagebox.askquestion("askquestion", "Are you sure?") == "yes":
            selection = self.contact_list.curselection()
            if not selection:
                return

            index = selection[0]
        self.contacts.pop(index)
        self.contact_list.delete(index)
        for contact in self.contacts:
            print(contact["name"])
        
    def update_contact(self, contact, index):
        data = {field_id: entry.get() for field_id, entry in self.entries.items()}

        name = data["name"]
        phoneNumber = data["mobilePhone"]

        if name.strip() == "" and phoneNumber.strip() == "":
            messagebox.showerror("Missing fields", "Name and phone number are required!", parent=self.popup)
            return
        elif not phoneNumber.isnumeric():
            messagebox.showerror("Wrong fields", "Phone must be a number!", parent=self.popup)
            return

        print("Contact Info Entered:")
        for key, value in data.items():
            print(f"{key}: {value}")

        for key, value in data.items():
            setattr(contact, key, value)

        self.contacts[index] = contact
        self.contact_list.delete(index)
        self.contact_list.insert(index, contact.name)

        self.popup.destroy()
        messagebox.showinfo("Saved", "Contact information updated successfully!")

    def save_contact(self):
        data = {field_id: entry.get() for field_id, entry in self.entries.items()}
        
        name=data["name"]
        phoneNumber = data["mobilePhone"]
        
        if name.strip == "" and phoneNumber.strip == "":
            messagebox.showerror("Missing fields", "Name and phone number are requered!", parent=self.popup)
            return
        elif not phoneNumber.isnumeric():
            messagebox.showerror("Wrong fields", "Phone must be a number!", parent=self.popup)
            return
        
        print("Contact Info Entered:")
        for key, value in data.items():
            print(f"{key}: {value}")
        
        contact = Contact(**data)

        self.contacts.append(contact)
        
        self.contact_list.insert(tk.END, contact.name)
        
        self.popup.destroy()
        messagebox.showinfo("Saved", "Contact information saved successfully!")
        
    def show_contact_details(self, event):
        selection = self.contact_list.curselection()
        if not selection:
            return

        index = selection[0]
        contact = self.contacts[index]

        details = (
            f"Name: {contact.name}\n"
            f"Mobile Phone: {contact.mobilePhone}\n"
            f"Company: {contact.companyName}, {contact.companyOccupation}, {contact.companyAddress}, {contact.companyWebPage}\n"
            f"Other Phones: {contact.phone2}, {contact.phone3}, Home: {contact.homePhone}, Office: {contact.officePhone}\n"
            f"Emails: Private1: {contact.privateEmail1}, Private2: {contact.privateEmail2}, Office: {contact.officeEmail}\n"
            f"Address: {contact.address}\n"
            f"Birthday: {contact.birthDay}\n"
            f"Notes: {contact.notes}\n"
            f"Child: {contact.childName}, Birthday: {contact.childBirthDay}, Notes: {contact.childNotes}"
        )

        messagebox.showinfo("Contact Details", details, parent=self.master)
# Contact Book Program

contacts = []

def add_contact():
    print("Add a contact:")
    name = input("Name: ")
    phone = input("Phone number: ")
    email = input("Email: ")
    contacts.append({
        'name': name,
        'phone': phone,
        'email': email
    })
    print(f"Contact '{name}' added successfully.\n")

def view_contact_list():
    print("Contact List:")
    if not contacts:
        print("No contacts found.")
    else:
        for idx, contact in enumerate(contacts):
            print(f"{idx + 1}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
    print()

def search_contact():
    if not contacts:
        print("No contacts found.")
        return
    
    search_term = input("Enter name to search: ").strip().lower()
    found_contacts = []
    
    for contact in contacts:
        if search_term in contact['name'].lower():
            found_contacts.append(contact)
    
    if not found_contacts:
        print(f"No contacts found with name '{search_term}'.")
    else:
        print(f"Search results for '{search_term}':")
        for contact in found_contacts:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
    print()

def update_contact():
    if not contacts:
        print("No contacts found.")
        return
    
    view_contact_list()
    index = int(input("Enter the index of the contact to update: ")) - 1
    
    if 0 <= index < len(contacts):
        contact = contacts[index]
        print(f"Updating contact: {contact['name']}")
        new_name = input(f"New Name (press enter to keep '{contact['name']}'): ").strip()
        new_phone = input(f"New Phone (press enter to keep '{contact['phone']}'): ").strip()
        new_email = input(f"New Email (press enter to keep '{contact['email']}'): ").strip()
        
        if new_name:
            contact['name'] = new_name
        if new_phone:
            contact['phone'] = new_phone
        if new_email:
            contact['email'] = new_email
        
        print("Contact updated successfully.\n")
    else:
        print("Invalid index.\n")

def delete_contact():
    if not contacts:
        print("No contacts found.")
        return
    
    view_contact_list()
    index = int(input("Enter the index of the contact to delete: ")) - 1
    
    if 0 <= index < len(contacts):
        deleted_contact = contacts.pop(index)
        print(f"Contact '{deleted_contact['name']}' deleted successfully.\n")
    else:
        print("Invalid index.\n")

# Main menu loop
while True:
    print("Contact Book")
    print("1. Add Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")
    
    choice = input("Enter your choice (1-6): ").strip()
    
    if choice == '1':
        add_contact()
    elif choice == '2':
        view_contact_list()
    elif choice == '3':
        search_contact()
    elif choice == '4':
        update_contact()
    elif choice == '5':
        delete_contact()
    elif choice == '6':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 6.\n")


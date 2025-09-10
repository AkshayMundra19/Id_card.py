def get_user_info():
    print("Enter the following information for your ID card:")
    name = input("Full Name: ")
    dob = input("Date of Birth (DD/MM/YYYY): ")
    gender = input("Gender: ")
    address = input("Address: ")
    phone = input("Phone Number: ")
    id_number = input("Aadhar / Govt ID Number: ")
    return {
        "name": name,
        "dob": dob,
        "gender": gender,
        "address": address,
        "phone": phone,
        "id_number": id_number
    }

def print_government_id(info):
    print("\n" + "="*34)
    print("      GOVERNMENT OF INDIA")
    print("="*34)
    print(f"Name       : {info['name']}")
    print(f"DOB        : {info['dob']}")
    print(f"Gender     : {info['gender']}")
    print(f"Aadhar No. : {info['id_number']}")
    print("-"*34)
    print(f"Address    : {info['address']}")
    print("="*34)

def print_personal_id(info):
    print("\n" + "+"*34)
    print("          PERSONAL ID CARD")
    print("+"*34)
    print(f"Name    : {info['name']}")
    print(f"DOB     : {info['dob']}")
    print(f"Phone   : {info['phone']}")
    print(f"Gender  : {info['gender']}")
    print("-"*34)
    print(f"Address : {info['address']}")
    print("+"*34)

def main():
    user_info = get_user_info()
    print_government_id(user_info)
    print_personal_id(user_info)

if __name__ == "__main__":
    main()
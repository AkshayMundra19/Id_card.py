from PIL import Image, ImageDraw, ImageFont

def get_user_info():
    name = input("Full Name: ")
    dob = input("Date of Birth (DD/MM/YYYY): ")
    gender = input("Gender: ")
    address = input("Address: ")
    phone = input("Phone Number: ")
    id_number = input("Aadhar / Govt ID Number: ")
    photo_path = input("Path to your photo (e.g., photo.jpg): ")
    return {
        "name": name,
        "dob": dob,
        "gender": gender,
        "address": address,
        "phone": phone,
        "id_number": id_number,
        "photo_path": photo_path
    }

def make_id_card(info, card_type="government"):
    card = Image.new('RGB', (500, 300), (255, 255, 255))
    draw = ImageDraw.Draw(card)

    # Fonts: use default if 'arial.ttf' is unavailable
    try:
        title_font = ImageFont.truetype("arialbd.ttf", 24)
        field_font = ImageFont.truetype("arial.ttf", 16)
    except:
        title_font = ImageFont.load_default()
        field_font = ImageFont.load_default()

    # Load and place photo
    try:
        photo = Image.open(info["photo_path"]).resize((100, 120))
        card.paste(photo, (25, 40))
    except Exception as e:
        draw.text((25, 90), "No Photo", fill="gray", font=field_font)

    # Card title
    if card_type == "government":
        draw.text((170, 20), "GOVERNMENT OF INDIA", fill="navy", font=title_font)
        y_offset = 60
    else:
        draw.text((170, 20), "PERSONAL ID CARD", fill="green", font=title_font)
        y_offset = 60

    # ID Field Texts
    fields = [
        ("Name", info["name"]),
        ("DOB", info["dob"]),
        ("Gender", info["gender"]),
        ("Address", info["address"])
    ]

    if card_type == "government":
        fields.insert(3, ("Aadhar No.", info["id_number"]))
    else:
        fields.insert(3, ("Phone", info["phone"]))

    for idx, (label, value) in enumerate(fields):
        draw.text((170, y_offset + idx * 35), f"{label}: {value}", fill="black", font=field_font)

    # Save card
    outfile = f"{card_type}_id_card.png"
    card.save(outfile)
    print(f"{card_type.capitalize()} ID Card saved as {outfile}")

def main():
    print("Enter your details for ID card:")
    info = get_user_info()
    make_id_card(info, "government")
    make_id_card(info, "personal")

if __name__ == "__main__":
    main()
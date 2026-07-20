# Welcome users to EcoImpact and show privacy policy

print("==========================================")
print("🌍 ♻️ 🔌 Welcome to EcoImpact 🔌 ♻️ 🌍")
print("Your electronic recycling support tool")
print("==========================================")

print("\nPlease read our privacy policy:\n")

print("We collect the following data to provide recycling recommendations:")
print("- The item you wish to recycle")
print("- The condition of the item")
print("- Your location for local council recycling guidance")

print("\nWe do not store or share your personal data with third parties.")
print("Your data is only used during this session.")
print("For questions about data protection, contact:")
print("support@ecoimpact.co.uk")

print("\nBy proceeding, you agree to this privacy policy.\n")

print("------------------------------------------")

another_device = "yes"

while another_device.lower() == "yes":

    # Find out user location
    borough = input("\nEnter your local borough: ").lower()

    # Give advice based on user location
    if borough in ["southwark", "lambeth", "lewisham", "tower hamlets"]:
        print("\n✅ We support this borough.")
        print("Your local council recycling guidelines will be provided.")
    else:
        print("\n❌ We do not currently support this borough.")
        print("We are working hard to cover more areas.")
        exit()

    # Show devices available
    print("\n------------------------------------------")
    print("Devices we currently recycle:")
    print("- Laptops")
    print("- Computers")
    print("- Mobiles")
    print("- Printers")
    print("------------------------------------------")

    device = input("\nWhat type of electronic device do you want to recycle? ").lower()

    # Give advice based on device
    if device in ["laptop", "laptops"]:
        print("\n💻 Laptops can be recycled at your local IT recycling centre.")
    elif device in ["computer", "computers"]:
        print("\n🖥️ Computers can be recycled at your local IT recycling centre.")
    elif device in ["mobile", "mobiles"]:
        print("\n📱 Mobile phones can be recycled, donated, or sold safely.")
    elif device in ["printer", "printers"]:
        print("\n🖨️ Printers can be recycled at electronics recycling points.")
    else:
        print("\nSorry, we only provide guidance for laptops, computers, mobiles and printers.")

    # Ask condition
    condition = input("\nWhat is the condition of the device?\nWorking, Damaged, Broken or Faulty: ").lower()

    if condition in ["working", "works"]:
        print("\nThis item may be suitable for donation or selling.")
    elif condition in ["faulty", "broken"]:
        print("\nThis item may be suitable for repair.")
    elif condition in ["damaged", "damage"]:
        print("\nThis item can be recycled for parts.")
    else:
        print("\nPlease enter a valid condition.")

    # Disposal choice
    disposal = input("\nHow do you want to dispose of your item?\nRecycle, Donate, Repair or Sell: ").lower()

    if disposal == "recycle":
        print("\nYour item will be prepared for recycling.")
    elif disposal == "donate":
        print("\nYour item will be donated to Little Lives UK.")
    elif disposal == "repair":
        print("\nYour item will be assessed for repair options.")
    elif disposal == "sell":
        print("\nYour item may be suitable for selling.")
    else:
        print("\nPlease choose a valid disposal option.")

    another_device = input("\nDo you have another device you wish to recycle? Yes or No: ")

print("\n==========================================")
print("Thank you for using EcoImpact! 🌱")
print("Have a lovely day 😊")
print("==========================================")
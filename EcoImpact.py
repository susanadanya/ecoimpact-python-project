# Welcome users to EcoImpact and show privacy policy

print("==============================================")
print("🌍 ♻️ 🔌 Welcome to EcoImpact - Your electronic recycling support tool! 🌍 ♻️ 🔌")
print("==============================================")

print("\nPlease read our privacy policy\n")

print("We collect the following data for the purpose of providing tailored recycling recommendations:")
print("- The item you wish to recycle: This helps us guide you through the appropriate disposal process.")
print("- The condition of the item: Used to give specific advice on recycling, donating, repairing or selling.")
print("- Your location: We use this to provide local council guidelines for recycling and disposal.")

print("\nWe do not store or share your personal data with third parties.")
print("Your data is only used during the session and will not be retained after the session ends.")
print("For any questions about data protection, please contact us at support@ecoimpact.co.uk")

print("\nBy proceeding, you agree to this privacy policy.")

print("\n==============================================")

another_device = "yes"

while another_device.lower() == "yes":

    # Find out user location
    borough = input("\nEnter your local borough:\n").lower()

    # Give advice based on user location
    if borough == "southwark" or borough == "lambeth" or borough == "lewisham" or borough == "tower hamlets":
        print("\n----------------------------------------------")
        print("✅ We support this borough.")
        print("Your local council's guidelines will be provided.")
        print("----------------------------------------------")

    else:
        print("\n----------------------------------------------")
        print("❌ We do not currently support this borough.")
        print("We are working hard to cover more areas.")
        print("----------------------------------------------")
        exit()


    # Show list of devices
    print("\n----------------------------------------------")
    print("Here is our current list of devices we recycle:")
    print("- Laptops")
    print("- Computers")
    print("- Mobiles")
    print("- Printers")
    print("----------------------------------------------")

    device = input("\nWhat type of electronic device do you want to recycle?\n").lower()


    # Give advice based on electronic item
    if device == "laptop" or device == "laptops":
        print("\n----------------------------------------------")
        print("💻 You can recycle laptops at your local IT recycling centre.")
        print("----------------------------------------------")

    elif device == "computer" or device == "computers":
        print("\n----------------------------------------------")
        print("🖥️ You can recycle computers at your local IT recycling centre.")
        print("----------------------------------------------")

    elif device == "mobile" or device == "mobiles":
        print("\n----------------------------------------------")
        print("📱 Mobile phones can be recycled, donated, or sold safely after wiping personal data.")
        print("----------------------------------------------")

    elif device == "printer" or device == "printers":
        print("\n----------------------------------------------")
        print("🖨️ Printers can be recycled at electronics recycling points.")
        print("----------------------------------------------")

    else:
        print("\n----------------------------------------------")
        print("Sorry, we only provide guidance for laptops, computers, mobiles and printers.")
        print("----------------------------------------------")


    # Ask condition of device
    condition = input("\nWhat is the condition of the device?\nWorking, Damaged, Broken or Faulty:\n").lower()


    # Give advice based on condition
    if condition == "working" or condition == "works":
        print("\n----------------------------------------------")
        print("This item may be eligible to be donated or sold.")
        print("----------------------------------------------")

    elif condition == "faulty" or condition == "broken":
        print("\n----------------------------------------------")
        print("This item may be eligible for repair.")
        print("----------------------------------------------")

    elif condition == "damaged" or condition == "damage":
        print("\n----------------------------------------------")
        print("This item can be recycled for parts.")
        print("----------------------------------------------")

    else:
        print("\n----------------------------------------------")
        print("Please use a valid condition.")
        print("----------------------------------------------")


    # Ask disposal choice
    disposal = input("\nHow do you want to dispose of your item?\nRecycle, Donate, Repair or Sell:\n").lower()


    # Give options based on disposal choice
    if disposal == "recycle":
        print("\n----------------------------------------------")
        print("♻️ Your item will be prepared for recycling.")
        print("----------------------------------------------")

    elif disposal == "donate":
        print("\n----------------------------------------------")
        print("💚 Your item will be donated to Little Lives UK.")
        print("----------------------------------------------")

    elif disposal == "repair":
        print("\n----------------------------------------------")
        print("🔧 Your item will be assessed for repair options.")
        print("----------------------------------------------")

    elif disposal == "sell":
        print("\n----------------------------------------------")
        print("💰 Your item may be suitable for selling.")
        print("----------------------------------------------")

    else:
        print("\n----------------------------------------------")
        print("Please use a valid disposal option.")
        print("----------------------------------------------")


    # Ask if user has another device
    another_device = input("\nDo you have another device you wish to recycle? Yes or No:\n")


print("\n==============================================")
print("Thank you for using EcoImpact.")
print("Have a lovely day! 😊")
print("==============================================")
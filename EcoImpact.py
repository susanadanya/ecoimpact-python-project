#Welcome users to EcoImpact and show my privacy policy

print("🌍 ♻️ 🔌 Welcome to EcoImpact - Your electronic recycling support tool!🌍 ♻️ 🔌 ")
print ("Please read our privacy policy")
print("We collect the following data for the purpose of providing tailored recycling recommendations:")
print("The item you wish to recycle: This helps us guide you through the appropiate disposal ")
print("The condition of the item: Used to give more specific advice on whether to recycle, donating, repairing or recycling process.")
print("Your location: We use this to provide local council guidelines for recycling and disposal.")
print("\nWe do not store or share your personal data with third parties.")
print("Your data is only used during the session and will not be reatined after the session ends.")
print("For any questions about data protection, please contact us at support@ecoimpact.co.uk")
print("\nBy proceeding, you agree to this privacy policy.\n")

another_device = "yes"
while another_device == "yes":

    #Find out user location
    borough = input("\nEnter your local borough:\n").lower()

    #Give advice based on user location
    if borough == "southwark":
        print("We support this borough. Your local council's guidelines will be provided.\n")
    elif borough == "lambeth":
        print("We support this borough. Your local council's guidelines will be provided.\n")
    elif borough == "lewisham":
        print("We support this borough. Your local council's guidelines will be provided.\n")
    elif borough == "tower hamlets":
        print("We support this borough. Your local council's guidelines will be provided.\n")
    else:
        print("We do not currently support this borough, but we are working hard to cover more areas.\n")
        exit() 

    #Show the list of devices and ask user for device type
    print("Here is our current list of devices we recycle:\nLaptops, Computers, Mobiles, Printers\n")
    device = input("What type of electronic device do you want to recycle?\n").lower()

    # Give advice based on their electronic item
    if device == "laptop" or device == "laptops":
        print("You can recycle laptops at your local IT recycling centre.\n")
    elif device == "computer" or device == "computers":
        print("You can recycle computers at your local IT recycling centre.\n")
    elif device == "mobile" or device == "mobiles":
        print("Mobile phones can be recycled, donated, or sold safely after wiping personal data.\n")
    elif device == "printer" or device == "printers":
        print("Printers can be recycled at electronics recycling points.\n")
    else: 
        print("Sorry, we only provide guidance for computers, laptops, mobiles and printers")

    # Ask the user for condition of device
    condition = input("What is the condition of the device? Working, Damaged, Broken or Faulty\n").lower()
    # Give advice based on their item condition
    if condition == "working" or condition == "works":
        print("This item may be eligible to be donated or sold.")
    elif condition == "faulty" or condition == "broken":
        print("This item may be eligible for repair.")
    elif condition == "damaged" or condition == "damage": 
        print("This item can be recycled for parts.")
    else: 
        print("Please use a valid condition")
    
    #Ask the user for disposal choice
    disposal = input("\nHow do you want to dispose of your item? Recycle, Donate, Repair or Sell:\n").lower()
    
    #Give options based on disposal choice
    if disposal == "recycle":
        print("Your item will be prepared for recycling.")
    elif disposal == "donate":
        print("Your item will be donated to Little Lives UK.")
    elif disposal == "repair":
        print("Your item will be assessed for repair options.")
    elif disposal == "sell":
        print("Your item may be suitable for selling.")
    else:
        print("Please use a valid disposal option")

    #Ask user if they have another device
    another_device = input("\nDo you have another device you wish to recycle? Yes or No\n")
    
print ("Thank you for using EcoImpact, Have a lovely day! 😊")







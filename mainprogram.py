from userint import UserInt

ui = UserInt()

while True:
    # ask the user to input his name
    username = input(f"\n\33[33mHi, Good day! Please enter your name.\n\33[0m")
    if username.isnumeric():
        raise TypeError("Please check your typings to avoid errors! ")
    
    ui.firstNumberInput()
    ui.secondNumberInput()
    

    # ask the operation to be used
    chosen_operation = input(
        "\n\33[1mPress \33[32m1\33[0m\33[1m if you want to \33[32mADD\33[0m\33[1m the variables. Press \33[32m2\33[0m\33[1m to \33[32mSUBTRACT\33[0m\33[1m. Press \33[32m3\33[0m\33[1m to \33[32mMULTIPLY\33[0m\33[1m. Or press \33[32m4\33[0m\33[1m to \33[32mDIVIDE\33[0m\33[1m. ")
    
    ui.performOperation(chosen_operation,username)
    

    # try again
    askyesno = input("\n\33[46mDo you still want to continue? (yes/no):\33[0m ")
    if askyesno.lower() == 'no':
        print("\33[41mTerminating Program... ")
        exit()
    elif askyesno.lower() == 'yes':
        continue
    else:
        raise TypeError
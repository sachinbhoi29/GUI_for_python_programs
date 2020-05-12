import sys


####################################################### For Tkinter ##################################################################

def options():
    print '''\n**************************************************************
          Welcome to the GUI interface of the python program
**************************************************************'''




def main(selection):
    print(selection)
    if selection == "1":
        bob_obj = bob.mof_loading_script()
        bob_obj.main()
    elif selection == "2":
        can_obj = can2.mof_loading_script()
        can_obj.main()
    elif selection == "3":
        dena_obj = dena2.mof_loading_script()
        dena_obj.main()
    elif selection == "4":
        mof_obj = mof.mof_loading_script()
        mof_obj.main()
    elif selection == "5":
        mof_obj = ncr.mof_loading_script()
        mof_obj.main()
    elif selection == "6":
        mof_obj = sbitom.mof_loading_script()
        mof_obj.main()
    elif selection == "7":
        up.upload_options()
    elif selection == "8":
        sys.exit()
    else:
       pass


if __name__ == "__main__":
    main()

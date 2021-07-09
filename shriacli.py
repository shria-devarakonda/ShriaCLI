import datetime
def cli():
    said = input("You can say anything to me, " + name + ". How can i help you? (Say 'help' if you need help!)")
    newname = name
    if "help" in said.lower() or "man" in said.lower():
        print("+++===Commands Guide===+++")
        print("name : say name to ask the cli name.")
        print("version : say version to check the cli version.")
        print("your name: NEW!!! say your name to hear how the cli feels about your name. She'll only give an opinion of your name if she likes it.")
        print("kill/exit : say kill or exit to Exit this cli hell")
        print("help / man : say help or man to see this text! wait...")
        print("date : say date to see the date")
        print("datetime : say datetime to see the date and time of wherever you are")

    elif "name" in said.lower():
        print("My name is ShriaCLI.")

    elif "version" in said.lower():
        print("I'm version 1.0")


    elif newname.lower() in said.lower():
        print("Hmm... "+newname+", " +newname.lower()+", " + newname.upper()+"... No matter How i say it its a pretty nice name!")

    elif "date" in said.lower():
        #a = date.today()
        print(datetime.date.today())

    elif "datetime" in said.lower():
        #a = date.today()
        print(datetime.datetime.now())

    elif "kill" in said.lower() or "exit" in said.lower():
        print("GOODBYE!")
        return 0

    else:
        print("Unknown Command! Please only use the known commands! (Use 'help' or 'man' as your next command, or 'kill' if you want to exit.)")
    cli()

name = input("Hi, welcome. What is your name?")
cli()

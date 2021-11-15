import urllib.parse
import requests
import tkinter  as tk
from tkinter import *
from tkinter import messagebox
# 3Rguwll95IyFGzeG9Rhvf3BJdmKIECHU
# main_api =  "https://www.mapquestapi.com/directions/v2/route?"
main_api = "http://www.mapquestapi.com/directions/v2/alternateroutes?"
# secondary_api = "http://www.mapquestapi.com/directions/v2/alternateroutes?"
# orig = "Washington, D.C."
# dest = "Baltimore, Md"
key = "3Rguwll95IyFGzeG9Rhvf3BJdmKIECHU"

# print("Welcome to the Mapquest API Application.")
# print("a. Start")
# print("b. Exit")
root = tk.Tk()
root.title("MAPQUEST API Application")
label = Label(root, text = "Welcome to MAPQUEST API Application!", font=("Times New Roman", 25, 'bold')).pack()

def start():
    win_loc = Toplevel(root)
    win_loc.title('Starting Point and Destination')
    display = Label(win_loc, text = "Enter Starting Point and Destination", font=("Times New Roman", 25, 'bold')).grid(row=0,column=1)
    
    starting_loc = Label(win_loc, text = "Starting Location: ", font=("Times New Roman", 15)).grid(row=1)
    orig = Entry(win_loc, borderwidth = 5)
    orig.grid(row=1, column=2)
    
    destination_loc = Label(win_loc, text = "Destination: ", font=("Times New Roman", 15)).grid(row=2)
    dest = Entry(win_loc, borderwidth = 5)
    dest.grid(row=2, column=2)

    route_return = Label(win_loc, text = "How many routes to return?: ", font=("Times New Roman", 15)).grid(row=3)
    max_routes = Entry(win_loc, borderwidth = 5)
    max_routes.grid(row=3, column=2)

    def confirm():
        if len(orig.get()) == 0 and len(dest.get()) == 0:
            messagebox.showinfo("Error Occured", "Please enter starting point and destination.")
        elif len(orig.get()) == 0:
            messagebox.showinfo("Error Occured", "Please enter the starting point.")
        elif len(dest.get()) == 0:
            messagebox.showinfo("Error Occured", "Please enter destination.")
        elif len(max_routes.get()) == 0:
            messagebox.showinfo("Error Occured", "Please enter number of routes.")
        else: 
            win_loc2 = Toplevel(root)
            win_loc2.title('Route Type')
            display = Label(win_loc2, text = "Enter Route Type", font=("Times New Roman", 25, 'bold')).grid(row=0,column=1)
            
            var = StringVar()

            selection_route = Label(win_loc2, text = "Selection Route: ", font=("Times New Roman", 15)).grid(row=2, column = 1)
            Radiobutton(win_loc2, text = "Fastest", font=("Times New Roman", 15), variable = var,
                value = main_api + urllib.parse.urlencode({"key":key, "from":orig.get(), "to":dest.get(), "maxRoutes":max_routes.get(), "routeType": 'fastest'})).grid(row=3, column = 0)
            Radiobutton(win_loc2, text = "Shortest", font=("Times New Roman", 15), variable = var,
                value = main_api + urllib.parse.urlencode({"key":key, "from":orig.get(), "to":dest.get(), "maxRoutes":max_routes.get(), "routeType": 'shortest'})).grid(row=4, column = 0)
            Radiobutton(win_loc2, text = "Pedestrian", font=("Times New Roman", 15), variable = var,
                value = main_api + urllib.parse.urlencode({"key":key, "from":orig.get(), "to":dest.get(), "maxRoutes":max_routes.get(), "routeType": 'pedestrian'})).grid(row=3, column = 2)
            Radiobutton(win_loc2, text = "Bicycle", font=("Times New Roman", 15), variable = var,
                value = main_api + urllib.parse.urlencode({"key":key, "from":orig.get(), "to":dest.get(), "maxRoutes":max_routes.get(), "routeType": 'bicycle'})).grid(row=4, column = 2)
            
            def results():
                win_loc3 = Toplevel(root)
                win_loc3.title('Results from ' + orig.get() + ' to ' + dest.get())
                display = Label(win_loc3, text = "Results from " + orig.get() + " to " + dest.get(), font=("Times New Roman", 25, 'bold')).pack()
                
                sb = Scrollbar(win_loc3, orient = VERTICAL)  
                sb.pack(side = RIGHT, fill = BOTH)
                mylist = Listbox(win_loc3, yscrollcommand = sb.set)

                url = var.get()
                Label(win_loc3, text = "==========================================================================================", font=("Times New Roman", 15)).pack()
                Label(win_loc3, text = "URL: " + url, font=("Times New Roman", 15)).pack()

                json_data = requests.get(url).json()
                json_status = json_data["info"]["statuscode"]

                if json_status == 0:
                    Label(win_loc3, text = "==========================================================================================", font=("Times New Roman", 15)).pack()
                    Label(win_loc3, text = "API Status: " + str(json_status) + " = A sucessfull route call.\n", font=("Times New Roman", 15)).pack()
                    Label(win_loc3, text = "==========================================================================================", font=("Times New Roman", 15)).pack()
                    Label(win_loc3, text = "Directions from " + (orig.get()) + " to " + (dest.get()), font=("Times New Roman", 15)).pack()
                    Label(win_loc3, text = "Trip Duration: " + (json_data["route"]["formattedTime"]), font=("Times New Roman", 15)).pack()
                    Label(win_loc3, text = "Kilometers: " + str("{:.2f}".format((json_data["route"]["distance"]) * 1.61)), font=("Times New Roman", 15)).pack()
                    if ["routeType"] == 'fastest' or ["routeType"] == 'shortest':
                        Label(win_loc3, text = "Fuel Used (Ltr): " + str("{:.2f}".format((json_data["route"]["fuelUsed"]) * 3.78)), font=("Times New Roman", 15)).pack()
                    Label(win_loc3, text = "Route Type: " + (json_data["route"]["options"]["routeType"]), font=("Times New Roman", 15)).pack()
                    Label(win_loc3, text = "Max Routes: " + (json_data["route"]["maxRoutes"]), font=("Times New Roman", 15)).pack()
                    Label(win_loc3, text = "==========================================================================================", font=("Times New Roman", 15)).pack()
                    
                    alternative = Label(win_loc3, text = "Do you want to know an alternative route?", font=("Times New Roman", 15))
                    alternative.pack()
                    alternative_route = StringVar()
                    
                    # for each in json_data["route"]["legs"][0]["maneuvers"]:
                    #     mylist.insert(END, (each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])*1.61) + " km)"))
                    #     mylist.insert(END, "Time: " + str("{:.2f}".format((each["time"]) / 60)  + " minutes"))
                    #     mylist.insert(END, "Using " + each["transportMode"] + " as a means of transportation.\n")
                    #     mylist.pack(side = LEFT, fill= BOTH, expand = TRUE)
                    #     mylist.configure(justify = CENTER)

                    # alternative = Label(win_loc3, text = "Do you want to know an alternative route?", font=("Times New Roman", 15))
                    # alternative.pack()
                    # alternative_route = StringVar()

                    def try_again():
                        win_loc5 = Toplevel(root)
                        win_loc5.title('Try Again?')
                        Label(win_loc5, text = "Do you want to try again?", font=("Times New Roman", 15)).grid(row=0,column=0)
                        Button(win_loc5, text = "Yes", font=("Times New Roman", 15), fg = "white", bg = "green", command = start).grid(row=4, column = 0, sticky = "W")
                        Button(win_loc5, text = "No", font=("Times New Roman", 15), fg = "white", bg = "red", command = thank_you).grid(row=4, column = 0, sticky = "E")
                    
                    def thank_you():
                        messagebox.showinfo("Thank You", "Thank You for using Mapquest API Application.")
                        root.destroy()
                    
                    def alternative_routes():
                        win_loc4 = Toplevel(root)
                        win_loc4.title('Results from ' + orig.get() + ' to ' + dest.get())
                        display = Label(win_loc4, text = "Alternative Results from " + orig.get() + " to " + dest.get(), font=("Times New Roman", 25, 'bold')).pack()
                        try:
                            for alternativeRoute in json_data["route"]["alternateRoutes"]:
                                for alternatives in json_data["route"]["legs"][0]["maneuvers"]:
                                    Label(win_loc4, text = (alternatives["narrative"])  + " (" + str("{:.2f}".format((alternatives["distance"])*1.61) + " km)"), font=("Times New Roman", 15)).pack()
                                    # mylist.pack(side = LEFT, fill= BOTH, expand = TRUE)
                                    # mylist.configure(justify = CENTER)
                            Label(win_loc4, text = "==========================================================================================", font=("Times New Roman", 15)).pack()
                            Label(win_loc4, text = "Do you want to try again?", font=("Times New Roman", 15)).pack()
                    
                            Button(win_loc4, text = "Yes", font=("Times New Roman", 15), fg = "white", bg = "green", command = start).pack(side=LEFT, fill=Y, expand = TRUE)
                            Button(win_loc4, text = "No", font=("Times New Roman", 15), fg = "white", bg = "red", command = thank_you).pack(side=RIGHT, fill=Y, expand = TRUE)
                        except:
                            Label(win_loc4, text = "Sorry, there are no alternative route for this location.", font=("Times New Roman", 15)).pack()
                            Label(win_loc4, text = "Do you want to try again?", font=("Times New Roman", 15)).pack()

                            Button(win_loc4, text = "Yes", font=("Times New Roman", 15), fg = "white", bg = "green", command = start).pack(side=LEFT, fill=Y, expand = TRUE)
                            Button(win_loc4, text = "No", font=("Times New Roman", 15), fg = "white", bg = "red", command = thank_you).pack(side=RIGHT, fill=Y, expand = TRUE)

                    alt_route_confirm = Button(win_loc3, text = "Yes", font=("Times New Roman", 15), fg = "white", bg = "green", command = alternative_routes)
                    alt_route_confirm.pack()
                    alt_route_try = Button(win_loc3, text = "No", font=("Times New Roman", 15), fg = "white", bg = "red", command = try_again)
                    alt_route_try.pack()

                    Label(win_loc3, text = (json_data["route"]["options"]["routeType"]) + " Route: ", font=("Times New Roman", 15, "bold")).pack()
                    for each in json_data["route"]["legs"][0]["maneuvers"]:
                        mylist.insert(END, (each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])*1.61) + " km)"))
                        mylist.insert(END, "Time: " + str("{:.2f}".format((each["time"]) / 60)  + " minutes"))
                        mylist.insert(END, "Using " + each["transportMode"] + " as a means of transportation.\n")
                        mylist.pack(side = LEFT, fill= BOTH, expand = TRUE)
                        mylist.configure(justify = CENTER)

                elif json_status == 402:
                    Label(win_loc3, text = "****************************************************************************************", font=("Times New Roman", 15)).grid(row=0,column=0)
                    Label(win_loc3, text = "Status Code: " + str(json_status) + "; Invalid user inputs for one or both locations.", font=("Times New Roman", 15)).grid(row=1,column=0)
                    Label(win_loc3, text = "****************************************************************************************", font=("Times New Roman", 15)).grid(row=2,column=0)
                elif json_status == 611: 
                    Label(win_loc3, text = "****************************************************************************************", font=("Times New Roman", 15)).grid(row=0,column=0)
                    Label(win_loc3, text = "Status Code: " + str(json_status) + "; Missing an entry for one or both locations.", font=("Times New Roman", 15)).grid(row=1,column=0)
                    Label(win_loc3, text = "****************************************************************************************", font=("Times New Roman", 15)).grid(row=2,column=0)
                else: 
                    Label(win_loc3, text = "****************************************************************************************", font=("Times New Roman", 15)).grid(row=0,column=0)
                    Label(win_loc3, text = "For Staus Code: " + str(json_status) + "; Refer to:", font=("Times New Roman", 15)).grid(row=1,column=0)
                    Label(win_loc3, text = "https://developer.mapquest.com/documentation/directions-api/status-codes", font=("Times New Roman", 15)).grid(row=2,column=0)
                    Label(win_loc3, text = "****************************************************************************************", font=("Times New Roman", 15)).grid(row=3,column=0)

            confirm_route = Button(win_loc2, text = "Confirm", font=("Times New Roman", 15), fg = 'white', bg ='green', command = results).grid(row = 5, column = 1, sticky= 'W')
            exit_route = Button(win_loc2, text = "Exit ", font=("Times New Roman", 15), fg = 'white', bg ='red', command = quit).grid(row = 5, column = 1, sticky= 'E')

    confirm_loc = Button(win_loc, text = "Confirm", font=("Times New Roman", 15), fg = 'white', bg ='green', command = confirm).grid(row = 4, column = 1, sticky= 'W')
    exit_loc = Button(win_loc, text = "Exit ", font=("Times New Roman", 15), fg = 'white', bg ='red', command = quit).grid(row = 4, column = 1, sticky= 'E')


    # tk.messagebox.showinfo("Message","Hey There! I hope you are doing well.")

startbutton = Button(root, text = 'Start', font=("Times New Roman", 25), fg = 'white', bg ='green', command = start)
startbutton.pack(side=LEFT, fill=Y, expand = TRUE)
exitbutton = Button(root, text = 'Exit', fg = 'white', bg = 'red', font=("Times New Roman", 25), command = quit)
exitbutton.pack(side=RIGHT, fill=Y, expand = TRUE)

root.mainloop()

selection = input("Enter a letter: ")
if selection == 'a' or selection == 'A':
    while True:
        orig = input("Starting Location: ")
        if orig == "quit" or orig == "q":
            break
        dest = input("Destination: ")
        if dest == "quit" or dest == "q":
            break

        max_routes = input("Enter how many routes to return? ")
        print("Select a type of route to use: ")
        print("1. Fastest")
        print("2. Shortest")
        print("3. Pedestrian")
        print("4. Bicycle")
        route = input("Enter name of the route: ")
        if route == '1':
            url = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest, "maxRoutes":max_routes, "routeType": 'fastest'})
        elif route == '2':
            url = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest, "maxRoutes":max_routes, "routeType": 'shortest'})
        elif route == '3':
            url = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest, "maxRoutes":max_routes, "routeType": 'pedestrian'})
        elif route == '4':
            url = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest, "maxRoutes":max_routes, "routeType": 'bicycle'})
        else:
            print("Enter number from 1 - 4 only")
            break
    # json_data = requests.get(url).json()
# print(json_data)
        print("URL: " + (url))
    # print("Second URL: " + (second_url))
        json_data = requests.get(url).json()
    # json_data2 = requests.get(second_url).json()
        json_status = json_data["info"]["statuscode"]

    # print("Max Routes: " + (json_data2["maxRoutes"]))

        if json_status == 0:
            print("API Status: " + str(json_status) + " = A sucessfull route call.\n")
            print("=============================================")
            print("Directions from " + (orig) + " to " + (dest))
            print("Trip Duration: " + (json_data["route"]["formattedTime"]))
            print("Kilometers: " + str("{:.2f}".format((json_data["route"]["distance"]) * 1.61)))
            if ["routeType"] == 'fastest' or ["routeType"] == 'shortest':
                print("Fuel Used (Ltr): " + str("{:.2f}".format((json_data["route"]["fuelUsed"]) * 3.78)))
            print("Route Type: " + (json_data["route"]["options"]["routeType"]))
            print("Max Routes: " + (json_data["route"]["maxRoutes"]))
            print("=============================================")

            for each in json_data["route"]["legs"][0]["maneuvers"]:
                print((each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])*1.61) + " km)"))
                print("Time: " + str("{:.2f}".format((each["time"]) / 60)  + " minutes"))
                print("Using " + each["transportMode"] + " as a means of transportation.\n")
        
            alternative = input("Do you want to know an alternative route?(Y/N) ")
            if alternative == 'Y' or alternative == 'y':
                for alternativeRoute in json_data["route"]["alternateRoutes"]:
                    for alternatives in json_data["route"]["legs"][0]["maneuvers"]:
                        print((alternatives["narrative"])  + " (" + str("{:.2f}".format((alternatives["distance"])*1.61) + " km)"))
                break
            if alternative == 'N' or alternative == 'n':
                break
            print("=============================================\n")
    
        elif json_status == 402:
            print("**********************************************")
            print("Status Code: " + str(json_status) + "; Invalid user inputs for one or both locations.")
            print("**********************************************\n")
        elif json_status == 611:
            print("**********************************************")
            print("Status Code: " + str(json_status) + "; Missing an entry for one or both locations.")
            print("**********************************************\n")
        else:
            print("************************************************************************")
            print("For Staus Code: " + str(json_status) + "; Refer to:")
            print("https://developer.mapquest.com/documentation/directions-api/status-codes")
            print("************************************************************************\n")
elif selection == 'b' or selection == 'B':
    quit()
else: 
    print("Enter letter a to b only.")
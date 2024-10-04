#Modules
import folium
from geopy.geocoders import Nominatim
#Ipython works in jupyter
from IPython.display import display
from tkinter import*

#We create the main window
mw=Tk()
mw.geometry('500x600')
mw.title('Geolocation')
mw.config(bg='slategrey')

#Heading of the window
headingFrame=Frame(mw,bg='slategrey',bd=5)
headingFrame.place(relx=0.15,rely=0.05,relwidth=0.7,relheight=0.1)
headingLabel=Label(headingFrame,text='Geolocation',bg='white',font=('Times',20,'bold'))
headingLabel.place(relx=0,rely=0,relwidth=1,relheight=1)

#We define 3 global variables
street=StringVar()
number=StringVar()
town=StringVar()

#We need the information of the address that we are going to locate
#First we need the input of number of the street
Frame1=Frame(mw,bg='slategrey')
Frame1.place(relx=0.1,rely=0.15,relwidth=0.7,relheight=0.3)
label1=Label(Frame1,text='Enter the number of the address:',bg='slategrey',fg='white',font=('Times',12))
label1.place(relx=0.05,rely=0.2,relheight=0.08)
number=Entry(Frame1,font=('Times 12'))
number.place(relx=0.05,rely=0.3,relwidth=1,relheight=0.2)

#Now we need the name of the street
Frame2=Frame(mw,bg='slategrey')
Frame2.place(relx=0.1,rely=0.35,relwidth=0.7,relheight=0.3)
label2=Label(Frame2,text='Enter the name of the street: ',bg='slategrey',fg='white',font=('Times',12))
label2.place(relx=0.05,rely=0.4,relheight=0.08)
street=Entry(Frame2,font=('Times 12'))
street.place(relx=0.05,rely=0.5,relwidth=1,relheight=0.2)

#And last the name of the town/city
Frame3=Frame(mw,bg='slategrey')
Frame3.place(relx=0.1,rely=0.55,relwidth=0.7,relheight=0.3)
label3=Label(Frame3,text='Enter the name of the town/city: ',bg='slategrey',fg='white',font=('Times',12))
label3.place(relx=0.05,rely=0.6,relheight=0.08)
town=Entry(Frame3,font=('Times 12'))
town.place(relx=0.05,rely=0.7,relwidth=1,relheight=0.2)

#We define the object geolocator with Nominatim
geolocator = Nominatim(user_agent="http")

#Function that determinates the coordinates of the input and shows the map
def coordinates():
    streetR = street.get()
    numberR = number.get()
    townR = town.get()
    input=streetR+','+numberR+','+townR
    location = geolocator.geocode(input)
    coord=[location.latitude,location.longitude]
    mymap = folium.Map(location=coord, zoom_start=17)
    folium.Marker(
        coord,
        icon=folium.Icon(color='red',icon='arrow-down')).add_to(mymap)
    display(mymap)

#A button is created so that the user can see the map
button=Button(mw,text='Go!',font='Times 12',bg='slategrey',fg='white',padx=2,command=coordinates)
button.place(relx=0.35,rely=0.85,relwidth=0.25,relheight=0.05)

mw.mainloop()
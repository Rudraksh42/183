from tkinter import *
import json
import requests 
root=Tk()
#root.overrideredirect(True)
root.title("My Weather App")
root.geometry("350x300")

root.configure(background="white")
#Setting labels
city_name_label=Label(root, text="City Name",font=("Helvetica", 18,'bold'),bg="white")
city_name_label.place(relx=0.5,rely=0.2,anchor=CENTER)

city_entry=Entry(root)
city_entry.place(relx=0.5,rely=0.35,anchor=CENTER)

weather_info_label = Label(root,text="Weather: ", bg="white", font=("bold", 10))
weather_info_label.place(relx=0.5,rely=0.55,anchor=CENTER) 

humidity_info_label = Label(root,text="Humidity: ", bg="white", font=( "bold",10)) 
humidity_info_label.place(relx=0.5,rely=0.65,anchor=CENTER) 
    

def climate_info():
    api_info = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city_entry.get()+"&appid="+"21cab08deb7b27f4c2b55f3e2df28ea4")
    
    api_json_info = json.loads(api_info.content)
    
    weather_info = api_json_info["weather"][0]["main"]
    print(weather_info)
    
    humidity_info = api_json_info["main"]["humidity"]
    print(str(humidity_info) + "%")
    
    
    weather_info_label['text'] = "Weather: " + weather_info
    humidity_info_label['text'] = "Humidity: " + str(humidity_info) + "%"
    
    
    city_name_label['text'] = city_entry.get()
    city_entry.destroy()
    btn.destroy()
    
    
btn = Button(root , text = " Search Weather!" , command =climate_info)
btn.place(relx = 0.5 , rely = 0.45 , anchor = CENTER)



root.mainloop()

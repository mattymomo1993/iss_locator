#!/usr/bin/env python
import json
import turtle
import urllib.request
import time

__author__ = 'Matthew Morris and "https://www.101computing.net/real-time-iss-tracker/"'


#A first JSON request to retrieve the name of all the astronauts currently in space.
url = "http://api.open-notify.org/astros.json"
response = urllib.request.urlopen(url)
result = json.loads(response.read())
print("There are currently " + str(result["number"]) + " astronauts in space:")
print("")
people = result["people"]

for p in people:
  print(p["name"] + " on board of " + p["craft"])
  #A first JSON request to retrieve the name of all the astronauts currently in space.
url = "http://api.open-notify.org/astros.json"
response = urllib.request.urlopen(url)
result = json.loads(response.read())
print("There are currently " + str(result["number"]) + " astronauts in space:")
print("")

people = result["people"]

for p in people:
    print(p["name"] + " on board of " + p["craft"])


def over_indiana():
    url = "http://api.open-notify.org/iss-pass.json?lat=39.6411238&lon=-86.0512185"
    response = urllib.request.urlopen(url)
    result = json.loads(response.read())
    return("Will Pass over Indianapolis " + str(time.ctime(result["request"]["datetime"])))

#Display information on world map using Python Turtle
screen = turtle.Screen()
screen.setup(720, 360)
screen.setworldcoordinates(-180, -90, 180, 90)
#Load the world map picture
screen.bgpic("map.gif")
  
screen.register_shape("iss.gif")
iss = turtle.Turtle()
iss.shape("iss.gif")
iss.setheading(45)
iss.penup()
iss.goto(-86.0512185, 39.6411238)
iss.dot(10, "yellow")
iss.color("white")
iss.write(over_indiana())




while True:
#A JSON request to retrieve the current longitude and latitude of the IIS space station (real time)  
    url = "http://api.open-notify.org/iss-now.json"
    response = urllib.request.urlopen(url)
    result = json.loads(response.read())
    
#Let's extract the required information
    location = result["iss_position"]
    lat = location["latitude"]
    lon = location["longitude"]
    
  #Output informationon screen
    print("\nLatitude: " + (lat))
    print("Longitude: " + (lon))
    
    #Plot the ISS on the map  
    iss.goto(float(lon), float(lat))
    #refresh position every 5 seconds
    time.sleep(5)
    
def main(iss_position):
    screen = turtle.register_shape



if __name__ == '__main__':
    main()
import turtle
import time
import math

SCALE = 0.5
SPEED = 0.5
SUNSIZE = 150 * SCALE
blk = turtle.Turtle(visible=False)
#blk.circle(60)
blk.penup()
screen = turtle.Screen()
screen.setup(1080, 1000)  # Set the dimensions of the Turtle Graphics window.
screen.title("SOLAR SYSTEM ")
screen.bgcolor("black")
screen.register_shape("planet_photos/sun_resized.gif")
screen.register_shape("planet_photos/mars_resized.gif")
screen.register_shape("planet_photos/earth_resized.gif")
screen.register_shape("planet_photos/mars_resized.gif")
screen.register_shape("planet_photos/venus_resized.gif")
screen.register_shape("planet_photos/jupiter_resized.gif")
screen.register_shape("planet_photos/saturn_resized.gif")
screen.register_shape("planet_photos/uranus_resized.gif")
screen.register_shape("planet_photos/neptune_resized.gif")


planets_turtle = {"mercury" : None, "venus":None,"earth":None, "mars":None}
planets_line   = {"mercury" : None, "venus":None,"earth":None, "mars":None}
planets_data = {
            "mercury"  : {"distance":105,  "size" :12, "speed" : 11,  "color" :"gray",   "pos" : 0, "xoffset" : 10,  "yoffset": 0},
            "venus"    : {"distance":150,  "size" :32, "speed" : 2.9, "color" : "orange","pos" : 0, "xoffset" : 20, "yoffset": 0},
            "earth"    : {"distance":250,  "size" :35, "speed" : 4,   "color" : "blue",  "pos" : 0, "xoffset" : 25, "yoffset": 0},
            "mars"     : {"distance":350,  "size" :20, "speed" : 2.6, "color" : "red",   "pos" : 0, "xoffset" : 35, "yoffset": 0},
            "jupiter"  : {"distance":530,  "size" :80, "speed" : 2.1, "color" : "orange","pos" : 0, "xoffset" : 50, "yoffset": 0},
            "saturn"   : {"distance":710,  "size" :70, "speed" : 1.9, "color" : "yellow","pos" : 0, "xoffset" : 55, "yoffset": 0},
            "uranus"   : {"distance":880,  "size" :62, "speed" : 1.2, "color" : "cyan",  "pos" : 0, "xoffset" : 70, "yoffset": 0},
            "neptune"  : {"distance":1000, "size" :60, "speed" : 1.0, "color" : "purple","pos" : 0, "xoffset" : 90, "yoffset": 0.6},
}

sun = turtle.Turtle()
sun.shape("planet_photos/sun_resized.gif")
#sun.fillcolor("yellow")
sun.shapesize(170 * SCALE/20)
sun.goto([0,0])

for planets,planet_info in planets_data.items():
    distance = planet_info["distance"]
    size     = planet_info["size"]
    speed    = planet_info["speed"]
    color    = planet_info["color"]
    xoffset   = planet_info["xoffset"]
    yoffset   = planet_info["yoffset"]
    planets_turtle[planets] = turtle.Turtle()
    planets_turtle[planets].shape("circle")
    if(planets not in ('mercury')):
        planets_turtle[planets].shape(f"planet_photos/{planets}_resized.gif")
    planets_turtle[planets].shapesize(size*SCALE/20)
    planets_turtle[planets].fillcolor(color)
    planets_turtle[planets].penup()
    planets_turtle[planets].goto([(distance*SCALE)+xoffset,0])
    planets_line[planets] = turtle.Turtle(visible=False)
    planets_line[planets].shape("circle")
    planets_line[planets].shapesize(0.2/20)
    planets_line[planets].fillcolor(color)
    planets_line[planets].color("white")
    planets_line[planets].penup()
    

while True:
    for planets, planet_info in planets_data.items():
        distance = planet_info["distance"]
        speed    = planet_info["speed"]
        color    = planet_info["color"]
        angle    = planet_info["pos"]
        xoffset   = planet_info["xoffset"]
        x = ((distance*SCALE) + xoffset)* math.cos(math.radians(angle * SPEED))
        y = ((distance*SCALE) + yoffset)* math.sin(math.radians(angle * SPEED))
        planets_turtle[planets].goto([x,y])
        planets_line[planets].goto([x,y])
        planets_line[planets].pendown()
        angle += speed
        planets_turtle[planets].goto([x,y])
        planets_line[planets].goto([x,y])
        planet_info["pos"] = angle

#for i in range(0,20):
#    blk.circle(i*i, steps=8)

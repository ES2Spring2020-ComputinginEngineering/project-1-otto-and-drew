##################
# Drew and Otto
# Time: 2 hr
# We worked alone on this project
#################

import microbit as mb
import radio  # Needs to be imported separately

# Change the channel if other microbits are interfering. (Default=7)
radio.on()  # Turn on radio
radio.config(channel=12, length=100)

print('Program Started')
mb.display.show(mb.Image.HAPPY)

while not mb.button_a.is_pressed():  # wait for button A to be pressed to begin logging
    mb.sleep(10)

radio.send('start') # Send the word 'start' to start the receiver
mb.sleep(1000)
mb.display.show(mb.Image.HEART)  # Display Heart while logging
time = 0

# Read and send accelerometer data repeatedly until button A is pressed again
while not mb.button_a.is_pressed():
    time0 = microbit.running_time() #get the current running time
    microbit.sleep(100) #wait .1 seconds
    time1 = microbit.running_time() #get the current running time
    elapsed_time = time1 - time0
    time = time + elapsed_time
    x = mb.accelerometer.get_x()
    y = mb.accelerometer.get_y()
    z = mb.accelerometer.get_z()
    message = str(time + '' + x + '' + y + '' + z + '')
    radio.send(message)
    mb.sleep(10)



mb.display.show(mb.Image.SQUARE)  # Display Square when program ends
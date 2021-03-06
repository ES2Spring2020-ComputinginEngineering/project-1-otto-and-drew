""" Step 3 Data Receiver Code """

import microbit as mb
import radio  # Needs to be imported separately

radio.on()  # Turn on radio
radio.config(channel=12, length =100)
# Change the channel if other microbits are interfering. (Default=7)

print('Program Started')
mb.display.show(mb.Image.HAPPY, delay=1000, clear=True)

# Wait for start message before beginning printing
incoming = ''
while not incoming == 'start':
    incoming = radio.receive()
print('start')

while True:
    incoming = radio.receive() # Read from radio

    if incoming is not None: # message was received
        mb.display.show(mb.Image.HEART, delay=100, clear=True, wait=False)

        rc = eval(incoming)
        print(rc)

        mb.sleep(10)
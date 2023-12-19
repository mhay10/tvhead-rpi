import network
import socket
import esp
import gc

# Disable debug messages
esp.osdebug(None)

# Run garbage collector
gc.collect()

# Wifi credentials
SSID = "tvhead-control"
PASSWORD = "ChangeMePlease"

# Create access point
ap = network.WLAN(network.AP_IF)
ap.active(True)
ap.config(essid=SSID, password=PASSWORD)

# Wait for connection
while ap.active() == False:
    pass

# Print connection info
print("Access Point started")
print(ap.ifconfig())

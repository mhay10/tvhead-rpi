import socket


# Function to parse button value from request
def get_button(req: str):
    # Get params from request
    try:
        params = req.split("?")[1].split(" ")[0].split("&")

        # Find button param
        for param in params:
            if "=" in param:
                key, value = param.split("=")
                if key == "button":
                    # Make sure value is a number
                    allDigits = len(value) > 0 and all([c.isdigit() for c in value])
                    if allDigits:
                        return int(value)
    except IndexError:
        pass

    # Return None if button was not found
    return None


# Function to return 200 OK response
def return_ok(con: socket.socket):
    con.send("HTTP/1.1 200 OK\n")
    con.send("Content-Type: text/plain\n")
    con.send("\n")
    con.send("200")
    con.close()


# Function to return 400 Bad Request response
def return_bad_request(con: socket.socket):
    con.send("HTTP/1.1 400 Bad Request\n")
    con.send("Content-Type: text/plain\n")
    con.send("\n")
    con.send("400")
    con.close()


# Create socket on port 80
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", 80))
s.listen(5)

# Main loop
running = True
while running:
    # Get data from connection
    con, addr = s.accept()
    req = con.recv(1024).decode()

    # Parse button value from request
    button = get_button(req)
    print(button)

    # Send response if button was found
    if button is not None:
        return_ok(con)
    else:
        return_bad_request(con)

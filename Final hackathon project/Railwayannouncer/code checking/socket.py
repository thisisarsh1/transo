import socket

def is_internet_available():
    try:
        # Try to connect to a well-known website (in this case, Google's DNS server)
        socket.create_connection(("8.8.8.8", 53), timeout=3)
        return True
    except OSError:
        return False

if is_internet_available():
    # Code to run when there is an active internet connection
    a = ("Internet is available. Running code A.")
    # Your code A here
else:
    # Code to run when there is no active internet connection
    a = ("No internet connection. Running code B.")
    # Your code B here

# PCA Wardrive WebPage
![alt text](https://github.com/eternity336/WardrivePage/blob/main/dr_screenshot.png?raw=true)
Created a python application that lists out wifi ESSIDs and Bluetooth devices that are active within the area.

Application needs to run as root to get best data from the devices.  Python libraries need to be installed to root to make sure they are present when you run the application.

app.py is the flask application for serving up the website.

bluetooth_discover is the library for pulling bluetooth devices.

essid_discover is the library for pulling wifi information.

Both run as threads so they are actively polling for data.

- sudo systemctl enable wardrive.service
- sudo systemctl start wardrive.service

Then you can access the site with the http://< serverIP >:8000

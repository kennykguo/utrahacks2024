# Introduction
Welcome to the Smart Trash Sorting System project! This innovative hackathon project combines Arduino C++, Flask, HTML, and CSS to create a smart waste management solution. The goal of this system is to automate the process of sorting trash into different categories, making waste management more efficient and environmentally friendly.

# Motivation
Waste management is a critical challenge in today's world, and effective waste sorting is a key aspect of sustainable living. The motivation behind this project is to leverage technology to simplify and automate the waste sorting process, making it easier for individuals and communities to contribute to a cleaner environment.

# Description
The Smart Trash Sorting System utilizes an Arduino-based sorting mechanism, involving electrical hardware, to categorize trash into either garbage, or composable materials. 

The list of hardware includes an ultrasonic sensor, a 9G servo motor, an Arduino Uno, a soil moisture sensor, two breadboards, two buttons, and relevant electrical wiring. The technical aspects of this project involve using the ultrasonic sensor to detect objects, the moisture sensor to detect if an object is compostable, or garbage, and then using the motor to turn the object to be placed in the correct bin. 

The system is complemented by a web interface built with Flask, HTML, and CSS, providing real-time data visualization and control. Users can monitor the sorting process, receive status updates, and contribute to a more sustainable future. 

# Setup
Following  the setup for the electrical components, clone the entire repository into VSCode. connect the Arduino UNO using a USB-C a computer. Run the .ino file on the Arduino IDE, according to official documentation. Then, in the app.py directory, run "flask run" to run the Flask web server. Make sure to close the serial monitor before running the Flask server using "flask run" in the terminal so that you do not receive an error. Open a web browser and go to http://localhost:5000 to access the Smart Trash Sorting System dashboard.

# Next Steps
- Add features to the web interface, such as user authentication, historical data visualization, and notifications.
- Explore options for optimizing communication between the Arduino and Flask server for faster response times.
Scale the System: Consider scalability by testing the system with a larger number of trash items and optimizing performance accordingly.

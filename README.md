## Inspiration

Waste management is a critical challenge in today's world, and effective waste sorting is a key aspect of sustainable living. The motivation behind this project is to leverage technology to simplify and automate the waste sorting process, making it easier for individuals and communities to contribute to a cleaner environment.

## What it does

The Smart Trash Sorting System utilizes an Arduino-based sorting mechanism, involving electrical hardware, to categorize trash into either garbage, or compostable materials.

The list of hardware includes an ultrasonic sensor, a 9G servo motor, an Arduino Uno, a soil moisture sensor, two breadboards, two buttons, and relevant electrical wiring. The technical aspects of this project involve using the ultrasonic sensor to detect objects, the moisture sensor to detect if an object is compostable, or a piece of garbage, and then using the motor to turn the trapdoor to place the object in the correct bin. 

There are 2 buttons that temporarily pause the sensors, allowing you to empty the trash.

The system is complemented by a web interface built with Flask, HTML, and CSS, providing real-time data visualization and control. Users can monitor the sorting process, receive status updates, and contribute to a more sustainable future.

## How we built it

We started off by testing the moisture sensor and servo motor to ensure that we would be able to properly sort items. We then assembled the various components on our prototype cardboard box. The Arduino tracks data that gets sent to a Flask web server, to be dynamically displayed on a webpage. 

## How to run the Project

Following the setup for the electrical components, clone the entire repository into VSCode. connect the Arduino UNO to a computer. Run the .ino file on the Arduino IDE, according to official documentation. Then, in the app.py directory, run "flask run" to run the Flask web server. Make sure to close the serial monitor before running the Flask server using "flask run" in the terminal so that you do not receive an error. Open a web browser and go to http://localhost:5000 to access the Smart Trash Sorting System dashboard.

## Challenges we ran into

The moisture sensor that we used is actually meant to be used in soil, so it is not completely ideal for our project, however, it can still detect compostable vs. dry items to a somewhat accurate extent.

## Accomplishments that we're proud of
Our group was able to integrate a web server and update web page dynamically to display real-time data to the user. We were able to discover along the way how hardware and software can interact with each other.

## What we learned
Through this project, our group learned a lot about electrical and hardware safety, as we made a mistake in our circuitry, and caused a computer connected the Arduino, to shut down as a result of the high voltage sent to the computer. Thankfully, computers have resistance to high voltages, however, we learned that it is crucial to be methodological in our testing process, as to not be hasty and make mistakes that could have devastating consequences when there are greater risks. 

## What's next for TrashTalker
1. Add features to the web interface, such as user authentication, historical data visualization, and notifications.
2. Explore options for optimizing communication between the Arduino and Flask server for faster response times. Scale the System: Consider scalability by testing the system with a larger number of trash items and optimizing performance accordingly.


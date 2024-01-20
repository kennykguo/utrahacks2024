from flask import Flask, redirect, render_template, request
import serial

# Initializes the Flask application
app = Flask(__name__)


# Route file for index.html page
@app.route('/')
def main_page():
    return render_template("index.html", sensor_value = sensor_value)



# Get data from the Arduino and move it to the server
ser = serial.Serial('COM5', 9600)

while True:
    try:
        # Read data from Serial
        data = ser.readline().decode('utf-8').strip()

        # Process the data (you may want to parse it and perform specific actions)
        if data.startswith("Soil Moisture:"):
            sensor_value = data.split(":")[1]
            print(f"Received sensor data: {sensor_value}")

    except KeyboardInterrupt:
        # Close the serial port when the script is interrupted (e.g., Ctrl+C)
        ser.close()
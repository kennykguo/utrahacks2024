from flask import Flask, redirect, render_template
import serial
import plotly.express as px
import plotly.io as pio
from datetime import datetime

# Initializes the Flask application
app = Flask(__name__)

# ser = serial.Serial('COM5', 9600)

# Route file for index.html page
# When the homepage is accessed

categories = ['Compost', 'Garbage']
values = [5, 8]  # One value for each category

@app.route('/')
def index():
    # Get data from the Arduino
    # data = ser.readline().decode('utf-8').strip()
    # Get the soil moisture data
    # if data.startswith("Soil Moisture:"):
        # global sensor_value
        # sensor_value = data.split(":")[1]
        # print(f"Received sensor data: {sensor_value}")
    return render_template("index.html")
# Make sure to pass in a value after


@app.route('/aboutus')
def aboutus():
    return render_template("aboutus.html")



@app.route('/leaderboard')
def leaderboard():
    return render_template("leaderboard.html", compost = values[1])

@app.route('/dataanalytics')
def data():
    # Create a bar graph with two columns
    fig = px.bar(
        x=categories,
        y=values,
        labels={'x': 'Categories', 'y': 'Values'},
        title='Trash bin data',
        width=1000  # Adjust the width of the bars
    )

    fig.update_layout(
    clickmode='event+select',
    dragmode=False,
    hovermode=False,
    )

    # Convert the Plotly figure to HTML
    graph_html = pio.to_html(fig, full_html=False)

    # Get the current time
    current_time = datetime.now().strftime('%A %I:%M %p')

    return render_template('dataanalytics.html', graph_html=graph_html, time = current_time)





# Get data from the Arduino and move it to the server

# while True:
#     try:
#         # Read data from Serial
#         data = ser.readline().decode('utf-8').strip()

#         # Process the data (you may want to parse it and perform specific actions)
#         if data.startswith("Soil Moisture:"):
#             sensor_value = data.split(":")[1]
#             print(f"Received sensor data: {sensor_value}")

#     except KeyboardInterrupt:
#         # Close the serial port when the script is interrupted (e.g., Ctrl+C)
#         ser.close()

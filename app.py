from flask import Flask, redirect, render_template
import serial
import plotly.express as px
import plotly.io as pio
from datetime import datetime

# Initializes the Flask application
app = Flask(__name__)

ser = serial.Serial('COM5', 9600)

# Route file for index.html page
# When the homepage is accessed

categories = ['Compost', 'Garbage']
values = [0, 0]  # One value for each category

@app.route('/')
def index():
    # Get data from the Arduino
    data = ser.readline().decode('utf-8').strip()
    # Get the soil moisture data
    if data.startswith("Total Wet Items:"):
        global wet_items
        wet_items = data.split(":")[1]
        print(f"Received sensor wet: {wet_items}")
        values[0] = wet_items
    if data.startswith("Total Dry Items:"):
        global dry_items
        dry_items = data.split(":")[1]
        print(f"Received sensor dry: {dry_items}")
        values[1] = dry_items
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
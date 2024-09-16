import can
import obd
from tkinter import *
import logging

# Setup logging to capture faults and warnings
logging.basicConfig(filename='motorcycle_monitor.log', level=logging.INFO)

# OBD-II connection (adjust port if needed)
obd_conn = obd.OBD()  # or specify port, e.g., obd.OBD(portstr='COM3')

# CAN Bus connection (adjust channel and bustype based on your hardware setup)
can_bus = can.interface.Bus(channel='can0', bustype='socketcan')

# Initialize a GUI for displaying real-time data
root = Tk()
root.title("Motorcycle Real-Time Monitoring System")

# Labels for monitoring key indicators
engine_status = Label(root, text="Engine Status: Normal", font=("Arial", 14))
engine_status.pack(pady=10)
battery_status = Label(root, text="Battery Voltage: Normal", font=("Arial", 14))
battery_status.pack(pady=10)
oil_pressure = Label(root, text="Oil Pressure: Normal", font=("Arial", 14))
oil_pressure.pack(pady=10)

# Function to update real-time status
def update_data():
    # Example OBD-II request (for battery voltage)
    if obd_conn.is_connected():
        battery_voltage = obd_conn.query(obd.commands.ELM_VOLTAGE).value
        if battery_voltage and battery_voltage.magnitude < 12.0:
            battery_status.config(text=f"Battery Voltage Warning: {battery_voltage.magnitude}V")
            logging.warning(f"Low Battery Voltage: {battery_voltage.magnitude}V")
        else:
            battery_status.config(text="Battery Voltage: Normal")

    # Example CAN Bus request (for oil pressure)
    try:
        msg = can_bus.recv(1.0)
        if msg and int.from_bytes(msg.data, byteorder='big') > 100:  # Adjust threshold
            oil_pressure.config(text="Oil Pressure Warning: High")
            logging.warning(f"High Oil Pressure detected: {msg.data}")
        else:
            oil_pressure.config(text="Oil Pressure: Normal")
    except can.CanError:
        logging.error("Error reading CAN message")

    # Schedule the function to update every second
    root.after(1000, update_data)

# Start monitoring data
update_data()

# Run the GUI loop
root.mainloop()

# Count the number of non-zero pixels in the edge-detected image (indicating vehicles)
vehicle_density = np.count_nonzero(edges)

# Simple traffic light control logic based on vehicle density
if vehicle_density > 5000:
    print("High Traffic Density - Keep Green Light ON for 10 seconds.")
    # Green light ON (simulate with a print statement)
    time.sleep(10)
elif vehicle_density > 2000:
    print("Medium Traffic Density - Keep Green Light ON for 5 seconds.")
    # Green light ON (simulate with a print statement)
    time.sleep(5)
else:
    print("Low Traffic Density - Keep Red Light ON for 3 seconds.")
    # Red light ON (simulate with a print statement)
    time.sleep(3)


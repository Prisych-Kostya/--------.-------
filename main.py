import matplotlib.pyplot as plt


x_values = []
y_values = []
# reading values from file
with open("DS3.txt", 'r') as f:
    for lines in f:
        line = f.readline()
        point = line.strip().split()
        if(point != []):
            x_values.append(int(point[0]))
            y_values.append(int(point[1]))
f.close()

# Figsize – is a canvas size in inches. 1 inch = 96 pixels, so to get canvas size 960x540px
# we need to divide 960px and 540px by 96px to get canvas size in inches
fig, ax = plt.subplots(figsize=(960/96, 540/96))

print(y_values)
# adding plot title and axes labels
plt.title("Data Set visualisation")
plt.ylabel("Value (y-coordinate)")
plt.xlabel("Point # (x-coordinade)")

plt.scatter(
    x=x_values,
    y=y_values, 
    s=0.2 # width of line
)
plt.show()
import time

# Set the number of seconds to count down from
seconds = 10

# Loop through the countdown and print each second
for i in range(seconds, 0, -1):
    print(i)
    time.sleep(1)

# Print "Time's up!" when the countdown is done
print("Time's up!")



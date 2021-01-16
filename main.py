import OID
import winsound


frequency = 2500  # Set Frequency To 2500 Hertz
duration = 1000  # Set Duration To 1000 ms == 1 second
# winsound.Beep(frequency, duration)
print("Camera started")



try:
    OID.Process(camera=0)
except:
    print("Could not open camera")

import time

def countdown():
  global timepas
  timepas = float(input('Hello! How much time do you want to pass?'))
  while timepas != 0:
    timepas -= 0.01
    print(timepas)
    time.sleep(0.5)

from tkinter import *

from controller.calculator_controller import CalculatorController
from service.feet_to_meter_service import FeetToMeterService
from view.feet_to_meters import FeetToMeters

if __name__ == "__main__":
    root = Tk()
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    service = FeetToMeterService()
    controller = CalculatorController(service)
    feet_to_meters = FeetToMeters(root, controller)
    controller.view = feet_to_meters
    root.mainloop()
from tkinter import *

from controller.calculator_controller import CalculatorController
from service.feet_to_meter_service import FeetToMeterService
from view.feet_to_meters import FeetToMeters
from view.utils.tkinter_utils import center_window

if __name__ == "__main__":
    root = Tk()
    center_window(root, 300, 150)
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    service = FeetToMeterService()
    controller = CalculatorController(service)
    feet_to_meters = FeetToMeters(root, controller)
    controller.view = feet_to_meters
    root.mainloop()
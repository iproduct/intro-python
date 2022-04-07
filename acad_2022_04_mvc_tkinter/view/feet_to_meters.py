import functools
from tkinter import *
from tkinter import ttk

from controller.calculator_controller import CalculatorController
from service.feet_to_meter_service import FeetToMeterService
from view.command.calculate_feet_to_meters_command import CalculateFeetToMetersCommand
from view.command.exit_command import ExitCommand
from view.utils.tkinter_utils import center_resize_window


class FeetToMeters(ttk.Frame):
    def __init__(self, root, controller: CalculatorController):
        super().__init__(root, padding="3 3 12 12")
        self.root = root
        self.controller = controller

        # Set root
        center_resize_window(root)
        self.root.title('Feet to Meters Calculator')
        self.grid(column=0, row=0, sticky=NSEW)

        # Create view-models
        feet = StringVar()
        meters = StringVar()

        # Add views - text Entry (input) and Label (output) widgets
        feet_entry = ttk.Entry(self, width=12, textvariable=feet)
        feet_entry.grid(column=2, row=1, sticky=EW)

        ttk.Label(self, textvariable=meters).grid(column=2, row=2, sticky=W)

        # Add child widgets
        # btn_calc = ttk.Button(self, text='Calculate', command=lambda : print('Calculating...'))
        # btn_calc = ttk.Button(self, text='Calculate', command=functools.partial(print, 'Calculating...'))
        btn_calc = ttk.Button(self, text='Calculate', command=CalculateFeetToMetersCommand(self.controller))
        btn_calc.grid(column=3, row=3, sticky=EW)
        btn_calc = ttk.Button(self, text='Exit', command=ExitCommand(self.root))
        btn_calc.grid(column=4, row=3, sticky=EW)

if __name__ =="__main__":
    root = Tk()
    feet_to_meter_service = FeetToMeterService()
    calculator_controller = CalculatorController(feet_to_meter_service)
    feet_to_meters_view = FeetToMeters(root, calculator_controller )
    calculator_controller.view = feet_to_meters_view
    root.mainloop()
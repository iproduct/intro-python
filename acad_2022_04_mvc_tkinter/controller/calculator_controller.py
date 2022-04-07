from tkinter import messagebox

from service.feet_to_meter_service import FeetToMeterService


class CalculatorController:
    def __init__(self, service: FeetToMeterService, view=None):
        self.service = service
        self.view = view

    def calculate_feet_to_meters(self):
        try:
            self.view.meters.set(self.service.feet_to_meters(self.view.feet.get()))
        except ValueError:
            self.show_error_dialog()

    def show_error_dialog(self):
        messagebox.showerror(message=f"Invalid feet value: '{self.view.feet.get()}'")

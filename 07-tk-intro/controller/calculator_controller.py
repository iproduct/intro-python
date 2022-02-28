from tkinter import messagebox

from service.feet_to_meter_service import FeetToMeterService


class CalculatorController:
    def __init__(self, service: FeetToMeterService, view = None):
        self.view = view
        self.service = service
    def calculate_feet_to_meters(self, suffix="m"):
        try:
            # call the service and update view model with result
            self.view.meters.set(str(self.service.feet_to_meters(self.view.feet.get())) + suffix)
        except ValueError:
            self.show_error_dialog()

    def show_error_dialog(self):
        messagebox.showinfo(message=f"Invalid feet value '{self.view.feet.get()}'")
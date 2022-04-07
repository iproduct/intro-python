from controller.calculator_controller import CalculatorController


class CalculateFeetToMetersCommand:
    def __init__(self, controller: CalculatorController):
        self.controller = controller

    def __call__(self, *args, **kwargs):
        self.controller.calculate_feet_to_meters()
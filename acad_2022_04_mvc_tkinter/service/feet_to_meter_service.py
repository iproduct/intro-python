class FeetToMeterService:
    def feet_to_meters(self, feet_value):
        value = float(feet_value)
        return int(0.3048 * value * 10000.0 + 0.5) / 10000.0

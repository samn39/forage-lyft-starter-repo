from datetime import datetime

from battery import battery


class Calliope(battery):


    # def __init__(self, last_service_date, current_date, ):
    #     super().__init__(last_service_date)
    #     self.current_mileage = current_mileage
    #     self.last_service_mileage = last_service_mileage

    # def needs_service(self):
    #     service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 2)
    #     if service_threshold_date < datetime.today().date() or self.engine_should_be_serviced():
    #         return True
    #     else:
    #         return False
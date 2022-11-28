from requests import get
from tabulate import tabulate


class Deanonymize:
    def __init__(self):
        self.api = "http://htmlweb.ru"

    def save_information(self, info: str):
        with open("Deanonymize.txt", "a") as file:
            file.write(f"{info}\n")
            file.close()

    def deanonymize_ip_address(self, ip_address: int):
        ip_address_data = get(f"{self.api}/geo/api.php?json&ip={ip_address}").json()
        ip_address_info = [
            [f"Info about {ip_address}"],
            ["Country", f"{ip_address_data['country']['english']}"],
            ["Region", f"{ip_address_data['region']['english']}"],
            ["City", f"{ip_address_data['city_english']}"],
            ["Longitude", f"{ip_address_data['longitude']}"],
            ["Latitude", f"{ip_address_data['latitude']}"],
            ["Time zone", f"{ip_address_data['capital']['time_zone']}"],
            ["CityCode", f"{ip_address_data['country']['telcod']}"]
        ]
        print(tabulate(ip_address_info, tablefmt="fancy_grid"))
        self.save_information(info=ip_address_info)
        print(f"Information about::: {ip_address} saved in txt file!")

    def deanonymize_phone_number(self, phone_number: str):
        phone_number_data = get(f"{self.api}/geo/api.php?json&telcod={phone_number}").json()
        phone_number_info = [
            [f"Info about {phone_number}"],
            ["Country", f"{phone_number_data['country']['english']}"],
            ["City", f"{phone_number_data['capital']['english']}"],
            ["Longitude", f"{phone_number_data['capital']['longitude']}"],
            ["Latitude", f"{phone_number_data['capital']['latitude']}"],
            ["Time zone", f"{phone_number_data['capital']['time_zone']}"],
            ["Operator", f"{phone_number_data['0']['oper']}"],
            ["Part of the light", f"{phone_number_data['country']['location']}"]
        ]
        print(tabulate(phone_number_info, tablefmt="fancy_grid"))
        self.save_information(info=phone_number_info)
        print(f"-- Information about::: {phone_number} saved in txt file!")

    def main_process(self):
        main_menu = [
            [1, "Deanonymize ip address"],
            [2, "Deanonymize phone number"]
        ]
        print(tabulate(main_menu, tablefmt="fancy_grid"))
        select = int(input("-- Select::: "))
        if select == 1:
            self.deanonymize_ip_address(input("-- IP Address::: "))
        elif select == 2:
            self.deanonymize_phone_number(input("-- Phone Number::: "))
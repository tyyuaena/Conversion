class Length:
    @staticmethod
    def cm_to_mm(cm):
        return cm * 10
    
    @staticmethod
    def mm_to_cm(mm):
        return mm / 10

    @staticmethod
    def m_to_cm(m):
        return m * 100
    
    @staticmethod
    def cm_to_m(cm):
        return cm / 100

    @staticmethod
    def km_to_m(km):
        return km * 1000

    @staticmethod
    def m_to_km(m):
        return m / 1000

    @staticmethod
    def inch_to_cm(inch):
        return inch * 2.54
    
    @staticmethod
    def cm_to_inch(cm):
        return cm / 2.54

    @staticmethod
    def foot_to_m(foot):
        return foot * 0.3048
    
    @staticmethod
    def m_to_foot(m):
        return m / 0.3048

    @staticmethod
    def yard_to_ft(yard):
        return yard * 3
    
    @staticmethod
    def ft_to_yard(ft):
        return ft / 3

    @staticmethod
    def mile_to_m(mile):
        return mile * 1609.34
    
    @staticmethod
    def m_to_mile(m):
        return m / 1609.34

    @staticmethod
    def nautical_mile_to_m(nautical_mile):
        return nautical_mile * 1852
    
    @staticmethod
    def m_to_nautical_mile(m):
        return m / 1852

class Mass:
    @staticmethod
    def g_to_mg(g):
        return g * 1000
    
    @staticmethod
    def mg_to_g(mg):
        return mg / 1000

    @staticmethod
    def kg_to_g(kg):
        return kg * 1000
    
    @staticmethod
    def g_to_kg(g):
        return g / 1000

    @staticmethod
    def ton_to_kg(t):
        return t * 1000
    
    @staticmethod
    def kg_to_ton(kg):
        return kg / 1000

    @staticmethod
    def ounce_to_g(oz):
        return oz * 28.3495
    
    @staticmethod
    def g_to_ounce(g):
        return g / 28.3495

    @staticmethod
    def pound_to_ounce(lb):
        return lb * 16
    
    @staticmethod
    def ounce_to_pound(oz):
        return oz / 16

    @staticmethod
    def stone_to_pound(stone):
        return stone * 14
    
    @staticmethod
    def pound_to_stone(pound):
        return pound / 14

class Time:
    @staticmethod
    def min_to_sec(min):
        return min * 60

    @staticmethod
    def sec_to_min(sec):
        return sec / 60
    
    @staticmethod
    def hour_to_sec(hour):
        return hour * 3600
    
    @staticmethod
    def sec_to_hour(sec):
        return sec / 3600
    
    @staticmethod
    def hour_to_min(hour):
        return hour * 60
    
    @staticmethod
    def min_to_hour(min):
        return min / 60

    @staticmethod
    def day_to_hour(day):
        return day * 24
    
    @staticmethod
    def hour_to_day(hour):
        return hour / 24

    @staticmethod
    def week_to_day(week):
        return week * 7
    
    @staticmethod
    def day_to_week(day):
        return day / 7

    @staticmethod
    def month_to_day(month):
        return month * 30.44
    
    @staticmethod
    def day_to_month(day):
        return day / 30.44

    @staticmethod
    def year_to_month(year):
        return year * 12
    
    @staticmethod
    def month_to_year(month):
        return month / 12
        
    @staticmethod
    def year_to_day(year):
        return year * 365
    
    @staticmethod
    def day_to_year(day):
        return day / 365
    
    @staticmethod
    def decade_to_year(decade):
        return decade * 10
    
    @staticmethod
    def year_to_decade(year):
        return year / 10
    
    @staticmethod
    def century_to_year(century):
        return century * 100
    
    @staticmethod
    def year_to_century(year):
        return year / 100
    
    @staticmethod
    def millennium_to_year(mill):
        return mill * 1000
    
    @staticmethod
    def year_to_millennium(year):
        return year / 1000

class NumberSystem:
    @staticmethod
    def binary_to_decimal(binary):
        return int(binary, 2)

    @staticmethod
    def decimal_to_binary(decimal):
        return bin(decimal)[2:]

    @staticmethod
    def binary_to_hex(binary):
        return hex(int(binary, 2))[2:]

    @staticmethod
    def hex_to_binary(hex):
        return bin(int(hex, 16))[2:]
    
    @staticmethod
    def binary_to_octal(binary):
        return oct(int(binary,2))[2:]

    @staticmethod
    def octal_to_binary(octal):
        return bin(int(octal, 8))[2:]

    @staticmethod
    def decimal_to_hex(decimal):
        return hex(decimal)[2:]

    @staticmethod
    def hex_to_decimal(hex):
        return int(hex, 16)

    @staticmethod
    def decimal_to_octal(decimal):
        return oct(decimal)[2:]

    @staticmethod
    def octal_to_decimal(octal):
        return int(octal, 8)

    @staticmethod
    def hex_to_octal(hex):
        return oct(int(hex, 16))[2:]
    
    @staticmethod
    def octal_to_hex(octal):
        return hex(int(octal, 8))[2:]

class ConverterApp:
    def __init__(self):
        self.length_converter = Length()
        self.mass_converter = Mass()
        self.time_converter = Time()
        self.number_system_converter = NumberSystem()
    
    def get_decimal_input(self):
        while True:
            try:
                return int(input("Enter a decimal value: "))
            except ValueError:
                print("Invalid decimal input. Please enter a valid integer.")

    def get_binary_input(self):
        while True:
            value = input("Enter a binary value (0s and 1s only): ")
            if all(char in '01' for char in value):
                return value
            print("Invalid binary input. Please enter only 0s and 1s.")

    def get_hex_input(self):
        while True:
            value = input("Enter a hexadecimal value (0-9, A-F): ").lower()
            if all(char in '0123456789abcdef' for char in value):
                return value
            print("Invalid hexadecimal input. Please enter only hexadecimal characters (0-9, A-F).")

    def get_octal_input(self):
        while True:
            value = input("Enter an octal value (0-7): ")
            if all(char in '01234567' for char in value):
                return value
            print("Invalid octal input. Please enter only octal characters (0-7).")

    def get_input(self, prompt, func, unit):
        while True:
            try:
                if 'binary' in prompt:
                    user_input = self.get_binary_input()
                elif 'octal' in prompt:
                    user_input = self.get_octal_input()
                elif 'hexadecimal' in prompt:
                    user_input = self.get_hex_input()
                else:
                    user_input = float(input(prompt))

                result = func(user_input)

                if isinstance(result, int):
                    print(f"Converted to {unit}: {result}")
                else:
                    print(f"Converted to {unit}: {result:.2f}")
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    def length_menu(self):
        print("\nLength conversions:")
        print("1. millimeter to centimeter")
        print("2. centimeter to millimeter")
        print("3. centimeter to meter")
        print("4. centimeter to inch")
        print("5. inch to centimeter")
        print("6. foot to meter")
        print("7. foot to yard")
        print("8. yard to foot")
        print("9. meter to centimeter")
        print("10. meter to kilometer")
        print("11. meter to foot")
        print("12. meter to mile")
        print("13. meter to nautical mile")
        print("14. kilometer to meter")
        print("15. mile to meter")
        print("16. nautical mile to meter")
        print("17. Go back to main menu")

    def length_conversion(self):
        length_conversions = {
            '1': ("Enter value in mm: ", self.length_converter.mm_to_cm, "cm"),
            '2': ("Enter value in cm: ", self.length_converter.cm_to_mm, "mm"),
            '3': ("Enter value in cm: ", self.length_converter.cm_to_m, "m"),
            '4': ("Enter value in cm: ", self.length_converter.cm_to_inch, "in"),
            '5': ("Enter value in in: ", self.length_converter.inch_to_cm, "cm"),
            '6': ("Enter value in ft: ", self.length_converter.foot_to_m, "m"),
            '7': ("Enter value in ft: ", self.length_converter.ft_to_yard, "yd"),
            '8': ("Enter value in yd: ", self.length_converter.yard_to_ft, "ft"),
            '9': ("Enter value in m: ", self.length_converter.m_to_cm, "cm"),
            '10': ("Enter value in m: ", self.length_converter.m_to_km, "km"),
            '11': ("Enter value in m: ", self.length_converter.m_to_foot, "ft"),
            '12': ("Enter value in m: ", self.length_converter.m_to_mile, "mi"),
            '13': ("Enter value in m: ", self.length_converter.m_to_nautical_mile, "NM"),
            '14': ("Enter value in km: ", self.length_converter.km_to_m, "m"),
            '15': ("Enter value in mi: ", self.length_converter.mile_to_m, "m"),
            '16': ("Enter value in NM: ", self.length_converter.nautical_mile_to_m, "m"),
            '17': None
        }

        while True:
            self.length_menu()
            length_choice = input("Enter the number of your choice: ")

            if length_choice == '17':
                break
            elif length_choice in length_conversions:
                prompt, func, unit = length_conversions[length_choice]
                self.get_input(prompt, func, unit)
            else:
                print("Invalid choice. Please try again.")

    def mass_menu(self):
        print("\nMass conversions:")
        print("1. mg to g")
        print("2. g to mg")
        print("3. g to kg")
        print("4. g to ounce")
        print("5. ounce to g")
        print("6. ounce to pound")
        print("7. pound to ounce")
        print("8. pound to stone")
        print("9. kg to g")
        print("10. kg to ton")
        print("11. stone to pound")
        print("12. ton to kg")
        print("13. Go back to main menu")
    
    def mass_conversion(self):
        mass_conversions = {
            '1': ("Enter value in mg: ", self.mass_converter.mg_to_g, "g"),
            '2': ("Enter value in g: ", self.mass_converter.g_to_mg, "mg"),
            '3': ("Enter value in g: ", self.mass_converter.g_to_kg, "kg"),
            '4': ("Enter value in g: ", self.mass_converter.g_to_ounce, "oz"),
            '5': ("Enter value in oz: ", self.mass_converter.ounce_to_g, "g"),
            '6': ("Enter value in oz: ", self.mass_converter.ounce_to_pound, "lb"),
            '7': ("Enter value in lb: ", self.mass_converter.pound_to_ounce, "oz"),
            '8': ("Enter value in lb: ", self.mass_converter.pound_to_stone, "st"),
            '9': ("Enter value in kg: ", self.mass_converter.kg_to_g, "g"),
            '10': ("Enter value in kg: ", self.mass_converter.kg_to_ton, "t"),
            '11': ("Enter value in st: ", self.mass_converter.stone_to_pound, "lb"),
            '12': ("Enter value in t: ", self.mass_converter.ton_to_kg, "kg"),
            '13': None
        }

        while True:
            self.mass_menu()
            mass_choice = input("Enter the number of your choice: ")

            if mass_choice == '13':
                break
            elif mass_choice in mass_conversions:
                prompt, func, unit = mass_conversions[mass_choice]
                self.get_input(prompt, func, unit)
            else:
                print("Invalid choice. Please try again.")

    def time_menu(self):
        print("\nTime conversions:")
        print("1. second to minute")
        print("2. second to hour")
        print("3. minute to second")
        print("4. minute to hour")
        print("5. hour to second")
        print("6. hour to minute")
        print("7. hour to day")
        print("8. day to hour")
        print("9. day to week")
        print("10. day to month")
        print("11. day to year")
        print("12. week to day")
        print("13. month to day")
        print("14. month to year")
        print("15. year to day")
        print("16. year to month")
        print("17. year to decade")
        print("18. year to century")
        print("19. year to millennium")
        print("20. decade to year")
        print("21. century to year")
        print("22. millennium to year")
        print("23. Go back to main menu")

    def time_conversion(self):
        time_conversions = {
            '1': ("Enter value in sec: ", self.time_converter.sec_to_min, "min"),
            '1': ("Enter value in sec: ", self.time_converter.sec_to_hour, "hour"),
            '2': ("Enter value in min: ", self.time_converter.min_to_sec, "sec"),
            '3': ("Enter value in min: ", self.time_converter.min_to_hour, "hour"),
            '4': ("Enter value in hour: ", self.time_converter.hour_to_sec, "sec"),
            '4': ("Enter value in hour: ", self.time_converter.hour_to_min, "min"),
            '5': ("Enter value in hour: ", self.time_converter.hour_to_day, "day"),
            '6': ("Enter value in day: ", self.time_converter.day_to_hour, "hour"),
            '7': ("Enter value in day: ", self.time_converter.day_to_week, "week"),
            '8': ("Enter value in day: ", self.time_converter.day_to_month, "month"),
            '9': ("Enter value in day: ", self.time_converter.day_to_year, "year"),
            '10': ("Enter value in week: ", self.time_converter.week_to_day, "day"),
            '11': ("Enter value in month: ", self.time_converter.month_to_day, "day"),
            '11': ("Enter value in month: ", self.time_converter.month_to_year, "year"),
            '12': ("Enter value in year: ", self.time_converter.year_to_day, "day"),
            '12': ("Enter value in year: ", self.time_converter.year_to_month, "month"),
            '13': ("Enter value in year: ", self.time_converter.year_to_decade, "decade"),
            '14': ("Enter value in year: ", self.time_converter.year_to_century, "century"),
            '15': ("Enter value in year: ", self.time_converter.year_to_millennium, "millennium"),
            '16': ("Enter value in decade: ", self.time_converter.decade_to_year, "year"),
            '17': ("Enter value in century: ", self.time_converter.century_to_year, "year"),
            '18': ("Enter value in millennium: ", self.time_converter.millennium_to_year, "year"),
            '25': None
        }

        while True:
            self.time_menu()
            time_choice = input("Enter the number of your choice: ")

            if time_choice == '23':
                break
            elif time_choice in time_conversions:
                prompt, func, unit = time_conversions[time_choice]
                self.get_input(prompt, func, unit)
            else:
                print("Invalid choice. Please try again.")

    def number_system_menu(self):
        print("\nNumber System conversions:")
        print("1. Binary to Decimal")
        print("2. Binary to Octal")
        print("3. Binary to Hexadecimal")
        print("4. Decimal to Binary")
        print("5. Decimal to Octal")
        print("6. Decimal to Hexadecimal")
        print("7. Octal to Binary")
        print("8. Octal to Decimal")
        print("9. Octal to Hexadecimal")
        print("10. Hexadecimal to Binary")
        print("11. Hexadecimal to Decimal")
        print("12. Hexadecimal to Octal")
        print("13. Go back to main menu")
    
    def number_system_conversion(self):
        number_system_conversions = {
            '1': ("binary", self.number_system_converter.binary_to_decimal, "decimal"),
            '2': ("binary", self.number_system_converter.binary_to_octal, "octal"),
            '3': ("binary", self.number_system_converter.binary_to_hex, "hexadecimal"),
            '4': ("decimal", self.number_system_converter.decimal_to_binary, "binary"),
            '5': ("decimal", self.number_system_converter.decimal_to_octal, "octal"),
            '6': ("decimal", self.number_system_converter.decimal_to_hex, "hexadecimal"),
            '7': ("octal", self.number_system_converter.octal_to_binary, "binary"),
            '8': ("octal", self.number_system_converter.octal_to_decimal, "decimal"),
            '9': ("octal", self.number_system_converter.octal_to_hex, "hexadecimal"),
            '10': ("hexadecimal", self.number_system_converter.hex_to_binary, "binary"),
            '11': ("hexadecimal", self.number_system_converter.hex_to_decimal, "decimal"),
            '12': ("hexadecimal", self.number_system_converter.hex_to_octal, "octal"),
            '13': None 
        }

        while True:
            self.number_system_menu()
            choice = input("Enter the number of your choice: ")

            if choice == '13':
                break
            elif choice in number_system_conversions:
                input_type, func, target_system = number_system_conversions[choice]

                if input_type == "binary":
                    user_input = self.get_binary_input()
                elif input_type == "octal":
                    user_input = self.get_octal_input()
                elif input_type == "hexadecimal":
                    user_input = self.get_hex_input()
                elif input_type == "decimal":
                    user_input = self.get_decimal_input()

                result = func(user_input)
                print(f"Converted to {target_system}: {result}")
            else:
                print("Invalid choice. Please try again.")

    def main(self):
        while True:
            print("\nChoose a category:")
            print("1. Length")
            print("2. Mass")
            print("3. Time")
            print("4. Number System")
            print("5. Exit")

            choice = input("Enter the number of your choice: ")

            if choice == '1':
                self.length_conversion()
            elif choice == '2':
                self.mass_conversion()
            elif choice == '3':
                self.time_conversion()
            elif choice == '4':
                self.number_system_conversion()
            elif choice == '5':
                print("Exiting the program.")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    app = ConverterApp()
    app.main()
from mt5linux import MetaTrader5
import time
import datetime
import os

# Init MetaTrader5
mt5 = MetaTrader5()

# Function Robot Memix


def memixBot():
    if not mt5.initialize():
        print("Failed To Connect -Memix Robot v0.1")
        return
    else:
        print("\n==============================")
        print("\n|WELCOME TO MEMIX ROBOT v0.1|")
        print("\n=============================")
    symbols = {1: "USDJPY", 2: "EURUSD", 3: "USDCNH", 4: "GBPUSD"}
    howlong_default = 2
    try:
        while True:
            howlong_delay = input(
                "How many second you want for the delay to the new data? (Default = 2 second) :"
            )
            if howlong_delay.strip() == "":
                howlong = howlong_default
            else:
                try:
                    howlong = int(howlong_delay)
                except ValueError:
                    print("Invalid Numbber using default 2sec")
                    howlong = howlong_default
            try:
                userinput = int(
                    input(
                        "Choose 1 OF 4, Most Popular Currency for Info: 1:USDJPY, 2:EURUSD, 3:USDCNH, 4:GBPUSD: "
                    )
                )
                if userinput in symbols:
                    symbols_name = symbols[userinput]
                    break
                else:
                    print("Invalid Number")
            except ValueError:
                print("Please Choose a Number")

            # Main Logic
        print(f"Checking The Data of {symbols_name}... ctrl+C to End this Program..")
        while True:
            tick = mt5.symbol_info_tick(f"{symbols_name}")
            if tick:
                print(
                    f"Todays date : {datetime.datetime.now().date()} | Bid : {
                        tick.bid
                    } | Ask : {tick.ask}"
                )
            else:
                print("Cannot Connect to Server")
                break
            time.sleep(howlong)
    except KeyboardInterrupt:
        print(" Program is Closed By User")
        print("==========================\n")
        print("Thanks For Using My Program\n")
        print("===========================\n")
        userinput = input("Use Again? [Y] :").upper()
        os.system("clear")
        if userinput == "Y":
            memixBot()
        else:
            print("==========================\n")
            print("Thanks For Using My Program\n")
            print("===========================\n")
            return
    finally:
        mt5.shutdown()


if __name__ == "__main__":
    memixBot()

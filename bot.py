from mt5linux import MetaTrader5
import time
import datetime
import os

# Init MetaTrader5
mt5 = MetaTrader5()

# Logo
GREEN = "\033[92m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
RESET = "\033[0m"  # Buat balikin warna ke normal

# Function Robot Memix


def memixBot():
    if not mt5.initialize():
        print("Failed To Connect -Memix Robot v0.1")
        return
    else:
        print(f"{CYAN}=============================={RESET}")
        print(f"{GREEN}   WELCOME TO MEMIX ROBOT     {RESET}")
        print(f"{CYAN}=============================={RESET}")
    symbols = {"1": "USDJPY", "2": "EURUSD", "3": "USDCNH", "4": "GBPUSD"}
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
            while True:
                userinput = str(
                    input(
                        f"Choose 1 OF 4, Most Popular Currency for Info: 1:{
                            GREEN
                        }USDJPY{RESET}, 2:{CYAN}EURUSD{RESET}, 3:{GREEN}USDCNH{
                            RESET
                        }, 4:{CYAN}GBPUSD{RESET}, Or Just {CYAN}Search{
                            RESET
                        } What You want!: "
                    )
                    .upper()
                    .strip()
                )
                # pake symbols
                if userinput in symbols:
                    symbols_name = symbols[userinput]
                    break

                user_srch = mt5.symbol_info(userinput)
                if user_srch is not None:
                    symbols_name = user_srch.name
                    break
                else:
                    print("Currency Pair Not Found...")

            # Main Logic
            print(
                f"Checking The Data of {GREEN}{symbols_name}{
                    RESET
                }... ctrl+C to End this Program.."
            )
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
            print(f"{GREEN}==========================\n{RESET}")
            print(f"{CYAN}Thanks For Using My Program\n{RESET}")
            print(f"{GREEN}===========================\n{RESET}")
            return
    finally:
        mt5.shutdown()


if __name__ == "__main__":
    memixBot()

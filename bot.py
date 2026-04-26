from mt5linux import MetaTrader5
import time
import datetime

# init mt5
mt5 = MetaTrader5()


def bot():
    if not mt5.initialize():
        print("Robot Failed to Connect")
        return
    else:
        print("----------------------------")
        print("Welcome To Mexi Robot v0.1")
        print("----------------------------")
    try:
        usrinpt = int(input("Pilih Mata Uang (USDJPY): 1, (EURUSD): 2, (USDCNH): 3,:"))
        while True:
            if usrinpt == 1:
                tick = mt5.symbol_info_tick("USDJPY")
                if tick:
                    print(
                        f"Harga USDJPY Terbaru pertanggal ",
                        datetime.datetime.now().date(),
                        f"| Bid : {tick.bid} | Ask : {tick.ask}",
                    )
                time.sleep(2)
            if usrinpt == 2:
                tick = mt5.symbol_info_tick("EURUSD")
                if tick:
                    print(
                        f"Harga EURUSD Terbaru pertanggal ",
                        datetime.datetime.now().date(),
                        f"| Bid : {tick.bid} | Ask : {tick.ask}",
                    )
                time.sleep(2)
            if usrinpt == 3:
                tick = mt5.symbol_info_tick("USDCNH")
                if tick:
                    print(
                        f"Harga USDCNH Terbaru pertanggal ",
                        datetime.datetime.now().date(),
                        f"| Bid : {tick.bid} | Ask : {tick.ask}",
                    )
                time.sleep(2)
    except KeyboardInterrupt:
        print(" Gagal Memproses data")
    finally:
        mt5.shutdown()


if __name__ == "__main__":
    bot()

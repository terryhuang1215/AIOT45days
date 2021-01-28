import sys
import time
import gpiozero

RELAY_PIN = 26

# 開始時設定動作狀態為假(GPIO為0, active_high=False) 
# 初始狀態值設定為關閉: (initial_value=False)
relay = gpiozero.OutputDevice(RELAY_PIN, active_high=False, initial_value=False)

def set_relay(status):
    if status:
        print("繼電器導通")
        relay.on()
    else:
        print("繼電器斷路")
        relay.off()

def toggle_relay():
    print("切換繼電器狀態, 開變關, 關變開")
    relay.toggle()

def main_loop():
    # 程式開始, 設定繼電器狀態為假 (GPIO輸出0)
    set_relay(False)
    while 1:
        # 切換繼電器狀態
        toggle_relay()
        # 等待一秒鐘時間 
        time.sleep(1)

if __name__ == "__main__":
    try:
        main_loop()
    except KeyboardInterrupt:
        # 如果按了鍵盤，執行底下的程式片段
        # 繼電器關閉
        set_relay(False)
        print("\n程式結束執行\n")
        # 跳出程式，程式執行結束
        sys.exit(0)



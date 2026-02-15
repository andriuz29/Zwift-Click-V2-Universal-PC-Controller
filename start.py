import asyncio
import time
import pyautogui
from bleak import BleakClient, BleakScanner

DEVICE_NAME_FILTER = "Zwift Click"

NOTIFY_CHAR = "00000002-19ca-4651-86e5-fa29dcdd09d1"
WRITE_CHAR = "00000003-19ca-4651-86e5-fa29dcdd09d1"

# Debounce settings, safe from multiple clicks
last_click_time = 0
DEBOUNCE_DELAY = 0.20

# clicks map
BUTTON_MAP = {
    "2308FFDFFFFF0F": ("PLUS triggers K", "k"), 
    "2308FFFDFFFF0F": ("MINUS triggers I", "i"),
    "2308FEFFFFFF0F": ("LEFT triggers left", "left"), 
    "2308FDFFFFFF0F": ("UP triggers U", "u"),
    "2308FBFFFFFF0F": ("RIGHT triggers right", "right"),
    "2308F7FFFFFF0F": ("DOWN triggers down", "down"),
}
async def notification_handler(sender, data):
    global last_click_time
    hex_data = data.hex().upper()
    
    if hex_data == "2308FFFFFFFF0F" or len(hex_data) > 20:
        return

    current_time = time.time()
    if (current_time - last_click_time) < DEBOUNCE_DELAY:
        return

    if hex_data in BUTTON_MAP:
        btn_name, key_to_press = BUTTON_MAP[hex_data]
        print(f">>> [ {btn_name} ] -> Click: {key_to_press.upper()}")
        
        try:
            pyautogui.press(key_to_press)
        except Exception as e:
            print(f"Klaida spaudžiant klavišą: {e}")
            
        last_click_time = current_time
   # else:
        # prints out not handled buttons
    #    print(f"Unknown: {hex_data}")

async def run():
    print("Searching for Zwift Click...")
    
    device = await BleakScanner.find_device_by_filter(
        lambda d, ad: d.name and DEVICE_NAME_FILTER in d.name
    )

    if not device:
        print("Device not found. Make sure you see blue blinking lights on Zwift Click")
        return

    print(f"Device Found!: {device.name} [{device.address}]")
    
    try:
        async with BleakClient(device.address) as client:
            print(f"Connected: {client.is_connected}")

            await client.start_notify(NOTIFY_CHAR, notification_handler)
            print("Sending activation password")
            await client.write_gatt_char(WRITE_CHAR, bytearray.fromhex("526964654f6e0203"), response=False)
            await asyncio.sleep(0.1)
            await client.write_gatt_char(WRITE_CHAR, bytearray.fromhex("000800"), response=False)
            await asyncio.sleep(0.1)
            await client.write_gatt_char(WRITE_CHAR, bytearray.fromhex("000810"), response=False)

            print("\n--- All ready ---")
            print("Gears: I (-), K (+). Up - hide/show HUD")

            while True:
                if not client.is_connected:
                    print("Disconnected!")
                    break
                
                await client.write_gatt_char(WRITE_CHAR, bytearray.fromhex("000810"), response=False)
                await asyncio.sleep(5)

    except Exception as e:
        print(f"Something wrong: {e}")

if __name__ == "__main__":
    try:
        asyncio.run(run())
    except KeyboardInterrupt:
        print("\nExit.")

import hid
import os
import subprocess
from time import sleep
from datetime import datetime


class SLD:
    def __init__(self, nom, type, ID):
        self.nom = nom
        self.type = type
        self.ID = ID


def find_devices(vendor_id, product_id):
    devices = hid.enumerate()
    sleep(0.2)
    selected_devices = []
    #print(devices)
    for device_info in devices:
        if device_info['vendor_id'] == vendor_id and device_info['product_id'] == product_id:
            selected_devices.append(device_info)
            sleep(0.1)

    return selected_devices

def update_check():
    h = hid.device()
    VID = 0x1EFB
    PID = 0x1590

    selected_devices = find_devices(VID, PID)
    if selected_devices:
        print("device found")
        for device in selected_devices:
            answer = [0, 0, 0, 0, 0, 0, 0, 0, 0]
            Manufacturer = device['manufacturer_string']
            sleep(0.2)
            Product = device['product_string']
            sleep(0.2)
            Release = device['serial_number']
            sleep(0.2)
            print(f"\n Manufacturer: {Manufacturer} ")
            print(f"\n Product: {Product} ")
            print(f"\n Release: {Release} ")
    with open("/home/tester/Desktop/Slider_updated.txt", "a") as log:
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_message = f"{current_time} - Manufacturer: {Manufacturer}, Product: {Product}, Release: {Release}\n"
        log.write(log_message)
    
def flash_firmware(bin_file):
    commande = [
    'dfu-util',
    '-a', '0',
    '-s', '0x08000000:leave',
    '-D', bin_file
    ]
    #print("commande:", commande)
    answer = subprocess.run(commande, capture_output=True, text=True)
    print("output:")
    print(answer.stdout)
    print("Error:")
    print(answer.stderr)
    
def DFU_mode():
    h = hid.device()
    VID = 0x1EFB
    PID = 0x1590

    selected_devices = find_devices(VID, PID)
    if selected_devices:
        print("device found")
        for device in selected_devices:
            answer = [0, 0, 0, 0, 0, 0, 0, 0, 0]
            device_ID = device['path']
            print("device path: ", device_ID)

            try:
                print("try to open")
                sleep(0.2)
                h.open_path(device_ID)
                print("path open")
                h.set_nonblocking(1)
                h.write(b'\x00\x00\x03')  # commande for read serial number 
                sleep(0.2)
                data = h.read(64)
                dataByte = bytes(data)
                serial_number = dataByte[3:11]
                serial_number = serial_number.decode('utf-8')
                serial_number = bytes.fromhex(serial_number)
                print('serial_number = ', serial_number)
                cmd = b"".join([b'\x00\xFF\xFF', serial_number])
                h.write(cmd)  # commande for start dfu 
                sleep(10)
                DFU = subprocess.run("dfu-util --list", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                print("DFU avalaible :", DFU.stdout)
            except Exception as e:
                print(f"Erreur : {e}")
            finally:
                h.close()
    else:   
        print("No devices found with the specified VID and PID")

if __name__ == "__main__":
    DFU_mode()
    firmware_file = "/home/tester/Desktop/KNX_updater/TA-SLIDER-160-KNX-R24-v0.4.11.bin"
    flash_firmware(firmware_file)
    sleep(2)
    update_check()
    print("\nPress 'Enter' to update slider or 'esc' to quit...\n")
    

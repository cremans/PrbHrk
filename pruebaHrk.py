import time
import psutil

print("Numero de nucleos CPU: " + str(psutil.cpu_count()))
print("Numero de Threads: " + str(psutil.cpu_count(logical=False)))

dat_freq = psutil.cpu_freq()
print("Frecuencia del CPU: %.2f" %(dat_freq.current/1000))
dat_ram = psutil.virtual_memory()
print("Memoria RAM: %.2f" %(dat_ram.total/1024/1024/1024))

print("Particiones de disco: \n\n")
particiones = psutil.disk_partitions()

for particion in particiones:
    print("Device: " + particion.device)
    print("Mountpoint: " + particion.mountpoint)
    dat_almc = psutil.disk_usage(particion.mountpoint)
    print("Almacenamiento Total: %.2f GB" %(dat_almc.total/1024/1024/1024))
    print("Almacenamiento Usado: %.2f GB" %(dat_almc.used/1024/1024/1024))
    print("Almacenamiento Libre: %.2f GB" %(dat_almc.free/1024/1024/1024))
    print("\n")

for i in range(20):
    print(str(i))
    time.sleep(1)

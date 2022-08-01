from pyshorteners import Shortener
from colorama import Back as b, Fore as f
from subprocess import call
from qrcode import make 
from time import strftime
from platform import system
import sys

my_os = system()
command_clear = ""

if my_os == "Linux":
    command_clear = "clear"
elif my_os == "Windows":
    command_clear = "cls"
elif my_os == "Darwin":
    command_clear = "clear"
else:
    command_clear = "clear"

def banner():
    print(f.YELLOW + "┈" + f.RED + "┏━━━━━━┓" + f.YELLOW + "┈┈┈┈┈╭--[URLsource]")
    print(f.YELLOW + "┈┈" + f.RED + "▏" + f.YELLOW + "╱╱╱╱" + f.RED + "▕" + f.YELLOW + "┈┈┈┈┈╭╯")
    print(f.YELLOW + "┈" + f.RED + "━╋━┻━┻╋━" + f.YELLOW + "┈┈╭---[NOT-RISKS]")
    print(f.YELLOW + "┈" + f.RED + "╭┫" + f.YELLOW + "▊┃┃▊" + f.RED + "┣╮" + f.YELLOW + "┈╭╯")
    print(f.YELLOW + "┈" + f.RED + "┃┃" + f.YELLOW + "▔" + f.RED + "╰╯" + f.YELLOW + "▔" + f.RED + "┃┃" + f.YELLOW + "╭╯-----[VERSION_v1]")
    print(f.YELLOW + "┈" + f.RED + "╰┫┏━━▂▂▂█")
    print(f.YELLOW + "┈┈" + f.RED + "╭╰━━╯╮")

# ==================/To shorten url // Acortar url/==================
def short_url():
    banner()
    print(f.YELLOW + "========================================>>\n" + f.GREEN + "Seleccione un servicio para acortar la URL" + f.YELLOW+ "\n========================================>>")
    print(f.YELLOW + "[" + f.RED + "01" + f.YELLOW + "]-" + f.GREEN + "Chilp.it" + f.YELLOW + "         [" + f.RED + "02" + f.YELLOW + "]-" + f.GREEN + "Clck.ru") 
    print(f.YELLOW + "[" + f.RED + "03" + f.YELLOW + "]-" + f.GREEN + "Da.gd" + f.YELLOW + "            [" + f.RED + "04" + f.YELLOW + "]-" + f.GREEN + "Is.gd") 
    print(f.YELLOW + "[" + f.RED + "05" + f.YELLOW + "]-" + f.GREEN + "Os.db" + f.YELLOW + "            [" + f.RED + "06" + f.YELLOW + "]-" + f.GREEN + "Salir")
    option_shorturl = input(f.YELLOW + "[" + f.RED + "URLsource" + f.YELLOW + "]" + f.GREEN + ">> ")

    obj_short = Shortener()
    
    if option_shorturl == "01" or option_shorturl == "1":
        print(f.YELLOW + "\n========================================>>\n" + f.GREEN + "Introduzca la URL a acortar" + f.YELLOW + "\n========================================>>")
        no_process_url_short = input(f.YELLOW + "[" + f.RED + "URLsource" + f.YELLOW + "]" + f.GREEN + ">> ")
        try:
            process_url_short = obj_short.chilpit.short(no_process_url_short)
        except:
            print("\n[!] Este servicio no esta disponible ahora, pruebe con otro, precione ENTER para continuar")
            input()
            call(command_clear, shell=True)
            short_url()
        print(f.YELLOW + "\n[" + f.RED + "!" + f.YELLOW + "]" + f.GREEN + " La URL acortada por Chilp.it: " + f.RED + process_url_short)
        input(f.YELLOW + "[" + f.RED + "!" + f.YELLOW + "]" + f.GREEN + " Precione" + f.RED + " ENTER " + f.GREEN + "para volver al inicio.")
        cuestions_initials()

    elif option_shorturl == "02" or option_shorturl == "2":
        print(f.YELLOW + "\n========================================>>\n" + f.GREEN + "Introduzca la URL a acortar" + f.YELLOW + "\n========================================>>")
        no_process_url_short = input(f.YELLOW + "[" + f.RED + "URLsource" + f.YELLOW + "]" + f.GREEN + ">> ")
        
        try:
            process_url_short = obj_short.clckru.short(no_process_url_short)
        
        except:
            print("\n[!] Este servicio no esta disponible ahora, pruebe con otro, precione ENTER para continuar")
            input()
            call(command_clear, shell=True)
            short_url()
            
        print(f.YELLOW + "\n[" + f.RED + "!" + f.YELLOW + "]" + f.GREEN + " La URL acortada por Clck.ru: " + f.RED + process_url_short)
        input(f.YELLOW + "[" + f.RED + "!" + f.YELLOW + "]" + f.GREEN + " Precione" + f.RED + " ENTER " + f.GREEN + "para volver al inicio.")
        cuestions_initials()

    elif option_shorturl == "03" or option_shorturl == "3":
        print(f.YELLOW + "\n========================================>>\n" + f.GREEN + "Introduzca la URL a acortar" + f.YELLOW + "\n========================================>>")
        no_process_url_short = input(f.YELLOW + "[" + f.RED + "URLsource" + f.YELLOW + "]" + f.GREEN + ">> ")
        
        try:
            process_url_short = obj_short.dagd.short(no_process_url_short)
        
        except:
            print("\n[!] Este servicio no esta disponible ahora, pruebe con otro, precione ENTER para continuar")
            input()
            call(command_clear, shell=True)
            short_url()
            
        print(f.YELLOW + "\n[" + f.RED + "!" + f.YELLOW + "]" + f.GREEN + " La URL acortada por Da.gd: " + f.RED + process_url_short)
        input(f.YELLOW + "[" + f.RED + "!" + f.YELLOW + "]" + f.GREEN + " Precione" + f.RED + " ENTER " + f.GREEN + "para volver al inicio.")
        cuestions_initials()

    elif option_shorturl == "04" or option_shorturl == "4":
        print(f.YELLOW + "\n========================================>>\n" + f.GREEN + "Introduzca la URL a acortar" + f.YELLOW + "\n========================================>>")
        no_process_url_short = input(f.YELLOW + "[" + f.RED + "URLsource" + f.YELLOW + "]" + f.GREEN + ">> ")
        
        try:
            process_url_short = obj_short.isgd.short(no_process_url_short)
        
        except:
            print("\n[!] Este servicio no esta disponible ahora, pruebe con otro, precione ENTER para continuar")
            input()
            call(command_clear, shell=True)
            short_url()
            
        print(f.YELLOW + "\n[" + f.RED + "!" + f.YELLOW + "]" + f.GREEN + " La URL acortada por Is.gd: " + f.RED + process_url_short)
        input(f.YELLOW + "[" + f.RED + "!" + f.YELLOW + "]" + f.GREEN + " Precione" + f.RED + " ENTER " + f.GREEN + "para volver al inicio.")
        cuestions_initials()

    elif option_shorturl == "05" or option_shorturl == "5":
        print(f.YELLOW + "\n========================================>>\n" + f.GREEN + "Introduzca la URL a acortar" + f.YELLOW + "\n========================================>>")
        no_process_url_short = input(f.YELLOW + "[" + f.RED + "URLsource" + f.YELLOW + "]" + f.GREEN + ">> ")
        
        try:
       	    process_url_short = obj_short.osdb.short(no_process_url_short)
        
        except:
            print("\n[!] Este servicio no esta disponible ahora, pruebe con otro, precione ENTER para continuar")
            input()
            call(command_clear, shell=True)
            short_url()
            
        print(f.YELLOW + "\n[" + f.RED + "!" + f.YELLOW + "]" + f.GREEN + " La URL acortada por Os.db: " + f.RED + process_url_short)
        input(f.YELLOW + "[" + f.RED + "!" + f.YELLOW + "]" + f.GREEN + " Precione" + f.RED + " ENTER " + f.GREEN + "para volver al inicio.")
        cuestions_initials()
        
    elif option_shorturl == "06" or option_shorturl == "6":
        call(command_clear, shell=True); sys.exit()

    else:
        input(f.YELLOW + "\n[" + f.RED + "!" + f.YELLOW + "]" + f.GREEN + " La opcion seleccionada no existe, precione" + f.RED + " ENTER " + f.GREEN + "para volver a intentar.")
        call(command_clear, shell=True)
        short_url()


# ==================/To detect shortened url // Detectar url acortada/==================
def detect_url_short():
    banner()
    print(f.YELLOW + "========================================>>\n" + f.GREEN + "Introduzca la URL para analizar" + f.YELLOW + "\n========================================>>")
    no_process_url_detect = input(f.YELLOW + "[" + f.RED + "URLsource" + f.YELLOW + "]" + f.GREEN + ">> ")
    
    obj_short = Shortener()

    try:
        process_url_detect = obj_short.chilpit.expand(no_process_url_detect)
        print(f.YELLOW + "\n[" + f.RED + "!" + f.YELLOW + "]" + f.GREEN + " La URL original es: " + f.RED + process_url_detect)
        input(f.YELLOW + "[" + f.RED + "!" + f.YELLOW + "]" + f.GREEN + " Precione" + f.RED + " ENTER " + f.GREEN + "para volver al inicio.")
        cuestions_initials()
    except:
        input(f.YELLOW + "\n[" + f.RED + "!" + f.YELLOW + "]" + f.GREEN + " La URL no existe, precione" + f.RED + " ENTER " + f.GREEN + "para volver a intentar.")
        call(command_clear, shell=True)
        detect_url_short()


# ==================/To generate qr starting from url // Generar qr a partir de url/==================
def generate_qr():
    banner()
    print(f.YELLOW + "========================================>>\n" + f.GREEN + "Introduzca la URL para generar el QR" + f.YELLOW + "\n========================================>>")
    url_qr = input(f.YELLOW + "[" + f.RED + "URLsource" + f.YELLOW + "]" + f.GREEN + ">> ")

    hour_now = strftime("%H_%M_%S")
    file_name = hour_now + ".jpg"

    img_qr = make(url_qr)

    img_qr.save(f"images_qr/{file_name}")
    print(f.YELLOW + "\n[" + f.RED + "!" + f.YELLOW + "]" + f.GREEN + " EL codigo QR fue guardado en un archivo (.jpg) en la carpeta 'images_qr' con el nombre de:", hour_now,".jpg")
    input(f.YELLOW + "[" + f.RED + "!" + f.YELLOW + "]" + f.GREEN + " Precione" + f.RED + " ENTER " + f.GREEN + "para volver al inicio.")
    cuestions_initials()


def cuestions_initials():
    call(command_clear, shell=True)
    banner()
    print(f.YELLOW + "[" + f.RED + "01" + f.YELLOW + "]-" + f.GREEN + "Acortar URL" + f.YELLOW + "\n[" + f.RED + "02" + f.YELLOW + "]-" + f.GREEN + "Detectar acortador de URL"  + f.YELLOW +  "\n[" + f.RED + "03" + f.YELLOW + "]-" + f.GREEN + "Sacar QR de URL" + f.YELLOW + "\n[" + f.RED + "04" + f.YELLOW + "]-" + f.GREEN + "Salir")
    option_initial = input(f.YELLOW + "[" + f.RED + "URLsource" + f.YELLOW + "]" + f.GREEN + ">> ")

    if option_initial == "01" or option_initial == "1":
        call(command_clear, shell=True)
        short_url()
    
    elif option_initial == "02" or option_initial == "2":
        call(command_clear, shell=True)
        detect_url_short()

    elif option_initial == "03" or option_initial == "3":
        call(command_clear, shell=True)
        generate_qr()

    elif option_initial == "04" or option_initial == "4":
        call(command_clear, shell=True); sys.exit()

    else:
        input(f.YELLOW + "\n[" + f.RED + "!" + f.YELLOW + "]" + f.GREEN + " La opcion seleccionada no existe, precione" + f.RED + " ENTER " + f.GREEN + "para volver a intentar.")
        call(command_clear, shell=True)
        cuestions_initials()

cuestions_initials()

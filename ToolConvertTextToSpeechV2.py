#!/usr/bin/env python3


def Tool_Convert_Text_To_Speech_Version_2(created_by="Ruben Leonardo Sigalingging."):
	from os import system
	from pyfiglet import figlet_format
	import pyttsx3
	system("clear")
	system("pip install pyttsx3")
	system("pip install pyfiglet")
	system("pip install gTTS")
	system("clear")


	tampilan=figlet_format("gTTS",font="slant")
	print(tampilan)
	print("[!] Dibuat Oleh: Ruben Leonardo Sigalingging.")
	print("[!] Dibuat Pada: Rabu, 29 Juni 2022, Pukul 1:08 PM")
	print("[!] Fungsi: Untuk Mengkonversi Teks Ke Audio.\n")


	# Buat Variabel Untuk Menampung Fungsi Modul 
	from gtts import gTTS
	print("\n")
	hal_yang_ingin_diucapkan=str(input("[!] Kalimat Yang Ingin Dijadikan Audio: "))
	print("\n")
	konversi_ke_audio=gTTS(hal_yang_ingin_diucapkan)
	nama_file_audionya=input("[!] Nama File Audionya: ")
	print("\n")
	konversi_ke_audio.save(nama_file_audionya)
Tool_Convert_Text_To_Speech_Version_2()
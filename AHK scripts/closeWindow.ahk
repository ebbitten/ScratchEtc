;
; AutoHotkey Version: 1.x
; Language:       English
; Platform:       Windows XP+
; Author:         Cyborg Commando
;
; Script Function:
;	This script will detect when the TeamViewer "Sponsored Session: Thanks for playing fair!" message box pops up and 
;	close it automatically.
;
;	This script is not to discourage paying for TeamViewer but to provide anonmyity in sensitive situations such as
;	recovering a stolen laptop, etc.
;
;	This script will run best when it is compiled and placed in the Windows startup folder.
;	You can find the startup folder for all users here:
;		WinXP: C:\Documents and Settings\All Users\Start Menu\Programs\Startup
;		Win 7: C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup
;
 
#Persistent			; This keeps the script running permanently.

#SingleInstance			; Only allows one instance of the script to run.
 
IfWinExist, Sponsored session
	WinClose 		; When this script detects the TeamViewer "Thanks for playing fair!" pop up it closes it.
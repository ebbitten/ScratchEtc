;logout
;you can add #IfWinActive ahk_class PuTTY to make it apply to only PuTTY windows
;...the script sends Shift + F7 a few times, then quit, then h twice, then exit.
#IfWinActive ahk_class PuTTY
esc::

   Send +{F7}
   Send +{F7}
   Send +{F7}
   Send +{F7}
   Send +{F7}
   Send +{F7}
   Sleep,500
   Send quit{Enter}
   Sleep,500
   Send h{Enter}
   Sleep,500
   Send h{Enter}
   Sleep,500
   Send q{ENTER}
   Sleep,500
   Send q{ENTER}
   Sleep,500
return
   Send exit{Enter}
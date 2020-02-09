;~ ; Copyright (C) 2008-2015 Epic Systems Corporation
;*********************************************************************
; TITLE:   PuttyPaste.ahk
; PURPOSE: PuTTY I/O Stream is asynchronous with the content of the screen.  This script will "paste" the commands 1 at a time from the clipboard and then pause after each line.
;                                               The script should only insert the pauses for PuTTY, otherwise it should just paste normally.
; TRIGGER: In main script, use #import PuttyPaste.ahk
; AUTHOR:  Dave Palay
; REVISION HISTORY:
; *dpalay 4/22/15 - Created
;*********************************************************************
SetTitleMatchMode, 2

^+z::
IfWinActive, UNIVERSITY OF MISSISSIPPI MEDICAL CENTER SUP
{
                loop, parse, clipboard, `n
                {
                                SendRaw, %A_LoopField%
                                Sleep 100
                }
}
else
                Send ^v
return


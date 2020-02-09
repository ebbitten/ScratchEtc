;Check if copied SU is in environment
^s::
clipboard= w $$isPkgInstalled{^}`%ZaHRS7("%clipboard%")
Send %clipboard%{Enter}
return
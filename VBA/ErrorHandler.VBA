Function AddOlTask(sSubject As String, sBody As String, _
                    dtDueDate As Date, _
                    dtReminderDate As Date, sImportance As Integer, sStartDate As Date)
On Error GoTo Error_Handler
 
    Const olTaskItem = 3
    Dim OlApp As Object
    Dim OlTask As Object
 
    Set OlApp = CreateObject("Outlook.Application")
    Set OlTask = OlApp.CreateItem(olTaskItem)
 
    With OlTask
        .Subject = sSubject
        .DueDate = dtDueDate
        .Status = 0                 '0=not started, 1=in progress, 2=complete, 3=waiting,
                                    '4=deferred
        .Importance = sImportance             '0=low, 1=normal, 2=high
        .ReminderSet = True
        .ReminderTime = dtReminderDate
        .StartDate = sStartDate
        .Body = sBody
        .Save   'use .Display if you wish the user to see the task form and make
                'them perform the save
    End With
 
Error_Handler_Exit:
    On Error Resume Next
    Set OlTask = Nothing
    Set OlApp = Nothing
    Exit Function
 
Error_Handler:
    MsgBox "The following error has occured" & vbCrLf & vbCrLf & "Error Number: " & _
    Err.Number & vbCrLf & "Error Source: AddOlkTask" & vbCrLf & "Error Description: " & _
    Err.Description, vbCritical, "An Error has Occured!"
    Resume Error_Handler_Exit
End Function


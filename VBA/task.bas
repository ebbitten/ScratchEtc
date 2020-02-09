Attribute VB_Name = "Module3"
Public tFolder As String

Private Sub CreateTasks()
      
Dim Ns As Outlook.NameSpace
Dim olTask As Outlook.TaskItem
Dim Item As Outlook.MailItem

Set Ns = Application.GetNamespace("MAPI")

' Get Function athttp://slipstick.me/e8mio
Set Item = GetCurrentItem()

Set taskFolder = Ns.GetDefaultFolder(olFolderTasks).Folders(tFolder)
Set olTask = taskFolder.Items.Add(olTaskItem)
With olTask
        .Subject = Item.Subject
        .Attachments.Add Item
        .Body = Item.Body
        .DueDate = Now + 1
        .Save
        .Display 'show the task to add notes
End With
Set Ns = Nothing
End Sub

' create one macro for Tasks each folder
' add to ribbon or QAT button
Sub TasksFoldername1()
tFolder = "My Tasks"
CreateTasks
End Sub

Sub TasksFoldername2()
tFolder = "Old Tasks"
CreateTasks
End Sub


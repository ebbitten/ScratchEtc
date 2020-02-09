VERSION 1.0 CLASS
BEGIN
  MultiUse = -1  'True
END
Attribute VB_Name = "ThisOutlookSession"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = True
Public Sub ReplyBySpecAccount()
Dim oAccount As Outlook.Account
Dim oMail As Outlook.MailItem
  
For Each oAccount In Application.Session.Accounts
If oAccount.DisplayName = "ahelitzer@mba2019.hbs.edu" Then
    Set oMail = Application.ActiveExplorer.Selection(1).Reply
      oMail.SendUsingAccount = oAccount
    oMail.Display
End If
Next
  
End Sub
Public Sub ReplyAllBySpecAccount()
Dim oAccount As Outlook.Account
Dim oMail As Outlook.MailItem
Dim Recipients As Outlook.Recipients
Dim aRecipient As Outlook.Recipient
  
For Each oAccount In Application.Session.Accounts
If oAccount.DisplayName = "ahelitzer@mba2019.hbs.edu" Then
    Set oMail = Application.ActiveExplorer.Selection(1).ReplyAll
      oMail.SendUsingAccount = oAccount
      oMail.Display
      Set Recipients = oMail.Recipients
      For i = Recipients.Count To 1 Step -1
        Set aRecipient = Recipients.Item(i)
        If aRecipient = "Ahelitzer@mba2019.hbs.edu" Or aRecipient = "Helitzer, Adam" Then
            Recipients.Remove i
            Exit For
        End If
      Next
      
End If
Next

End Sub


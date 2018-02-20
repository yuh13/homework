Sub HomeworkVBA2()

'set variables for ticker, volume, and year prices
Dim ws As Worksheet
'---
Dim sTicker As String
Dim volTotal As Double
'---
Dim finalTableRow As Integer
Dim yStart As Double
Dim yEnd As Double
Dim yChange As Double
Dim yPercChange As Double
'---
Dim lastRow As Double
Dim lastcolumn As Double
Dim lastSrow As Double
Dim gIncrease As Double
Dim gIncreaseT As String
Dim gDecrease As Double
Dim gDecreaseT As String
Dim gVolume As Double
Dim gVolumeT As String


    
'loop through all sheets
For Each ws In Worksheets

    'Find Last Rows and Columns

    lastRow = ws.Cells(Rows.Count, 1).End(xlUp).Row
    lastcolumn = ws.Cells(1, Columns.Count).End(xlToLeft).Column
    

    'create final table greatest variables
    gIncrease = 0
    gDecrease = 0
    gVolume = 0
    finalTableRow = 0
    
    'Create Summary Table Header and row marker
    finalTableRow = 3
    ws.Cells(2, (lastcolumn + 2)).Value = "Ticker"
    ws.Cells(2, (lastcolumn + 3)).Value = "Total Stock Volume"
    ws.Cells(2, (lastcolumn + 4)).Value = "Yearly Change"
    ws.Cells(2, (lastcolumn + 5)).Value = "Percent Change"
    
    
    'Loop through all stock tickers
    i = 2
    For i = 2 To lastRow
        If ws.Cells(i - 1, 1).Value <> ws.Cells(i, 1).Value Then
            yStart = ws.Cells(i, 3).Value
            If yStart = 0 Then
                Dim w As Double
                w = i
                While yStart = 0 And ws.Cells(w, 1).Value = ws.Cells(w + 1, 1).Value
                    yStart = ws.Cells(w + 1, 3).Value
                    w = w + 1
                 Wend
            End If
        End If
    
        If ws.Cells(i + 1, 1).Value <> ws.Cells(i, 1).Value Then
            sTicker = ws.Cells(i, 1).Value
            volTotal = volTotal + ws.Cells(i, 7).Value
            yEnd = ws.Cells(i, 6).Value
            yChange = yEnd - yStart
            yPercChange = (100 * yEnd / yStart) - 100
            ws.Cells(finalTableRow, (lastcolumn + 2)).Value = sTicker
            ws.Cells(finalTableRow, (lastcolumn + 3)).Value = volTotal
            ws.Cells(finalTableRow, (lastcolumn + 4)).Value = yChange
            ws.Cells(finalTableRow, (lastcolumn + 5)).Value = yPercChange
            finalTableRow = finalTableRow + 1
            volTotal = 0
        Else
            volTotal = volTotal + ws.Cells(i, 7).Value
        End If
        Next i
    
    'set last summary table row
    lastSrow = ws.Cells(Rows.Count, (lastcolumn + 2)).End(xlUp).Row

    'set loop to color Percent Change column in summary table
    x = 3
    For x = 3 To lastSrow
        If ws.Cells(x, (lastcolumn + 5)).Value > 0 Then
            ws.Cells(x, (lastcolumn + 5)).Interior.ColorIndex = 4
        ElseIf ws.Cells(x, (lastcolumn + 5)).Value < 0 Then
            ws.Cells(x, (lastcolumn + 5)).Interior.ColorIndex = 3
        End If
    Next x

    'Store greatest values in variable
    j = 3
    For j = 3 To lastSrow
        If ws.Cells(j, lastcolumn + 5).Value > gIncrease Then
            gIncrease = ws.Cells(j, lastcolumn + 5).Value
            gIncreaseT = ws.Cells(j, lastcolumn + 2).Value
        End If
        If ws.Cells(j, lastcolumn + 5) < gDecrease Then
            gDecrease = ws.Cells(j, lastcolumn + 5).Value
            gDecreaseT = ws.Cells(j, lastcolumn + 2).Value
        End If
        If ws.Cells(j, lastcolumn + 3).Value > gVolume Then
            gVolume = ws.Cells(j, lastcolumn + 3).Value
            gVolumeT = ws.Cells(j, lastcolumn + 2).Value
        End If
    Next j
        
    'Fill FinalTable
    ws.Cells(2, (lastcolumn + 8)).Value = "Ticker"
    ws.Cells(2, (lastcolumn + 9)).Value = "Value"
    ws.Cells(3, (lastcolumn + 7)).Value = "Greatest % Increase"
    ws.Cells(4, (lastcolumn + 7)).Value = "Greatest % Decrease"
    ws.Cells(5, (lastcolumn + 7)).Value = "Highest Volume"
    ws.Cells(3, lastcolumn + 8).Value = gIncreaseT
    ws.Cells(4, lastcolumn + 8).Value = gDecreaseT
    ws.Cells(5, lastcolumn + 8).Value = gVolumeT
    ws.Cells(3, lastcolumn + 9).Value = gIncrease
    ws.Cells(4, lastcolumn + 9).Value = gDecrease
    ws.Cells(5, lastcolumn + 9).Value = gVolume
    
    
Next ws

End Sub






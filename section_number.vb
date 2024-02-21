Sub section_number()

    Set pres = Application.ActivePresentation
    Page_Count = pres.Slides.Count
    
    
    For i = 2 To Page_Count
    
        Set Current_Slide = pres.Slides(i)
        
        If ShapeExists(Current_Slide, "Section Number") Then Current_Slide.Shapes("Section Number").Delete
        
        Current_Slide.Shapes.AddShape(msoShapeRectangle, 775, 511, 215, 29).Name = "Section Number"
        Current_Slide.Shapes("Section Number").Fill.Transparency = 1
        Current_Slide.Shapes("Section Number").Line.Transparency = 1
        
        Current_Slide.Shapes("Section Number").TextFrame.TextRange.Text = Current_Slide.sectionIndex
        
        With Current_Slide.Shapes("Section Number").TextFrame.TextRange.Font
        
            .Name = "CMU Serif"
            .Size = 12
            .Color.RGB = RGB(58, 49, 112)
        
        End With
        
    
    Next




End Sub

Private Function ShapeExists(ByVal oSl As Slide, ByVal ShapeName As String) As Boolean
        Dim oSh As Shape
        For Each oSh In oSl.Shapes
          If oSh.Name = ShapeName Then
             ShapeExists = True
             Exit Function
          End If
        Next ' Shape
        ' No shape here, so though it's not strictly necessary:
        ShapeExists = False
    End Function

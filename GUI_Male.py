# -------------------------------------------------------------------------------------------------------------------------------
# Gluonix Runtime
# -------------------------------------------------------------------------------------------------------------------------------
#################################################################################################################################
if __name__=='__main__':
    from Nucleon.Runner import * ###!REQUIRED ------- Any Script Before This Won't Effect GUI Elements
#################################################################################################################################
#################################################################################################################################
# -------------------------------------------------------------------------------------------------------------------------------
# Developer Programming Start
# -------------------------------------------------------------------------------------------------------------------------------

    import Database_control as DB

    global sucess, scereen
    sucess=False
    scereen=""

    def Contniue_save(E,VALS):
        Root.SaveConform.Show()
        Root.SaveConform.Text="Saved contact"

    def info(E,VALS):
        Root.List.Hide()
        Root.Info.Show()
        Root.Save1.Show()
        Root.Save2.Show()
        Root.Back.Show()
    
    def search(E,VALS, SearchE):
        search_val=SearchE.Get()
        for i in range(len(VALS)):
            if VALS[i][1]==search_val:
                Root.List.NameList.clear()
                Root.List.StateList.clear()
                Root.List.NameList.append(VALS[i][0])
                Root.List.StateList.append(VALS[i][11])
            elif VALS[i][2]==search_val:
                Root.List.NameList.clear()
                Root.List.StateList.clear()
                Root.List.NameList.append(VALS[i][0])
                Root.List.StateList.append(VALS[i][11])
            elif VALS[i][5]==search_val:
                Root.List.NameList.clear()
                Root.List.StateList.clear()
                Root.List.NameList.append(VALS[i][0])
                Root.List.StateList.append(VALS[i][11])
            elif VALS[i][6]==search_val:
                Root.List.NameList.clear()
                Root.List.StateList.clear()
                Root.List.NameList.append(VALS[i][0])
                Root.List.StateList.append(VALS[i][11])
            elif VALS[i][7]==search_val:
                Root.List.NameList.clear()
                Root.List.StateList.clear()
                Root.List.NameList.append(VALS[i][0])
                Root.List.StateList.append(VALS[i][11])
            elif VALS[i][8]==search_val:
                Root.List.NameList.clear()
                Root.List.StateList.clear()
                Root.List.NameList.append(VALS[i][0])
                Root.List.StateList.append(VALS[i][11])
            elif VALS[i][9]==search_val:
                Root.List.NameList.clear()
                Root.List.StateList.clear()
                Root.List.NameList.append(VALS[i][0])
                Root.List.StateList.append(VALS[i][11])
    
    
    def pending(sucess, scereen):
        if sucess == True and scereen == "Pending":
            Root.Login.Hide()
            Root.List.Show()
            Root.Title.Show()
            Root.Contniue.Show()
            Root.ContniueBT.Show()
            Root.Regect.Show()
            Root.RejectBT.Show()
            Root.Search.Show()
            Root.SearchE.Show()
            Root.SearchBT.Show()
            value = DB.get_sheet_vals(DB.sheet_id)
            VALS = DB.get_raw_data(value)


    

    def Login(E):  
    
        print("DEBUG: Login button clicked!")  
        
        User = Root.Login.UsernameE.Get()
        Pass = Root.Login.PasswordE.Get()
        
        if User == "test" and Pass == "1234":
            global sucess, scereen
            sucess=True
            scereen="Pending"
        else:
            Root.Login.ERROR.Show()



    Root.List.Hide()
    Root.Info.Hide()
    Root.Save1.Hide()
    Root.Save2.Hide()
    Root.Back.Hide()
    Root.Login.ERROR.Hide()
    Root.Title.Hide()
    Root.Contniue.Hide()
    Root.ContniueBT.Hide()
    Root.Regect.Hide()
    Root.RejectBT.Hide()
    Root.Search.Hide()
    Root.SearchE.Hide()
    Root.SearchBT.Hide()
    Root.SaveConform.Hide()

    go=Root.Login.Enter.Bind(On_Click=Login)


# -------------------------------------------------------------------------------------------------------------------------------
# Developer Programming End
# -------------------------------------------------------------------------------------------------------------------------------
#################################################################################################################################
#################################################################################################################################
    Root.Start() ###!REQUIRED ------- Any Script After This Will Not Execute
#################################################################################################################################
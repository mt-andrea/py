class Tanulo:
    def __init__(self,nev,word,excel,ppt,html,access):
        self.nev=nev
        self.word=word
        self.excel=excel
        self.ppt=ppt
        self.html=html
        self.access=access
    
    def kimenet(self):
        avg=(self.access+self.excel+self.word+self.html+self.ppt)/5
        if self.word==1 or self.access==1 or self.excel==1 or self.ppt==1 or self.html==1:
            kim=str(avg)+" évismétlés"
        elif avg>4.5:
            kim=str(avg)+" kiváló"
        else:
            kim=str(avg)+" megfelelt"
        return kim
        
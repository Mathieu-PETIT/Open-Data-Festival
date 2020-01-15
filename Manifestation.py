class Manifestation():
    def __init__(self,nom,code,site,date_d,date_f,com,dom):
        self.nom=nom
        self.code=code
        self.site=site
        self.date_d=date_d
        self.date_f=date_f
        self.com=com
        self.dom=dom

    def get_nom(self):
        return self.nom
    def get_code(self):
        return self.code
    def get_site(self):
        return self.site
    def get_date_d(self):
        return self.date_d
    def get_date_f(self):
        return self.date_f
    def get_com(self):
        return self.com
    def get_dom(self):
        return self.dom

    def set_nom(self,nom):
        self.nom=nom
    def set_code(self,code):
        self.code=code
    def set_site(self,site):
        self.site=site
    def set_date_d(self,date_d):
        self.date_d=date_d
    def set_date_f(self,date_f):
        self.date_f=date_f
    def set_com(self,com):
        self.com=com
    def set_dom(self,dom):
        self.dom=dom

class Socio:

    def __init__(self, idSocio=None, uid='', ci='', foto=None, fechaIngreso=None, estado=''):
        self.idSocio      = idSocio
        self.uid          = uid
        self.ci           = ci
        self.foto         = foto
        self.fechaIngreso = fechaIngreso
        self.estado       = estado

    def missingAttributes(self, socio):
        listaAtributos = []
        if self.uid != socio.uid:
            listaAtributos.append("uid")
        if self.foto != socio.foto:
            listaAtributos.append("foto")
        if self.estado is not socio.estado:
            listaAtributos.append("estado")                                    
        return listaAtributos

    def __str__(self):
        return ("SOCIO".center(25, '_')+"\nI.D.\t     : "+str(self.idSocio)+"\nUID\t     : "+str(self.uid)+"\nC.I.\t     : "+str(self.ci)+"\nFOTO\t     : "+str(self.foto)+"\nFECHA INGRESO: "+str(self.fechaIngreso)+"\nESTADO       : "+str(self.estado)+"\n"+"-".center(25, '-'))
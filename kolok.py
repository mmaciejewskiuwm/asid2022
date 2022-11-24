from typing import Any


class ListaWpis:
    wart: Any
    nast: 'ListaWpis'
    poprz: 'ListaWpis'
    def __init__(self, wart: Any, nast: 'ListaWpis' = None, poprz: 'ListaWpis' = None):
        self.wart = wart
        self.poprz = poprz
        self.nast = nast

    def dodaj_po_nim(self, wart: Any):
        temp = ListaWpis(wart)
        if self.nast is self:
            temp.poprz = self
            temp.nast = None
            self.nast = temp
            return None
        if self.nast is None:
            temp.poprz = self
            temp.nast = None
            self.nast = temp

            return None

        temp.poprz = self
        temp.nast = self.nast
        self.nast.poprz = temp
        self.nast = temp

    def dodaj_przed_nim(self, wart: Any):
        if self.nast is self:
            self.dodaj_po_nim(wart)
            return None
        temp = ListaWpis(wart)
        temp.poprz = self.poprz
        temp.nast = self
        self.poprz.nast = temp
        self.poprz = temp


class Lista_2k_1w:
    def __init__(self):
        self.wartow = ListaWpis('wartow')
        self.wartow.nast = self.wartow
        self.wartow.poprz = self.wartow

    def ostatni_el(self) -> ListaWpis:
        if self.wartow.nast is self.wartow:
            return self.wartow
        else:
            koniec = self.wartow
            while koniec.nast is not None:
                koniec = koniec.nast
            return koniec

    def pierwszy_el(self) -> ListaWpis:
        return self.wartow.nast

    def pobierz_el(self, idx: int) -> ListaWpis:
        temp = self.pierwszy_el()
        counter = 0
        while temp:
            counter +=1
            temp = temp.nast
        if counter<abs(idx):
            print('Nie ma tylu wartosci')
            return None
        if idx == 0:
            return self.pierwszy_el()
        if idx>0:
            temp = self.pierwszy_el()
            while idx>0:
                idx-=1
                temp = temp.nast
            return temp
        if idx<0:
            temp = self.ostatni_el()
            while idx<-1:
                idx+=1
                temp = temp.poprz
            return temp


    def co_drugi(self) -> 'Lista_2k_1w':
        temp = Lista_2k_1w()
        if self.wartow.nast is self.wartow:
            return temp
        codrugi = 0
        szukane = self.pierwszy_el()
        while szukane:
            if codrugi % 2 == 1:
                codrugi += 1
                szukane = szukane.nast
                continue
            temp.ostatni_el().dodaj_po_nim(szukane.wart)
            codrugi +=1
            szukane = szukane.nast
        return temp

    def wyszukaj(self, wart: Any) -> ListaWpis:
        if self.wartow.nast is self.wartow:
            return None
        temp = self.pierwszy_el()
        while temp:
            if temp.wart == wart:
                return temp
            temp = temp.nast
        return None

    def print_w_tyl(self):
        temp = self.ostatni_el()
        if self.wartow.nast is self.wartow:
            print('Lista jest pusta')
        drukowanie = ''
        while temp is not self.wartow:
            drukowanie += temp.wart
            if temp is not self.wartow.nast:
                drukowanie += '‘; ‘'
            temp = temp.poprz
        print(drukowanie)


    def princik(self):
        temp = self.pierwszy_el()
        if self.wartow.nast is self.wartow:
            print('Lista jest pusta')
        drukowanie = ''
        while temp is not None:
            if temp.nast is None:
                drukowanie += temp.wart
            else:
                drukowanie += temp.wart
                drukowanie += ': '
            temp = temp.nast
        print(drukowanie)



lista = Lista_2k_1w()
lista.ostatni_el().dodaj_po_nim('3')
lista.pierwszy_el().dodaj_po_nim('2')
lista.ostatni_el().dodaj_po_nim('4')
lista.ostatni_el().dodaj_przed_nim('0')
lista.ostatni_el().dodaj_po_nim('34')
lista.ostatni_el().dodaj_po_nim('5')
lista.ostatni_el().dodaj_po_nim('6')
lista.ostatni_el().dodaj_po_nim('7')
lista.ostatni_el().dodaj_po_nim('11')
lista.ostatni_el().dodaj_po_nim('8')
lista.ostatni_el().dodaj_po_nim('3')
lista.print_w_tyl()
lista.princik()
lista.pobierz_el(0)
lista.wyszukaj('3')
lista.pobierz_el(-4)
lista2 = lista.co_drugi()
lista2.print_w_tyl()

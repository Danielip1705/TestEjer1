from Ejercicio1 import cifradoCesar


def test_1():
   assert cifradoCesar("a",3)=="d"

def test_2():
   assert cifradoCesar("z",2)=="b"

def test_3():
   assert cifradoCesar("patata",3)=="sdwdwd"

def test_4():
   assert cifradoCesar("a ,b",1)=="b ,c"

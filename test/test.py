def f1():
    print('a')
    
from pydantic import BaseModel

class Item(BaseModel):
    p1: str

x=Item(p1='a')

def f(x: Item):
    x.p1=4

    

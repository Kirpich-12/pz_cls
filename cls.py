#We write code to try classes
#============================


class Birds:

    def __init__(self, name:str, flying_ability:bool, size:int):
        self.name = name
        self.flying_ability = flying_ability
        self.size = size
    
    def sounding(self):
        print('*sounding')
    
    def eating(self):
        print('*eating something')
    
    def sleping(self):
        print('zzzz')
    
    def __del__(self):
        print(f'{self.name} has delited')


def tst():
    pts = Birds('Petux', False, 15)
    pts.eating()
    print(type(pts))

def main():
    tst()

if __name__ == '__main__':
    main()
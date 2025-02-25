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
    
    def flying_range(self, n):
        if self.flying_ability is False:
            print(f"{self.name} can't fly")
        else:
            print(f'{self.name} can fly {self.size * n}')

    def __del__(self):
        print(f'{self.name} has delited')


def tst():
    pts = Birds('Petux', False, 15)
    pts.flying_range(4)
    pts2 = Birds('Nightingale', True, 15)
    pts2.flying_range(4)


def main():
    tst()

if __name__ == '__main__':
    main()
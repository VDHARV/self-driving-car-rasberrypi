import pygame

def pygame_setup():
    '''This Function helps to setup the pygame'''
    pygame.init()
    win = pygame.display.set_mode((100,100))

def getKey(key):
    '''This helps to detect the key sent by user'''
    ans  = False
    for eve in pygame.event.get(): pass
    keyInput = pygame.key.get_pressed()
    key_sent = getattr(pygame, 'K_{}'.format(key))
    if keyInput [key_sent]:
        ans = True    
    return ans
    
def main():
    '''This is used to drive the code'''
    if getKey('LEFT'):
        print("A was pressed")
    if getKey('RIGHT'):
        print('B was pressed')

if __name__ == "__main__":
    pygame_setup()
    while True:
        main()
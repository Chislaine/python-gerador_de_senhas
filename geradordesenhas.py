import random
import string

tamanho = int(input('Digite o tamanho de senha que você deseja: '))

chars = string.ascii_letters + string.digits + 'Ç!@#$&*()-=+,.:;/?'

rnd = random.SystemRandom() #os.urandom
print(''.join(rnd.choice(chars) for i in range(tamanho)))
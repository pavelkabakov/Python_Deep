import os
import pickle

res = pickle.loads(b"cos\nsystem\n(S'echo Hello world!'\ntR.")
print(res)

os.system('echo Hello world!')

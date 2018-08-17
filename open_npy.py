import numpy as np
import scipy.io as scio
import sys

doSave = False
fnames = []
for arg in sys.argv[1:]:
    if arg == '--save' or arg == '-s':
        doSave = True
    else:
        fnames.append(arg)

for fname in fnames:
    contents = np.load(fname)
    if contents.size == 1:
        contents = contents.item()
    print(contents)
    fname_mat = fname.replace('.npy', '')
    _dict = contents if type(contents) == dict else {fname_mat: contents}
    scio.savemat(fname_mat, _dict, oned_as='column')

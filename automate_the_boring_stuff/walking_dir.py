#! python3

import os

for folderName, subfolders, filenames in os.walk('c:\\delicious'):
    print('The folder is %s ' % folderName)
    print('The subfolders in %s are %s' % folderName, str(subfolders))
    print('The filenames in %s are %s ' % folderName, str(filenames))
    print()

    for subfolder in subfolders:
        if 'fish' in subfolder: # Simple example but you can use anything
            os.rmdir(subfolder)
    for file in filenames:
        if file.endswith('.py'): # Simple example but you can use anything
            shutil.copy(os.join(folderName, file), os.join(folderName, file + '.backup')

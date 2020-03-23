def reduce_file_path(path):
    newPath = path
    newPath=''.join([path[i] for i in range(len(path)-1) if path[i]!="/" or path[i] != path[i+1]]+[newPath[-1]])

    dots = '..'
    while dots in newPath:
       position = newPath.rfind(dots)
        
       if position == 1:
            newPath = newPath[3:]
            break

       newPath = newPath[:(position-1)]+newPath[(position+2):]

       while True:
            newPath = newPath[:position-1]
            position -=1
            if newPath.endswith('/'):                
                break
    
    newPath=newPath.replace('./','')
    
    if len(newPath)>1 and newPath[-1:] == '/':
       newPath = newPath[:-1]
    return newPath

print(reduce_file_path("/"))
print(reduce_file_path("/srv/../"))
print(reduce_file_path("/srv/www/htdocs/wtf/"))
print(reduce_file_path("/srv/www/htdocs/wtf"))
print(reduce_file_path("/srv/./././././"))
print(reduce_file_path("/etc//wtf/"))
print(reduce_file_path("/etc/../etc/../etc/../"))
print(reduce_file_path("//////////////"))
print(reduce_file_path("/../"))
import os
import shutil

#路径设置
folder_path="C:\\Users\\NYX\\codeProjects"
files=os.listdir(folder_path)  

#字典定义
category_map={           
    ".png":"picture",  
    ".docx":"text",
    ".js":"code",
    ".java":"code",
}

#执行分类
for file in files:
    full_path=os.path.join(folder_path,file)
    if os.path.isfile(full_path):
        name,ext=os.path.splitext(file)
        category=category_map.get(ext,"insummary")
        target_folder=os.path.join(folder_path,category)
        os.makedirs(target_folder,exist_ok=True)
        target_path=os.path.join(target_folder,file)

        shutil.move(full_path,target_path)
        print(file,"moved to",category)

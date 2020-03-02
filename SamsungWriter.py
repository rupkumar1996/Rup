
import xlrd
from string import Template
import os
import shutil 




def jsWriter(folder_name):
    if os.path.exists(folder_name +'/js'):
        shutil.rmtree(folder_name +'/js')
        shutil.copytree('/Users/rupkumar.saha/Desktop/Code/js', folder_name+'/js')
    with open(folder_name+'/js/externalFile.js', "a") as fp:
        wb = xlrd.open_workbook(folder_name+'/scraped_data.xlsx') 
        sheet = wb.sheet_by_index(0)
        nrows = sheet.nrows
        for j in range(nrows-1):   
            fp.writelines("\n{")
            fp.writelines(Template("id: \"$i\",\n").substitute(i=j+1))
            fp.writelines(Template("image: \"images/$k.webp\",\n").substitute(k=j+1))
            fp.writelines(Template("price: \"Rs. $price\",\n").substitute(price=int(float((sheet.cell_value(j+1,1).replace('INR','').replace(',', '')).strip()))))
            fp.writelines(Template("name: \"$name\",\n").substitute(name=sheet.cell_value(j+1,0 )))
            fp.writelines("merchantName: \"amazon\",\n")
            fp.writelines(Template("viewproductUrl: \"$url\"\n").substitute(url=sheet.cell_value(j+1,3)))
            fp.writelines("},")


    fp.close()
    with open(folder_name+'/js/externalFile.js', 'rb+') as f:
        f.seek(0,2)                 
        size=f.tell()
        f.truncate(size-1)
    f.close()


    with open(folder_name+'/js/externalFile.js', "a") as fp:
        fp.writelines('\n\n]')

    fp.close()

def samWriter():

    rootdir = '/Users/rupkumar.saha/Desktop/Sam_Files/'
    for folders in os.listdir(rootdir):
      
#        print(folders)
        jsWriter(rootdir + folders)

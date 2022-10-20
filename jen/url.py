import re

pattern = r"^([\w\-\.]+).*$"

def new_url_check(x):
    if 'some condition' in x:
        x = 'some random condition'           
            
    else:
       baseurl = re.findall(pattern, x)
            
    return baseurl


def main():
    x = new_url_check("somesite.com/somepage?param=1&else=2")
    print(x)

if __name__=="__main__":
    main()

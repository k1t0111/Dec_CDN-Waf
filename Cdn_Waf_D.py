# @Author:K1t0
# @Des: cdn 8 waf 相关批量检测脚本
# @Time: 2024/9/5

from argparse import  ArgumentParser
def main():
    arg = ArgumentParser(description=
                         """
                       [+]Author: K1t0\n\n       
                       [+] A perfect tools for you !!!
                       """)
    arg.add_argument("-u", "--url", dest='url', type=str, help="cdn &waf 检测域名")
    args = arg.parse_args()
    Dec_Cdn(args.url)

def Dec_Cdn(url):
    print(url)

if __name__=="__main__":
    main()
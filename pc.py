
import re
import requests
import parsel


lis = []
lis_1 = []

for page in range(1, 100):
    url = f'https://free.kuaidaili.com/free/inha/{page}/'
    print(url)
    response = requests.get(url)

   
    # print(response.text)

    # ip_list = re.findall('<td data-title="IP">(.*?)</td>',response.text)
    # port_list = re.findall('<td data-title="PORT">(.*?)</td>',response.text)
    selector = parsel.Selector(response.text)
    ip_list = selector.css('#list tbody tr td:nth-child(1)::text').getall()
    port_list = selector.css('#list tbody tr td:nth-child(2)::text').getall()


    print(ip_list)
    print(port_list)

    for ip,port in zip(ip_list,port_list):
        
        proxy = ip+':'+port
        proxies_dict = {
            'http':'http://'+proxy,
            'https':'https://'+proxy
        }
        
        # print(proxies_dict)
        lis.append(proxies_dict)
        try:
            response = requests.get(url=url,proxies=proxies_dict,timeout=1)
            if response.status.code==200:
                print('当前代理ip'+proxies_dict,'可以使用')
                lis_1.append(proxies_dict)
                print('获取可用的ip代理数量',len(lis_1))  
                print('获取可用的ip代理数量',lis_1)  
                
                
        except:
            print('当前代理ip请求超时')
   
print('获取ip代理数量',len(lis))
print('获取可用的ip代理数量',len(lis_1))  
print('获取可用的ip代理数量',lis_1)  
  
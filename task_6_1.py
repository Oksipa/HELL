#Не используя библиотеки для парсинга, распарсить (получить определённые данные) файл
# логов web-сервера nginx_logs.txt
#(https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs)
# — получить список кортежей вида: (<remote_addr>, <request_type>, <requested_resource>). Например:
#[ ...
#('141.138.90.60', 'GET', '/downloads/product_2'),
#('141.138.90.60', 'GET', '/downloads/product_2'),
#('173.255.199.22', 'GET', '/downloads/product_2'),
#..]

result = []
with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    for line in f:
        ln = line.split()
        result.append((ln[0], ln[5].strip(''), ln[6]))
print(result)
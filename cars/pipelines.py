from scrapy.exceptions import DropItem

class CarsPrice(object):
    def process_item(self, item, spider):
        price = item['price'].replace('.', '')
        if item['symbol'] == '$':
            if float(price) > 2500000:
                item['price'] = 'Expensive'
            else:
                item['price'] = price
        else:
            if float(price) > 15000:
                item['price'] = 'Expensive'
            else:
                item['price'] = price

        return item

class CarsBrand(object):
    def process_item(self, item, spider):
        title = item['title']
        item['brand'] = title.split(" ")[0]

        return item

class CarsModel(object):
    def process_item(self, item, spider):
        model = item['model']
        if int(model) < 2018:
            item['model'] = 'Oldie'
        else:
            item['model'] = model

        return item

class CarsKMs(object):
    def process_item(self, item, spider):
        kms = item['kms'].replace('Km', '').replace('.', '')
        if float(kms) > 30000:
            item['kms'] = 'VeryUsed'
        else:
            item['kms'] = kms

        return item

class CheckAsViable(object):
    def process_item(self, item, spider):
        if item['price'] != 'Expensive' and item['kms'] != 'VeryUsed' and item['model'] != 'Oldie':
            print('\r\n Car Found ->')
            print('title: ' + item['title'])
            print('brand: ' + item['brand'])
            print('symbol: ' + item['symbol'])
            print('price: ' + item['price'])
            print('model: ' + item['model'])
            print('kms: ' + item['kms'])
            # print('imageurl: ' + item['imageurl'])
            print('carurl: ' + item['carurl'])
        else:
            raise DropItem()
        return item
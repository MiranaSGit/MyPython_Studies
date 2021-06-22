from ebaysdk.finding import Connection as finding
from bs4 import BeautifulSoup
# from ebayapi import ebayapi

# from ebaysdk.exception import ConnectionError
import xlrd
# import time
# import xlwt

Store = 'transitpartcenter'

api = finding(
    siteid='EBAY-GB', appid='omerfaru-miranas-PRD-8a5abeab0-cf6fe95c', config_file=None)
api.request = {'storeName': Store, 'categoryId': '61513'}
response = api.execute('findItemsIneBayStores', api.request)
soup = BeautifulSoup(response.content, 'lxml')

totalentries = int(soup.find('totalentries').text)
items = soup.find_all('item')
i = 0
for item in items:
    item_id = item.itemid
    title = item.title
    price = item.currentprice
    i += 1
    print(item_id)
    print(title)
    print(price)
    print(i)
# def ebay_query(ItemID):
#     try:
#         api = shopping(
#             siteid='EBAY-GB', appid='omerfaru-miranas-PRD-8a5abeab0-cf6fe95c', config_file=None)
#         MPN = 'Null'
#         print(str(ItemID))
#         response = api.execute('GetSingleItem', {
#             'ItemID': str(ItemID),
#             'IncludeSelector': ['ItemSpecifics']
#         })
#         for item in response.dict()['Item']['ItemSpecifics']['NameValueList']:
#             if isinstance(item, dict):
#                 if item['Name'] == 'Manufacturer Part Number':
#                     MPN = item['Value']
#                     #print('ItemID:' + str(ItemID),item)

#         return MPN
#     except ConnectionError as e:
#         print(e)
#         print(e.response.dict())
#         return False


# workbook = xlrd.open_workbook('Ebay_List.xlsx')
# worksheets = workbook.sheet_names()
# workbook_out = xlwt.Workbook()
# # print(worksheets)
# for sheet in worksheets:
#     sheet_out = workbook_out.add_sheet(sheet)
#     worksheet = workbook.sheet_by_name(sheet)
#     print(sheet + ' sorgulanıyor..')
#     for row in range(worksheet.nrows):
#         while True:
#             mpn = ebay_query(str(int(worksheet.cell(row, 0).value)))
#             if mpn:
#                 sheet_out.write(row, 0, int(worksheet.cell(row, 0).value))
#                 sheet_out.write(row, 1, mpn)
#                 break
#             time.sleep(5)
# workbook_out.save('Ebay_List_out.xls')
# print('Ebay_Shafts_out.xlsx --> kaydedildi')

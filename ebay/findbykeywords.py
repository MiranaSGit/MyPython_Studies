from ebaysdk.finding import Connection

if __name__ == '__main__':
    api = Connection(config_file=None, debug=True, siteid="EBAY-GB",
                     appid='omerfaru-miranas-PRD-8a5abeab0-cf6fe95c')

    request = {
        'keywords': 'lord of the rings',
        'itemFilter': [
            {'name': 'condition', 'value': 'new'}
        ],
        'paginationInput': {
            'entriesPerPage': 10,
            'pageNumber': 1
        },
        'sortOrder': 'PricePlusShippingLowest'
    }

    response = api.execute('findItemsByKeywords', request)

    for item in response.reply.searchResult.item:
        print(
            f"Title: {item.title}, Price: {item.sellingStatus.currentPrice.value}")

import time


class Zadderjka:
    def __init__(self, get_response):
        self.get_response = get_response


    def __call__(self, request):
        if 'addrcollection' not in locals():
            addrcollection={}
        remip = request.META.get('REMOTE_ADDR')
        if remip in addrcollection.keys():
            addrcollection[str(remip)] += 1
        else:
            addrcollection[str(remip)] = 1
        if addrcollection[str(remip)] % 5 == 0:
            time.sleep(5)
        return self.get_response(request)


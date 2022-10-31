import time
from django.shortcuts import render

class Zadderjka:
    def __init__(self, get_response):
        self.bannedaddrcoll429= {}
        self.addrcollection={}
        self.get_response = get_response


    def __call__(self, request):
        remip = request.META.get('REMOTE_ADDR')
        if remip in self.bannedaddrcoll429.keys() and self.bannedaddrcoll429[remip] > time.time_ns():
            return render(request, 'homepage/429.html', status=429)
        elif remip in self.bannedaddrcoll429.keys() and self.bannedaddrcoll429[remip] <= time.time_ns():
            try:
                del self.bannedaddrcoll429[remip]
            except KeyError:
                pass
        if remip in self.addrcollection.keys():
            self.addrcollection[str(remip)][0] += 1
            if self.addrcollection[str(remip)][0] % 5 == 0:
                if time.time_ns() - self.addrcollection[str(remip)][1] < 1000000000:
                    self.bannedaddrcoll429[remip] = time.time_ns()+10000000000
                self.addrcollection[str(remip)][1] = time.time_ns()
        else:
            self.addrcollection[str(remip)] = [1, time.time_ns()]
        if self.addrcollection[str(remip)][0] % 15 == 0:
            time.sleep(5)
        return self.get_response(request)


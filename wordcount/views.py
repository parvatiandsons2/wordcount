from django.shortcuts import render
import operator
def homepage(request):
    return render(request, 'Index.html')


def count(request):
    data = request.GET['txtContent']
    objEachWord = data.split()
    objLength = len(objEachWord)

    objDataDictionary={}

    for obj in objEachWord:
        if obj in objDataDictionary:
            objDataDictionary[obj] += 1
        else:
            objDataDictionary[obj] = 1

    print(objDataDictionary)
    objDataDictionary = sorted(objDataDictionary.items(), key=operator.itemgetter(1), reverse=True)
    return render(request, 'count.html', {'data': data, 'len':objLength, 'objDataDictionary': objDataDictionary})

def about(request):
    return render(request,'about.html')
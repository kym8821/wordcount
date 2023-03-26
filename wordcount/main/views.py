from django.shortcuts import render

# Create your views here.

def main(request):
    return render(request, 'main.html')

def about(request):
    return render(request, 'about.html')

def result(request):    
    text = request.GET.get("text", "")
    # GET[키값]을 통해 키값에 해당하는 데이터를 요청  + 여기서는 text에 이동
    text_dict = {}
    text_list = text.split()
    total=0
    for word in text_list:
        if word in text_dict:
            text_dict[word] +=1
        else:
            text_dict[word] = 1
        total+=1
    words = sorted(text_dict.items(), key=lambda x: x[1], reverse=True)
    return render(request, 'result.html',{'total':total, 'words':words})
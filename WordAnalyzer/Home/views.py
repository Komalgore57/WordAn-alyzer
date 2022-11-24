from django.shortcuts import render

# Create your views here.
def index(request):
    result= ''
    text=request.GET.get('text')
    if( request.GET.get('cap')=='on'):
        result=text.capitalize()
        text=result

    if( request.GET.get('pr')=='on'):
        ne=''
        for i in text :
            if i not in ["'",'!',"@","#","$","%","^","&","*","(",")",'_','+',"<",">",':',"{",'}',
                "|","?",",",".",'/',';','[',"]" ]:
                ne+=i
        text=ne
        result=text

                
    if(request.GET.get('res')=='on'):
        text=text.split(' ')
        text=[ i for i in text if i!= '']
        result=' '.join(text)
        text=result
        print(result)


    if(request.GET.get('RLL') =='on'):
        result+=result.split('\n')[0]
        text=result
        print(result)
    
        charCount=request.GET.get('cc')
    
    if(request.GET.get('cc') =='on'):
        cc=dict.fromkeys(text,0)
        for i in cc.keys():
            cc[i]=text.count(i)
        result=result+" \n\n"+ str(cc)
    
    return render(request,'index.html',{'data':request.GET.get('text'),'result':result})
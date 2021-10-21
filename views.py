from .forms import UpLoadCoodinateForm
from .models import coordinateInfo, User

def image_upload(request):
    if request.method == 'GET':
        form = UpLoadCoodinateForm
    else:
        form = UpLoadCoodinateForm(request.POST, request.FILES)
        if form.is_valid():

            coordinateInfo.image = request.FILES['image']
            coordinateInfo.name = request.POST['coodinate_name']
            coordinateInfo. = request.POST['']
            # 削除フラグも必要であれば追加する（画面に反映されるか）

            coordinateInfo.save()

    context = {
        'form': form
    }
    return render(request, 'アプリ名/templates/edit_avator.html', context)
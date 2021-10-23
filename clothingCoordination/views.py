from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def test(request):
  return render(request, 'clothing/test.html')



def image_upload(request):
    if request.method == 'GET':
        form = UpLoadCoodinateForm
    else:
        form = UpLoadCoodinateForm(request.POST, request.FILES)
        if form.is_valid():

            coordinateInfo.image = request.FILES['image']
            coordinateInfo.name = request.POST['coodinate_name']
            # coordinateInfo. = request.POST['']
            # 削除フラグも必要であれば追加する（画面に反映されるか）

            coordinateInfo.save()

    context = {
        'form': form
    }
    return render(request, 'アプリ名/templates/edit_avator.html', context)



def __init__(self):
    self.params = {
    "AccountCreate":False,
    "signup_form": SignUpForm(),
    # "add_account_form":AddAccountForm(),
    }

#Get処理
def get(self,request):
    self.params["signup_form"] = AccountForm()
    # self.params["add_account_form"] = AddAccountForm()
    self.params["AccountCreate"] = False
    return render(request,"App_Folder_HTML/register.html",context=self.params)

#Post処理
def post(self,request):
    self.params["signup_form"] = SignUpForm(data=request.POST)
    # self.params["add_account_form"] = AddAccountForm(data=request.POST)

    #フォーム入力の有効検証
    if self.params["signup_form"].is_valid():
        # アカウント情報をDB保存
        account = self.params["signup_form"].save()
        # パスワードをハッシュ化
        account.set_password(account.password)
        # ハッシュ化パスワード更新
        account.save()

        # # 下記追加情報
        # # 下記操作のため、コミットなし
        # add_account = self.params["add_account_form"].save(commit=False)
        # # AccountForm & AddAccountForm 1vs1 紐付け
        # add_account.user = account

        # # モデル保存
        # add_account.save()

        # アカウント作成情報更新
        self.params["AccountCreate"] = True

    else:
        # フォームが有効でない場合
        print(self.params["signup_form"].errors)

    return render(request,"App_Folder_HTML/register.html",context=self.params)

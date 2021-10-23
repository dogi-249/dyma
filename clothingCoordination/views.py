from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth import login


from django.http import HttpResponse
from django.http import HttpResponseRedirect

from .forms import SignUpForm, LoginForm

# Create your views here.
def test(request):
  return render(request, 'clothing/test.html')


class Login(LoginView):
  form_class = LoginForm
  template_name = 'clothing/login.html'


class SignUp(CreateView):
  form_class = SignUpForm
  template_name = 'clothing/Sign-Up.html'
  success_url = reverse_lazy('')
  
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

  def form_valid(self, form):
    user = form.save()
    login(self.request, user)
    self.object = user
    return HttpResponseRedirect(self.get_success_url())


from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def test(request):
  return render(request, 'clothing/test.html')








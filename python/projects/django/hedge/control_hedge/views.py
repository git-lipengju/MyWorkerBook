from django.shortcuts import render
from django.shortcuts import render_to_response
from django.shortcuts import redirect
from django.http import HttpResponse
import json
import hashlib
import os
from control_hedge import models
# Create your views here.


def index(request):
    username = request.session.get("username")
    token = request.session.get("token")
    if not username or not token or token != hashlib.md5(username.encode("utf-8")).hexdigest():
        return render_to_response('login.html')
    return redirect('start.html')


def login(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    if not username or not password:
        return render_to_response('login.html')
    data = {"code": -1, "msg": "账号或密码错误"}
    token = hashlib.md5(username.encode("utf-8")).hexdigest()
    if username == "root" and password == "123":
        data["code"] = 0
        data["msg"] = "登录成功"
        request.session.__setitem__("username", username)
        request.session.__setitem__("token", token)
        request.session.set_expiry(0)  # 关闭浏览器失效
    else:
        return render_to_response('login.html')
    return redirect('start.html') # 登录成功，初始化数据，并跳转


def start(request):
    data = os.popen("ps -ef |grep /data/biup/joycoin/hedge/src/ |grep -v grep |awk -F' ' '{{print $10}}'").readlines()
    #data = ['6346 /data/biup/joycoin/hedge/src/hds_deal.py\n', '15981 /data/biup/joycoin/hedge/src/vds_depth.py\n', '15994 /data/biup/joycoin/hedge/src/vds_order.py\n', '16006 /data/biup/joycoin/hedge/src/vds_create.py\n', '17519 /data/biup/joycoin/hedge/src/hds_depth.py\n', '17531 /data/biup/joycoin/hedge/src/hds_order.py\n', '17543 /data/biup/joycoin/hedge/src/hds_create.py\n']
    run = []
    for x in data:
        fname = x.replace(".py\n", "").split("/")[-1]
        run.append(fname)
    symbol_configs = models.SymbolConfig.objects.filter(status=1).values()  # filter 多条数据，get 只能是一条数据
    no_run = []
    print(symbol_configs)
    for symbol_config in symbol_configs:
        coin_name = symbol_config.get("symbol").lower().replace("-", "").replace("usdt", "")
        for run_type in ["depth", "deal", "order", "create"]:
            no_run_name = coin_name+"_"+run_type
            if no_run_name not in run:
                no_run.append(no_run_name)
    result = {"run": sorted(run), "no_run": sorted(no_run)}
    return render_to_response('start.html', result)


def cancel(request):
    symbol = request.POST.get("symbol")
    side = request.POST.get("side")
    depth = request.POST.get("depth")
    fname = symbol.lower().split("-")[0] + "_depth"
    print(symbol, side, depth, fname)
    stop_data = os.system("sh /data/biup/joycoin/hedge/src/shell/stop_depth.sh %s" % fname)
    cancel_data = os.system("python /data/biup/joycoin/hedge/src/cancel_order.py %s %s %s" % (symbol, side, depth))
    print(stop_data)
    print(cancel_data)
    return redirect('start.html')


def to_start(request):
    symbol = request.POST.get("symbol")
    begin_data = os.system("sh /data/biup/joycoin/hedge/src/shell/start.sh %s" % symbol)
    return HttpResponse(json.dumps({"code": begin_data}))


def to_stop(request):
    symbol = request.POST.get("symbol")
    stop_data = os.system("sh /data/biup/joycoin/hedge/src/shell/stop.sh %s" % symbol)
    return HttpResponse(json.dumps({"code": stop_data}))



import bottle

app = bottle.Bottle()


@app.error(404)
def errorpage(err):
    return 'Page under Construction'


@app.route('/')
def indexpage():
    return '<h1> Welcome </h1> <ul><ll>Home<ll> <ll>About<ll> <ll>login<ll></ul>'


@app.route('/about')
def aboutpage():
    return '<h1> About </h1>'


@app.route('/login')
def loginpage():
    bottle.TEMPLATE_PATH.append(r'D:\Python Dev\training\bin')
    return bottle.template('login.tpl')


@app.route('/verify', method='POST')
def verify():
    u = bottle.request.forms.get('uname')
    p = bottle.request.forms.get('pw')
    if not (u == 'abc' and p == 'xyz'):
        return bottle.abort(403, 'access denied')
    else:
        import sqlite3
        con = sqlite3.connect('mydb.sqlite3')
        cur = con.cursor()
        cur.execute('select * from logdata')
        result = cur.fetchall()
        bottle.TEMPLATE_PATH.append(r'D:\Python Dev\training\bin')
        return bottle.template('report.tpl', res=result)
        # return 'Login success'


@app.route('/download/<f>')
def downloadpage(f):
    bottle.TEMPLATE_PATH.append(r'D:\Python Dev\training\bin')
    return bottle.static_file(root=r'D:\Python Dev\training\bin', filename=f)

@app.route('/json')
def jsonpage ():
    f=open('data.json', 'w')
    import  json
    d = {'a':10 , 'b':20}
    json.dump(d,f)
    f.close()
    F= open('data.json')
    e=json.load(F)
    f.close()
    return e
@app.route('/api2',method='GET')
def myapi2():
    d = {'api1': 'this is api-1'}
    return d
@app.route('/api3' , method='POST')
def myapi3():
    res = bottle.request.params
    res = dict(res)
    return res

app.run(debug=True)

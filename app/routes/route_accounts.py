from . import app, render_template, request


@app.route('/accounts', methods=['GET', 'POST'])
def accounts():
    if request.method == 'POST':
        #TODO 회원가입
        pass
    elif request.method == 'GET':
        #TODO 기존 가입 조회
        pass


@app.route('/accounts/auth', methods=['POST'])
def signin():
    #TODO 로그인 조회
    pass




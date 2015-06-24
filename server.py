from flask import Flask,render_template
import subprocess
app=Flask(__name__)
app.debug=True
@app.route('/')
def index():
	a=subprocess.Popen(['ps -ef'],stdout=subprocess.PIPE,shell=True)
	f1 =subprocess.Popen(["grep","python"],stdin=a.stdout,stdout=subprocess.PIPE)
	f2 =subprocess.Popen(["grep","cinder"],stdin=f1.stdout,stdout=subprocess.PIPE)
	out=f2.communicate()[0]
	cinder=[]
	if out==' ':
		cinder = ['cinder-volume not working','cinder-scheduler not working','cinder-api not working',]
		return render_template('hello.html',**locals())
	c=out.split()
	new=[item for item in c if not item.isdigit()]
	ind=[5,13,21,30,38,45]
	
	for i in ind:
	    cinder.append(new[i])
	return render_template('hello.html',**locals())

if __name__ == '__main__':
    app.run()
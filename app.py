from flask import Flask, render_template, url_for, request, Response
import pandas as pd
import itertools
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/allocate', methods=['GET', 'POST'])
def allocate():
    if request.method == 'POST':

        file1 = request.form['file1']
        file2 = request.form['file2']
        file3 = request.form['file3']

        cs = pd.read_csv(file1)
        ee = pd.read_csv(file2)
        tl = pd.read_csv(file3)

        nm = tl['Lecturer_name']
        List = []
        for n in nm:
            List.append(n)
        LecturerList = random.sample(List,7)
        csn = cs['Student_name']
        csr = cs['Roll_num']

        een = ee['Student_name']
        eer = ee['Roll_num']

        names = []
        roll = []
        bench = []

        total = int(len(een)+len(csn))
        for i in range(1, total+1):
            bench.append('BN{:04}'.format(i))

        for  i in range(10):
            st = 10*i
            sp = 10*(i+1)
            
            for i in csn[st:sp]:
                names.append(i)

            for i in een[st:sp]:
                names.append(i)

            for i in csr[st:sp]:
                roll.append(i)

            for i in eer[st:sp]:
                roll.append(i)
                
        col1=[]
        col2=[]
        col3=[]
        
        for i in range(4):
            st = 30*i
            sp = 30*(i+1)
            for a, b , c in zip(bench[st:sp], roll[st:sp], names[st:sp]):
                col1.append(a)
                col2.append(b)
                col3.append(c)
            
            dict = {'Invigilator':LecturerList[i],'Bench_num':col1,'Roll_num': col2, 'Student_name':col3}
            df = pd.DataFrame(dict)
            df.to_csv('Room_{}.csv'.format(i+1))
            num = int(len(bench))
        
        return render_template('index.html',  Bench_num=bench, Roll_num=roll, Student_name=names, Num=num, LecturerList=LecturerList)

    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)

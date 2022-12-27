from flask import Flask,render_template
import xmltodict
app=Flask(__name__)
@app.route('/')
def home_page():
    handle =open("fortified.xml","r")
    content=handle.read()
    d=xmltodict.parse(content)
    """
    #print(d['NessusClientData_v2']['Policy']['Preferences']['ServerPreferences']['preference'])
    #print(d['NessusClientData_v2']['Report'])
    #PluginsPreferences
    #print(d['NessusClientData_v2']['Policy']['Preferences']['PluginsPreferences']['item'])
    #print(d['NessusClientData_v2']['Report']['ReportHost'])
    #print(d['NessusClientData_v2']['Report']['ReportHost'][1])
    a=d['NessusClientData_v2']['Report']['ReportHost'][4]
    b=(a['ReportItem'])
    print(b)
    for i in b:
        if i.get('@severity')=='0':
            i['@severity']='Low'
        elif i.get('@severity')=='1':
            i['@severity']='Meduim'
        elif i.get('@severity')=='2':
            i['@severity']='High'
        elif i.get('@severity')=='3':
            i['@severity']='Critical'
        #print(i.get('@pluginID'),i.get('@pluginName'),i.get('@severity'),i.get('@pluginFamily'))
    #print(d.values())
    """
    a=d['NessusClientData_v2']['Report']['ReportHost']
    c=[]
    for i in a:
        b=(i['ReportItem'])
        for j in b:
            if j.get('@severity')=='0':
                j['@severity']='Low'
            elif j.get('@severity')=='1':
                j['@severity']='Meduim'
            elif j.get('@severity')=='2':
                j['@severity']='High'
            elif j.get('@severity')=='3':
                j['@severity']='Critical'
            c.append(j)
    return render_template("home.html",data=c)

@app.route('/plugindetails/<string:id>')
def plugin_details(id):
    handle =open("fortified.xml","r")
    content=handle.read()
    d=xmltodict.parse(content)
    a=d['NessusClientData_v2']['Report']['ReportHost']
    """
    b=(a['ReportItem'])
    print(b)
    for i in b:
         if i.get('@pluginID')==id:
            return render_template("details.html",data=i)
    #print(d.values())"""
    c=[]
    for i in a:
        b=(i['ReportItem'])
        for j in b:
            c.append(j)
    for i in c:
         if i.get('@pluginID')==id:
            return render_template("details.html",data=i)
if __name__=="__main__":
    app.run(debug=True)
from flask import Flask,render_template
import xmltodict
app=Flask(__name__)
@app.route('/')
def home_page():
    handle =open("fortified.xml","r")
    content=handle.read()
    xmltodict_content=xmltodict.parse(content)
    report_host_list=xmltodict_content['NessusClientData_v2']['Report']['ReportHost']
    report_items_new_list=[]
    for report_host_item in report_host_list:
        report_item_list=(report_host_item['ReportItem'])
        for report_item in report_item_list:
            if report_item.get('@severity')=='0':
                report_item['@severity']='Low'
            elif report_item.get('@severity')=='1':
                report_item['@severity']='Meduim'
            elif report_item.get('@severity')=='2':
                report_item['@severity']='High'
            elif report_item.get('@severity')=='3':
                report_item['@severity']='Critical'
            report_items_new_list.append(report_item)
    result = list({dictionary['@pluginID']: dictionary for dictionary in report_items_new_list}.values())
    return render_template("home.html",data=result)

@app.route('/plugindetails/<string:id>')
def plugin_details(id):
    handle =open("fortified.xml","r")
    content=handle.read()
    xmltodict_content=xmltodict.parse(content)
    report_host_list=xmltodict_content['NessusClientData_v2']['Report']['ReportHost']
    report_item_new_list=[]
    for report_host_item in report_host_list:
        report_item_list=(report_host_item['ReportItem'])
        for report_item in report_item_list:
            report_item_new_list.append(report_item)
    for report_new_item in report_item_new_list:
         if report_new_item.get('@pluginID')==id:
            return render_template("details.html",data=report_new_item)

if __name__=="__main__":
    app.run(debug=True)

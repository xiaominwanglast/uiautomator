#coding:utf-8
import xlsxwriter

def get_format(wd, option={}):
    return wd.add_format(option)

# 设置居中
def get_format_center(wd,num=1):
    return wd.add_format({'align': 'center','valign': 'vcenter','border':num,'font_size': 10})
def set_border(wd, num=1):
    return wd.add_format({}).set_border(num)
def set_text_wrap(wd):
    return wd.add_format({}).set_text_wrap()
# 写数据
def _write_center(worksheet, cl, data, wd):
    return worksheet.write(cl, data, get_format_center(wd))
def _write_data(worksheet, cl, data, wd):
    return worksheet.write(cl, data, get_format_center(wd))
workbook = xlsxwriter.Workbook(r'E:\os\work1.xlsx')
worksheet = workbook.add_worksheet(u"测试总况")

def init(worksheet,):

    # 设置列行的宽高
    worksheet.set_column("A:A", 25)
    worksheet.set_column("B:B", 15)
    worksheet.set_column("C:C", 25)
    worksheet.set_column("D:D", 15)
    worksheet.set_column("E:E", 25)
    worksheet.set_column("F:F", 15)

    worksheet.set_row(1, 30)
    worksheet.set_row(2, 30)
    worksheet.set_row(3, 30)
    worksheet.set_row(4, 30)
    worksheet.set_row(5, 30)

    # worksheet.set_row(0, 200)

    define_format_H1 = get_format(workbook, {'bold': 1, 'font_size': 18,'align':'center','bg_color':'bule'})
 #   define_format_H2 = get_format(workbook, {'bold': 1, 'font_size': 14,'align':'center','bg_color':'blue','color':'#ffffff'})

    define_format_H1.set_border(1)
    define_format_H1.set_text_wrap()
    define_format_H1.set_align("center")
   # define_format_H2.set_align("center")
   # define_format_H2.set_bg_color("blue")
  #  define_format_H2.set_color("#ffffff")
    # Create a new Chart object.

    worksheet.merge_range('A1:F1', u"测试报告总概况", define_format_H1)
#    worksheet.merge_range('A2:F2', u"测试概括", define_format_H2)

#    worksheet.merge_range('A3:A6', u"这里放图片", get_format_center(workbook))
    worksheet.write("A2",u"app名称第三方第三个第三个是非得失",define_format_H1)
 #   _write_center(worksheet, "A2", u"app名称第三方第三个第三个是非得失", workbook)
    _write_center(worksheet, "A3", u"app版本", workbook)
    _write_center(worksheet, "A4", u"脚本语言", workbook)
    _write_center(worksheet, "A5", u"测试网络", workbook)
    _write_center(worksheet, "A6", u"测试日期", workbook)
    list=[]
    '''
    data = {"test_name": u"智商", "test_version": "v2.0.8", "test_pl": "android", "test_net": "wifi"}
    _write_center(worksheet, "C3", data['test_name'], workbook)
    _write_center(worksheet, "C4", data['test_version'], workbook)
    _write_center(worksheet, "C5", data['test_pl'], workbook)
    _write_center(worksheet, "C6", data['test_net'], workbook)
    '''
    _write_center(worksheet, "C2", u"用例总数", workbook)
    _write_center(worksheet, "C3", u"可执行总数", workbook)
    _write_center(worksheet, "C4", "pass", workbook)
    _write_center(worksheet, "C5", "fail", workbook)
    _write_center(worksheet, "C6", "error", workbook)

    _write_center(worksheet,"E2",u"可执行用例率",workbook)
    _write_center(worksheet,"E3",u"可执行pass率",workbook)
    _write_center(worksheet,"E4",u"可执行fail率",workbook)
    _write_center(worksheet,"E5",u"可执行error率",workbook)
    _write_center(worksheet,"E6",u"可执行pass预期目标",workbook)


    '''
    data1 = {"test_sum": 100, "test_success": 80, "test_failed": 20, "test_date": "2018-10-10 12:10"}
    _write_center(worksheet, "E3", data1['test_sum'], workbook)
    _write_center(worksheet, "E4", data1['test_success'], workbook)
    _write_center(worksheet, "E5", data1['test_failed'], workbook)
    _write_center(worksheet, "E6", data1['test_date'], workbook)
    _write_center(worksheet, "F3", u"分数", workbook)
    worksheet.merge_range('F4:F6', '60', get_format_center(workbook))
    pie(workbook, worksheet)

 # 生成饼形图

def pie(workbook, worksheet):
    chart1 = workbook.add_chart({'type': 'pie'})
    chart1.add_series({
    'name':       u"接口测试统计",
    'categories': u"=测试总况!$D$4:$D$5",
   'values':    u"=测试总况!$E$4:$E$5",
    })
    chart1.set_title({'name': u'接口测试统计'})
    chart1.set_style(10)
    worksheet.insert_chart('A9', chart1, {'x_offset': 25, 'y_offset': 10})
'''
init(worksheet)
workbook.close()















'''
def test_detail(worksheet):

    # 设置列行的宽高
    worksheet.set_column("A:A", 30)
    worksheet.set_column("B:B", 20)
    worksheet.set_column("C:C", 20)
    worksheet.set_column("D:D", 20)
    worksheet.set_column("E:E", 20)
    worksheet.set_column("F:F", 20)
    worksheet.set_column("G:G", 20)
    worksheet.set_column("H:H", 20)

    worksheet.set_row(1, 30)
    worksheet.set_row(2, 30)
    worksheet.set_row(3, 30)
    worksheet.set_row(4, 30)
    worksheet.set_row(5, 30)
    worksheet.set_row(6, 30)
    worksheet.set_row(7, 30)



    worksheet.merge_range('A1:H1', '测试详情', get_format(workbook, {'bold': True, 'font_size': 18 ,'align': 'center','valign': 'vcenter','bg_color': 'blue', 'font_color': '#ffffff'}))
    _write_center(worksheet, "A2", '用例ID', workbook)
    _write_center(worksheet, "B2", '接口名称', workbook)
    _write_center(worksheet, "C2", '接口协议', workbook)
    _write_center(worksheet, "D2", 'URL', workbook)
    _write_center(worksheet, "E2", '参数', workbook)
    _write_center(worksheet, "F2", '预期值', workbook)
    _write_center(worksheet, "G2", '实际值', workbook)
    _write_center(worksheet, "H2", '测试结果', workbook)

    data = {"info": [{"t_id": "1001", "t_name": "登陆", "t_method": "post", "t_url": "http://XXX?login", "t_param": "{user_name:test,pwd:111111}",
                      "t_hope": "{code:1,msg:登陆成功}", "t_actual": "{code:0,msg:密码错误}", "t_result": "失败"}, {"t_id": "1002", "t_name": "商品列表", "t_method": "get", "t_url": "http://XXX?getFoodList", "t_param": "{}",
                      "t_hope": "{code:1,msg:成功,info:[{name:123,detal:dfadfa,img:product/1.png},{name:456,detal:dfadfa,img:product/1.png}]}", "t_actual": "{code:1,msg:成功,info:[{name:123,detal:dfadfa,img:product/1.png},{name:456,detal:dfadfa,img:product/1.png}]}", "t_result": "成功"}],
            "test_sum": 100,"test_success": 20, "test_failed": 80}
    temp = 4
    for item in data["info"]:
        _write_center(worksheet, "A"+str(temp), item["t_id"], workbook)
        _write_center(worksheet, "B"+str(temp), item["t_name"], workbook)
        _write_center(worksheet, "C"+str(temp), item["t_method"], workbook)
        _write_center(worksheet, "D"+str(temp), item["t_url"], workbook)
        _write_center(worksheet, "E"+str(temp), item["t_param"], workbook)
        _write_center(worksheet, "F"+str(temp), item["t_hope"], workbook)
        _write_center(worksheet, "G"+str(temp), item["t_actual"], workbook)
        _write_center(worksheet, "H"+str(temp), item["t_result"], workbook)
        temp = temp -1

'''
#test_detail(worksheet2)
'''
import xlsxwriter,xlrd
import sys,os.path
fname = 'zm6.xlsx'
if not os.path.isfile(fname):
    print u'文件路径不存在'
    sys.exit()
data = xlrd.open_workbook(fname)            # 打开fname文件
data.sheet_names()                          # 获取xls文件中所有sheet的名称
table = data.sheet_by_index(0)              # 通过索引获取xls文件第0个sheet
nrows = table.nrows                         # 获取table工作表总行数
ncols = table.ncols                         # 获取table工作表总列数
workbook = xlsxwriter.Workbook('zm6.xlsx')  #创建一个excel文件
worksheet = workbook.add_worksheet()        #创建一个工作表对象
worksheet.set_column(0,ncols,22)            #设定列的宽度为22像素
#border：边框，align:对齐方式，bg_color：背景颜色，font_size：字体大小，bold：字体加粗
top = workbook.add_format({'border':1,'align':'center','bg_color':'cccccc','font_size':13,'bold':True})
green = workbook.add_format({'border':1,'align':'center','bg_color':'green','font_size':12})
yellow = workbook.add_format({'border':1,'bg_color':'yellow','font_size':12})
red = workbook.add_format({'border':1,'align':'center','bg_color':'red','font_size':12})
blank = workbook.add_format({'border':1})
for i in xrange(nrows):
    worksheet.set_row(i,22)                 #设定第i行单元格属性，高度为22像素，行索引从0开始
    for j in  xrange(ncols):
        cell_value = table.cell_value(i,j,) #获取第i行中第j列的值
        if i == 0:
            format = top
        elif i == 3 or i == 6:
            format = blank
        else:
            if j == 0 or j == 2:
                format = yellow
            elif j == 1:
                format = red
            elif j == 3:
                format = green
                green.set_num_format('yyyy-mm-dd')  #设置时间格式
        worksheet.write(i,j,cell_value,format)      #把获取到的值写入文件对应的行列
        format.set_align('vcenter')                 #设置单元格垂直对齐
workbook.close()
'''

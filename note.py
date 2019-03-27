# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## 
## by kxhuang 2018.11.09
###########################################################################

import wx
import wx.xrc
import sqlite3
#导入内置数据库
import datetime
import math


conn = sqlite3.connect('note.db') #连接或建立db数据库



#是否存在CheckBook表
try:
    create_tb_cmd='''CREATE TABLE CheckBook(ID INTEGER PRIMARY KEY AUTOINCREMENT,Date DATE NOT NULL,Category TEXT NOT NULL,Price INT NOT NULL,Remark TEXT);'''
    conn.execute(create_tb_cmd)
    print ("create CheckBook")
except:
    print ('table is exists')
    conn = sqlite3.connect('note.db')
    c = conn.cursor()
    print ("now is writting date")
    c.execute("select count(ID) from CheckBook")
    num = int(c.fetchall()[0][0])
    print ("num is =======================:",num,type(num))
conn.commit()
conn.close
# 计算表总页码
page = math.ceil(num/18) # 每页显示18条数据，计算出总页数
current_page = 0


class MyFrame ( wx.Frame ):
    
    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"菲菲记账本", pos = wx.DefaultPosition, size = wx.Size( 800,600 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        
        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
        self.SetIcon(wx.Icon('icon.ico', wx.BITMAP_TYPE_ICO))
        self.m_menubar1 = wx.MenuBar( 0 )
        self.m_menu1 = wx.Menu()
        self.m_menubar1.Append( self.m_menu1, u"文件" ) 
        self.m_menu3 = wx.Menu()
        self.m_menuItem2 = wx.MenuItem( self.m_menu3, wx.ID_ANY, u"指引", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu3.Append( self.m_menuItem2 )
        self.m_menuItem3 = wx.MenuItem( self.m_menu3, wx.ID_ANY, u"关于", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu3.Append( self.m_menuItem3 )
        self.m_menubar1.Append( self.m_menu3, u"帮助" )
        self.SetMenuBar( self.m_menubar1 )
        
        bSizer3 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_toolBar1 = wx.ToolBar( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TB_HORIZONTAL ) 
        self.m_toolBar1.Realize() 
        
        bSizer3.Add( self.m_toolBar1, 0, wx.EXPAND, 5 )
        
        bSizer7 = wx.BoxSizer( wx.HORIZONTAL )
        
        bSizer4 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_panel2 = wx.Panel( self, wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 100,600 ),style = wx.TAB_TRAVERSAL )
        self.m_panel2.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ) )
        
        bSizer6 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_bpButton1 = wx.BitmapButton( self.m_panel2, wx.ID_ANY, wx.Bitmap( u"1.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
        self.m_bpButton1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ) )
        
        bSizer6.Add( self.m_bpButton1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
        
        self.m_bpButton2 = wx.BitmapButton( self.m_panel2, wx.ID_ANY, wx.Bitmap( u"2.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
        self.m_bpButton2.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ) )
        
        bSizer6.Add( self.m_bpButton2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
        
        self.m_bpButton3 = wx.BitmapButton( self.m_panel2, wx.ID_ANY, wx.Bitmap( u"3.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
        self.m_bpButton3.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ) )
        
        bSizer6.Add( self.m_bpButton3, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
        
        self.m_bpButton4 = wx.BitmapButton( self.m_panel2, wx.ID_ANY, wx.Bitmap( u"4.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
        self.m_bpButton4.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ) )
        
        bSizer6.Add( self.m_bpButton4, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

        
        
        self.m_panel2.SetSizer( bSizer6 )
        self.m_panel2.Layout()
        bSizer6.Fit( self.m_panel2 )
        bSizer4.Add( self.m_panel2, 1, wx.EXPAND |wx.ALL, 0 )
        
        
        bSizer7.Add( bSizer4, 1, wx.EXPAND, 5 )
        
        bSizer5 = wx.BoxSizer( wx.VERTICAL )
# 1. 首页板块========================================================
        self.m_panel3 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer8 = wx.BoxSizer( wx.VERTICAL )
        self.m_bitmap3 = wx.StaticBitmap( self.m_panel3, wx.ID_ANY, wx.Bitmap( u"index.jpg", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer8.Add( self.m_bitmap3, 0, wx.ALL, 5 )
        self.m_panel3.SetSizer( bSizer8 )
        self.m_panel3.Layout()
        bSizer8.Fit( self.m_panel3 )
        bSizer5.Add( self.m_panel3, 1, wx.EXPAND |wx.ALL, 0 )
#===================================================================

# 2. 报表板块=======================================================
        self.m_panel4 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.m_panel4.Hide()
        bSizer8 = wx.BoxSizer( wx.VERTICAL )      
        self.m_listCtrl1 = wx.ListCtrl( self.m_panel4, wx.ID_ANY,pos=wx.DefaultPosition, size = wx.Size( 700,450 ), style = wx.LC_HRULES|wx.LC_REPORT )
        self.m_listCtrl1.InsertColumn(0,u"日期",width=75)
        self.m_listCtrl1.InsertColumn(1,u"类别",width=100)
        self.m_listCtrl1.InsertColumn(2,u"消费(单位：元)",width=100)
        self.m_listCtrl1.InsertColumn(3,u"备注",width=425)
        self.m_listCtrl1.SetItemState(0, 0, wx.LIST_STATE_SELECTED)  
        bSizer8.Add( self.m_listCtrl1, 1, wx.ALL|wx.EXPAND, 0 )

     # 增加页码功能，防止数据量过大导致速度变慢
        self.m_panel5 = wx.Panel( self.m_panel4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer9 = wx.BoxSizer( wx.HORIZONTAL )
        self.m_button6 = wx.Button( self.m_panel5, wx.ID_ANY, u"上一页", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer9.Add( self.m_button6, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        self.m_button6.Enable( False )
        self.m_button7 = wx.Button( self.m_panel5, wx.ID_ANY, u"下一页", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer9.Add( self.m_button7, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        self.m_panel5.SetSizer( bSizer9 )
        self.m_panel5.Layout()
        bSizer9.Fit( self.m_panel5 )
        bSizer8.Add( self.m_panel5, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )       
        self.m_panel4.SetSizer( bSizer8 )
        self.m_panel4.Layout()
        bSizer8.Fit( self.m_panel4 )
        bSizer5.Add( self.m_panel4, 1, wx.EXPAND |wx.ALL, 0 )
#==================================================================

        bSizer7.Add( bSizer5, 1, wx.EXPAND, 5 )
        bSizer3.Add( bSizer7, 1, wx.EXPAND, 5 )
        
        self.statusbar = self.CreateStatusBar(1, 0)
        #状态栏
        self.statusbar.SetStatusText(u"欢迎使用记账工具！", 0)
        self.SetSizer( bSizer3 )
        self.Layout()
        
        self.Centre( wx.BOTH )
        
# 绑定动作集中区

        #绑定菜单栏“设置”触发器
        self.m_bpButton1.Bind( wx.EVT_BUTTON, self.OnHome)
        #左侧第一个按钮动作
        self.m_bpButton2.Bind( wx.EVT_BUTTON, self.OnAdd)
        #左侧第二个按钮动作
        self.m_bpButton3.Bind( wx.EVT_BUTTON, self.OnReport)
        #左侧第三个按钮动作
        self.m_bpButton4.Bind( wx.EVT_BUTTON, self.OnSearch)
        #左侧第四个按钮动作
        self.Bind( wx.EVT_BUTTON, self.OnPrev,id = self.m_button6.GetId() )
        #上一页
        self.Bind( wx.EVT_BUTTON, self.OnNext,id = self.m_button7.GetId())
        #下一页
# 方法集中区
    def OnSetting(self,event):
    # 增加支出分类函数
        cfgset=Cfg_set(self)
        cfgset.Show(True)
    def OnAdd(self,event):
    # 添加一笔支出
        cfgadd=Cfg_add(self)
        cfgadd.Show(True)
    def __del__( self ):
        pass
    def OnReport(self,event):
        self.m_panel4.Show()
        self.m_panel3.Hide()
        self.Layout() # 不加self.Layout右侧面板位置会跳
        self.m_listCtrl1.DeleteAllItems()
        # 读取数据库
        cat = []
        conn = sqlite3.connect('note.db')
        c = conn.cursor()
        print ("now is writting date")
        c.execute("select * from CheckBook order by Date desc limit 0,18")
        res = c.fetchall()
        for line in res:
            cat.append(line)
        conn.close()
        # 遍历从数据库获取到的元组
        for i in range (len(cat)):
            self.m_listCtrl1.InsertItem(i,str(cat[i][1]))
            self.m_listCtrl1.SetItem(i,1,str(cat[i][2]))
            cati_3 = str(cat[i][3])+u'元'
            self.m_listCtrl1.SetItem(i,2,str(cati_3))
            self.m_listCtrl1.SetItem(i,3,str(cat[i][4]))
        self.m_button7.Enable( True )
        global current_page
        current_page = 0  # 预防点击时，导致下一页和上一页功能混乱
    def OnHome(self,event):
        self.m_panel3.Show()
        self.m_panel4.Hide()
        self.Layout() # 不加self.Layout右侧面板排版会乱

    def OnSearch( self, event ):
        self.m_panel4.Show()
        self.m_panel3.Hide()
        self.Layout()
        cfgsea=Cfg_sea(self)
        cfgsea.Show(True)
        self.m_button7.Enable( False )
        self.m_button6.Enable( False )

    def OnPrev( self, event ):
        global current_page
        if page == 1:
            pass
        else:
            current_page -=1
            self.m_button7.Enable( True )
            self.m_listCtrl1.DeleteAllItems()
            print ("onprev!==totally page is:",page,"current page is:",current_page) # 调试
            folio = current_page*18
            cat = []
            conn = sqlite3.connect('note.db')
            c = conn.cursor()
            print ("folio:",folio)
            print ("current_page:",current_page)
            c.execute("select * from CheckBook  order by Date desc limit '%s',18" %(folio))
            res = c.fetchall()
            for line in res:
                cat.append(line)
            conn.close()
            for i in range (len(cat)):
                self.m_listCtrl1.InsertItem(i,str(cat[i][1]))
                self.m_listCtrl1.SetItem(i,1,str(cat[i][2]))
                cati_3 = str(cat[i][3])+u'元'
                self.m_listCtrl1.SetItem(i,2,str(cati_3))
                self.m_listCtrl1.SetItem(i,3,str(cat[i][4]))
            if current_page == 0:
                print ('no more data！')
                self.m_button6.Enable( False )
            	

    def OnNext( self, event ):
        global current_page
        if page == 1:
            pass
        else:
            current_page +=1
            self.m_button6.Enable( True )
            self.m_listCtrl1.DeleteAllItems()
            print ("onnext!===Totally page is:",page,"current page is:",current_page) # 调试
            folio = current_page*18
            cat = []
            conn = sqlite3.connect('note.db')
            c = conn.cursor()
            print ("folio:",folio)
            print ("current_page:",current_page)
            c.execute("select * from CheckBook  order by Date desc limit '%s',18" %(folio))
            res = c.fetchall()
            for line in res:
                cat.append(line)
            conn.close()
            for i in range (len(cat)):
                self.m_listCtrl1.InsertItem(i,str(cat[i][1]))
                self.m_listCtrl1.SetItem(i,1,str(cat[i][2]))
                cati_3 = str(cat[i][3])+u'元'
                self.m_listCtrl1.SetItem(i,2,str(cati_3))
                self.m_listCtrl1.SetItem(i,3,str(cat[i][4]))
            
            if current_page == (page-1):
                print ('no more data！')
                self.m_button7.Enable( False )
                

#记一笔分类        
class Cfg_add ( wx.Frame ):
    
    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u'记一笔', pos = wx.DefaultPosition, size = wx.Size( 500,350 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        
        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
        
        bSizer1 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer2 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_bitmap1 = wx.StaticBitmap( self.m_panel1, wx.ID_ANY, wx.Bitmap( u"1.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer2.Add( self.m_bitmap1, 0, wx.ALL, 5 )
        
        bSizer3 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_staticText1 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"日期", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText1.Wrap( -1 )
        bSizer3.Add( self.m_staticText1, 0, wx.ALL, 5 )

        today = str(datetime.date.today())
        # 获取当天日期，因无法通过赋值成 u'value'，所以只能用str格式成字符串
        self.m_textCtrl4 = wx.TextCtrl( self.m_panel1, wx.ID_ANY, today, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer3.Add( self.m_textCtrl4, 0, wx.ALL, 5 )
        
        self.m_staticText3 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"分类", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText3.Wrap( -1 )
        bSizer3.Add( self.m_staticText3, 0, wx.ALL, 5 )

    # 获取category值
        cat = []
        conn = sqlite3.connect('note.db')
        c = conn.cursor()
        print ("now is writting date")

        #判断是否存在Category表，不存在则跳出,cat默认值
        try:
            c.execute("select * from Category")
            res = c.fetchall()
            for line in res:
                cat.append(line[0])
        except:
            pass
        conn.close()    

        m_choice1Choices = cat
        self.m_choice1 = wx.Choice( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice1Choices, 0 )
        self.m_choice1.SetSelection( 0 )
        bSizer3.Add( self.m_choice1, 0, wx.ALL, 5 )
        
        self.m_staticText4 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"支出", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText4.Wrap( -1 )
        bSizer3.Add( self.m_staticText4, 0, wx.ALL, 5 )
        
        self.m_textCtrl2 = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer3.Add( self.m_textCtrl2, 0, wx.ALL, 5 )

        self.m_staticText5 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"备注", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText5.Wrap( -1 )
        bSizer3.Add( self.m_staticText5, 0, wx.ALL, 5 )
        
        self.m_textCtrl3 = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_AUTO_URL|wx.TE_MULTILINE )
        bSizer3.Add( self.m_textCtrl3, 0, wx.ALL, 5 )
        
        self.m_button1 = wx.Button( self.m_panel1, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer3.Add( self.m_button1, 0, wx.ALL, 5 ) 
        
        bSizer2.Add( bSizer3, 1, wx.EXPAND, 5 )
        
        
        self.m_panel1.SetSizer( bSizer2 )
        self.m_panel1.Layout()
        bSizer2.Fit( self.m_panel1 )
        bSizer1.Add( self.m_panel1, 1, wx.EXPAND |wx.ALL, 0 )
        
        self.m_panel2 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.m_panel2.SetBackgroundColour( wx.Colour( 255, 157, 206 ) )
        
        bSizer4 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_staticText1 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"新增分类", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText1.Wrap( -1 )
        bSizer4.Add( self.m_staticText1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
        
        self.m_textCtrl1 = wx.TextCtrl( self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer4.Add( self.m_textCtrl1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
        
        self.m_button2 = wx.Button( self.m_panel2, wx.ID_ANY, u"确认添加", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer4.Add( self.m_button2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
        
        
        self.m_panel2.SetSizer( bSizer4 )
        self.m_panel2.Layout()
        bSizer4.Fit( self.m_panel2 )
        bSizer1.Add( self.m_panel2, 0, wx.ALL|wx.EXPAND, 0 )
        self.SetSizer( bSizer1 )
        self.Layout()
        
        self.Centre( wx.BOTH )
        self.Bind( wx.EVT_BUTTON, self.OnOK, id = self.m_button1.GetId() )
        self.Bind( wx.EVT_BUTTON, self.OnSet, id = self.m_button2.GetId() )
    def __del__( self ):
        pass
    def OnOK( self, event ):
        c_dat = self.m_textCtrl4.GetValue()
        print (c_dat)
        c_cat = self.m_choice1.GetString(self.m_choice1.GetSelection())
        # 获取下拉值（分类）
        c_pri = self.m_textCtrl2.GetValue()
        c_mar = self.m_textCtrl3.GetValue()
        if c_pri == "": #检查用户是否输入空值
            dlg = wx.MessageDialog(self,"支出为空！","Error",wx.ICON_ERROR) #语法是(self, 内容, 标题, ID)
            dlg.ShowModal() #显示对话框
            dlg.Destroy()   #当结束之后关闭对话框
        else:
            conn = sqlite3.connect('note.db')
            c = conn.cursor()
            print ("now is writting date")
            c.execute("insert into CheckBook(Date,Category,Price,Remark) VALUES ('%s','%s','%s','%s')"%(c_dat,c_cat,c_pri,c_mar));
            conn.commit()
            conn.close()
            #记账成功后，弹窗通知，防止重复输入
            dlg = wx.MessageDialog(self,"记账成功，再记一笔吗？","提示",wx.YES_NO) #语法是(self, 内容, 标题, ID)
            if dlg.ShowModal() == wx.ID_NO:
                self.Close(True)
                dlg.Destroy()   #当结束之后关闭对话框 
            else:
                self.m_choice1.SetSelection( 0 )
                self.m_textCtrl2.Clear()
                self.m_textCtrl3.Clear()

    #设置增加分类
    def OnSet( self, event ):
        conn = sqlite3.connect('note.db')
        #判断是否存在Category表
        try:
            create_tb_cmd='''CREATE TABLE Category(Cat_Name TEXT NOT NULL);'''
            conn.execute(create_tb_cmd)
            print ("create Category!")
        except:
            print ('Category table is exists')
        conn.commit()
        conn.close
        cat_name = self.m_textCtrl1.GetValue()
        if cat_name == "":
            dlg = wx.MessageDialog(self,"不要输入空值","提醒",wx.ICON_ERROR) #语法是(self, 内容, 标题, ID)
            dlg.ShowModal() #显示对话框
            dlg.Destroy()   #当结束之后关闭对话框

        else:
            conn = sqlite3.connect('note.db')
            c = conn.cursor()
            print ("now is writting date")
            c.execute("insert into Category(Cat_Name) VALUES ('%s')"%(cat_name));
            conn.commit()
            conn.close()
            dlg = wx.MessageDialog(self,u"添加成功",u"提醒",wx.OK)
            dlg.ShowModal() #显示对话框
            dlg.Destroy()   #当结束之后关闭对话框
            self.m_choice1.Append(cat_name) # 动态更新下拉选择分类项
            self.m_textCtrl1.Clear() # 清空增加分类内容


# 查找分类
class Cfg_sea ( wx.Frame ):
    
    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"消费记录查询", pos = wx.DefaultPosition, size = wx.Size( 250,200 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        
        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
        
        bSizer1 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer2 = wx.BoxSizer( wx.HORIZONTAL )
        
        bSizer3 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_staticText1 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"日期", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText1.Wrap( -1 )
        bSizer3.Add( self.m_staticText1, 0, wx.ALL, 5 )
        
        today = str(datetime.date.today())
        self.m_textCtrl1 = wx.TextCtrl( self.m_panel1, wx.ID_ANY, today, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer3.Add( self.m_textCtrl1, 0, wx.ALL, 5 )
        
        self.m_staticText2 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"类型*", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText2.Wrap( -1 )
        bSizer3.Add( self.m_staticText2, 0, wx.ALL, 5 )
        
        m_choice2Choices = [ u"暂时不启用" ]
        self.m_choice2 = wx.Choice( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice2Choices, 0 )
        self.m_choice2.SetSelection( 0 )
        self.m_choice2.Enable( False )
        
        bSizer3.Add( self.m_choice2, 0, wx.ALL, 5 )
        
        self.m_button1 = wx.Button( self.m_panel1, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer3.Add( self.m_button1, 0, wx.ALL, 5 )
        
        
        bSizer2.Add( bSizer3, 1, wx.EXPAND, 5 )
        
        self.m_bitmap1 = wx.StaticBitmap( self.m_panel1, wx.ID_ANY, wx.Bitmap( u"7.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer2.Add( self.m_bitmap1, 0, wx.ALL, 5 )
        
        
        self.m_panel1.SetSizer( bSizer2 )
        self.m_panel1.Layout()
        bSizer2.Fit( self.m_panel1 )
        bSizer1.Add( self.m_panel1, 1, wx.EXPAND |wx.ALL, 0 )
        
        
        self.SetSizer( bSizer1 )
        self.Layout()
        
        self.Centre( wx.BOTH )
        self.Bind( wx.EVT_BUTTON, self.OnOK, id = self.m_button1.GetId() )
        # 确认绑定动作
    def __del__( self ):
        pass
    
    def OnOK( self, event ):
        self.Parent.m_listCtrl1.DeleteAllItems()
        # 清除listctrl所有数据
        c_date = self.m_textCtrl1.GetValue()
        cat = []
        conn = sqlite3.connect('note.db')
        c = conn.cursor()
        print ("now is writting date")
        c.execute("select * from CheckBook where Date = '%s' order by Category"%(c_date))
        res = c.fetchall()
        for line in res:
            cat.append(line)
        conn.close()
        total = 0
        for i in range (len(cat)):
            self.Parent.m_listCtrl1.InsertItem(i,str(cat[i][1]))
            self.Parent.m_listCtrl1.SetItem(i,1,str(cat[i][2]))
            cati_3 = str(cat[i][3])+u'元'
            self.Parent.m_listCtrl1.SetItem(i,2,str(cati_3))
            self.Parent.m_listCtrl1.SetItem(i,3,str(cat[i][4]))
            total = round(cat[i][3]+total,2)
            print (total)
        Totally = str(total) + '元'
        self.Parent.m_listCtrl1.InsertItem(len(cat),str('总计'))
        self.Parent.m_listCtrl1.SetItem(len(cat),2,str(Totally))
        
app = wx.App()
app.locale = wx.Locale(wx.LANGUAGE_ENGLISH)
fm = MyFrame(None)
fm.Show()
app.MainLoop()
    


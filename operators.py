import bpy
from .bilibili_spider import *
from .bangumi_spider import *
import os
import pickle
import webbrowser
import re
from . import ui

class Bilibili_Spider(bpy.types.Operator):
    bl_idname = "bangumi.bilibili"
    bl_label = "bilibili_bangumi_spider"
    bl_description = "bilibili数据更新"
    bl_options = {"REGISTER"}

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        bilibili_main()
        ui.ui_unregister()
        ui.ui_register()
        get_link_bilibili()
        return {"FINISHED"}

class Bangumi_Spider(bpy.types.Operator):
    bl_idname = "bangumi.bangumi"
    bl_label = "bangumi_bangumi_spider"
    bl_description = "bangumi数据更新"
    bl_options = {"REGISTER"}


    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        bangumi_main()
        ui.ui_unregister()
        ui.ui_register()
        get_link_bangumi()
        return {"FINISHED"}



class Open_bilibili_url(bpy.types.Operator):
    bl_idname = "bangumi.open_bilibili_url"
    bl_label = "open_bilibili_url"
    bl_description = "在浏览器中打开该番剧页面"
    bl_options = {"REGISTER"}

    flag:bpy.props.StringProperty(name='flag', default='0')

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        #实在不知道怎么往这里面传参了，不得已用上了这个离大谱的办法，知道咋办的兄弟救一下plz!!!!!!!!!!
        i=int(re.search(r"\+.*?_",self.flag).group()[1:-1])
        j=int(re.search(r"_.*?-",self.flag).group()[1:-1])
        webbrowser.open(url = bilibili_link_list[0][i][j], new = 0)
        return {"FINISHED"}
        


class Open_bangumi_url(bpy.types.Operator):
    bl_idname = "bangumi.open_bangumi_url"
    bl_label = "open_bangumi_url"
    bl_description = "在浏览器中打开该番剧页面"
    bl_options = {"REGISTER"}

    bangumi_flag:bpy.props.StringProperty(name='bangumi_flag', default='0')

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        x=int(re.search(r"\+.*?_",self.bangumi_flag).group()[1:-1])
        y=int(re.search(r"_.*?-",self.bangumi_flag).group()[1:-1])
        webbrowser.open(url = bangumi_link_list[0][x][y], new = 0)
        return {"FINISHED"}




bilibili_link_list={}
bangumi_link_list={}

def get_link_bilibili():
    bilibili_info_path=os.path.join(os.path.join(os.path.dirname(os.path.abspath(__file__)),'src'),'bilibili_info')
    with open(bilibili_info_path,'rb') as f:
        total_list=pickle.load(f)
        bilibili_link_list[0]=total_list[2]

def get_link_bangumi():
    bangumi_info_path=os.path.join(os.path.join(os.path.dirname(os.path.abspath(__file__)),'src'),'bangumi_info')
    with open(bangumi_info_path,'rb') as f:
        total_list=pickle.load(f)
        bangumi_link_list[0]=total_list[2]



def operator_register():
    get_link_bilibili()
    get_link_bangumi()

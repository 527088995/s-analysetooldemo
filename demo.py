from Manage import Manage

white_list=['blog.csdn.net/A757291228','www.cnblogs.com/1-bit','blog.csdn.net/csdnnews']#白名单
#配置信息
conf={
       'engine':'baidu',
       'target_page':5
       'white_list':white_list,
    }

print(Manage(conf).get_local_analyse())
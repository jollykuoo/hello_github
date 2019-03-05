from bs4 import BeautifulSoup
import csv
import re
# from pyecharts import Bar,Page,Pie
import urllib.request
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

if __name__ == "__main__":
    file = open("douban.html","r")
    html = file.read()
    file.close() #读取网页数据
    soup = BeautifulSoup(html,"lxml")
    all_movie = soup.find('div',id='showing-soon')
    csv_file = open("data.csv","w",encoding="gbk",newline="")
    writer = csv.writer(csv_file)
    writer.writerow(["电影名","链接","上映时间","类型","产地","关注者","预告片链接","图片链接","封面"])
    url_res = r'<img class="" src="([^"]+\.jpg)"'
    all_movies_info = []

    for each_para in all_movie.findAll('div',class_="item"):
        all_a = each_para.findAll('a')
        all_li = each_para.findAll('li')
        movie_name = all_a[1].text
        movie_href = all_a[1]['href']
        movie_date = all_li[0].text
        movie_type = all_li[1].text
        movie_place = all_li[2].text
        movie_wanna = all_li[3].text.replace('想看','')
        # list = re.findall(url_res,str(all_a[0]))
        # image_url = ''.join(list)
        # filename = image_url.split('/')[-1]
        # urllib.request.urlretrieve(image_url,filename)
        if len(all_a) ==2 :
            movie_prelink = all_a[1]['href']
        else:
            movie_prelink = "--"
        # all_movies_info.append({'name': movie_name, 'date': movie_date, 'type': movie_type,'area': movie_place, 'lovers': movie_wanna})
        # writer.writerow([movie_name,movie_href,movie_date,movie_type,movie_place,movie_wanna,movie_prelink,image_url,image_file])
        writer.writerow([movie_name,movie_href,movie_date,movie_type,movie_place,movie_wanna])
    csv_file.close()
    print("finished collecting!\n\n")


    #Alys
    # sort_by_lovers = sorted(all_movies_info, key=lambda x: int(x['lovers']))
    # all_names = [i['name'] for i in sort_by_lovers]
    # all_lovers = [i['lovers'] for i in sort_by_lovers]
    #
    # lovers_rank_bar = Bar('电影关注者排行榜')  # 初始化图表，给个名字
    # # all_names是所有电影名，作为X轴, all_lovers是关注者的数量，作为Y轴。二者数据一一对应。
    # # is_convert=True设置x、y轴对调,。is_label_show=True 显示y轴值。 label_pos='right' Y轴值显示在右边
    # lovers_rank_bar.add('', all_names, all_lovers, is_convert=True, is_label_show=True, label_pos='right')
    # lovers_rank_bar  # jupyter下直接显示图表在输出框内

    # # 绘制电影类型占比图
    # all_types = [i['type'] for i in all_movies_info]
    # type_count = {}
    # for each_types in all_types:
    #     # 把 爱情 / 奇幻 这种分成[爱情, 奇幻]
    #     type_list = each_types.split(' / ')
    #     for e_type in type_list:
    #         if e_type not in type_count:
    #             type_count[e_type] = 1
    #         else:
    #             type_count[e_type] += 1
    # # print(type_count) # 检测是否数据归类成功
    # type_pie = Pie('上映类型占比', title_top=20)  # 因为类型过多影响标题，所以标题向下移20px
    # # 直接取出统计的类型名和数量并强制转换为list。
    # type_pie.add('', list(type_count.keys()), list(type_count.values()), is_label_show=True)
    # type_pie  # jupyter下直接显示

    # 绘制电影上映日期柱状图
    # all_dates = [i['date'] for i in all_movies_info]
    # dates_count = {}
    # for date in all_dates:
    #     if date not in dates_count:
    #         dates_count[date] = 1
    #     else:
    #         dates_count[date] += 1
    # # print(dates_count)  # 输出验证数据是否正确
    #
    # dates_bar = Bar('上映日期占比')
    # dates_bar.add('', list(dates_count.keys()), list(dates_count.values()), is_label_show=True)
    # dates_bar  # jupyter下直接显示


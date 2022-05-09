# file: hn_site_grouper.py
import datetime

import requests
from lxml import etree
from typing import Dict
from collections import Counter
from abc import ABCMeta, abstractmethod

# 假设我要开发一个和 HN 页面有关的新功能： 我想在不同时间点对 HN 首页内容进行归档，观察热点新闻在不同时间点发生的变化。
# 所以除了页面文本内容外，我还需要拿到页面的大小、生成时间这些额外信息，然后将它们都保存到数据库中。
# 但这时候不应该扩展HNWebPage了 不然就代码就要跟着改
from abc import ABCMeta, abstractmethod


class HNWebPage(metaclass=ABCMeta):
    """抽象类：Hacker New 站点页面（仅提供内容）
    """

    @abstractmethod
    def get_text(self) -> str:
        raise NotImplementedError


class HNWebPagePlus(HNWebPage):
    """抽象类：Hacker New 站点页面（含元数据）
    """

    @abstractmethod
    def get_size(self) -> int:
        """获取页面大小"""

    @abstractmethod
    def get_generated_at(self) -> datetime.datetime:
        """获取页面生成时间"""


class RemoteHNWebPage(HNWebPage):
    """远程页面，通过请求 HN 站点返回内容"""

    def __init__(self, url: str):
        self.url = url

    def get_text(self) -> str:
        resp = requests.get(self.url)
        return resp.text


class LocalHNWebPage(HNWebPage):
    """本地页面，根据本地文件返回页面内容"""

    def __init__(self, path: str):
        self.path = path

    def get_text(self) -> str:
        with open(self.path, 'r') as fp:
            return fp.read()


# 主程序代码垃圾版
class SiteSourceGrouper:
    """对 HN 页面的新闻来源站点进行分组统计
    """

    def __init__(self, url: str):
        self.url = url

    def get_groups(self) -> Dict[str, int]:
        """获取 (域名, 个数) 分组
        """
        resp = requests.get(self.url)
        html = etree.HTML(resp.text)
        # 通过 xpath 语法筛选新闻域名标签
        elems = html.xpath('//table[@class="itemlist"]//span[@class="sitestr"]')

        groups = Counter()
        for elem in elems:
            groups.update([elem.text])
        return groups


def main():
    groups = SiteSourceGrouper("https://news.ycombinator.com/").get_groups()
    # 打印最常见的 3 个域名
    for key, value in groups.most_common(3):
        print(f'Site: {key} | Count: {value}')


# 主程序代码拓展版
class SiteSourceGrouper2:
    """对 HN 页面的新闻来源站点进行分组统计
    """

    def __init__(self, page: HNWebPage):
        self.page = page

    def get_groups(self) -> Dict[str, int]:
        """获取 (域名, 个数) 分组
        """
        html = etree.HTML(self.page.get_text())
        # 通过 xpath 语法筛选新闻域名标签
        elems = html.xpath('//table[@class="itemlist"]//span[@class="sitestr"]')

        groups = Counter()
        for elem in elems:
            groups.update([elem.text])
        return groups


def main2():
    # 实例化 page，传入 SiteSourceGrouper
    page = RemoteHNWebPage(url="https://news.ycombinator.com/")
    grouper = SiteSourceGrouper2(page).get_groups()


# 主程序代码拓展版需求变更
class SiteAchiever:
    """将不同时间点的 HN 页面归档"""

    def save_page(self, page: HNWebPagePlus):
        """将页面保存到后端数据库
        """
        data = {
            "content": page.get_text(),
            "generated_at": page.get_generated_at(),
            "size": page.get_size(),
        }
        # 将 data 保存到数据库中


#  单元测试
from collections import Counter


def test_grouper_returning_valid_types():
    """测试 get_groups 是否返回了正确类型
    """
    grouper = SiteSourceGrouper('https://news.ycombinator.com/')
    result = grouper.get_groups()
    assert isinstance(result, Counter), "groups should be Counter instance"


def test_grouper_from_local():
    page = LocalHNWebPage(path="./static_hn.html")
    grouper = SiteSourceGrouper2(page)
    result = grouper.get_groups()
    assert isinstance(result, Counter), "groups should be Counter instance"


if __name__ == '__main__':
    main()

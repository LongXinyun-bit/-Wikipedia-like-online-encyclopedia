from django.shortcuts import render, redirect
from django.http import HttpResponse
from django import forms  # 导入 Django 表单模块
from . import util
import markdown  # 确保 markdown 也正确导入了

def convert_md_to_html(title):
    content = util.get_entry(title)
    markdowner = markdown.Markdown()
    if content is None:
        return None
    else:
        html_content = markdowner.convert(content)
        print("Raw content:", content)  # 调试用
        print("Converted HTML:", html_content)  # 调试用
        return html_content

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    html_content = convert_md_to_html(title)
    if html_content is None:
        return render(request, "encyclopedia/error.html", {"message": "Entry not found."})
    return render(request, "encyclopedia/entry.html", {
        "title": title,
        "content": html_content
    })

def search(request):
    if request.method == "POST":
        entry_search = request.POST['q']
        html_content = convert_md_to_html(entry_search)

        if html_content is not None:
            return render(request, "encyclopedia/entry.html", {
                "title": entry_search,
                "content": html_content
            })

        all_entries = util.list_entries()
        recommendation = []
        for entry in all_entries:
            if entry_search.lower() in entry.lower():
                recommendation.append(entry)

        return render(request, "encyclopedia/search.html", {
            "recommendation": recommendation
        })

# 修改 new_page 视图函数
def new_page(request):
    if request.method == "POST":
        title = request.POST.get("title")  # 获取表单中的标题
        content = request.POST.get("content")  # 获取表单中的内容

        # 检查是否已存在同名条目
        if util.get_entry(title):
            return render(request, "encyclopedia/error.html", {
                "message": f"An entry with the title '{title}' already exists."
            })

        # 保存新条目
        util.save_entry(title, content)
        return redirect("entry", title=title)  # 重定向到新创建的条目页面

    # 如果是 GET 请求，显示创建新页面的表单
    return render(request, "encyclopedia/new_page.html")

# 添加 edit 视图函数
def edit(request, title):
    # 获取当前条目的内容
    content = util.get_entry(title)
    if content is None:
        return render(request, "encyclopedia/error.html", {"message": "Entry not found."})

    # 如果是 POST 请求，保存修改后的内容
    if request.method == "POST":
        new_content = request.POST["content"]
        util.save_entry(title, new_content)
        return redirect("entry", title=title)

    # 如果是 GET 请求，显示编辑表单
    return render(request, "encyclopedia/edit.html", {
        "title": title,
        "content": content
    })

title = input()
content = input()
comment_list = []
while True:
    comments = input()
    if comments == "end of comments":
        break
    comment_list.append(comments)
print(f"<h1>\n\t{title}\n</h1>")
print(f"<article>\n\t{content}\n</article>")
for comment in comment_list:
    print(f"<div>\n\t{comment}\n</div>")

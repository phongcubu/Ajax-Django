from django.shortcuts import render
from .models import Post, Like
from django.http import HttpResponse


def index(request):
    posts = Post.objects.all()

    return render(request, 'index.html', {'posts': posts})
"""
Nếu đó là phương thức GET, thì nó sẽ đọc dữ liệu. Dữ liệu là id của bài đăng mà chúng tôi thích.
Sau đó, chúng tôi tạo một đối tượng lớp Like và lưu id của nó bằng dữ liệu. 
Sau đó, chúng tôi lưu trữ đối tượng trong cơ sở dữ liệu của chúng tôi.
Cuối cùng, chúng tôi đang trả về một HttpResponse.
Phản hồi này sẽ không làm gì trong mã của chúng tôi vì chúng tôi không in giống nhau.
Chúng tôi có thể chỉ cần thông qua một kịch bản.
Chúng có thể được sử dụng tùy theo trường hợp sử dụng của một người.
"""
#  xử lý yêu cầu Ajax
def like(request):
    if request.method == 'GET':
        post_id = request.GET['post_id']
        likedpost = Post.objects.get(id=post_id)
        m = Like(post=likedpost)
        m.save()

        return HttpResponse('thanh cong')
    else:
        return HttpResponse('that bai')




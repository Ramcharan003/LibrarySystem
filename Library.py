class Library:
    def __init__(self,name,book_list):
        self.name=name
        self.book_list=book_list
    def add_book(self,book_title):
        self.book_list.append(book_title)
    def remove_book(self,book_title):
        self.book_list.remove(book_title)
    def list_books(self):
        print(set(self.book_list))
    def search_book(self,book_title):
        for i in set(self.book_list):
            print(f"{i}",end=" ")
    def display_info(self):
        for i in set(self.book_list):
            print(f"{i}: {self.book_list.count(i)}")
obj=Library("Rc",["telugu","Hindi","English","Sceince"])
print("select one:\n1.add book\n2.remove book\n3.list of books\n4.search a book\n5.display books and counts")
    `while(1):
        ch=int(input("enter your choice:"))
        if ch==1:
            obj.add_book(input("enter book:"))
        elif ch==2:
            obj.remove_book(input("enter book:"))
        elif ch==3:
            obj.list_books()
        elif ch==4:
            obj.search_book(input("enter book:"))
        elif ch==5:
            obj.display_info()
        if int(input("\n1.continue or 2.exit :: "))==1:
            continue
        else:
            break

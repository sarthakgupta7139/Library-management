import sys
import pandas as pd

def MainMenu():
    print('You are logged in successfully')
    while True:
        print('-'*50)
        print('WELCOME MENU')
        print('1. Go to Member Menu')
        print('2. Go to Book Menu')
        print('3. Go to Book-Issue Menu')
        print('4. Exit')
        choice=int(input('Enter your choice:'))
        if choice==1:
            MemberMenu()
        elif choice==2:
            BookMenu()
        elif choice==3:
            IssueMenu()
        elif choice==4:
            print('Thank You for visiting Library')
            print('       See you soon')
            sys.exit(0)
        else:
            print('Invalid choice')

def MemberMenu():
    while True:
        print('*'*50)
        print('Welcome to MEMBER MENU')
        print('1. Add member')
        print('2. Display all Members')
        print('3. Search Member')
        print('4. Remove Member')
        print('5. Go to Main Menu')
        x = int(input('Enter your choice:'))
        mm = pd.read_csv('member.csv')
        bm=pd.read_csv('book.csv')
        im=pd.read_csv('issue.csv')

        if x==1:
            k = mm.index
            n = len(k)
            mid=input('Enter member id:')
            mname=input('Enter member name:')
            cno=input('Enter member contact number:')
            noi=0
            mm.at[n] = [mid,mname,cno,noi]
            mm.to_csv('member.csv', index=False)
            print('Member is added successfully')

        elif x==2:
            print(mm)

        elif x==3:
            memid=input('Input the Member id you want to check:')
            f=0
            for row,rowdata in mm.iterrows():
                if str(mm.iloc[row,0]) == memid:
                    f=1
                    break
            if f==0:
                print('Invalid member')
            else:
                print('Valid member')
                print(rowdata)

        elif x==4:
            memid=input('Enter Member id you want to delete:')
            f = 0
            for row, rowdata in mm.iterrows():
                if str(mm.iloc[row, 0]) == memid:
                    f = 1
                    break
            if f == 0:
                print('Invalid Member id')
            else:
                mm.drop(row,axis=0,inplace=True)
                mm.to_csv('member.csv', index=False)
                print('Member deleted successfully')

        elif x==5:
            MainMenu()
        else:
            print('Invalid choice')

def BookMenu():
    while True:
        print('*'*50)
        print('Welcome to BOOK MENU')
        print('1. Add a new book')
        print('2. Display all books')
        print('3. Search book')
        print('4. Remove book')
        print('5. Go to Main Menu')
        y = int(input('Enter your choice:'))
        mm = pd.read_csv('member.csv')
        bm=pd.read_csv('book.csv')
        im=pd.read_csv('issue.csv')

        if y==1:
            l = bm.index
            m = len(l)
            bookid=input('Enter book id:')
            title=input('Enter title of book:')
            author=input('Enter Author of book:')
            edition=input('Enter edition of book:')
            cost=input('Enter cost of book:')
            category=input('Enter category of book:')
            bm.at[m] = [bookid, title, author, edition, cost, category]
            bm.to_csv('book.csv', index=False)
            print('Book added successfully')

        elif y==2:
            print(bm)

        elif y==3:
            bookid = input('Input the Book-id you want to check:')
            f = 0
            for row, rowdata in bm.iterrows():
                if str(bm.iloc[row, 0]) == bookid:
                    f = 1
                    break
            if f == 0:
                print('Invalid Book id')
            else:
                print('Valid Book')
                print(rowdata)

        elif y==4:
            bookid=input('Enter Book id you want to delete:')
            f = 0
            for row, rowdata in bm.iterrows():
                if str(bm.iloc[row, 0]) == bookid:
                    f = 1
                    break
            if f == 0:
                print('Invalid Book id')
            else:
                bm.drop(row,axis=0,inplace=True)
                bm.to_csv('book.csv', index=False)
                print('Book deleted successfully')

        elif y==5:
            MainMenu()

        else:
            print('Invalid choice')


def IssueMenu():
    while True:
        print('*'*50)
        print('Welcome to Book-Issue MENU')
        print('1. Issue book')
        print('2. Return book')
        print('3. Show all issued books')
        print('4. Delete issued book')
        print('5. Go back to Main Menu')
        z=int(input('Enter your choice:'))
        mm = pd.read_csv('member.csv')
        bm=pd.read_csv('book.csv')
        im=pd.read_csv('issue.csv')
        if z==1:
            f=0
            memid=input('Enter your member id:')
            for row,rowdata in mm.iterrows():
                if str(mm.iloc[row,0]) == memid:
                    f=1
                    break
            if f==0:
                print('Invalid member')
            else:
                if int(mm.iloc[row,3]) < 2:
                    r=row
                    bname=input('Enter book you want to issue:')
                    f = 0
                    for row, rowdata in bm.iterrows():
                        if str(bm.iloc[row, 1]) == bname:
                            f = 1
                            break
                    if f == 0:
                        print('Invalid Book name')
                    else:
                        doi=input('Enter date of issue:')
                        l = im.index
                        m = len(l)
                        im.at[m] = [bname, memid, doi, '']
                        im.to_csv('issue.csv', index=False)
                        i = int(mm.iloc[row, 3])
                        print(r)
                        #print('value at ', i)
                        k = i + 1
                        mm.at[row, 3] = k
                        mm.to_csv('member.csv', index=False)

                        print('Book issued successfully')
        elif z==2:
            f = 0
            memid = input('Enter your member id:')
            for row, rowdata in im.iterrows():
                if str(im.iloc[row, 1]) == memid:
                    f = 1
                    break
            if f == 0:
                print('Invalid member id')
            else:
                if int(mm.iloc[row, 3]) >= 0:
                    bname = input('Enter book you want to return:')
                    f = 0
                    for row, rowdata in bm.iterrows():
                        if str(im.iloc[row, 0]) == bname:
                            f = 1
                            break
                    if f == 0:
                        print('Invalid Book name')
                    else:
                        im.drop(row, axis=0, inplace=True)
                        im.to_csv('issue.csv', index=False)
                        print('Book is returned successfully')
        elif z==3:
            print(im)

        elif z==4:
            bname = input('Enter book name:')
            f = 0
            for row, rowdata in bm.iterrows():
                if str(im.iloc[row, 0]) == bname:
                    f = 1
                    break
            if f == 0:
                print('Invalid Book name')
            else:
                im.drop(row, axis=0, inplace=True)
                im.to_csv('issue.csv', index=False)
                print('Deleted issued book successfully')

        elif z==5:
            MainMenu()

        else:
            print('Invalid choice')


print("SARTHAK'S LIBRARY")
print('-Login Wizard-')
user=input('Enter username:')
password=input('Enter password:')
df=pd.read_csv('login.csv')
f=0
for row, rowdata in df.iterrows():
    if str(rowdata[1])==user and str(rowdata[2])==password:
        f=1
        break

if f==1:
    MainMenu()
else:
    print('Incorrect username or password')
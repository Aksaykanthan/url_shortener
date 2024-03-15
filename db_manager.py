
import csv

filename = "db.csv"

def add_url(orginal_url,encoded_url):
    with open(filename,'a+') as f:
        f.seek(0)
        reader = csv.reader(f)

        for shorten_link, _ in reader:
            if shorten_link == encoded_url:
                print('This URL is already added!')
                break
        else:
            writer = csv.writer(f)
            writer.writerow([encoded_url,orginal_url])


def get_url(shorten_link):
    data = []
    with open('db.csv','r') as f:
        data.extend(list(csv.reader(f)))
        
    for shorten_url, orginal_link in data:
        if shorten_url == shorten_link:
            return orginal_link
    return None

# with open(filename,'a+') as f:
#     f.seek(0)
#     reader = csv.reader(f)

#     print(*list(reader),sep="\n")



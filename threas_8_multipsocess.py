import requests, time, multiprocessing
img_urls = [
    'https://cdn.pixabay.com/photo/2022/06/01/09/12/duck-7235180_1280.jpg', 
    'https://cdn.pixabay.com/photo/2022/11/01/15/11/seagull-7562623_1280.jpg'
]

def download_image(img_url):
    img_bytes = requests.get(img_url).content
    img_name = img_url.split('/')[5]+'.jpg'
    with open(img_name, 'wb') as img_file:
        img_file.write(img_bytes)
        print(f"{img_name} was downloaded")
        
if __name__ == '__main__':
    start = time.perf_counter()
    p1 = multiprocessing.Process(target=download_image, args=[img_urls[0]])
    p2 = multiprocessing.Process(target=download_image, args=[img_urls[1]])
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    end = time.perf_counter()
    print(f"Tasks ended in {round(end - start, 2)} second(s)")
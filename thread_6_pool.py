import time, requests
import concurrent.futures
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
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(download_image, img_urls)
    end = time.perf_counter()
    print(f"Tasks ended in {round(end - start, 2)} second(s)")
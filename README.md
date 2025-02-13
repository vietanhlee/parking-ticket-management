# Chương trình nhận diện biển số xe phục cho bãi gửi xe

## Cơ sở để đọc được biển số xe:
> Đây là phần mềm được phát triển từ chương trình đọc biển số xe. Có thể tham khảo code chạy console ở [đây](https://github.com/vietanhlee/license-plate-recognition)
- Dùng dataset về nhận diện biển số của các loại xe của Việt Nam sau đó train model nhận diện biển số. [Tải tại đây](https://drive.google.com/drive/folders/1Ofqqey7Yqcas_uQSeUc2E8aB1ZTe_S6K?usp=drive_link)

- Dùng dataset về nhận diện các chữ cái xuất hiện ở biển xe sau đó train model nhận diện ra các chữ cái. [Tải tại đây](https://drive.google.com/drive/folders/1fOh2m80gi0309jYNByFMj2AL0098_w0Q?usp=drive_link)

- Kết hợp hai model trên lại với nhau và dùng một số xử lý logic về khoảng cách các tâm của bounding box với nhau mà cho ra được biển số đó có những kí tự gì, và sắp xếp chúng để thành biển số hoàn chỉnh

> File `OcrPlate.py` chính là class gồm một số công cụ trong đó có chức năng trả về kí tự đọc được trên biển số từ một ảnh được đưa vào

## Kết quả với từng loại biển
Việc phát hiện biển số và các kí tự có trên biển có thể được coi là dễ nhưng việc từ các kí tự đó sắp xếp sao cho đúng trình tự thì là một vấn đề khá phức tạp

![anh](https://raw.githubusercontent.com/vietanhlee/license-plate-recognition/refs/heads/main/display%20github/1%20line.png)

<p align = 'center'>Nhận diện với biển 1 dòng</p>

![anh](https://raw.githubusercontent.com/vietanhlee/license-plate-recognition/refs/heads/main/display%20github/2%20line.png)

<p align = 'center'>Nhận diện với biển 2 dòng</p>

## Demo code
### Trường hợp không nhận diện thể biển số hoặc không xuất hiện biển số
Các thông số hiển thị không nhận diện được

   ![](https://raw.githubusercontent.com/vietanhlee/parking-ticket-management/refs/heads/main/display_github/Screenshot%202025-02-13%20191322.png)

### Trường hợp xe chưa vào bãi
Các thông số hiển thị xe không tồn tại tức ko có trong bãi

  ![](https://raw.githubusercontent.com/vietanhlee/parking-ticket-management/refs/heads/main/display_github/Screenshot%202025-02-13%20191310.png)

**Sau khi nhấn `xác nhận vào`:** 

Chương trình sẽ tạo một folder tên là biển số được đọc và lưu ảnh được chụp toàn cảnh khi xe vào kèm với tên là ngày và giờ xe vào

>Ví dụ: 36X1-4359/19-14-23 13-02-2025.jpg thì có nghĩa là xe 36X1-4359 vào bãi lúc 19h 14p 23s ngày 13 tháng 2 năm 2025

Khi đó xe đã được đặt trạng thái nằm trong bãi và một số thông tin kèm theo như giá vé và thời gian vào

![](https://raw.githubusercontent.com/vietanhlee/parking-ticket-management/refs/heads/main/display_github/Screenshot%202025-02-13%20191431.png)
### Trường hợp xe đã vào bãi
Hiển thị trạng thái nằm trong bãi và một số thông tin kèm theo như giá vé và thời gian vào

![](https://raw.githubusercontent.com/vietanhlee/parking-ticket-management/refs/heads/main/display_github/Screenshot%202025-02-13%20191333.png)

**Sau khi nhấn `Xác nhận ra`:**

Chương trình sẽ xóa dữ liệu về chiếc xe đó tức có nghĩa xóa toàn bộ thư mục có tên là biển số xe đó bao gồm cả dữ liệu bên trong thư mục đó. Các thông tin về trạng thái được đặt lại như lúc chưa vào bãi

![](https://raw.githubusercontent.com/vietanhlee/parking-ticket-management/refs/heads/main/display_github/Screenshot%202025-02-13%20191343.png)


## Chạy code
- **B1**: clone dự án về và chạy lệnh sau trên terminal tại chính folder mà đã clone:
    ```bash
    pip install -r 'requirements.txt'
    ```
- **B2**: tại file `main_ui.py` nhấn run để chạy demo theo video có sẵn hoặc nếu muốn nhận diện theo real time bằng camera chính thì có thể thay dòng:
    ```python
    cam = cv2.VideoCapture(r"test.MOV")
    ```
    thành :
    ```python
    cam = cv2.VideoCapture(0)
# import sys
# import exifread
# import subprocess
#
#
# def extract_gps_info(file_path):
#     try:
#         if file_path.endswith('.jpg') or file_path.endswith('.jpeg'):
#             with open(file_path, 'rb') as f:
#                 tags = exifread.process_file(f)
#                 if 'GPS GPSLatitude' in tags and 'GPS GPSLongitude' in tags:
#                     latitude = tags['GPS GPSLatitude'].values
#                     longitude = tags['GPS GPSLongitude'].values
#                     return latitude, longitude
#                 else:
#                     return None
#         elif file_path.endswith('.mp4') or file_path.endswith('.avi'):
#             cmd = ['ffprobe', '-v', 'error', '-select_streams', 'v:0', '-show_entries', 'stream_tags=location', '-of',
#                    'default=noprint_wrappers=1', file_path]
#             result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
#             location_info = result.stdout.strip()
#             if location_info:
#                 latitude, longitude = map(float, location_info.split(','))
#                 return latitude, longitude
#             else:
#                 return None
#         else:
#             return None
#     except Exception as e:
#         return None
#
#
# if __name__ == '__main__':
#     if len(sys.argv) < 2:
#         print("请拖入一个视频或图片文件。")
#         sys.exit(1)
#
#     file_path = sys.argv[1]
#     gps_info = extract_gps_info(file_path)
#
#     if gps_info:
#         latitude, longitude = gps_info
#         print(f"经度: {longitude}, 纬度: {latitude}")
#     else:
#         print("GPS信息未找到。")
#
#     input("按 Enter 键继续...")

import exifread
from geopy.geocoders import Nominatim

def extract_gps_info(file_path):
    with open(file_path, 'rb') as f:
        tags = exifread.process_file(f, details=False)

        if 'GPS GPSLatitude' in tags and 'GPS GPSLongitude' in tags:
            latitude = tags['GPS GPSLatitude'].values
            longitude = tags['GPS GPSLongitude'].values

            latitude = float(latitude[0].num) / float(latitude[0].den) + \
                       float(latitude[1].num) / float(latitude[1].den) / 60 + \
                       float(latitude[2].num) / float(latitude[2].den) / 3600

            longitude = float(longitude[0].num) / float(longitude[0].den) + \
                        float(longitude[1].num) / float(longitude[1].den) / 60 + \
                        float(longitude[2].num) / float(longitude[2].den) / 3600

            return latitude, longitude
        else:
            return None

def main():
    while True:
        file_path = input("拖入视频或图片文件并按回车键：")

        try:
            gps_info = extract_gps_info(file_path)
            if gps_info:
                latitude, longitude = gps_info
                print(f"GPS位置信息：纬度 {latitude}, 经度 {longitude}")
            else:
                print("GPS not found")
        except Exception as e:
            print(f"发生错误：{str(e)}")

if __name__ == "__main__":
    main()